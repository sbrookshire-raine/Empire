# EMPIRE Operational Handoff

This document completes the **build phase** and defines how to run EMPIRE in the **operational phase**: fully local inference (Ollama), PocketBase tasks, Cognee memory, MCP tooling in Cursor, and the Eve task agent.

**Build phase is complete.** The zero-build Tasks UI CRUD loop is verified. You may now switch Cursor to local Ollama when ready.

---

## 1. Prerequisites

### Software

| Component | Version / notes |
|-----------|----------------|
| Windows 10/11 | Primary dev target for this repo |
| Python 3.11+ | Shared venv at `venv/` |
| Node.js 24.x | **Only** for `agents/empire-task-agent/` |
| [Ollama](https://ollama.com/) | Local LLM + embeddings |
| Git | Optional; Eve scaffold includes nested repo under `agents/empire-task-agent/.git` |

### One-time setup

```powershell
cd C:\EMPIRE
.\scripts\setup.ps1
```

This creates the Python venv, downloads PocketBase, writes `config/cognee.env`, and seeds `.env.local` from `.env.example`.

### Ollama models

Pull chat and embedding models (adjust names to match your `.env.local` / `config/cognee.env`):

```powershell
ollama pull llama3.1:8b
ollama pull llama3.1:latest
ollama pull nomic-embed-text:latest
```

Verify Ollama:

```powershell
ollama list
curl http://localhost:11434/api/tags
```

### Default credentials (local dev only)

| Service | URL | Login |
|---------|-----|-------|
| PocketBase Admin | http://127.0.0.1:8090/_/ | `admin@empire.local` / `empire-admin-change-me` |
| Tasks UI | http://127.0.0.1:8080 | No login (public dev rules) |
| Eve production server | http://127.0.0.1:2000 | Built local API, explicitly bound to loopback |

**Rotate these before any non-local exposure.**

---

## 2. Start order (Operational Phase)

**Preferred:** one command from the repo root (UAC if `V:` is missing):

```powershell
.\scripts\start-stack.ps1
```

That mounts `V:\Cognee`, starts Docker `empire-cognee-postgres` and PocketBase, launches
the frontend as `venv\Scripts\python.exe -m frontend.serve`, conditionally rebuilds Eve
only when source/package inputs are newer, and starts the built Eve server on
`127.0.0.1:2000`.
Ollama must already be running. For normal use, open **http://127.0.0.1:8080/eve.html**.
Upload `.md`, `.txt`, or `.pdf` files there and chat with Eve in the same Workbench. Uploads
default to Cognee dataset `eve_memory`; curated primitives remain in `primitives_test`.

### Troubleshooting: manual service order

Use the command-line steps below only when the preferred start or browser Workbench needs diagnosis.

#### Step 1 — Ollama

```powershell
ollama serve
```

Confirm: `http://localhost:11434/api/tags` returns model list.

#### Step 2 — PocketBase

```powershell
cd C:\EMPIRE
.\scripts\start-pocketbase-background.ps1
# or foreground: .\scripts\start-pocketbase.ps1
```

Confirm: http://127.0.0.1:8090/health.html shows healthy status.

#### Step 3 — (Optional) Mock ingest into Cognee

Required only if you want graph recall over fixture data:

```powershell
.\scripts\ingest-all-mocks.ps1
# or single file: .\scripts\ingest-mock.ps1 mock_data_ingest/github_issue.json
```

Cognee storage: `V:\Cognee` on an NTFS VHDX backed by `I:\EMPIRE_VHDX\empire_cognee.vhdx` (heavy storage off C:; mount with `scripts\mount-cognee-vhdx.ps1`, see [COGNEE_VHDX.md](COGNEE_VHDX.md)). Control files (`cognee.lock`, `wiki-checkpoint.json`) stay under `%LOCALAPPDATA%\EMPIRE`.

#### Step 4 — MCP servers (Cursor)

MCP is configured in `.cursor/mcp.json`:

| Server | Purpose |
|--------|---------|
| `empire-pocketbase` | PocketBase CRUD tools |
| `empire-cognee` | Cognee remember/recall/improve/forget |

In Cursor: open MCP panel and ensure both servers show **green**. They use stdio + the repo venv Python.

#### Step 5 — Frontend

```powershell
.\scripts\start-frontend.ps1
```

Open http://127.0.0.1:8080/eve.html after the frontend starts.

#### Step 6 — Eve task agent

```powershell
.\scripts\start-eve.ps1
```

`start-eve.ps1` runs the same conditional production-build check as `start-stack.ps1`
and then starts `eve start --host 127.0.0.1 --port 2000`. Do not use Eve dev mode for
the operational Workbench.

#### Quick status check

```powershell
.\scripts\check-status.ps1
.\scripts\refresh-dashboard.ps1
```

Open **http://127.0.0.1:8080/dashboard.html** for a live service board (manual refresh + auto-refresh interval).

#### Automated integration verification

`check-status.ps1` confirms each service responds on its health URL. To verify **communication paths** (Tasks UI → PocketBase, Eve → Ollama/PocketBase, MCP tools, task round-trip) without clicking through UIs:

```powershell
.\scripts\verify-stack.ps1
.\scripts\verify-stack.ps1 -SkipCognee    # faster when graph memory not needed
.\scripts\verify-stack.ps1 -FullIngest    # also runs pipeline/verify_ingest.py (slow)
.\venv\Scripts\python.exe .\scripts\verify-eve-workbench.py # complete Workbench flow
```

From the dashboard, click **Verify integration** (requires the Workbench frontend launched as `python -m frontend.serve`).

Reports are written to `%LOCALAPPDATA%\EMPIRE\verify-stack.json` and `frontend/verify-stack.json`.

**Corrections vs generic advice:** Eve’s built API is explicitly bound to
`127.0.0.1:2000`, not the default port 3000. PocketBase health is
`http://127.0.0.1:8090/api/health` (or `/health.html`). Frontend readiness requires
`http://127.0.0.1:8080/api/memory/status`, not merely a static page. The supported user
interface is the browser Workbench at `/eve.html`.

#### Graceful roll-in / roll-out

Managed services can be started and stopped in dependency order for dashboard and operational use:

```powershell
# Start (Ollama health verify → PocketBase → Tasks UI → Eve)
.\scripts\roll-in.ps1

# Start subset only
.\scripts\roll-in.ps1 -Only pocketbase,frontend
.\scripts\roll-in.ps1 -SkipOllamaCheck   # skip Ollama health gate

# Stop managed services in reverse order (Eve → UI → PocketBase; Ollama left running)
.\scripts\roll-out.ps1
.\scripts\roll-out.ps1 -Only frontend,eve
```

Service definitions live in `config/services.json`. Runtime PID/state: `%LOCALAPPDATA%\EMPIRE\services.state.json`. Dashboard snapshot: `%LOCALAPPDATA%\EMPIRE\dashboard-status.json` (also copied to `frontend/dashboard-status.json` and `backend/pocketbase/pb_public/dashboard/status.json`).

Roll-in waits for each service health check before starting the next. Roll-out sends graceful stop, waits for the port to clear, then force-kills if needed.

---

## 3. Cursor Operational Phase — switch to Ollama

Do this **after** build verification (Tasks CRUD, MCP smoke tests). During the build phase, Cursor used frontier cloud models by design.

### Cursor Settings → Models

1. Open **Cursor Settings** → **Models** (or **Features** → **Chat** → model provider).
2. Enable **OpenAI-compatible** / custom base URL (wording varies by Cursor version).
3. Set:
   - **Base URL:** `http://localhost:11434/v1`
   - **API Key:** `ollama` (literal string; Ollama does not validate it)
4. Select a pulled model (e.g. `llama3.1:8b` or `llama3.1:latest`).
5. Save and start a **new chat** to confirm requests hit Ollama (watch `ollama serve` logs).

### Keep MCP enabled

Leave `empire-pocketbase` and `empire-cognee` enabled in `.cursor/mcp.json` so the local model can call the same tools as during build.

### Rollback

To return to cloud models, disable the custom base URL and select a Cursor-hosted model again.

---

## 4. Verification checklist

Run through this list once when entering operational phase.

### Eve Workbench

- [ ] http://127.0.0.1:8080/eve.html loads
- [ ] File uploads default to `eve_memory` and reach Ready
- [ ] Initial chat and a follow-up both return visible assistant text
- [ ] Task requests show readable PocketBase activity

### Tasks UI (Phase 4) — verified in build

- [ ] http://127.0.0.1:8080 loads
- [ ] Create task → appears in list and PocketBase admin (`tasks` collection)
- [ ] Inline edit (Save) updates record
- [ ] Delete removes record
- [ ] Hard refresh (Ctrl+F5) after frontend changes

### PocketBase MCP

In Cursor chat with MCP enabled:

- [ ] Ask agent to call `pb_health` or list tasks via `pb_list_records` / `pb_search_tasks`
- [ ] Confirm JSON response from http://127.0.0.1:8090

### Cognee MCP + pipeline

- [ ] `.\scripts\ingest-mock.ps1 mock_data_ingest/slack_thread.json` completes
- [ ] In Cursor, `cognee_recall` with a query about the thread returns hits
- [ ] Stale jobs: `.\scripts\cleanup-stale-ingestion-jobs.ps1` if needed

### Eve agent (Phase 5)

From the repo root:

```powershell
Push-Location agents\empire-task-agent
npm run typecheck
Pop-Location
.\scripts\start-eve.ps1
```

- [ ] `GET /eve/v1/info` (or production server banner) shows Ollama model from `agent/agent.ts`
- [ ] Create session: `POST /eve/v1/session` with a prompt like *"List my tasks"*
- [ ] Agent calls `list_tasks` and returns PocketBase data
- [ ] Prompt *"What do we know about the GitHub issue?"* triggers `cognee_recall` (after mock ingest)
- [ ] `delete_task` prompts for approval once per session

### Ollama end-to-end

- [ ] `ollama serve` log shows completion requests when using Cursor or Eve
- [ ] No paid API keys required for core loop

---

## 5. Architecture reference

```
Browser (8080)  ──HTMX/Alpine──►  PocketBase (8090)  SQLite
Cursor / Eve    ──tools/MCP───►  PocketBase + Cognee
Eve agent       ──Ollama──────►  http://localhost:11434/v1
Pipeline        ──subprocess──►  Cognee (V:\Cognee — NTFS VHDX backed by I:)
```

| Path | Role |
|------|------|
| `frontend/index.html` | Zero-build Tasks UI |
| `backend/pocketbase/` | PocketBase binary, migrations, `pb_public/` |
| `mcp/pocketbase_mcp.py` | FastMCP → PocketBase |
| `mcp/cognee_mcp.py` | FastMCP → Cognee (subprocess worker) |
| `pipeline/ingest_local.py` | Mock file ingestion |
| `agents/empire-task-agent/` | Eve agent (npm isolated here) |
| `config/cognee.env` | Cognee + Ollama config |

### Eve vs Cursor MCP

| Capability | Cursor | Eve agent |
|------------|--------|-----------|
| PocketBase | stdio MCP `empire-pocketbase` | Typed tools: `list_tasks`, `create_task`, … |
| Cognee | stdio MCP `empire-cognee` | `cognee_recall` / `cognee_remember` via Python worker |
| Inference | Cursor chat (switch to Ollama) | `agent/agent.ts` → Ollama via `@ai-sdk/openai` |

Eve `defineMcpClientConnection` expects HTTP/SSE MCP. EMPIRE FastMCP servers use **stdio**; Eve uses typed tools for parity unless you add an HTTP MCP bridge later.

---

## 6. Security hardening (before non-local use)

Current build uses **public CRUD** on `tasks`, `ingestion_jobs`, and `sources` for local dev speed.

Before exposing beyond localhost:

1. **PocketBase API rules** — tighten `listRule`, `viewRule`, `createRule`, `updateRule`, `deleteRule` on all collections; require auth for writes.
2. **Admin password** — change `POCKETBASE_ADMIN_PASSWORD` in `.env.local`; re-upsert superuser via setup or admin UI.
3. **Secrets** — never commit `.env.local` or `config/cognee.env`; keep `.gitignore` current.
4. **CORS** — restrict PocketBase allowed origins to known localhost ports if serving frontend elsewhere.
5. **Eve auth** — replace `placeholderAuth()` in `agent/channels/eve.ts` with real auth before any public deploy.
6. **Ollama** — bind to localhost only; do not expose `:11434` to the internet without a reverse proxy and auth.

---

## 7. Troubleshooting

| Symptom | Fix |
|---------|-----|
| HTMX `invalidPath` on Tasks UI | Hard refresh; ensure `<meta name="htmx-config" content='{"selfRequestsOnly":false}' />` (UI on :8080, API on :8090) |
| Create task does nothing | PocketBase not running; check Network tab for POST to `:8090` |
| Cognee lock / slow ingest | Use fast ingest (default); storage under `%LOCALAPPDATA%\EMPIRE\`; run `cleanup-stale-ingestion-jobs.ps1` |
| Eve `Cannot find python` | Set `EMPIRE_ROOT` and ensure `venv/Scripts/python.exe` exists |
| Ollama connection refused | Start `ollama serve`; verify model pulled |
| MCP red in Cursor | Check paths in `.cursor/mcp.json`; run venv Python manually on `mcp/*.py` |

---

## 8. Future Phase 6 — live connectors

Stub env keys already exist in `.env.example`:

- `SLACK_BOT_TOKEN`
- `GITHUB_TOKEN`
- `GMAIL_CREDENTIALS_PATH`

Planned work:

1. Implement `pipeline/ingest_slack.py`, `ingest_github.py`, `ingest_gmail.py` mirroring `ingest_local.py` job metadata in PocketBase.
2. Register `sources` collection records per connector.
3. Extend Eve tools or MCP with connector-specific ingest triggers.
4. Keep **zero-build frontend**; no npm for UI.

---

## 9. Troubleshooting command reference

```powershell
# Setup
.\scripts\setup.ps1

# Services
.\scripts\start-stack.ps1
.\scripts\start-pocketbase-background.ps1
.\scripts\start-frontend.ps1
.\scripts\start-eve.ps1
.\scripts\check-status.ps1

# Ingestion
.\scripts\ingest-all-mocks.ps1
.\scripts\cleanup-stale-ingestion-jobs.ps1

# Workbench end-to-end
.\venv\Scripts\python.exe .\scripts\verify-eve-workbench.py

# Eve typecheck
Push-Location agents\empire-task-agent
npm run typecheck
Pop-Location
# Conditionally build before production start
.\scripts\start-eve.ps1
```

---

## 10. Handoff sign-off

| Phase | Deliverable | Status |
|-------|-------------|--------|
| 1 | Rules, venv, setup | Complete |
| 2 | PocketBase + `empire-pocketbase` MCP | Complete |
| 3 | Mock ingest + `empire-cognee` MCP | Complete |
| 4 | HTMX Tasks UI CRUD | **Verified** |
| 5 | Eve agent + this document | Complete |

**You are cleared to enter the operational phase.** Switch Cursor to Ollama when you want fully local chat; keep PocketBase and the Tasks UI running for day-to-day task management.

For repo conventions and ports, see [AGENTS.md](../AGENTS.md).
