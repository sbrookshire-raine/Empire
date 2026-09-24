---
name: read_document
toolbelt: read_document
one_line: Extract text/markdown from a local document (md/txt/csv/json/pdf/docx/pptx/xlsx/html)
---

## Description (verbatim from the tool schema, pre-R-03)

Extract text/markdown from a local document (md/txt/csv/json/pdf/docx/pptx/xlsx/html). Uses MarkItDown with Docling fallback; read-only, offline. Returns provenance-stamped content. Never writes Cognee.

## Parameters

- `input_path` — Allowlisted local file path to read.
- `max_chars` — Max characters to return (default 200000).

## Usage

Registered by the Toolbelt category `read_document`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
