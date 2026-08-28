# EMPIRE Task Agent (Eve)

Local-first Eve agent for EMPIRE: PocketBase tasks + Cognee memory + Ollama model routing.

## Prerequisites

- Node.js 24.x
- EMPIRE Python venv at repo root (`venv/`)
- Ollama running with chat + embed models
- PocketBase on port 8090
- Postgres Docker for Cognee (when using memory tools)

## Environment

Copy `.env.example` to `.env.local` or set variables in the shell:

| Variable | Default |
|----------|---------|
| `OLLAMA_BASE_URL` | `http://localhost:11434/v1` |
| `OLLAMA_MODEL` | `llama3.1:8b` |
| `POCKETBASE_URL` | `http://127.0.0.1:8090` |
| `EMPIRE_ROOT` | auto-resolved to monorepo root |

Active chat model is read from `%LOCALAPPDATA%\EMPIRE\ollama-active-model.json` each agent step.

## Commands

```powershell
# From EMPIRE repo root
.\scripts\start-eve.ps1

# Or from this directory
npm run dev          # interactive REPL + dev server
npm run dev -- --no-ui   # HTTP API only
npm run typecheck
npm run build
npm start
```

## HTTP API

Production: http://127.0.0.1:2000/eve/v1/  
Workbench proxies via http://127.0.0.1:8080/api/eve/

```http
POST /eve/v1/session
GET  /eve/v1/session/:id/stream?startIndex=0
```

See [docs/manifest/06-eve-agent.md](../../docs/manifest/06-eve-agent.md) and [docs/OPERATIONAL_HANDOFF.md](../../docs/OPERATIONAL_HANDOFF.md).

## Tools (14)

| Tool | Purpose |
|------|---------|
| `list_tasks` | List PocketBase tasks |
| `search_tasks` | Search by title/description |
| `create_task` | Create task |
| `update_task` | Patch task |
| `delete_task` | Delete task (approval once) |
| `pb_health` | PocketBase health |
| `cognee_recall` | Query graph memory |
| `cognee_remember` | Store note (default `eve_memory`) |
| `cognee_improve` | Cognee enrichment pass |
| `cognee_forget` | Wipe dataset (approval) |
| `get_model_suite` | Model suite plan + routing |
| `list_models` | Installed Ollama chat models |
| `switch_chat_model` | Set active chat model |
| `ollama_health` | Ollama reachability |

## Skills (3)

| Skill | Purpose |
|-------|---------|
| `manage-tasks` | Multi-step PocketBase workflows |
| `recall-ingested-context` | Curated primitives / `primitives_test` |
| `route-local-models` | Model selection and switching |

Built-in Eve `ask_question` is **disabled** — use normal chat for clarifications. See `agent/instructions.md` for voice vs internal rules.

## MCP parity

Cursor uses stdio FastMCP (`empire-pocketbase`, `empire-cognee`); Eve uses typed REST/subprocess tools with the same backends. See [docs/manifest/09-mcp-cursor.md](../../docs/manifest/09-mcp-cursor.md).
