#!/usr/bin/env python3
"""
Fetch plantuml.com/sitemap and generate src/sitemap.yaml.

Sections map to directory slugs; subsections are URL paths without the
leading "/" (used to look up the markdown files under src/<slug>/).

Usage:
  python3 get_sitemap.py
"""

import os
import re
import sys

import requests
import yaml
from bs4 import BeautifulSoup, Tag

BASE_URL = "https://plantuml.com"

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
    return SECTION_SLUGS.get(title, slugify(title))


def fetch_sitemap():
    """Fetch the sitemap and return sections as [{"title", "slug", "pages": [...]}]."""
    resp = requests.get(f"{BASE_URL}/sitemap", timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "lxml")

    main = soup.find("main")
    run_div = next((d for d in main.find_all("div") if d.get("id") == "run"), None)
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
                continue
            title = h2.get_text(strip=True)
            current = {"title": title, "slug": section_slug(title), "pages": []}
            sections.append(current)
        elif child.name == "a" and "run1" in classes and current is not None:
            href = child.get("href", "")
            if href:
                current["pages"].append(href.lstrip("/"))
    return sections


def main():
    output = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src", "sitemap.yaml")
    sections = fetch_sitemap()
    data = [
        {"title": s["title"], "slug": s["slug"], "subsections": s["pages"]}
        for s in sections
    ]
    os.makedirs(os.path.dirname(output), exist_ok=True)
    with open(output, "w") as f:
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True, default_flow_style=False)
    total = sum(len(s["pages"]) for s in sections)
    print(f"Wrote {output} ({len(sections)} sections, {total} subsections)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
