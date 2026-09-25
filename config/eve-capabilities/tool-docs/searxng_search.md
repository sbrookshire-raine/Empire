---
name: searxng_search
toolbelt: web_research
one_line: Search the public web through the local SearXNG instance and get result titles + URLs + snippets
---

## Description (verbatim from the tool schema, pre-R-03)

Search the public web through the local SearXNG instance and get result titles + URLs + snippets. Use when the question needs current or outside knowledge; then read a page with web_scout.

## Parameters

- `query` — What to search for — a few keywords, not a URL.
- `limit` — Max results to return (default 5, hard cap 20).

## Usage

Registered by the Toolbelt category `web_research`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
