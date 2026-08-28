# postgres-mcp — EMPIRE reference pointers

## Upstream

- Repo: https://github.com/gabriel-herencia/postgres-mcp
- Stack: FastMCP, Python, psycopg3, stdio/Docker
- Access modes: `readonly` | `readwrite` | `admin` via `PG_MCP_ACCESS_MODE`

## EMPIRE wiring

- Docker service: `empire-cognee-postgres` (see `docker-compose.yml`)
- DB: `cognee_db` · user/pass: `cognee` / `cognee` · port: `5432`
- Env template: `config/cognee.env`
- Overnight / wiki notes: `docs/WIKI_INGEST_OVERNIGHT.md`
- Existing MCP (do not replace): `.cursor/mcp.json` → `empire-pocketbase`, `empire-cognee`, `empire-wiki`

## Recommended agent policy

1. Default MCP mode: **readonly**
2. `admin` only for explicit DBA tasks requested by the user
3. Tasks CRUD stays on PocketBase (`http://127.0.0.1:8090`) — not this server
4. No cloud DBaaS URIs

## Related skills (non-duplicates)

- `cognee-memory-pipeline` — remember/recall via Cognee APIs
- `data-processor` — generic SQL connectors; prefer this MCP for live agent PG tools
- `desktop-commander-mcp` — shell/FS only; not a Postgres specialist
