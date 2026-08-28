# 13 — Development

## Stack rules (mandatory)

From `.cursor/rules/stack-rules.mdc`:

### Banned

- React, Next.js, Vue, Svelte, or SPA frameworks
- Firebase, Supabase, cloud BaaS
- Paid cloud LLM APIs in application code
- Frontend build steps for core UI
- Cloud deployment in runtime config

### Required

- Frontend: HTML + HTMX + Alpine.js (CDN)
- Backend: PocketBase `http://127.0.0.1:8090`
- Inference: Ollama `http://localhost:11434/v1`
- Memory: Cognee remember/recall/improve/forget
- MCP: Python FastMCP in `mcp/`
- Eve agents **only** under `agents/*` with local Ollama

**Node/npm** is allowed **only** in `agents/empire-task-agent/`.

## Repo conventions

| Area | Convention |
|------|------------|
| Python imports | Top of file; no inline imports unless circular dep documented |
| Frontend | No `innerHTML` / `x-html` for untrusted content — use `x-text` |
| Eve tools | One file per tool in `agent/tools/` |
| Eve skills | Markdown in `agent/skills/` |
| Tests | `tests/frontend/`, `tests/pipeline/` |
| Config secrets | `.env.local`, `config/cognee.env` — never commit |

## Running tests

```powershell
# Python unit tests
.\venv\Scripts\python.exe -m unittest discover -s tests -p "test_*.py"

# Frontend static + inventory
.\venv\Scripts\python.exe -m unittest tests.frontend.test_eve_workbench_static tests.frontend.test_ollama_inventory -v

# Eve workbench JS harness
node tests\frontend\eve_workbench_harness.js

# Eve agent types
cd agents\empire-task-agent && npm run typecheck
```

## Common dev loops

### Frontend / API change

1. Edit `frontend/*.py`, `*.html`, `*.js`, `*.css`
2. Restart frontend: `.\scripts\start-frontend.ps1`
3. Hard refresh browser

### Eve tool/skill change

1. Edit `agents/empire-task-agent/agent/**`
2. `npm run typecheck && npm run build`
3. `.\scripts\start-eve.ps1`

### Inventory / model logic

1. Edit `frontend/ollama_inventory.py`
2. Run `tests.frontend.test_ollama_inventory`
3. Restart frontend

### PocketBase schema

1. Add migration in `backend/pocketbase/pb_migrations/`
2. Restart PocketBase (applies migrations)

### MCP tool

1. Edit `mcp/*_mcp.py`
2. Restart MCP in Cursor (`/mcp` reload)

## Project phases (historical)

| Phase | Deliverable |
|-------|-------------|
| 1–2 | PocketBase + migrations |
| 3 | Cognee pipeline + mock ingest + MCP |
| 4 | HTMX tasks UI |
| 5 | Eve agent |
| 6+ | Eve Workbench, memory upload, model suite |

## Cursor skills

Optional agent skills under `.cursor/skills/` (docling ingest, cognee pipeline, etc.). Not required for core EMPIRE runtime.

## Architecture diagram source

`docs/diagrams/empire-workspace.architecture.json` — Archify source for HTML diagram.

## Next

- [14-configuration](14-configuration.md)
- [16-github-prep](16-github-prep.md)
