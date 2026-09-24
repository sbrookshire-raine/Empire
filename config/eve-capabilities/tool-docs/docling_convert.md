---
name: docling_convert
toolbelt: file_ops
one_line: Convert a local PDF/Office file to Markdown with Docling and stage it under the Resource Queue
---

## Description (verbatim from the tool schema, pre-R-03)

Convert a local PDF/Office file to Markdown with Docling and stage it under the Resource Queue. Does not write Cognee — follow with cognee_remember or Workbench upload when ready.

## Parameters

- `input_path` — Absolute path to PDF/Office file.
- `output_path` — Optional output .md path (default Resource Queue).

## Usage

Registered by the Toolbelt category `file_ops`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
