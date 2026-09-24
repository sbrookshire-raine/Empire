---
name: wiki_scratch_upsert
toolbelt: wiki_local
one_line: Save a short bridging fact to the Wikipedia research scratchpad for multi-hop work
---

## Description (verbatim from the tool schema, pre-R-03)

Save a short bridging fact to the Wikipedia research scratchpad for multi-hop work. Use between hops (retain facts, drop raw markdown). Does NOT write Cognee.

## Parameters

- `text` — Bridging fact to retain.
- `title` — Source page title.
- `session_id` — Chat session id if known.

## Usage

Registered by the Toolbelt category `wiki_local`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
