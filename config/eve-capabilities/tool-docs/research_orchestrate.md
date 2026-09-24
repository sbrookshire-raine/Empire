---
name: research_orchestrate
toolbelt: web_research
one_line: Run Research Autopilot: admit read-only limbs, query Wikipedia (Weaviate), GitHub, Product Hunt feed, optiona…
---

## Description (verbatim from the tool schema, pre-R-03)

Run Research Autopilot: admit read-only limbs, query Wikipedia (Weaviate), GitHub, Product Hunt feed, optional web URL. Requires Research Partner mode ON. Never writes Cognee.

## Parameters

- `query` — Research question or search terms.
- `sources` — Sources to query (default wiki+github+producthunt).
- `github_limit` — Max GitHub repos (default 8).
- `web_url` — Required when sources includes web.
- `note` — Optional Architect note for caches.

## Usage

Registered by the Toolbelt category `web_research`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
