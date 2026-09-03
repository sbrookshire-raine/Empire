# 06 — Eve agent

Location: `agents/empire-task-agent/`

Eve is the **conversational agent** for EMPIRE. It runs on port **2000**, uses **Ollama** for inference, and calls **tools** for PocketBase, Cognee, and model management.

## Runtime

| Item | Value |
|------|-------|
| Framework | [Eve](https://www.npmjs.com/package/eve) (`defineAgent`, `defineTool`) |
| Build | `npm run build` → `.output/` |
| Dev | `npm run dev` (REPL + server) |
| Production | `npm start` or `scripts/start-eve.ps1` |
| Model selection | Dynamic per step from `ollama-active-model.json` |

### Model switching

`agent/agent.ts` reads active model on each `step.started`:

```
%LOCALAPPDATA%\EMPIRE\ollama-active-model.json
fallback: config/ollama-active-model.json
fallback: OLLAMA_MODEL env (default llama3.1:8b)
```

Eve tool `switch_chat_model` writes the same file via `frontend/ollama_cli.py`.

### Voice vs instructions

`agent/instructions.md` is **voice-only** (what users see). Operational tool routing lives in the on-demand `empire-operations` skill so rules do not leak into chat. Eve must not quote system rules, tool names, or framework errors in replies.

### Disabled harness tools

| Tool | Why disabled |
|------|----------------|
| `ask_question` | `agent/tools/ask_question.ts` — Workbench uses normal chat; local Ollama misfires on structured question tools |

Clarifications belong in **plain chat text**, not a separate question tool.

## Tools (14 EMPIRE tools)

| Tool | Backend | Purpose |
|------|---------|---------|
| `list_tasks` | PocketBase REST | List tasks (optional status filter) |
| `search_tasks` | PocketBase REST | Search title/description |
| `create_task` | PocketBase REST | Create task |
| `update_task` | PocketBase REST | Patch task |
| `delete_task` | PocketBase REST | Delete (approval once per session) |
| `pb_health` | PocketBase REST | Health check |
| `cognee_recall` | `pipeline.cognee_worker recall` | Query graph memory |
| `cognee_remember` | `pipeline.cognee_worker remember` | Store note (default `eve_memory`) |
| `cognee_improve` | `pipeline.cognee_worker improve` | Enrichment pass |
| `cognee_forget` | `pipeline.cognee_worker forget` | Wipe dataset (approval) |
| `get_model_suite` | `frontend.ollama_cli inventory` | Suite plan + routing |
| `list_models` | `frontend.ollama_cli models` | Installed chat models |
| `switch_chat_model` | `frontend.ollama_cli set-active` | Change active model |
| `ollama_health` | `frontend.ollama_cli models` | Ollama reachability |

Tool files: `agent/tools/*.ts`  
Libraries: `agent/lib/pocketbase.ts`, `agent/lib/cognee.ts`, `agent/lib/ollama.ts`

## Skills (4)

| Skill | File | When to load |
|-------|------|--------------|
| `empire-operations` | `empire-operations.md` | Tasks, memory, models — main operational playbook |
| `manage-tasks` | `manage-tasks.md` | Multi-step PocketBase workflows, "Have Eve do this" |
| `recall-ingested-context` | `recall-ingested-context.md` | Curated primitives, `primitives_test` |
| `route-local-models` | `route-local-models.md` | Model choice, suite gaps, switching |

System instructions: `agent/instructions.md` (voice only). Tool routing: `empire-operations` skill.

**Note:** Workbench "skills" in `ollama_inventory.py` (dailyChat, coding, etc.) are **model routing slots**, not Eve framework skills.

## System instructions

`agent/instructions.md` — voice, output contract, personality. Operational procedures: `agent/skills/empire-operations.md` (loaded on demand).

After adding tools or skills:

```powershell
cd agents\empire-task-agent
npm run build
.\scripts\start-eve.ps1   # from repo root
```

## HTTP API (direct)

Workbench uses proxied paths; direct Eve API:

```http
POST http://127.0.0.1:2000/eve/v1/session
GET  http://127.0.0.1:2000/eve/v1/session/:id/stream?startIndex=0
```

Session contract: NDJSON events (`message.delta`, `actions.requested`, `input.requested`, etc.). Workbench client: `eve-workbench.js`.

## Extending Eve

### Add a tool

1. Create `agent/tools/my_tool.ts` with `defineTool({ ... })`
2. Add backend in `agent/lib/` if needed
3. Document it in `agent/skills/empire-operations.md`
4. Add label in `frontend/eve-workbench.js` → `TOOL_LABELS`
5. `npm run typecheck && npm run build`

### Add a skill

1. Create `agent/skills/my-skill.md` with workflow steps
2. Reference it in `empire-operations.md` or `instructions.md` ("Load `my-skill` when…")
3. Rebuild Eve

### MCP parity

Cursor MCP may have extra tools (generic PocketBase CRUD, `cognee_ingest_mock_file`). Prefer adding Eve tools when Workbench users need the same capability.

## Next

- [07-memory-and-cognee](07-memory-and-cognee.md)
- [10-models-and-ollama](10-models-and-ollama.md)
