# 14 — Configuration

## Environment files

| File | Committed | Purpose |
|------|-----------|---------|
| `.env.example` | Yes | Template for `.env.local` |
| `.env.local` | **No** (gitignore) | PocketBase admin, Ollama URL, paths |
| `config/cognee.env.example` | Yes | Template for Cognee |
| `config/cognee.env` | **No** (gitignore) | Cognee LLM, embed, Postgres, storage root |
| `config/services.json` | Yes | Service orchestration metadata |

## `.env.local` variables

From `.env.example`:

```ini
POCKETBASE_URL=http://127.0.0.1:8090
POCKETBASE_ADMIN_EMAIL=admin@empire.local
POCKETBASE_ADMIN_PASSWORD=empire-admin-change-me

OLLAMA_BASE_URL=http://localhost:11434/v1
OLLAMA_MODEL=llama3.1:8b

COGNEE_SYSTEM_ROOT=./cognee/.cognee_system

# Future connectors (unused)
SLACK_BOT_TOKEN=
GITHUB_TOKEN=
GMAIL_CREDENTIALS_PATH=
```

Used by: MCP PocketBase auth, Eve agent (via `config/services.json` env block).

## `config/cognee.env`

Copy from `config/cognee.env.example` and customize.

Critical keys:

| Key | Description |
|-----|-------------|
| `LLM_PROVIDER`, `LLM_MODEL`, `LLM_ENDPOINT` | Cognee graph/cognify LLM |
| `EMBEDDING_*` | Ollama embed model and batch size |
| `SYSTEM_ROOT_DIRECTORY` | e.g. `V:\Cognee` |
| `DB_*`, `VECTOR_DB_*`, `GRAPH_DATABASE_*` | Postgres connection |
| `EMPIRE_REMEMBER_CONCURRENCY` | Parallel remember workers |
| `EMPIRE_QUIET_COGNEE` | Reduce Cognee log noise |

## Runtime state (not in repo)

| Path | Purpose |
|------|---------|
| `%LOCALAPPDATA%\EMPIRE\ollama-active-model.json` | Active Eve chat model |
| `%LOCALAPPDATA%\EMPIRE\cognee.lock` | Cognee process lock |
| `%LOCALAPPDATA%\EMPIRE\wiki-checkpoint.json` | Wiki checkpoint (if used) |
| `backend/pocketbase/pb_data/` | PocketBase SQLite |
| `data/eve_memory/uploads/`, `jobs/` | Workbench upload staging (gitignored) |
| `V:\Cognee` | Cognee databases (VHDX) |

## Cursor MCP paths

`.cursor/mcp.json` uses absolute paths to `venv/Scripts/python.exe` and `mcp/*.py`. After clone, update to your repo path (e.g. `C:/EMPIRE/...`). Full checklist: [16-github-prep](16-github-prep.md).

## Eve agent env

`agents/empire-task-agent/.env.example` — Ollama and PocketBase URLs.  
Production start injects env from `config/services.json` `eve.start.env`.

## Docker Postgres

Started by `ensure-cognee-postgres.ps1`. Container name: `empire-cognee-postgres`. Credentials must match `cognee.env`.

## Security checklist (before non-local use)

- [ ] Change PocketBase admin password
- [ ] Tighten PocketBase collection rules
- [ ] Remove default credentials from committed examples if customized
- [ ] Confirm all services bind 127.0.0.1 only
- [ ] Do not commit `.env.local` or `config/cognee.env`

## Next

- [03-getting-started](03-getting-started.md)
- [16-github-prep](16-github-prep.md)
