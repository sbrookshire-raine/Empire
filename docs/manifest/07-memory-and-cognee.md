# 07 — Memory and Cognee

EMPIRE uses **Cognee 1.0** for graph + vector memory: `remember`, `recall`, `improve`, `forget`.

## Datasets

| Dataset | Source | Use |
|---------|--------|-----|
| **`eve_memory`** | Eve Workbench Memory tab uploads | Default for user documents |
| **`primitives_test`** | `data/curated_primitives/raw_materials/` | Curated primitives pilot |
| **`mock`** | `mock_data_ingest/` fixtures | Development / tests |
| `wikipedia_2017` | Wiki pipeline (halted) | Do not add new data |

### Fuel vs directives (curated)

- **Fuel** → `raw_materials/*.md` → ingest → Cognee
- **Directives** → `directives/SYSTEM.md`, `LENS_*.md` → paste into chat as lens, **never** `cognee.add`

See [data/curated_primitives/README.md](../../data/curated_primitives/README.md).

## Configuration

Primary file: `config/cognee.env` (gitignored — copy from `config/cognee.env.example`).

Key settings:

| Variable | Typical value | Role |
|----------|---------------|------|
| `LLM_MODEL` | `llama3.1:latest` | Cognee graph/cognify LLM |
| `EMBEDDING_MODEL` | `nomic-embed-text:latest` | All embeddings |
| `EMBEDDING_ENDPOINT` | `http://localhost:11434/api/embed` | Ollama embed API |
| `SYSTEM_ROOT_DIRECTORY` | `V:\Cognee` | On-disk Cognee root |
| `DB_*` / `VECTOR_DB_*` / `GRAPH_DATABASE_*` | Postgres localhost | Metadata + pgvector |

**Chat model ≠ Cognee LLM:** Eve's active chat model (`ollama-active-model.json`) is independent of `LLM_MODEL` in cognee.env.

## Storage layout

### VHDX (production)

Heavy storage on **NTFS VHDX** mounted as `V:`:

- Backing file: `I:\EMPIRE_VHDX\empire_cognee.vhdx` (example)
- Cognee root: `V:\Cognee`

Details: [COGNEE_VHDX.md](../COGNEE_VHDX.md)

### Upload staging

Workbench uploads:

```
data/eve_memory/uploads/   # saved files per job
data/eve_memory/jobs/      # job JSON state
```

### Cross-process lock

```
%LOCALAPPDATA%\EMPIRE\cognee.lock
```

Serializes Cognee access between MCP, memory worker, CLI, and Eve tools.

## Workbench upload flow

1. `POST /api/memory/upload` (multipart)
2. `memory_api.py` validates, queues job
3. Subprocess: `python -m pipeline.cognee_worker ingest-files --path ... --dataset eve_memory`
4. States: `queued` → `converting` (PDF) → `embedding` → `ready` | `failed`
5. UI polls `GET /api/memory/jobs/:id`

Embed-only fast path skips heavy cognify when `full_graph` is false (default).

## Pipeline workers

| Entry | Purpose |
|-------|---------|
| `pipeline/cognee_worker.py` | CLI: remember, recall, improve, forget, ingest-files |
| `pipeline/cognee_client.py` | Async Cognee operations |
| `pipeline/cognee_subprocess.py` | MCP-safe subprocess wrapper |
| `pipeline/ingest_files.py` | Workbench file ingest |
| `pipeline/ingest_curated.py` | Curated primitives batch |
| `pipeline/ingest_local.py` | Mock/local ingest |

## Curated ingest

```powershell
.\scripts\ingest-curated-primitives.ps1
```

Or UI at http://127.0.0.1:8080/primitives.html

Graph cognify model (reference): `huihui_ai/qwen2.5-coder-abliterate:14b`  
Embeddings: `nomic-embed-text`

## Recall tips

- Always pass `dataset` when querying scoped content (`eve_memory`, `primitives_test`)
- With access control off, post-filtering may apply on large shared indexes
- Set `CACHING=false` during curated ingest/recall if VRAM contention with embed model

## Maintenance

```powershell
# Stuck ingestion_jobs in PocketBase
.\scripts\cleanup-stale-ingestion-jobs.ps1
```

## Next

- [08-pocketbase](08-pocketbase.md)
- [11-pipeline-and-ingestion](11-pipeline-and-ingestion.md)
