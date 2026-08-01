#!/usr/bin/env python3
"""
Crawls plantuml.com documentation pages and saves them as clean markdown.
- Strips navigation boilerplate, edit links, rendered images
- Wraps @startuml/@startsalt code blocks in ```plantuml fences
- Adds YAML frontmatter with source URL

Usage:
  python3 crawl-plantuml-docs.py --url https://plantuml.com/salt          # crawl a direct URL
  python3 crawl-plantuml-docs.py --sitemap ../src/sitemap.yaml           # crawl every page from a sitemap YAML
  python3 crawl-plantuml-docs.py -n 8 --sitemap ../src/sitemap.yaml      # crawl with 8 parallel workers
  python3 crawl-plantuml-docs.py --section language-specs                # crawl one live sitemap section
  python3 crawl-plantuml-docs.py                                         # crawl default diagram pages
  python3 crawl-plantuml-docs.py --skip-existing                         # skip already-crawled pages

With --sitemap, pages are saved as src/<section-slug>/<subsection-slug>.md.
"""

import os
import queue
import re
import sys
import threading
import time
from urllib.parse import urlsplit

import requests
from bs4 import BeautifulSoup, Tag, NavigableString
from tqdm import tqdm

BASE_URL = "https://plantuml.com"

# All diagram-type pages from the top menu #B3 > div.menu1
PAGES = [
    "/sequence-diagram",
    "/use-case-diagram",
    "/class-diagram",
    "/activity-diagram-beta",
    "/component-diagram",
    "/state-diagram",
    "/object-diagram",
    "/deployment-diagram",
    "/timing-diagram",
    "/regex",
    "/nwdiag",
    "/salt",
    "/archimate-diagram",
    "/gantt-diagram",
    "/mindmap-diagram",
    "/wbs-diagram",
    "/ebnf",
    "/json",
    "/yaml",
]

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src")
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

EDIT_PREFIX = "Edit in DokuwikiEdit in AsciidocEdit in Markdown"

# Slug used for each sitemap section. Keys are the exact sitemap section titles.
SECTION_SLUGS = {
    "Language specification": "language-specs",
    "News and information": "news-and-information",
    "Advanced Usage": "advanced-usage",
    "Plugins": "plugins",
}


def slugify(text: str) -> str:
    """Turn arbitrary text into a filesystem-safe slug."""
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def section_slug(title: str) -> str:
    """Return the output slug for a sitemap section title."""
    return SECTION_SLUGS.get(title, slugify(title))


def fetch_sitemap():
    """Fetch plantuml.com/sitemap and return a list of section dicts:
    [{"title": ..., "slug": ..., "pages": [(name, path), ...]}, ...]
    """
    url = f"{BASE_URL}/sitemap"
    headers = {"User-Agent": "Mozilla/5.0 (compatible; PlantUML Docs Crawler/1.0)"}
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "lxml")

    main = soup.find("main")
    run_div = None
    for div in main.find_all("div"):
        if div.get("id") == "run":
            run_div = div
            break
    if run_div is None:
        raise RuntimeError("Could not find sitemap #run container")

    sections = []
    current = None
    for child in run_div.children:
        if not isinstance(child, Tag):
            continue
        classes = child.get("class", [])
        if child.name == "div" and "runt" in classes:
            h2 = child.find("h2")
            if not h2:
                continue  # skip runt blocks without a section title
            title = h2.get_text(strip=True)
            current = {"title": title, "slug": section_slug(title), "pages": []}
            sections.append(current)
        elif child.name == "a" and "run1" in classes and current is not None:
            name = child.find("b")
            name = name.get_text(strip=True) if name else child.get_text(strip=True)
            href = child.get("href", "")
            if href:
                if not href.startswith("/"):
                    href = "/" + href
                current["pages"].append((name, href))
    return sections


def url_to_filename(path: str) -> str:
    """Convert URL path to output filename."""
    clean = path.strip("/")
    return clean + ".md"


def url_to_title(path: str) -> str:
    """Convert URL path to a page title."""
    clean = path.strip("/").replace("-", " ").replace("_", " ")
    return " ".join(word.capitalize() for word in clean.split())


def normalize_path(url: str) -> str:
    """Accept a full URL or a path, return the leading-/-path form."""
    if url.startswith("http://") or url.startswith("https://"):
        url = urlsplit(url).path
    if not url.startswith("/"):
        url = "/" + url
    return url


def load_sitemap(path: str):
    """Load a sitemap YAML file: [{"title", "slug", "subsections": [path, ...]}, ...]."""
    import yaml

    with open(path) as f:
        sections = yaml.safe_load(f)
    for section in sections:
        section["subsections"] = [normalize_path(p) for p in section.get("subsections", [])]
    return sections


def fetch_page(path: str) -> str:
    """Fetch a page (path or full URL) and return its HTML content."""
    if path.startswith("http://") or path.startswith("https://"):
        url = path
    else:
        url = f"{BASE_URL}{path}"
    headers = {"User-Agent": "Mozilla/5.0 (compatible; PlantUML Docs Crawler/1.0)"}
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.text


def clean_heading_text(el: Tag) -> str:
    """Get clean heading text, stripping edit dropdown pollution."""
    # Remove edit dropdown divs that pollute heading text
    for dropdown in el.select(".dropdown"):
        dropdown.decompose()
    for edit_link in el.select('a[href*="dokuwiki"], a[href*="asciidoc"], a[href*="markdown"]'):
        edit_link.decompose()
    text = el.get_text(" ", strip=True)
    # Strip known prefix if still present
    if text.startswith(EDIT_PREFIX):
        text = text[len(EDIT_PREFIX):].strip()
    return text


def is_plantuml_code(text: str) -> bool:
    """Check if text is plantuml code. Covers @startuml, @startsalt, @startebnf,
    @startgantt, @startmindmap, @startwbs, @startjson, @startyaml, @startregex, etc."""
    return bool(re.match(r'@start\w+\b', text.strip()))


def is_nwdiag_code(text: str) -> bool:
    """Check if text is nwdiag code."""
    return bool(re.match(r'@start(nwdiag|rackdiag|blockdiag|seqdiag|actdiag|packetdiag)\b', text.strip()))


def extract_page_content(html: str, page_path: str) -> str:
    """Extract clean markdown from a plantuml.com page HTML."""
    soup = BeautifulSoup(html, "lxml")
    main = soup.find("main")
    if not main:
        main = soup.find("body")

    output_lines = []
    seen_headings = set()

    # Remove unwanted elements globally in main
    for selector in [
        ".edit_section", ".secedit", ".dropdown",
        'img[src*="backtop"]', 'img[src*="edit1.svg"]',
        'img[src*="dokuwiki"]', 'img[src*="asciidoc32"]',
        'img[src*="markdown.png"]', 'img[src*="svgrepo"]',
        ".plugin_box", ".sharebuttons",
        "#ext-promo",  # browser extension promo
    ]:
        for el in main.select(selector):
            el.decompose()

    # Remove empty/whitespace-only elements
    for el in main.find_all(["div", "span", "p"]):
        if not el.get_text(strip=True) and not el.find("img"):
            el.decompose()

    def extract_text(el):
        """Extract text content preserving some structure."""
        if isinstance(el, NavigableString):
            return str(el).strip()
        if not isinstance(el, Tag):
            return ""

        tag = el.name

        if tag in ("img", "svg"):
            return ""  # Skip images

        if tag == "a":
            href = el.get("href", "#")
            txt = el.get_text(strip=True)
            if not txt:
                return ""
            if "dokuwiki" in href or "asciidoc" in href or "backtop" in href:
                return ""
            if href.startswith("#"):
                return txt
            if href.startswith("/") or href.startswith("http"):
                return f"[{txt}]({href})"
            return txt

        if tag in ("b", "strong"):
            return f"**{el.get_text(strip=True)}**"

        if tag in ("i", "em"):
            return f"*{el.get_text(strip=True)}*"

        if tag in ("code", "kbd", "tt"):
            return f"`{el.get_text(strip=True)}`"

        if tag in ("br",):
            return "\n"

        # Recursively get text from children
        parts = []
        for child in el.children:
            part = extract_text(child)
            if part:
                parts.append(part)
        return " ".join(parts)

    def is_heading(tag_name):
        return tag_name in ("h1", "h2", "h3", "h4")

    # Find the first h1 in main (the page title)
    h1 = main.find("h1")
    if h1:
        title = clean_heading_text(h1)
        output_lines.append(f"# {title}")
        output_lines.append("")

    # Process all children of main in order
    pending_text = []

    def flush_text():
        nonlocal pending_text
        if pending_text:
            text = " ".join(pending_text).strip()
            if text:
                output_lines.append(text)
                output_lines.append("")
            pending_text = []

    for child in main.children:
        if not isinstance(child, Tag):
            continue

        tag = child.name
        classes = child.get("class", [])

        # Headings
        if is_heading(tag):
            flush_text()
            title = clean_heading_text(child)
            if title and title not in seen_headings:
                seen_headings.add(title)
                level = int(tag[1])
                # Don't duplicate the h1
                if tag == "h1":
                    continue
                output_lines.append(f"{'#' * level} {title}")
                output_lines.append("")
            continue

        # Code blocks (div.dyn with textarea)
        if "dyn" in classes:
            flush_text()
            textarea = child.find("textarea")
            if textarea:
                code = textarea.get_text().strip()
                if code:
                    if is_plantuml_code(code) or is_nwdiag_code(code):
                        output_lines.append("```plantuml")
                        output_lines.append(code)
                        output_lines.append("```")
                    else:
                        output_lines.append("```")
                        output_lines.append(code)
                        output_lines.append("```")
                    output_lines.append("")
            continue

        # Pre blocks (if any)
        if tag == "pre":
            flush_text()
            code = child.get_text().strip()
            if code:
                output_lines.append("```")
                output_lines.append(code)
                output_lines.append("```")
                output_lines.append("")
            continue

        # Tables
        if tag == "table":
            flush_text()
            rows = child.find_all("tr")
            for row in rows:
                cells = row.find_all(["td", "th"])
                output_lines.append("| " + " | ".join(c.get_text(strip=True) for c in cells) + " |")
            output_lines.append("")
            continue

        # Lists
        if tag == "ul":
            flush_text()
            for li in child.find_all("li", recursive=False):
                li_text = li.get_text(" ", strip=True)
                if li_text:
                    output_lines.append(f"- {li_text}")
            output_lines.append("")
            continue

        if tag == "ol":
            flush_text()
            for idx, li in enumerate(child.find_all("li", recursive=False), 1):
                li_text = li.get_text(" ", strip=True)
                if li_text:
                    output_lines.append(f"{idx}. {li_text}")
            output_lines.append("")
            continue

        # Paragraphs and generic text containers
        if tag in ("p", "div", "span", "section", "article"):
            # Check if this contains a plantuml code image
            imgs = child.find_all("img")
            plantuml_imgs = [img for img in imgs if "/imgw/" in (img.get("src", "")) or "/plantuml/" in (img.get("src", ""))]
            if plantuml_imgs and not child.get_text(strip=True):
                # Pure image block - skip
                continue

            # Check for back-to-top links
            backlinks = child.find_all("a", href=lambda h: h and "backtop" in h)
            if backlinks and len(backlinks) == len(child.find_all()) - len(child.find_all("img")):
                continue

            text = child.get_text(" ", strip=True)
            if not text:
                continue

            # Skip known boilerplate text
            skip_patterns = [
                "Edit in Dokuwiki", "Edit in Asciidoc", "Edit in Markdown",
                "Back to top", "PlantUML Language specification",
                r"^Home$", r"^What's New", r"^Getting Started$",
                r"^Online Server$", r"^Running$", r"^F\.A\.Q\.$",
                r"^Download$", r"^Forum$", r"^Theme$", r"^Preprocessing$",
                r"^Standard Library$", r"^PDF Guide$", r"^Hitchhiker",
            ]
            if any(re.match(p, text) for p in skip_patterns):
                continue

            pending_text.append(text)
            continue

    flush_text()

    # Post-processing: clean up
    final = "\n".join(output_lines)

    # Remove excessive blank lines
    final = re.sub(r"\n{4,}", "\n\n\n", final)
    final = re.sub(r"```plantuml\n\n+", "```plantuml\n", final)
    final = re.sub(r"\n\n+```\n", "\n```\n", final)

    # Strip the trailing TOC (list of repeated section names on one page only)
    lines_final = final.split("\n")
    # Find if last 10% looks like a TOC (mostly single-line, non-code, non-heading entries)
    toc_start = None
    toc_indicators = 0
    for i in range(len(lines_final) - 1, len(lines_final) // 2, -1):
        line = lines_final[i].strip()
        if not line or line.startswith("#") or line.startswith("```"):
            if toc_indicators > 5:
                toc_start = i + 1
                break
        elif not re.match(r'^[-*] ', line) and len(line) < 80:
            toc_indicators += 1
        else:
            toc_indicators = 0

    if toc_start and toc_start < len(lines_final) - 1:
        # Verify it looks like a TOC
        post_lines = [l.strip() for l in lines_final[toc_start:] if l.strip()]
        if len(post_lines) >= 5 and all(
            not l.startswith(("#", "```", "- ", "* ")) for l in post_lines
        ):
            lines_final = lines_final[:toc_start]
            final = "\n".join(lines_final)

    final = final.rstrip() + "\n"

    # Add frontmatter
    title = url_to_title(page_path)
    if page_path.startswith("http://") or page_path.startswith("https://"):
        source_url = page_path
    else:
        source_url = f"{BASE_URL}{page_path}"
    frontmatter = f"""---
title: {title} — PlantUML Official Documentation
source: {source_url}
description: Official documentation for PlantUML {title}
---

"""
    return frontmatter + final


def crawl_page(page_path: str, skip_existing: bool = False, output_dir: str = OUTPUT_DIR) -> dict:
    """Crawl a single page and save it. Returns a result dict."""
    page_path = normalize_path(page_path)
    filename = url_to_filename(page_path)
    output_path = os.path.join(output_dir, filename)
    result = {"page": page_path, "filename": filename}

    if skip_existing and os.path.exists(output_path):
        result.update(status="skipped", ok=True)
        return result

    try:
        html = fetch_page(page_path)
    except Exception as e:
        result.update(status="failed", ok=False, error=str(e))
        return result

    try:
        markdown = extract_page_content(html, page_path)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w") as f:
            f.write(markdown)
        code_blocks = markdown.count("```plantuml")
        result.update(status="ok", ok=True, chars=len(markdown), code_blocks=code_blocks)
    except Exception as e:
        result.update(status="failed", ok=False, error=f"parse: {e}")
        import traceback
        traceback.print_exc()
    return result


MAX_WORKERS = 4


def _worker(task_queue: queue.Queue, results: queue.Queue, skip_existing: bool, output_dir: str, delay: float = 0) -> None:
    """Worker loop: pull page paths off the task queue, crawl, push result."""
    while True:
        page = task_queue.get()
        if page is None:  # sentinel: no more work
            task_queue.task_done()
            break
        result = crawl_page(page, skip_existing, output_dir)
        results.put(result)
        task_queue.task_done()
        if delay > 0 and result["status"] != "skipped":
            time.sleep(delay)


def crawl_batch(pages, skip_existing: bool = False, output_dir: str = OUTPUT_DIR, max_workers: int = MAX_WORKERS, delay: float = 0.5) -> dict:
    """Crawl many pages in parallel (max_workers worker threads) with a tqdm progress bar.

    Uses a producer/worker-queue pattern: tasks go in, results come out, and the
    main thread consumes the result queue so it can render cumulative progress.

    pages: iterable of page paths (str) or (name, path) tuples.
    Returns {"ok": n, "failed": n, "skipped": n, "errors": [...]}.
    """
    def to_path(page):
        if isinstance(page, tuple):
            return page[1]
        return page

    paths = [to_path(p) for p in pages]

    task_queue = queue.Queue()
    results = queue.Queue()
    for p in paths:
        task_queue.put(p)
    for _ in range(max_workers):
        task_queue.put(None)  # one sentinel per worker

    workers = [
        threading.Thread(target=_worker, args=(task_queue, results, skip_existing, output_dir, delay), daemon=True)
        for _ in range(max_workers)
    ]
    for w in workers:
        w.start()

    summary = {"ok": 0, "failed": 0, "skipped": 0, "errors": []}
    with tqdm(total=len(paths), desc="Crawling", unit="page", dynamic_ncols=True) as pbar:
        for _ in range(len(paths)):
            result = results.get()
            status = result["status"]
            summary[status] = summary.get(status, 0) + 1
            if status == "failed":
                summary["errors"].append(f"{result['filename']}: {result.get('error', 'unknown')}")
            pbar.set_postfix_str(f"{summary['ok']} ok, {summary['failed']} failed")
            pbar.update(1)

    for w in workers:
        w.join()

    return summary


def main():
    skip_existing = "--skip-existing" in sys.argv

    def parse_flag(name):
        for arg in sys.argv[1:]:
            if arg.startswith(f"--{name}="):
                return arg.split("=", 1)[1]
            if arg == f"--{name}":
                i = sys.argv.index(arg)
                if i + 1 < len(sys.argv):
                    return sys.argv[i + 1]
        return None

    max_workers = MAX_WORKERS
    delay = 0.5
    for arg in sys.argv[1:]:
        if arg == "-n" or arg.startswith("-n=") or arg.startswith("--workers="):
            raw = arg.split("=", 1)[1] if "=" in arg else sys.argv[sys.argv.index(arg) + 1]
            try:
                max_workers = int(raw)
            except ValueError:
                print(f"Invalid worker count: {raw}")
                sys.exit(1)
        if arg.startswith("--delay="):
            try:
                delay = float(arg.split("=", 1)[1])
            except ValueError:
                print(f"Invalid delay: {arg}")
                sys.exit(1)

    KNOWN_FLAGS = {"--url", "--sitemap", "--page", "--section",
                   "--skip-existing", "--workers", "--delay", "-n"}
    for arg in sys.argv[1:]:
        if arg.startswith("-") and arg not in KNOWN_FLAGS:
            name = arg.split("=", 1)[0]
            if name in KNOWN_FLAGS:
                continue
            print(f"Unknown flag: {arg}")
            sys.exit(1)

    # Direct URL mode
    url = parse_flag("url")
    if url is not None:
        print(f"Crawling URL: {url}")
        result = crawl_page(normalize_path(url), skip_existing)
        if result["status"] == "failed":
            print(f"  FAILED: {result.get('error')}")
        elif result["status"] == "skipped":
            print("  SKIP (exists)")
        else:
            print(f"  OK → {result['filename']} ({result['chars']} chars, {result['code_blocks']} code blocks)")
        sys.exit(0 if result["ok"] else 1)

    # Sitemap YAML mode: crawl every section's pages into src/<slug>/<page>.md
    sitemap_path = parse_flag("sitemap")
    if sitemap_path is not None:
        sections = load_sitemap(sitemap_path)
        print(f"Crawling {len(sections)} sections from {sitemap_path} ({max_workers} workers)")
        print(f"Output directory: {OUTPUT_DIR}")
        print()

        total_ok = total_failed = total_skipped = 0
        for i, section in enumerate(sections, 1):
            slug = section["slug"]
            section_dir = os.path.join(OUTPUT_DIR, slug)
            print(f"[{i}/{len(sections)}] {section['title']} ({slug}) — {len(section['subsections'])} pages")
            summary = crawl_batch(section["subsections"], skip_existing, section_dir, max_workers, delay)
            total_ok += summary["ok"]
            total_failed += summary["failed"]
            total_skipped += summary["skipped"]
            for err in summary["errors"]:
                print(f"  FAILED: {err}")
            print()

        print(f"Done: {total_ok} ok, {total_failed} failed, {total_skipped} skipped")
        sys.exit(0 if total_failed == 0 else 1)

    # Single page mode
    for arg in sys.argv[1:]:
        if arg.startswith("--page="):
            page_path = arg.split("=", 1)[1]
            if not page_path.startswith("/"):
                page_path = "/" + page_path
            print(f"Crawling single page: {page_path}")
            result = crawl_page(page_path, skip_existing)
            if result["status"] == "failed":
                print(f"  FAILED: {result.get('error')}")
            elif result["status"] == "skipped":
                print("  SKIP (exists)")
            else:
                print(f"  OK → {result['filename']} ({result['chars']} chars, {result['code_blocks']} code blocks)")
            sys.exit(0 if result["ok"] else 1)

    # Section mode: crawl every page listed under a sitemap section
    for arg in sys.argv[1:]:
        if arg.startswith("--section="):
            requested = arg.split("=", 1)[1].strip().lower()
            sections = fetch_sitemap()
            section = None
            for s in sections:
                if s["slug"].lower() == requested or s["title"].lower() == requested:
                    section = s
                    break
            if section is None:
                available = ", ".join(s["slug"] for s in sections)
                print(f"Unknown section '{requested}'. Available: {available}")
                sys.exit(1)

            section_dir = os.path.join(OUTPUT_DIR, section["slug"])
            print(f"Crawling section: {section['title']} ({section['slug']})")
            print(f"  {len(section['pages'])} pages → {section_dir}")
            print()

            summary = crawl_batch(section["pages"], skip_existing, section_dir, max_workers, delay)
            for err in summary["errors"]:
                print(f"  FAILED: {err}")
            print()
            print(f"Done: {summary['ok']} ok, {summary['failed']} failed, {summary['skipped']} skipped")
            sys.exit(0 if summary["failed"] == 0 else 1)

    print(f"Crawling {len(PAGES)} pages from {BASE_URL} ({max_workers} workers)")
    print(f"Output directory: {OUTPUT_DIR}")
    print()

    summary = crawl_batch(PAGES, skip_existing, max_workers=max_workers, delay=delay)
    for err in summary["errors"]:
        print(f"  FAILED: {err}")
    print()
    print(f"Done: {summary['ok']} ok, {summary['failed']} failed, {summary['skipped']} skipped")


if __name__ == "__main__":
    main()
