# Embedding / retrieval A/B (test only)

Production Cognee stays on **`nomic-embed-text`**. Do not change `config/cognee.env` until the Architect approves a winning embed model.

## Embedding A/B eval (F-18)

Compare **nomic-embed-text** (production) vs **qwen3-embedding:0.6b** (trial) on a small fixture corpus. This is **eval only** — it does not ingest or re-embed `eve_memory`.

### Quick run

```powershell
# Optional: pull trial model
.\scripts\embedding-ab.ps1 pull

# Check Ollama has both models
.\scripts\embedding-ab.ps1 status

# Run fixture hit-rate eval
.\scripts\embedding-ab.ps1 eval
```

Or directly:

```powershell
.\venv\Scripts\python.exe -m pipeline.embedding_ab eval
.\venv\Scripts\python.exe -m pipeline.embedding_ab status
```

### What it does

1. Loads `data/eval/embedding_ab/cases.json` (query + candidate snippets + expected top IDs).
2. Embeds each query and candidate via Ollama (`/api/embed` with fallback to `/api/embeddings`).
3. Ranks by cosine similarity and counts **hits** (expected ID in top-k) per model.
4. Writes:
   - JSON report under `data/eval/embedding_ab/embedding_ab_*.json`
   - Acceptance YAML under `data/eval/acceptance/embedding_ab_*.yaml` (`status: pending_architect`)

Config: `config/embedding-ab.json`.

### Optional Cognee trial ingest

Only after a fixture win and Architect approval:

```powershell
ollama pull qwen3-embedding:0.6b
```

Create dataset **`embed_ab_test`** only. Ingest a tiny fixture set. Compare recall vs `eve_core` / `primitives_test`. **Never** re-embed all of `eve_memory` without explicit approval.

See also `scripts/embedding-ab-notes.ps1` for the checklist.

## Retrieval rerank eval (F-23 — forged)

Lexical rerank always available; optional CrossEncoder via `EMPIRE_RERANK_MODEL`.

```powershell
.\venv\Scripts\python.exe -m pipeline.retrieval_rerank eval
```

Eve Toolbelt **Retrieval Rerank** (default OFF) exposes `retrieval_rerank`.

Acceptance YAML lands under `data/eval/acceptance/retrieval_rerank_*.yaml`.

## Do not

- Re-embed all of `eve_memory` without Architect approval
- Make large embedding models default on 16 GB VRAM
- Change `config/cognee.env` embed model until A/B wins on fixtures **and** optional `embed_ab_test` ingest
