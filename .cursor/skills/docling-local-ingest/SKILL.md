---
name: docling-local-ingest
description: Converts local PDF/Office (and optional ASR) documents to Markdown with IBM Docling for air-gapped Cognee staging. Use when ingesting PDFs, DOCX, PPTX, or scanned docs into mock_data_ingest or the wiki pipeline; prefer this over MarkItDown/LiteDoc/pdf2md for Build1 RAG. No cloud embedding or Azure Document Intelligence APIs.
---

# Docling Local Ingest (Build1)

Run **docling-project/docling** fully locally to produce Markdown, then stage for Cognee. Inference/embeddings for memory stay on **Ollama** via existing Cognee wiring—Docling only converts documents.

## Winner vs alternatives

| Tool | Role |
|---|---|
| **Docling (this skill)** | Bin 1 winner — local PDF/Office→MD for RAG |
| microsoft/markitdown | Bin 2 lean CLI fallback (`convert_local` only) |
| LiteDoc / deepdiy/pdf2md | Bin 3 — redundant |
| markitdown Azure extras | Bin 3 — cloud |
| `data-processor` pdf_tools | Keep for light text/table pulls; Docling for heavy docs |

## Install

```bash
pip install docling
```

Use CPU wheels by default. Only enable optional ASR extras if the user needs audio and models are local.

## Workflow

1. Place source files outside OneDrive sync hotspots when possible (see `docs/ONEDRIVE.md`).
2. Convert with Docling CLI or `scripts/main.py`.
3. Write `.md` into `mock_data_ingest/` or approved staging.
4. Ingest via `.\scripts\ingest-mock.ps1` / `empire-cognee` — **no** cloud embed APIs.
5. For Wikipedia MD bulk on `D:\wiki_md`, Docling is usually unnecessary (already Markdown).

## Agent commands

```bash
# Helper (preferred entry for agents)
python .cursor/skills/docling-local-ingest/scripts/main.py path/to/file.pdf -o mock_data_ingest/file.md

# Upstream CLI (if installed)
docling path/to/file.pdf --to md
```

Exact Docling CLI flags vary by version—prefer `scripts/main.py`, which wraps the Python API and fails clearly if Docling is missing.

## Hard rules

- Local files only; do not require OpenAI/Anthropic for conversion
- Skip Azure Document Intelligence / paid OCR clouds
- Do not invent React frontends for a Docling UI—CLI/scripts only
- Frontend remains HTMX/Alpine CDN if any status UI is built later

## Scripts / references

- `scripts/main.py` — convert one file → Markdown path
- [references/docs.md](references/docs.md)
