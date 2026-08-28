# EMPIRE

**Local-first AI workbench** — tasks, graph memory, and an Eve agent, all on your machine. No paid cloud LLM APIs in application code.

| What | Where |
|------|--------|
| **Daily use** | http://127.0.0.1:8080/eve.html (Eve Workbench) |
| **Cold start** | `.\scripts\start-stack.ps1` |
| **Full documentation** | [docs/manifest/README.md](docs/manifest/README.md) |
| **Agent quick ref** | [AGENTS.md](AGENTS.md) |

## What it does

- **Chat with Eve** — local Ollama models, tool use, model routing by task type
- **PocketBase tasks** — create, track, and execute todos from the browser or via Eve
- **Cognee memory** — upload `.md` / `.txt` / `.pdf`, embed with `nomic-embed-text`, recall in chat
- **Cursor MCP** — PocketBase and Cognee tools for development in Cursor

## Stack (required)

| Layer | Technology |
|-------|------------|
| UI | Plain HTML + HTMX + Alpine.js (CDN, zero build) |
| API / static server | Python `frontend.serve` on `:8080` |
| Tasks DB | PocketBase (SQLite) on `:8090` |
| Memory | Cognee 1.0 + Postgres/pgvector on Docker |
| Inference | Ollama on `:11434` |
| Agent | Eve framework in `agents/empire-task-agent/` on `:2000` |
| MCP | Python FastMCP in `mcp/` |

## First-time setup

```powershell
git clone <your-repo-url> C:\EMPIRE
cd C:\EMPIRE
.\scripts\setup.ps1
copy config\cognee.env.example config\cognee.env   # then edit paths/models
ollama pull llama3.1:8b
ollama pull nomic-embed-text:latest
```

**Daily start:** double-click **`Start-EMPIRE.bat`** (or `.\scripts\launch-empire.ps1`).

## Documentation map

| Doc | Contents |
|-----|----------|
| [Manifest index](docs/manifest/README.md) | Start here for the full project guide |
| [Overview](docs/manifest/01-overview.md) | Mission, constraints, phases |
| [Architecture](docs/manifest/02-architecture.md) | How components connect |
| [Getting started](docs/manifest/03-getting-started.md) | Setup, cold start, daily workflow |
| [Services & ports](docs/manifest/04-services-and-ports.md) | Every service, URL, start order |
| [Frontend & APIs](docs/manifest/05-frontend-and-apis.md) | Pages, REST routes, Workbench |
| [Eve agent](docs/manifest/06-eve-agent.md) | Tools, skills, sessions |
| [Memory & Cognee](docs/manifest/07-memory-and-cognee.md) | Datasets, ingest, VHDX |
| [PocketBase](docs/manifest/08-pocketbase.md) | Schema, collections |
| [MCP & Cursor](docs/manifest/09-mcp-cursor.md) | Cursor integration |
| [Models & Ollama](docs/manifest/10-models-and-ollama.md) | Model suite, routing |
| [Pipeline & ingestion](docs/manifest/11-pipeline-and-ingestion.md) | Mock, curated, halted wiki |
| [Scripts reference](docs/manifest/12-scripts-reference.md) | All PowerShell scripts |
| [Development](docs/manifest/13-development.md) | Tests, conventions, extending |
| [Configuration](docs/manifest/14-configuration.md) | Env files, secrets |
| [Glossary](docs/manifest/15-glossary.md) | Terms |
| [GitHub prep](docs/manifest/16-github-prep.md) | Before you push |

Also see [docs/OPERATIONAL_HANDOFF.md](docs/OPERATIONAL_HANDOFF.md) for operational-phase checklist.

## License

See component licenses (PocketBase, Eve, Cognee, etc.). Project documentation and application code as contributed by the maintainer.
