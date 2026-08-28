# 01 — Overview

## What EMPIRE is

EMPIRE is a **meter-free, local-only AI ecosystem** for personal knowledge work and task management. It combines:

- A **browser workbench** for chat, tasks, memory uploads, and model planning
- **PocketBase** as a lightweight tasks database
- **Cognee** as graph + vector memory (remember / recall / improve / forget)
- **Ollama** for all LLM and embedding inference at runtime
- **Eve** as the conversational agent that calls tools against PocketBase, Cognee, and Ollama
- **FastMCP** servers so **Cursor** can use the same backends during development

There is no React/Next/Vue SPA, no Firebase/Supabase, and no paid cloud LLM APIs in application code.

## Mission

Provide a lightweight **tasks CRUD loop**, **graph memory**, **MCP tool exposure**, and **Eve agent orchestration** — all running locally.

Success looks like:

1. Open the Workbench, chat with Eve, manage tasks, upload documents
2. Eve recalls uploaded content and curated primitives from Cognee
3. Eve routes hard work to the right local model (coding, reasoning, deep quality)
4. Cursor can remember/recall and manage PocketBase via MCP without leaving the IDE

## Design principles

| Principle | Implementation |
|-----------|----------------|
| Local-first | Loopback URLs only; Ollama + PocketBase + Cognee on the machine |
| Zero-build UI | HTML + HTMX + Alpine.js via CDN in `frontend/` |
| Single Python venv | `venv/` for MCP, pipeline, frontend server, Cognee workers |
| Node only for Eve | `agents/empire-task-agent/` is the sole npm project |
| Serialized Cognee access | `%LOCALAPPDATA%\EMPIRE\cognee.lock` — MCP and CLI safe together |
| Heavy storage off C: | Cognee system root on `V:\Cognee` (NTFS VHDX); see [COGNEE_VHDX.md](../COGNEE_VHDX.md) |
| Fuel vs directives | Curated **fuel** goes into Cognee; **directives** (`SYSTEM.md`) are query lenses only |

## Build phase vs operational phase

| Phase | Who uses cloud LLMs | Ollama role |
|-------|---------------------|-------------|
| **Build** | Cursor (frontier models) | Runtime for Cognee graph/embed; do **not** point Cursor Base URL at Ollama during active building |
| **Operational** | Optional — user may point Cursor at `http://localhost:11434/v1` | Primary inference for Eve and optionally Cursor |

See [OPERATIONAL_HANDOFF.md](../OPERATIONAL_HANDOFF.md) for the operational checklist.

## Primary user surfaces

| Surface | URL / entry | User |
|---------|-------------|------|
| **Start launcher** | `Start-EMPIRE.bat` (repo root) | One-click start + browser |
| Eve Workbench | http://127.0.0.1:8080/eve.html | Daily chat, tasks, memory, models |
| Dashboard | http://127.0.0.1:8080/dashboard.html | Service health and links |
| Classic tasks UI | http://127.0.0.1:8080/index.html | HTMX tasks CRUD |
| Curated primitives | http://127.0.0.1:8080/primitives.html | Batch ingest of `raw_materials/` |
| PocketBase admin | http://127.0.0.1:8090/_/ | DB admin |
| Eve HTTP API | http://127.0.0.1:2000/eve/v1/ | Workbench proxy, direct API |
| Cursor MCP | stdio via `.cursor/mcp.json` | `cognee_*`, `pb_*` tools |

## What is intentionally halted

- **Wikipedia / Wiki Ops** — ingest pilot stopped; dataset may exist but do not use for new data
- **Live SaaS connectors** — Slack/GitHub/Gmail env vars exist as placeholders only
- **Cloud deployment** — no runtime config for remote hosts

## Hardware context (reference machine)

Documented target: **RTX 5080 16 GB VRAM**, **64 GB RAM**, external T7 drive for VHDX backing. Model suite planning in the Workbench assumes 16 GB VRAM. Adjust `ollama_inventory.py` `SUITE_SLOTS` if your hardware differs.

## Next

- [02-architecture](02-architecture.md) — how components connect
- [03-getting-started](03-getting-started.md) — run it
