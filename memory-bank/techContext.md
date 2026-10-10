# Tech Context — Technologies, dev setup, dependencies

## Platform
- Windows 11 (PowerShell for command runs).
- Local repo: `C:\EMPIRE` (branch **`revision-refactor`**).
- Workbench data: `C:\Empire_Workbench\` (plus `D:\Empire_Workbench` copy documented in estate).

## Storage & mounts (verified 2026-10-07)
| Path | Present | Notes |
|------|---------|--------|
| `E:\EMPIRE_HUB` | Yes | Backup staging; see `99_INDEX/INDEX.md`, `RESTORE.md` |
| `Z:` (pool) | Yes | rclone union cloud pool (~20 TiB) |
| Cognee file root | **`E:\EMPIRE_COGNEE`** | Fresh NTFS root (2026-10); `config/cognee.env` — graph in Postgres |
| `V:\Cognee` / VHDX | **Optional** | Legacy; not required for language-first memory |
| `D:\wiki_md` | (runtime) | ~20 GB markdown corpus — keep; do not delete for space recovery |
| Cognee backup image | `K:\…\09_i_drive_leftovers` | 2026-09-27 copy when live V: unavailable |

**Before memory ingest or assuming T7 workflow:** run `Test-Path V:\Cognee` and read `docs/COGNEE_VHDX.md` + ESTATE §12.

## Services & ports
| Service | URL | Managed by EMPIRE |
|---------|-----|-------------------|
| Frontend | http://127.0.0.1:8080 | Yes |
| PocketBase | http://127.0.0.1:8090 | Yes |
| Eve | http://127.0.0.1:2000 | Yes |
| Ollama | http://localhost:11434 | No (user/OS) |
| Postgres (Cognee) | localhost:5432 | Docker |
| Speaches (voice) | http://127.0.0.1:8000 | opt-in |

## Stack
| Layer | Technology |
|-------|-----------|
| UI | HTML + HTMX + Alpine.js (CDN) |
| API | Python `frontend.serve` |
| Tasks | PocketBase |
| Memory | Cognee 1.4.0 + Postgres/pgvector |
| Inference | Ollama |
| Agent | Eve in `agents/empire-task-agent/` |
| MCP | FastMCP in `mcp/` + Cursor `.cursor/mcp.json` (gitignored) |
| Code graph | `graft/` + MCP `graft` via `npx -y @nanonets/graft mcp` |

## Cursor MCP (local)
- Empire servers: pocketbase, cognee, workbench, work-orders, wiki-scout, daze, stem-factory, tool-forge, loom-intake, etc.
- **graft** — present in `.cursor/mcp.json`; reload MCP in Cursor after edits.
- **Secrets** — never commit `mcp.json`; hub `00_CORE/local_only/` for offline backup only.

## Ollama context (critical)
```powershell
.\scripts\ensure-ollama-parallel.ps1 -NumParallel 1 -ContextLength 24576 -KvCacheType q8_0 -FlashAttention
```
Match `SHARED_NUM_CTX` in `agents/empire-task-agent/agent/lib/ollama-config.ts`.

## Configuration
- `config/cognee.env` — Postgres + `SYSTEM_ROOT_DIRECTORY` (may still reference `V:\Cognee` when mounted)
- `config/services.json` — stack orchestration
- `%LOCALAPPDATA%\EMPIRE\cognee.lock` — MCP/CLI serialization

## Mechanic-green (last run: 2026-10-07, Cursor sync)
Command: `.\scripts\mechanic-green.ps1` → **exit 1** (stack not running; storage paths missing).

| Step | Result | Notes |
|------|--------|--------|
| Unit tests | FAIL | 579 run; 2 fail + 2 err — `test_prompt_budget` (2), `test_wiki_drift_api` (2) |
| Capability governance | PASS | 7/7 verified |
| LEGO contract | PASS | WARN: `wiki_local` still lists Weaviate :8091 (retired) |
| Foundation registry | PASS (advisory) | forbidden/unregistered vault paths reported |
| Infra checks | PASS (advisory) | deptry/ruff/gitleaks logged to `eve-audit/` |
| Wiki extract battery | FAIL | `I:\EMPIRE_DATA\wiki-reports\2026\title-index.sqlite` missing |
| Workbench UI harness | PASS | 15/15 |
| verify-stack | FAIL | Ollama, PocketBase, frontend, Eve, Speaches down; Cognee worker **`V:\Cognee` mkdir failed** |
| operating contract | FAIL | services down |

**To green:** start stack (`Start-EMPIRE.bat` or `.\scripts\start-stack.ps1`), remount Cognee VHDX **or** repoint `SYSTEM_ROOT_DIRECTORY` in `config/cognee.env`, restore/build wiki title index on available drive (or fix `WIKI_ROOT` / report paths off `I:`).

## Daily use
- Start: `Start-EMPIRE.bat` or `.\scripts\launch-empire.ps1`
- Eve UI: http://127.0.0.1:8080/eve.html
- Gate: `.\scripts\mechanic-green.ps1`

## Constraints
- Node/npm only under `agents/empire-task-agent/`.
- No paid cloud LLM in app code (build phase: Cursor frontier; runtime: Ollama).
- Cloud **backup pool** (`Z:`) is operational infrastructure — not a runtime BaaS violation.
