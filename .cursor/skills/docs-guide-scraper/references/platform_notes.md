# Platform notes (docs-guide-scraper)

Local EMPIRE reference — condensed from Gumloop TOOL_GATHERER scrape experience.

| Platform | Discovery | Fetch | Cleanup |
|---|---|---|---|
| Mintlify | `llms.txt` / `llms-full.txt` | append `.md` to doc URLs when supported | Tip/Card/Steps → plain Markdown |
| Fumadocs | sitemap.xml | HTML + readability | exclude prev/next nav siblings |
| Docusaurus | sitemap or llms.txt | web fetch usually enough | admonitions → blockquotes |
| Nextra | nav crawl | rendered `<main>` | callout divs → blockquotes |

Use `scripts/mdx_cleaners.py` before export. Cap crawls at 80–300 pages depending on scope.
