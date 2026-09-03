Use when the user asks about ingested curated primitives, Universal Primitives, learning/scaffolding
parallels, Pattern Weaver memory, or dataset `primitives_test`. Also use for mock Slack/GitHub/email
fixtures when those are named.

## Fuel vs Directives (critical)

- **Fuel** lives in `data/curated_primitives/raw_materials/` and is stored in Cognee dataset **`primitives_test`**.
- **Directives** live in `data/curated_primitives/directives/SYSTEM.md` (and `LENS_*.md`). They are the
  query lens — do **not** treat them as graph documents.
- Wikipedia dataset `wikipedia_2017` may exist but is halted for this pilot; prefer `primitives_test`
  unless the user explicitly asks about Wikipedia.

## Workflow

1. Call `cognee_recall` with a focused query and **`dataset=primitives_test`**.
2. Synthesize using Pattern Weaver vocabulary when relevant.
3. Cite concrete passages from recall; do not invent facts.

Do **not** use this skill for general user interests or `eve_memory` — use `memory-recall` instead.

## Prerequisites

- Curated ingest: `.\scripts\ingest-curated-primitives.ps1`
- Ollama: `huihui_ai/qwen2.5-coder-abliterate:14b` (graph) + `nomic-embed-text` (embeddings)
- Dashboard: http://127.0.0.1:8080/primitives.html

## If recall is empty

Suggest running curated ingest, confirm dataset name `primitives_test`, then retry.
