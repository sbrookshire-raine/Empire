# Embedding / retrieval A/B (test only)

Production Cognee stays on **`nomic-embed-text`**.

## Embedding trial (optional)

```powershell
ollama pull qwen3-embedding:0.6b
.\scripts\embedding-ab-notes.ps1
```

Create a **new** Cognee dataset (e.g. `embed_ab_test`) only. Do not re-embed `eve_memory`.

## Retrieval rerank eval (forged)

Lexical rerank always available; optional CrossEncoder via `EMPIRE_RERANK_MODEL`.

```powershell
.\venv\Scripts\python.exe -m pipeline.retrieval_rerank eval
```

Eve Toolbelt **Retrieval Rerank** (default OFF) exposes `retrieval_rerank`.

Acceptance YAML lands under `data/eval/acceptance/retrieval_rerank_*.yaml`.

## Do not

- Re-embed all of `eve_memory` without Architect approval
- Make large embedding models default on 16 GB VRAM
- Change `config/cognee.env` embed model until A/B wins
