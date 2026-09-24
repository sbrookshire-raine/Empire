---
name: docs_guide_scrape
toolbelt: tool_forge
one_line: Scrape an official documentation site into one Markdown guide under harvest_cache (llms.txt / sitemap discove…
---

## Description (verbatim from the tool schema, pre-R-03)

Scrape an official documentation site into one Markdown guide under harvest_cache (llms.txt / sitemap discovery). Does not auto-ingest to Cognee. Requires Tool Forge Toolbelt.

## Parameters

- `root_url` — Documentation root URL, e.g. https://docs.example.com
- `max_pages` — Page cap (default 80).
- `note` — Optional provenance note.

## Usage

Registered by the Toolbelt category `tool_forge`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
