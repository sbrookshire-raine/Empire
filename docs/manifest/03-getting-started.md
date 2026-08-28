# 03 — Getting started

## Prerequisites

| Component | Version / notes |
|-----------|-----------------|
| Windows 10/11 | Primary target |
| Python 3.11+ | Shared `venv/` |
| Node.js 24.x | Only for `agents/empire-task-agent/` |
| [Ollama](https://ollama.com/) | Local LLM + embeddings |
| Docker Desktop | Postgres for Cognee |
| Git | For clone and updates |
| Admin (once) | VHDX create/mount for `V:\Cognee` |

Optional: external drive `I:` for VHDX backing file per [COGNEE_VHDX.md](../COGNEE_VHDX.md).

## One-time setup

```powershell
cd C:\EMPIRE
.\scripts\setup.ps1
```

Setup creates:

- Python `venv/` and installs `requirements.txt`
- Downloads PocketBase binary to `backend/pocketbase/`
- Copies `.env.example` → `.env.local` if missing
- Creates directory scaffold

### Cognee configuration

`config/cognee.env` is **gitignored**. Copy the example and edit:

```powershell
copy config\cognee.env.example config\cognee.env
```

Set `SYSTEM_ROOT_DIRECTORY` to your Cognee root (default `V:\Cognee`). See [07-memory-and-cognee](07-memory-and-cognee.md).

### VHDX (first time, Administrator)

```powershell
powershell -ExecutionPolicy Bypass -File scripts\create-cognee-vhdx.ps1
```

### Ollama models (minimum)

```powershell
ollama pull llama3.1:8b
ollama pull nomic-embed-text:latest
```

Recommended suite — see [10-models-and-ollama](10-models-and-ollama.md):

```powershell
ollama pull qwen2.5-coder:14b      # or your preferred coder tag
ollama pull deepseek-r1:8b         # reasoning
```

### Eve agent dependencies

```powershell
cd agents\empire-task-agent
npm install
npm run build
```

Or let `start-stack.ps1` / `start-eve.ps1` rebuild when sources change.

## Cold start (daily)

**Easiest:** double-click **`Start-EMPIRE.bat`** at the repo root.

It will:

1. Start **Ollama** if not already running
2. Run the full stack (`V:\Cognee`, Postgres, PocketBase, frontend, Eve)
3. Open **http://127.0.0.1:8080/eve.html** in your default browser

PowerShell equivalent:

```powershell
.\scripts\launch-empire.ps1           # stack + browser
.\scripts\launch-empire.ps1 -NoBrowser  # stack only
```

Manual stack without launcher:

```powershell
.\scripts\start-stack.ps1
```

## Daily workflow

### Chat with Eve

- **Chat** tab — model dropdown, Enter to send, Shift+Enter for newline
- **Task overview** — collapsible Ollama summary of PocketBase tasks

### Manage tasks

- **Tasks** tab — full CRUD; **Ask Eve** / **Have Eve do this** jump to Chat with context

### Add memory

- **Memory** tab — drop `.md`, `.txt`, `.pdf` → **Add to memory**
- Default dataset: **`eve_memory`**
- Wait for job status **Ready**, then ask Eve about the files

### Plan models

- **Models** tab — suite planner: targets per skill, pull gaps, remove duplicates, Eve briefing

### Service health

- **More** tab — repair button, links to dashboard and PocketBase admin

## Giving Eve knowledge

| Source | How | Dataset |
|--------|-----|---------|
| Workbench upload | Memory tab | `eve_memory` |
| Curated primitives | `primitives.html` or `ingest-curated-primitives.ps1` | `primitives_test` |
| Mock fixtures | `ingest-mock.ps1` (dev) | per script default |
| Directives | Paste `SYSTEM.md` into chat — **never** ingest | N/A |

## Verification

```powershell
.\scripts\verify-stack.ps1
.\venv\Scripts\python.exe .\scripts\verify-eve-workbench.py
```

## Stop services

```powershell
.\scripts\roll-out.ps1
```

## Troubleshooting

| Symptom | Check |
|---------|-------|
| Eve won't chat | `http://127.0.0.1:2000/eve/v1/info`, restart `start-eve.ps1` |
| Memory upload fails | Postgres Docker, `V:` mounted, `config/cognee.env` |
| Models empty | `ollama serve`, `ollama list` |
| Stale UI | Hard refresh browser; restart `start-frontend.ps1` |
| Cognee lock stuck | Close MCP/Cursor cognee calls; delete lock only if no worker running |

Full operational guide: [OPERATIONAL_HANDOFF.md](../OPERATIONAL_HANDOFF.md).

## Next

- [04-services-and-ports](04-services-and-ports.md)
- [06-eve-agent](06-eve-agent.md)
