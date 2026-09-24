---
name: structured_extract
toolbelt: structured_extract
one_line: Extract DocumentMetadata (title, author, date, tags, summary) from text via local llama.cpp worker (Ollama JS…
---

## Description (verbatim from the tool schema, pre-R-03)

Extract DocumentMetadata (title, author, date, tags, summary) from text via local llama.cpp worker (Ollama JSON fallback). Scratch cache only — never Cognee. Requires Structured Extract Toolbelt.

## Parameters

- `text` — Plain text to extract from.
- `prefer` — Backend preference (default llama).
- `note` — Optional Architect note.

## Usage

Registered by the Toolbelt category `structured_extract`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
