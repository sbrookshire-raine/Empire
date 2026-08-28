# 08 — PocketBase

EMPIRE uses [PocketBase](https://pocketbase.io/) as a **local SQLite-backed API** for tasks and ingestion job tracking.

## Access

| Item | Value |
|------|-------|
| API | http://127.0.0.1:8090 |
| Admin UI | http://127.0.0.1:8090/_/ |
| Default admin | `admin@empire.local` / `empire-admin-change-me` |
| Data dir | `backend/pocketbase/pb_data/` (gitignored) |
| Binary | `backend/pocketbase/pocketbase.exe` (gitignored, setup downloads) |

## Collections

Defined in `backend/pocketbase/pb_migrations/`.

### `tasks`

| Field | Type | Notes |
|-------|------|-------|
| `title` | text | Required, 1–255 chars |
| `description` | text | Optional, max 5000 |
| `status` | select | `todo`, `in_progress`, `done` |
| `priority` | number | Optional |
| `created`, `updated` | autodate | |

Used by: Workbench Tasks tab, `index.html`, Eve tools `list_tasks` / `create_task` / etc.

REST: `GET/POST/PATCH/DELETE /api/collections/tasks/records`

### `ingestion_jobs`

Tracks pipeline ingest status (mock/curated/wiki).

| Field | Type | Values |
|-------|------|--------|
| `source_type` | select | slack, github, email, mock |
| `source_file` | text | |
| `status` | select | pending, running, success, failed |
| `records_ingested` | number | |
| `error` | text | |
| `started_at`, `finished_at` | date | |

Workbench memory jobs use **filesystem** job state under `data/eve_memory/jobs/`; PocketBase `ingestion_jobs` is used by older pipeline paths.

### `sources`

Connector metadata (stub for future live APIs).

| Field | Type |
|-------|------|
| `type` | select: slack, github, email, mock |
| `name` | text |
| `enabled` | bool |
| `last_sync_at` | date |

### Wikipedia extension

`1700000001_add_wikipedia_source.js` — wiki pilot schema (halted).

## Migrations

Apply automatically on PocketBase start. To reset dev DB: stop PocketBase, delete `pb_data/`, restart (migrations re-run).

## API consumers

| Consumer | Auth |
|----------|------|
| Frontend `index.html` | Public rules (dev) |
| `eve-workbench.js` | Public |
| Eve tools | Unauthenticated REST |
| MCP `empire-pocketbase` | Admin token from `.env.local` |

MCP has **generic** CRUD (`pb_list_records`, `pb_create_record`, …) beyond Eve's task-specific tools.

## Security

Migrations set **empty list/view/create/update/delete rules** = public access. This is intentional for **local-only** development. Harden rules before any non-loopback exposure.

## Next

- [06-eve-agent](06-eve-agent.md)
- [09-mcp-cursor](09-mcp-cursor.md)
