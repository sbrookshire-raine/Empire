# 05 — Frontend and APIs

## Pages

| Path | File | Purpose |
|------|------|---------|
| `/eve.html` | `frontend/eve.html` | **Eve Workbench** — Chat, Tasks, Memory, Models, More |
| `/index.html` | `frontend/index.html` | Classic PocketBase tasks CRUD (HTMX) |
| `/dashboard.html` | `frontend/dashboard.html` | Service status dashboard |
| `/primitives.html` | `frontend/primitives.html` | Curated primitives ingest UI |
| `/wiki.html` | `frontend/wiki.html` | Wiki ops UI (pilot halted) |

Shared assets: `empire-nav.js`, `empire-nav.css`, Pico CSS + Alpine.js via CDN.

## Eve Workbench tabs

| Tab | Features |
|-----|----------|
| **Chat** | Model select, transcript, composer (Enter sends), task overview |
| **Tasks** | PocketBase CRUD, filter, Ask Eve / Have Eve do this |
| **Memory** | File upload, job progress, embed model display |
| **Models** | Suite planner, pull/remove commands, Eve briefing copy |
| **More** | Service health, repair, external links |

Client logic: `frontend/eve-workbench.js`, styles: `frontend/eve-workbench.css`.

## HTTP API catalog

Base: `http://127.0.0.1:8080`. Implemented in `frontend/serve.py`.

### Eve (proxied to :2000)

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/api/eve/info` | Agent info |
| POST | `/api/eve/session` | Create session |
| POST | `/api/eve/session/:id` | Continue session |
| GET | `/api/eve/session/:id/stream?startIndex=` | NDJSON event stream |
| POST | `/api/eve/session/:id/cancel` | Cancel generation |

Proxy allowlist: `frontend/eve_proxy.py`.

### Ollama

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/api/ollama/models` | Chat models + active + embedded inventory |
| GET | `/api/ollama/inventory` | Full suite analysis |
| PUT | `/api/ollama/model` | Set active chat model |
| POST | `/api/ollama/summarize-tasks` | Task overview bullets (direct Ollama) |

Logic: `frontend/ollama_api.py`, `frontend/ollama_inventory.py`.

### Memory

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/api/memory/status` | Cognee readiness + embed config |
| POST | `/api/memory/upload` | Multipart file upload → background job |
| GET | `/api/memory/jobs/:id` | Job status poll |
| POST | `/api/memory/jobs/:id/retry` | Retry failed job |

Logic: `frontend/memory_api.py`. Upload limits: 50 MB/file, 20 files, `.md`/`.txt`/`.pdf` only. Blocks `SYSTEM.md`, `LENS_*`, `directives/`.

### Services

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/api/services/status` | Health of ollama, pocketbase, frontend, eve |
| POST | `/api/services/start` | Start/repair managed services |
| POST | `/api/services/stop` | Stop managed services |
| POST | `/api/services/refresh` | Refresh dashboard snapshot |

### Primitives

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/api/primitives/status` | Last curated ingest status |
| POST | `/api/primitives/ingest` | Trigger curated ingest |

### Wiki (halted pilot)

| Method | Path | Purpose |
|--------|------|---------|
| Various | `/api/wiki/*` | Title queue, priorities, status — see `wiki_api.py` |

### Verification

| Method | Path | Purpose |
|--------|------|---------|
| GET/POST | `/api/verify/stack` | Integration self-check |

## Static server

```powershell
.\venv\Scripts\python.exe -m frontend.serve
```

Or `.\scripts\start-frontend.ps1`.

CORS: memory upload restricted to same-origin loopback hosts.

## Security notes (local dev)

- PocketBase collections use **open rules** in migrations (no auth on tasks API)
- Default admin password in `.env.example` — **rotate before any network exposure**
- Eve and APIs bind to **127.0.0.1** only

## Next

- [06-eve-agent](06-eve-agent.md)
- [07-memory-and-cognee](07-memory-and-cognee.md)
