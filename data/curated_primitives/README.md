# Curated Primitives — Fuel vs Directives

Micro-deliverable: prove Cognee graph + recall on a small, high-signal set.
Wikipedia (`wikipedia_2017`) is **halted and preserved** — do not prune it.

## Folders

| Path | Role |
|------|------|
| `raw_materials/` | **Fuel only** — domain Markdown/PDF-derived text → Cognee dataset `primitives_test` |
| `directives/` | **Lens only** — system prompt + extraction lenses → LLM/Eve/Cursor chat, **never** `cognee.add` |
| `status/` | Last ingest job JSON |

## Models

- Graph cognify: `huihui_ai/qwen2.5-coder-abliterate:14b` (Ollama)
- Embeddings: `nomic-embed-text` (required by Cognee for recall)
- Do not put the 14b model name into Fuel files

## Commands

```powershell
# Convert new PDFs into raw_materials (if needed)
.\venv\Scripts\python.exe .cursor\skills\docling-local-ingest\scripts\main.py "path\to\file.pdf" -o data\curated_primitives\raw_materials\name.md

# Ingest + cognify + smoke recall
.\scripts\ingest-curated-primitives.ps1
```

## How to query

**Cursor:** Attach/paste `directives/SYSTEM.md`, then use MCP `cognee_recall` with dataset `primitives_test`.

**Eve:** `.\scripts\start-eve.ps1` → talk on port 2000; recall skill should target `primitives_test` for this pilot.

## Definition of Done

- [x] Wiki overnight stopped; `wikipedia_2017` intact (do not prune)
- [x] Fuel MD in `raw_materials/` (no directives mixed in) — Codex + Learning Techniques
- [x] `primitives_test` cognified (graph LLM: `huihui_ai/qwen2.5-coder-abliterate:14b`)
- [x] Smoke recall filtered to Fuel markers (global pgvector otherwise bleeds Wikipedia)
- [ ] Second PDF (*Learning, Remembering, Believing*, ~20MB scan) — Docling/pypdf text extract failed; re-convert with better OCR later, then re-ingest

## Notes

- Directives never go into `cognee.add`.
- With access control off, recall post-filters on dataset document names (and Fuel headers) because Wikipedia shares the global pgvector index.
- Set `CACHING=false` during curated ingest/recall so session cache does not pin the 14b LLM in VRAM while nomic embeds queries.
- If Cognee blocks writes with migration errors after a wiki-scale DB, stamp head (`cognee-cli stamp head -f`) and clear `global_migration_last_error` — EdgeType rekey hits Postgres 32767-arg limits on large stores.
