# MCP wiring deferred — wiki overnight ingest

**Status:** DEFERRED (2026-07-23)  
**Decision:** Do **not** edit `.cursor/mcp.json` until wiki overnight ingest is idle.

## Why

Wiki ingest was active when wiring was requested:

- Overnight script: `scripts/start-wiki-ingest-overnight.ps1` (Year 2017)
- `python -m pipeline.wiki_ingest --year 2017 --batch 1 --mode fast`
- Checkpoint: `%LOCALAPPDATA%\EMPIRE\wiki-checkpoint.json` → `2017/batch_00001` `in_progress`
- Log: `I:\EMPIRE_DATA\logs\wiki-ingest-overnight-2017-*.log` (live writes)

Risks of editing `mcp.json` now:

1. Cursor may reload **all** MCP servers, including `empire-cognee`, while ingest holds `cognee.lock` / Postgres.
2. Registering **postgres-mcp** against `cognee_db` adds connection/lock pressure during concurrent remember/embed.
3. Even **readable-mcp** alone is unsafe if the only way to add it is editing `mcp.json` (uncertain full MCP restart).

## When idle — wire both

Confirm ingest idle (no overnight / `wiki_ingest` processes; checkpoint batches not actively advancing; log not growing). Then add to `.cursor/mcp.json` **without** removing `empire-pocketbase` / `empire-cognee` / `empire-wiki`:

```json
"empire-postgres": {
  "command": "C:/EMPIRE/venv/Scripts/python.exe",
  "args": ["-m", "postgres_mcp"],
  "env": {
    "DATABASE_URI": "postgresql://cognee:cognee@localhost:5432/cognee_db",
    "PG_MCP_ACCESS_MODE": "readonly"
  }
},
"empire-readable": {
  "command": "C:/EMPIRE/venv/Scripts/python.exe",
  "args": ["-m", "readable_mcp"],
  "env": {}
}
```

Install first if needed (`pip install postgres-mcp readable-mcp` in the EMPIRE venv). Confirm module names via skill `scripts/main.py --check-install`. Prefer **readonly** Postgres mode.

Skills: `.cursor/skills/postgres-mcp-specialist/`, `.cursor/skills/readable-mcp-scrape/`.
