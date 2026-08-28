# 15 — Glossary

| Term | Meaning |
|------|---------|
| **EMPIRE** | This local AI ecosystem project |
| **Eve** | Conversational agent (`agents/empire-task-agent`) on port 2000 |
| **Workbench** | `eve.html` tabbed UI — chat, tasks, memory, models |
| **PocketBase** | Embedded SQLite backend for tasks API (:8090) |
| **Cognee** | Graph + vector memory library (remember/recall/improve/forget) |
| **Ollama** | Local LLM server (:11434) |
| **MCP** | Model Context Protocol — Cursor tool servers in `mcp/` |
| **Dataset** | Named Cognee memory partition (`eve_memory`, `primitives_test`, …) |
| **Fuel** | Markdown content ingested into Cognee (curated raw_materials) |
| **Directives** | Query lenses (`SYSTEM.md`) — never ingested as fuel |
| **Mock ingest** | Stub fixtures in `mock_data_ingest/` for dev |
| **Skill (Eve)** | Markdown workflow file in `agent/skills/` |
| **Skill slot (models)** | Model routing category in `ollama_inventory.py` (dailyChat, coding, …) |
| **Suite planner** | Models tab logic — target models, gaps, cleanup |
| **Active chat model** | Model Eve uses, stored in `ollama-active-model.json` |
| **Embed model** | `nomic-embed-text` for Cognee vectors — separate from chat |
| **VHDX** | Virtual disk for NTFS Cognee storage on `V:` |
| **cognee.lock** | Cross-process mutex for Cognee operations |
| **Build phase** | Development with Cursor cloud models |
| **Operational phase** | Daily use with local Ollama for inference |
| **HTMX** | HTML-over-the-wire library for tasks UI |
| **FastMCP** | Python MCP server framework used in `mcp/` |
| **Primitives** | Curated knowledge pilot (`primitives_test` dataset) |
| **Wiki Ops** | Halted Wikipedia ingest pilot |

## Status values

**Task status:** `todo`, `in_progress`, `done`

**Memory job status:** `queued`, `converting`, `embedding`, `ready`, `failed`

**Suite slot status:** `covered`, `weak`, `gap`

**Model fit (16 GB):** `excellent`, `good`, `tight`, `heavy`, `embed`
