---
name: wiki_remember
toolbelt: always
one_line: Remember a successful Wikipedia EXTRACT (fields/tables/lists) into Cognee
---

## Description (verbatim from the tool schema, pre-R-03)

Remember a successful Wikipedia EXTRACT (fields/tables/lists) into Cognee. Only when the Architect explicitly asks to save/keep/remember. Rejects empty extracts. Never bulk-ingests wiki_md.

## Parameters

- `subject` — Encyclopedia title just extracted.
- `year` — Snapshot year (default 2026).
- `dataset` — Cognee dataset (default eve_memory).
- `need_hint` — Same hint used for the extract.
- `extract_id` — Optional extract_id from a prior wiki_extract ok result.

## Usage

Registered by the Toolbelt category `always`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
