# PlantUML Docs

Crawled official [PlantUML](https://plantuml.com) documentation pages as clean markdown — code blocks wrapped in ```` ```plantuml ```` fences, images stripped (markdown preview handles rendering).

## Quick start

```bash
# Crawl all 19 diagram-type pages
python3 local/crawl-plantuml-docs.py

# Crawl a single page
python3 local/crawl-plantuml-docs.py --page=/sequence-diagram

# Skip already-crawled pages
python3 local/crawl-plantuml-docs.py --skip-existing
```

## Structure

```
local/
  crawl-plantuml-docs.py   # The crawler script
src/
  sequence-diagram.md       # Sequence diagrams
  use-case-diagram.md       # Use case diagrams
  class-diagram.md          # Class diagrams
  activity-diagram-beta.md  # Activity diagrams (beta)
  component-diagram.md      # Component diagrams
  state-diagram.md          # State diagrams
  object-diagram.md         # Object diagrams
  deployment-diagram.md     # Deployment diagrams
  timing-diagram.md         # Timing diagrams
  regex.md                  # Regex diagrams
  nwdiag.md                 # Network diagrams (nwdiag)
  salt.md                   # Salt (Wireframe) GUI mockups
  archimate-diagram.md      # ArchiMate diagrams
  gantt-diagram.md          # Gantt charts
  mindmap-diagram.md        # Mind maps
  wbs-diagram.md            # Work Breakdown Structure
  ebnf.md                   # Extended Backus-Naur Form
  json.md                   # JSON diagrams
  yaml.md                   # YAML diagrams
```

## Output format

Every page is a `.md` file with:
- YAML frontmatter (`title`, `source`, `description`)
- Clean headings (no edit-link pollution)
- PlantUML code blocks in ```` ```plantuml ```` fences
- No rendered images or navigation boilerplate

## Requirements

- Python 3
- `requests`, `beautifulsoup4`, `lxml`

```bash
pip install requests beautifulsoup4 lxml
```
