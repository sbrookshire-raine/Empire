---
name: web_scout
toolbelt: web_scout
one_line: Fetch one public http(s) page URL and cache markdown under 04_Thought_Experiments/web_cache
---

## Description (verbatim from the tool schema, pre-R-03)

Fetch one public http(s) page URL and cache markdown under 04_Thought_Experiments/web_cache. Not a search engine — needs a full URL. Auto-admits Web Scout when headroom allows. Does NOT write Cognee.

## Parameters

- `url` — Full page URL to fetch (https://…). Bare domains ok; not a search query.
- `note` — Optional Architect note.

## Usage

Registered by the Toolbelt category `web_scout`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
