# 11 — Pipeline and ingestion

Code lives in `pipeline/`. All ingestion is **local files only** — no live Slack/GitHub/Gmail APIs in runtime.

## Active paths

### Workbench memory (`eve_memory`)

- Trigger: Workbench Memory tab or `memory_api.py`
- Worker: `pipeline/cognee_worker.py ingest-files`
- Files: `.md`, `.txt`, `.pdf` (PDF via conversion in ingest pipeline)

### Curated primitives (`primitives_test`)

- Fuel: `data/curated_primitives/raw_materials/*.md`
- Script: `.\scripts\ingest-curated-primitives.ps1`
- UI: http://127.0.0.1:8080/primitives.html
- Module: `pipeline/ingest_curated.py`

### Mock fixtures (`mock`)

- Data: `mock_data_ingest/*.json`, `*.md`
- Scripts:

```powershell
.\scripts\ingest-all-mocks.ps1
.\scripts\ingest-mock.ps1 mock_data_ingest/github_issue.json
```

- Module: `pipeline/ingest_local.py`, `pipeline/normalizer.py`

### MCP mock ingest

`cognee_ingest_mock_file` in `mcp/cognee_mcp.py` — single file from mock_data_ingest.

## Halted: Wikipedia / Wiki Ops

The wiki pipeline (`pipeline/wiki_ingest.py`, `wiki.html`, `empire-wiki` MCP) is **preserved but halted**:

- Do not start new wiki ingests
- Existing `wikipedia_2017` dataset may remain in Cognee
- Scripts like `start-wiki-ingest-overnight.ps1` exist for historical reference only

## Cognee worker commands

```powershell
.\venv\Scripts\python.exe -m pipeline.cognee_worker remember --content "..." --dataset eve_memory
.\venv\Scripts\python.exe -m pipeline.cognee_worker recall --query "..." --dataset eve_memory
.\venv\Scripts\python.exe -m pipeline.cognee_worker improve --dataset eve_memory
.\venv\Scripts\python.exe -m pipeline.cognee_worker forget --dataset eve_memory
```

## Ingest modes

| Mode | Graph cognify (LLM) | Embed | Speed |
|------|---------------------|-------|-------|
| Full graph | Yes (`LLM_MODEL`) | Yes | Slow |
| Remember + embed only | Skipped | Yes | Fast (Workbench default) |

Controlled by `full_graph` flag on upload and scripts' fast-path options.

## Locking

`pipeline/cognee_lock.py` — file lock at `%LOCALAPPDATA%\EMPIRE\cognee.lock`. Always acquire before Cognee mutations when multiple processes may run (MCP + Eve + UI).

## Verification

```powershell
.\venv\Scripts\python.exe -m pipeline.verify_ingest
```

Tests: `tests/pipeline/`

## Next

- [07-memory-and-cognee](07-memory-and-cognee.md)
- [12-scripts-reference](12-scripts-reference.md)
