# Embedding A/B (test datasets only)

Production Cognee stays on **`nomic-embed-text`**.

## Optional trial

Pull a small upgrade candidate:

```powershell
ollama pull qwen3-embedding:0.6b
```

Create a **new** Cognee dataset (e.g. `embed_ab_test`) and ingest a tiny fixture set
only. Compare recall quality against `eve_core` / `primitives_test`.

## Do not

- Re-embed all of `eve_memory` without Architect approval
- Make `qwen3-embedding:8b` the default (fights chat VRAM on 16 GB)
- Change `config/cognee.env` embed model until the A/B wins

## Helper

```powershell
.\scripts\embedding-ab-notes.ps1
```

Prints the checklist; does not migrate data.
