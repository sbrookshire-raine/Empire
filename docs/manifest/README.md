# EMPIRE Project Manifest

Complete reference for understanding, using, and continuing work on EMPIRE. Read in order for onboarding, or jump to a section.

## Quick paths

| I want to… | Read |
|------------|------|
| **Re-bootstrap Gemini / lost context** | **[EMPIRE_GUIDE.md](../../EMPIRE_GUIDE.md)** (what / now / next) |
| Understand what EMPIRE is | [01-overview](01-overview.md) |
| See how pieces connect | [02-architecture](02-architecture.md) |
| Run it today | [03-getting-started](03-getting-started.md) |
| Find a port or service | [04-services-and-ports](04-services-and-ports.md) |
| Work on the UI or APIs | [05-frontend-and-apis](05-frontend-and-apis.md) |
| Extend Eve (tools/skills) | [06-eve-agent](06-eve-agent.md) |
| Feed memory / Cognee | [07-memory-and-cognee](07-memory-and-cognee.md) |
| Understand tasks DB | [08-pocketbase](08-pocketbase.md) |
| Use Cursor MCP | [09-mcp-cursor](09-mcp-cursor.md) |
| Tune Ollama models | [10-models-and-ollama](10-models-and-ollama.md) |
| Run ingestion pipelines | [11-pipeline-and-ingestion](11-pipeline-and-ingestion.md) |
| Find a script | [12-scripts-reference](12-scripts-reference.md) |
| Develop / test | [13-development](13-development.md) |
| Configure env | [14-configuration](14-configuration.md) |
| Look up a term | [15-glossary](15-glossary.md) |
| Push / backup / clone from GitHub | [16-github-prep](16-github-prep.md) |

## Manifest contents

1. [Overview](01-overview.md) — mission, design principles, build vs operational phase
2. [Architecture](02-architecture.md) — system diagram, data flows, process boundaries
3. [Getting started](03-getting-started.md) — prerequisites, setup, cold start, daily use
4. [Services and ports](04-services-and-ports.md) — Ollama, PocketBase, frontend, Eve, Postgres
5. [Frontend and APIs](05-frontend-and-apis.md) — pages, Workbench tabs, HTTP API catalog
6. [Eve agent](06-eve-agent.md) — tools, skills, model switching, HTTP API
7. [Memory and Cognee](07-memory-and-cognee.md) — datasets, upload jobs, storage, lock
8. [PocketBase](08-pocketbase.md) — collections, migrations, admin
9. [MCP and Cursor](09-mcp-cursor.md) — FastMCP servers, tool parity with Eve
10. [Models and Ollama](10-models-and-ollama.md) — suite planner, routing, hardware
11. [Pipeline and ingestion](11-pipeline-and-ingestion.md) — mock, curated, wiki (halted)
12. [Scripts reference](12-scripts-reference.md) — every `scripts/*.ps1`
13. [Development](13-development.md) — repo layout, tests, stack rules, extending
14. [Configuration](14-configuration.md) — `.env.local`, `cognee.env`, paths
15. [Glossary](15-glossary.md) — terms used across the project
16. [GitHub, backup & clone](16-github-prep.md) — canonical repo, clone, push, what stays local

## Related docs (outside manifest)

| Path | Purpose |
|------|---------|
| [AGENTS.md](../../AGENTS.md) | Day-to-day agent/operator cheat sheet |
| [docs/OPERATIONAL_HANDOFF.md](../OPERATIONAL_HANDOFF.md) | Operational phase handoff |
| [docs/COGNEE_VHDX.md](../COGNEE_VHDX.md) | NTFS VHDX storage on `V:` |
| [docs/ONEDRIVE.md](../ONEDRIVE.md) | Optional OneDrive tuning |
| [data/curated_primitives/README.md](../../data/curated_primitives/README.md) | Fuel vs directives for primitives |
| [agents/empire-task-agent/README.md](../../agents/empire-task-agent/README.md) | Eve npm project |

## Maintainer note

This manifest describes the repo **as built** (August 2026). Wikipedia/wiki ingest is **halted** but code remains. Curated primitives and Eve Workbench memory are the active data paths.
