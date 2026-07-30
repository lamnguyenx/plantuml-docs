#!/usr/bin/env python3
"""
Crawls plantuml.com documentation pages and saves them as clean markdown.
- Strips navigation boilerplate, edit links, rendered images
- Wraps @startuml/@startsalt code blocks in ```plantuml fences
- Adds YAML frontmatter with source URL

Usage:
  python3 crawl-plantuml-docs.py              # crawl all pages
  python3 crawl-plantuml-docs.py --page /salt  # crawl single page
  python3 crawl-plantuml-docs.py --skip-existing  # skip already-crawled pages
"""

import os
import re
import sys
import time
import requests
from bs4 import BeautifulSoup, Tag, NavigableString

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


def url_to_filename(path: str) -> str:
    """Convert URL path to output filename."""
    clean = path.strip("/")
    return clean + ".md"


def url_to_title(path: str) -> str:
    """Convert URL path to a page title."""
    clean = path.strip("/").replace("-", " ").replace("_", " ")
    return " ".join(word.capitalize() for word in clean.split())


def fetch_page(path: str) -> str:
    """Fetch a page and return its HTML content."""
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
    frontmatter = f"""---
title: {title} — PlantUML Official Documentation
source: {BASE_URL}{page_path}
description: Official documentation for PlantUML {title}
---

"""
    return frontmatter + final


def crawl_page(page_path: str, skip_existing: bool = False) -> bool:
    """Crawl a single page and save it."""
    filename = url_to_filename(page_path)
    output_path = os.path.join(OUTPUT_DIR, filename)

    if skip_existing and os.path.exists(output_path):
        print(f"  SKIP (exists): {filename}")
        return True

    print(f"  Fetching {BASE_URL}{page_path} ...", end=" ", flush=True)

    try:
        html = fetch_page(page_path)
        print("OK", end=" ", flush=True)
    except Exception as e:
        print(f"FAILED: {e}")
        return False

    try:
        markdown = extract_page_content(html, page_path)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w") as f:
            f.write(markdown)
        code_blocks = markdown.count("```plantuml")
        print(f"→ {filename} ({len(markdown)} chars, {code_blocks} code blocks)")
        return True
    except Exception as e:
        print(f"PARSE FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    skip_existing = "--skip-existing" in sys.argv

    # Single page mode
    for arg in sys.argv[1:]:
        if arg.startswith("--page="):
            page_path = arg.split("=", 1)[1]
            if not page_path.startswith("/"):
                page_path = "/" + page_path
            print(f"Crawling single page: {page_path}")
            success = crawl_page(page_path, skip_existing)
            sys.exit(0 if success else 1)

    print(f"Crawling {len(PAGES)} pages from {BASE_URL}")
    print(f"Output directory: {OUTPUT_DIR}")
    print()

    success = 0
    failed = 0
    skipped = 0

    for i, page_path in enumerate(PAGES, 1):
        print(f"[{i}/{len(PAGES)}]", end=" ")
        ok = crawl_page(page_path, skip_existing)
        if ok:
            success += 1
        else:
            failed += 1
        # Be polite between requests
        if i < len(PAGES):
            time.sleep(0.5)

    print()
    print(f"Done: {success} ok, {failed} failed, {skipped} skipped")


if __name__ == "__main__":
    main()
