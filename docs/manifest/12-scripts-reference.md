# 12 — Scripts reference

All scripts: `scripts/*.ps1` (Windows PowerShell). Run from **repo root** unless noted.

## Daily operations

| Script | Purpose |
|--------|---------|
| **`Start-EMPIRE.bat`** (repo root) | **Double-click launcher** — Ollama + full stack + browser |
| **`launch-empire.ps1`** | Same as bat; `-NoBrowser` to skip opening Eve Workbench |
| **`start-stack.ps1`** | **Preferred cold start** — VHDX mount, Postgres, PocketBase, frontend, Eve |
| `roll-in.ps1` | Start services in order (Ollama verify → PB → UI → Eve) |
| `roll-out.ps1` | Stop managed services (reverse order) |
| `verify-stack.ps1` | Integration health checks |
| `refresh-dashboard.ps1` | Regenerate `frontend/dashboard-status.json` |
| `check-status.ps1` | Quick status snapshot |

## Individual services

| Script | Purpose |
|--------|---------|
| `start-pocketbase.ps1` | PocketBase foreground (terminal attached) |
| `start-pocketbase-background.ps1` | PocketBase background |
| `start-frontend.ps1` | `python -m frontend.serve` on :8080 |
| `start-eve.ps1` | Conditional build + Eve on :2000 |

## Setup and storage

| Script | Purpose |
|--------|---------|
| `setup.ps1` | Venv, pip, PocketBase download, `.env.local` |
| `create-cognee-vhdx.ps1` | One-time VHDX create (Admin) |
| `mount-cognee-vhdx.ps1` | Attach VHDX → `V:` (Admin) |
| `ensure-cognee-postgres.ps1` | Docker Postgres for Cognee |

## Ingestion

| Script | Purpose |
|--------|---------|
| `ingest-curated-primitives.ps1` | Curated `primitives_test` ingest |
| `ingest-mock.ps1` | Single mock file |
| `ingest-all-mocks.ps1` | All mock fixtures |
| `cleanup-stale-ingestion-jobs.ps1` | Fix stuck PocketBase ingestion_jobs |

## Ollama / Eve helpers

| Script | Purpose |
|--------|---------|
| `ensure-ollama-parallel.ps1` | Ollama parallel env tuning |
| `ensure-eve-build.py` | Called by start-eve when sources newer than build |

## Wiki (halted — reference only)

| Script | Purpose |
|--------|---------|
| `start-wiki-ingest-overnight.ps1` | Overnight wiki batch |
| `watch-wiki-ingest.ps1` | Monitor wiki ingest |
| `wiki-maintenance.ps1` | Wiki maintenance |
| `wiki-handoff-after-overnight.ps1` | Post-run handoff |
| `export-wiki-report.ps1` | Export wiki report |
| `seed-priority-subjects-from-codex.ps1` | Seed wiki priorities |

## Python verification (not .ps1)

```powershell
.\venv\Scripts\python.exe .\scripts\verify-eve-workbench.py
```

## Next

- [03-getting-started](03-getting-started.md)
- [04-services-and-ports](04-services-and-ports.md)
