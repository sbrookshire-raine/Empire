---
name: promote_wiki_cache
toolbelt: wiki_local
one_line: Explicitly promote a wiki_cache .md file into Cognee memory
---

## Description (verbatim from the tool schema, pre-R-03)

Explicitly promote a wiki_cache .md file into Cognee memory. Never automatic — only when the Architect asks. Compare files route to truth_drift; single hits to eve_memory unless dataset override is set.

## Parameters

- `path` — Full path to a wiki_cache markdown file.
- `dataset` — Optional Cognee dataset override (eve_memory, truth_drift, eve_core, primitives_test). Omit to auto-route from cache kind.

## Usage

Registered by the Toolbelt category `wiki_local`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
