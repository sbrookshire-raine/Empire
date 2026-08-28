---
name: postgres-mcp-specialist
description: Installs and operates gabriel-herencia/postgres-mcp (FastMCP + Python + psycopg3) against EMPIRE's local Docker Postgres for Cognee graph/vector admin and SQL inspection. Use when querying or administering empire-cognee-postgres / cognee_db, setting PG_MCP_ACCESS_MODE, or wiring a Postgres MCP server beside empire-pocketbase—not for PocketBase SQLite task CRUD.
---

# Postgres MCP Specialist (Build1)

Local FastMCP server for PostgreSQL. Points at EMPIRE's Docker `empire-cognee-postgres` (`cognee` / `cognee` / `cognee_db` on `localhost:5432`). Does **not** replace `empire-pocketbase` (tasks live in PocketBase SQLite).

## When to use

- Inspect Cognee schema, tables, or row counts in Postgres
- Readonly agent SQL against graph/vector store
- Explicit DBA work (migrations, grants) with `admin` mode only when requested

## When not to use

- Task CRUD → `empire-pocketbase` MCP
- General CSV/Excel/PDF wrangling → `data-processor`
- Knowledge graph remember/recall → `empire-cognee` / `cognee-memory-pipeline`

## Install

```bash
pip install postgres-mcp
# or: pip install "git+https://github.com/gabriel-herencia/postgres-mcp.git"
```

Confirm package entrypoint from the repo README if the PyPI name differs.

## EMPIRE environment

Prefer values from `config/cognee.env` / Compose. Typical URI:

```text
postgresql://cognee:cognee@localhost:5432/cognee_db
```

| Variable | Build1 default | Notes |
|---|---|---|
| `DATABASE_URI` | URI above | Required |
| `PG_MCP_ACCESS_MODE` | `readonly` | Agents default; `readwrite` / `admin` only for explicit DBA tasks |

Ensure Docker Postgres is up (`empire-cognee-postgres` / `docker-compose.yml`) before starting the MCP process.

## Cursor MCP registration (stdio)

Add a server entry (do not remove existing empire MCP servers). Example shape:

```json
"empire-postgres": {
  "command": "python",
  "args": ["-m", "postgres_mcp"],
  "env": {
    "DATABASE_URI": "postgresql://cognee:cognee@localhost:5432/cognee_db",
    "PG_MCP_ACCESS_MODE": "readonly"
  }
}
```

Exact module/CLI name: verify with `python scripts/main.py --check-install` or the upstream README.

## Agent workflow

1. Confirm Postgres is listening on `5432` (Compose health / `docker ps`).
2. Use **readonly** mode for exploratory SQL and schema listing.
3. Escalate to `admin` only when the user explicitly asks for destructive DDL/grants.
4. Never point this MCP at cloud DBaaS; Docker/local only.
5. Do not use cloud LLM APIs for query planning—local Ollama + agent tools only.

## Safety

- Prefer `readonly` for agent sessions
- Scope queries to `cognee_db`; avoid cross-database sprawl
- Do not log credentials from `DATABASE_URI` into commits or chat dumps

## Scripts

- `scripts/main.py` — install check, URI smoke probe, suggested MCP env dump

## References

- Upstream notes: [references/docs.md](references/docs.md)
- EMPIRE Cognee Postgres wiring: `docs/WIKI_INGEST_OVERNIGHT.md`, `config/cognee.env`
