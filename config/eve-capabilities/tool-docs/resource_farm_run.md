---
name: resource_farm_run
toolbelt: always
one_line: Resource farm: search GitHub, cache READMEs, write scout Disassembly Cards for processed-material catalog
---

## Description (verbatim from the tool schema, pre-R-03)

Resource farm: search GitHub, cache READMEs, write scout Disassembly Cards for processed-material catalog. Omit query for catalog status only. Never writes Cognee. Heptabase: publishes new orange cards when architect_confirm=true and board is healthy.

## Parameters

- `query` — GitHub search keywords. Omit to list already-farmed repos and recent scout cards.
- `search_limit` — Max GitHub search hits (default 10).
- `max_new_cards` — Max new scout cards after dedupe (default 5).
- `architect_confirm` — Required true to publish new cards to Heptabase in this run.
- `publish_heptabase` — true=try board when confirmed; false=local cards only; omit=auto from confirm + board health.
- `note` — Optional note stored in GitHub cache provenance.

## Usage

Registered by the Toolbelt category `always`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
