# 09 — MCP and Cursor

EMPIRE exposes **FastMCP** Python servers for use inside **Cursor** during development. They share backends with Eve but run as **stdio** MCP processes, not HTTP.

## Registration

File: `.cursor/mcp.json`

| Server | Script | Purpose |
|--------|--------|---------|
| `empire-pocketbase` | `mcp/pocketbase_mcp.py` | PocketBase CRUD + health |
| `empire-cognee` | `mcp/cognee_mcp.py` | Cognee remember/recall/improve/forget/ingest |
| `empire-wiki` | `mcp/wiki_mcp.py` | Wiki ingest (pilot **halted**) |

After clone, update `.cursor/mcp.json` paths if the repo is not at `C:\EMPIRE`. See [16-github-prep](../manifest/16-github-prep.md).

Env loads from `.env.local` for PocketBase admin credentials.

## empire-pocketbase tools

| Tool | Purpose |
|------|---------|
| `pb_health` | API health |
| `pb_list_collections` | List collections |
| `pb_list_records` | Generic list with filter |
| `pb_get_record` | Get by id |
| `pb_create_record` | Create record |
| `pb_update_record` | Patch record |
| `pb_delete_record` | Delete record |

Eve uses **task-specific** tools instead of generic CRUD for safer, narrower access from chat.

## empire-cognee tools

| Tool | Purpose |
|------|---------|
| `cognee_remember` | Store content in dataset |
| `cognee_recall` | Query memory |
| `cognee_improve` | Enrichment pass |
| `cognee_forget` | Remove dataset |
| `cognee_ingest_mock_file` | Ingest `mock_data_ingest` file |

All route through `pipeline/cognee_subprocess.py` with **cognee.lock**.

Default dataset in MCP is often `mock` — specify `primitives_test` or `eve_memory` explicitly when recalling.

## empire-wiki tools

Registered but **do not use for new work** per project policy. See [11-pipeline-and-ingestion](11-pipeline-and-ingestion.md).

## Cursor usage examples

**Recall curated primitives:**

```
Use cognee_recall with dataset primitives_test and query: "Pattern Weaver nexus points"
```

**Remember a note:**

```
cognee_remember content="..." dataset=eve_memory
```

**List tasks:**

```
pb_list_records collection=tasks perPage=20
```

## MCP vs Eve parity

| Capability | MCP | Eve |
|------------|-----|-----|
| Task CRUD | Generic + Eve-specific via REST in Eve | Typed task tools |
| Cognee recall/remember | Yes | Yes |
| Cognee improve/forget | Yes | Yes (added) |
| Mock file ingest | Yes | No |
| Model suite / switch | No | Yes |
| Wiki ingest | Yes (halted) | No |

## Troubleshooting

| Issue | Fix |
|-------|-----|
| MCP won't start | Check `PYTHONPATH`, venv python path in mcp.json |
| Cognee lock timeout | Close other Cognee users; see lock file |
| Auth failed (PB) | Verify `.env.local` admin email/password |

## Deferred wiring

See [docs/reference/MCP_WIRING_DEFERRED.md](../reference/MCP_WIRING_DEFERRED.md) for planned Postgres MCP and other integrations.

## Next

- [06-eve-agent](06-eve-agent.md)
- [13-development](13-development.md)
