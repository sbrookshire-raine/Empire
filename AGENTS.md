# EMPIRE — Local AI Ecosystem

Meter-free, zero-cloud local AI stack. Build phase uses Cursor frontier models; runtime code hardwires local tools for the Operational Phase.

**Full project manifest (architecture, APIs, Eve tools, GitHub backup):** [docs/manifest/README.md](docs/manifest/README.md)  
**Canonical repo:** https://github.com/sbrookshire-raine/Empire

## Start here (day-to-day)

This repo is already built. You **feed documents into Cognee** so Eve (and Cursor MCP) can recall them. You do not rebuild the UI.

### Cold start

Plug in the T7 (`I:`). Then either:

- **Double-click** `Start-EMPIRE.bat` at the repo root (starts Ollama if needed, full stack, opens browser)
- **Double-click** `Stop-EMPIRE.bat` to shut down (batch-only; no PowerShell stop scripts — AV-safe), or
- From PowerShell:

```powershell
.\scripts\launch-empire.ps1
```

Equivalent manual stack (no browser):

```powershell
.\scripts\start-stack.ps1
```

That mounts `V:\Cognee` (UAC prompt if needed), starts Docker Postgres and PocketBase,
launches the frontend with the repo venv, conditionally rebuilds Eve only when its
authored inputs are newer, and starts the built Eve server on `127.0.0.1:2000`.

Open **http://127.0.0.1:8080/eve.html**

### Give Eve data

On the Eve Workbench, choose or drop `.md`, `.txt`, or `.pdf` files and click **Add to memory**. Workbench uploads use dataset **`eve_memory`** by default.

**Fast chat recall:** after bulk workbench ingest, run `.\scripts\optimize-eve-memory.ps1` (or **Optimize recall** on the Memory tab). That builds dataset **`eve_core`** — a small curated set Eve searches first.

For curated primitives, continue to use http://127.0.0.1:8080/primitives.html:

1. Drop `.md` files into `data/curated_primitives/raw_materials/` (convert PDFs first if needed).
2. Click **Run curated ingest** (or **Remember+embed only** for a faster pass).
3. Ask Cursor or Eve to recall dataset **`primitives_test`**.

Do **not** ingest `data/curated_primitives/directives/` — that is the query lens (`SYSTEM.md`), not fuel. Wikipedia / Wiki Ops is halted; do not use it for new data.

### Talk to it

| Who | How |
|-----|-----|
| You (browser) | http://127.0.0.1:8080/eve.html |
| Cursor | MCP `cognee_recall` / `cognee_remember` with dataset `primitives_test` |
| Eve | Chat and upload files at `/eve.html`; Workbench memory defaults to `eve_memory` |

## Mission

Provide a lightweight Tasks CRUD loop (PocketBase + HTMX/Alpine UI), graph memory (Cognee), MCP tool exposure (FastMCP), and Eve agent orchestration — all running locally without paid cloud APIs.

## Service ports

| Service | URL | Notes |
|---------|-----|-------|
| PocketBase | http://127.0.0.1:8090 | SQLite backend + admin UI at `/_/` |
| Frontend | http://127.0.0.1:8080 | Python static server (Phase 4) |
| Ollama | http://localhost:11434/v1 | Local inference (Operational Phase) |
| Eve | http://127.0.0.1:2000 | Agent runtime (headless API) |

## Start order (Operational Phase)

1. Ollama (`ollama serve`)
2. PocketBase (`scripts/start-pocketbase.ps1`)
3. MCP servers (via Cursor `/mcp` or stdio)
4. Frontend static server
5. Eve agent (`eve start` inside `agents/empire-task-agent/`)

## Build vs operational phase

- **Build phase:** Cursor uses frontier cloud models. Do not switch Cursor Base URL to Ollama.
- **Operational phase:** Switch Cursor Base URL to `http://localhost:11434/v1` per `docs/OPERATIONAL_HANDOFF.md`.

## Key directories

- `backend/pocketbase/` — PocketBase binary, data, migrations
- `mcp/` — FastMCP Python servers (`empire-pocketbase`, `empire-cognee`)
- `pipeline/` — Stub ingestion from `mock_data_ingest/` (no live APIs)
- `mock_data_ingest/` — Local `.json` / `.md` fixtures only
- `config/cognee.env` — Cognee + Ollama local configuration
- `V:\Cognee` — Cognee graph storage on an NTFS VHDX backed by `I:\EMPIRE_VHDX\empire_cognee.vhdx` (heavy storage off C:; see [docs/COGNEE_VHDX.md](docs/COGNEE_VHDX.md))
- `%LOCALAPPDATA%\EMPIRE\cognee.lock` — cross-process lock (MCP + CLI safe together)
- `frontend/` — Zero-build HTMX/Alpine UI
- `agents/` — Isolated Eve agent projects (npm allowed here only)

## Troubleshooting and command-line operations

Normal task, chat, and upload use belongs in http://127.0.0.1:8080/eve.html. Use the commands below only for troubleshooting, maintenance, or development.

### Phase 3 ingestion (stub-only)

MCP and CLI can run at the same time — access is serialized via `%LOCALAPPDATA%\EMPIRE\cognee.lock`.

```powershell
# Ingest all mock fixtures (~2 min each)
.\scripts\ingest-all-mocks.ps1

# Or one file
.\scripts\ingest-mock.ps1 mock_data_ingest/github_issue.json
```

See [docs/ONEDRIVE.md](docs/ONEDRIVE.md) for optional OneDrive tuning.

### Phase 4 Tasks UI (zero-build)

```powershell
# Terminal 1 — PocketBase (if not already running)
.\scripts\start-pocketbase.ps1

# Terminal 2 — static frontend
.\scripts\start-frontend.ps1
```

Open http://127.0.0.1:8080 — talks directly to PocketBase tasks API on port 8090.

### Phase 5 Eve agent (Ollama-local)

Isolated npm project at `agents/empire-task-agent/` — **only** place Node/npm is used in EMPIRE.

```powershell
# Terminal 1 — Ollama
ollama serve

# Terminal 2 — PocketBase (if not running)
.\scripts\start-pocketbase-background.ps1

# Terminal 3 — conditionally build and start the production Eve agent
.\scripts\start-eve.ps1
```

Tools wrap PocketBase REST and Cognee (Python subprocess), matching Cursor MCP backends.

**Operational phase:** see [docs/OPERATIONAL_HANDOFF.md](docs/OPERATIONAL_HANDOFF.md) for Ollama + Cursor switch, verification checklist, and security hardening.

### Maintenance

```powershell
# Graceful service orchestration (dashboard-ready)
.\scripts\start-stack.ps1      # preferred cold start: V: + Postgres + PocketBase + UI + Eve
.\scripts\roll-in.ps1          # start: Ollama verify → PocketBase → UI → Eve
.\scripts\stop-empire.ps1      # calls Stop-EMPIRE.bat (or double-click Stop-EMPIRE.bat)
.\scripts\roll-out.ps1         # Eve + Workbench + PocketBase only
.\scripts\refresh-dashboard.ps1
.\scripts\verify-stack.ps1     # integration checks (services talking to each other)
.\venv\Scripts\python.exe .\scripts\verify-eve-workbench.py # full Workbench workflow

# Dashboard UI: http://127.0.0.1:8080/dashboard.html

# Close ingestion_jobs stuck in "running" (e.g. after interrupted ingests)
.\scripts\cleanup-stale-ingestion-jobs.ps1
```

### Setup

```powershell
.\scripts\setup.ps1
.\scripts\start-pocketbase.ps1
```
