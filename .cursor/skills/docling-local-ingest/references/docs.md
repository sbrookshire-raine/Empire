# Docling local ingest — EMPIRE reference pointers

## Upstream

- Repo: https://github.com/docling-project/docling
- Job: PDF / Office / (optional) ASR → structured Markdown, local/air-gapped capable
- PyPI: `docling`

## EMPIRE pipeline

```
local file → Docling → .md → mock_data_ingest/ → scripts/ingest-mock.ps1 → Cognee (Ollama embeds)
```

- PocketBase: optional job tracking via existing ingestion_jobs helpers
- Do **not** enable MarkItDown Azure extras
- Wiki overnight path (`D:\wiki_md`) already Markdown — Docling optional

## Competitors (declared losers for primary ingest)

- microsoft/markitdown — keep as lean CLI reference only
- LiteDoc / deepdiy/pdf2md — graveyard (redundant)
- Cloud OCR / Azure Document Intelligence — graveyard

## Related skills

- `cognee-memory-pipeline` — graph memory after Markdown exists
- `docs-guide-scraper` — web docs sites (not binary Office)
- `data-processor` — light PDF/CSV tooling, not Docling replacement
