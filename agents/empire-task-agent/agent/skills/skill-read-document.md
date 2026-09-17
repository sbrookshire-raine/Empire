# skill-read-document

Use when the Architect asks you to read a local document (PDF, DOCX, PPTX, XLSX, HTML, or plain text/markdown) and summarize or extract from it.

## Mission

Extract text from a local file (MarkItDown first, Docling fallback) and answer from what's actually inside. Never invent content.

## Tools

- `read_document` — returns provenance-stamped markdown content.

## How to work a goal

1. Confirm the path is under an allowlisted root.
2. Call `read_document` with the file path.
3. Summarize the content; quote short passages only.

## Hard rules

- Read-only; never writes Cognee (scratch only).
- Network paths are forbidden.
- For Workbench files prefer `workbench_read_file`; use `read_document` for rich/Office formats.
