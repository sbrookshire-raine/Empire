# Active Context — Current work focus & next steps

## Current state snapshot (as of 2026-10-08, branch `revision-refactor`)
- **Canonical branch:** `revision-refactor` — **145 commits ahead of GitHub `main`** (last `main`: Eve Clarity / resource pulse). Do not treat `main` as current until merged.
- Repository is **already built**; day-to-day work = feed documents into Cognee + Architect smoke / refactor phases — not a UI rebuild.
- **Answer path** refactor target: `docs/REFACTOR_PLAN.md` (`intent → resolution → evidence → answer`), phases **R-01..R-05**.

## Backup tiers (Architect model — Oct 2026)
| Tier | Role | Status |
|------|------|--------|
| **C: / D:** | Primary EMPIRE workspace (repo, vault, `D:\wiki_md` runtime) | Active; not a backup alone |
| **E:** | `E:\EMPIRE_HUB` staging + local SSD backup (~797 GiB) | **Staging complete** (`stage_chain.log` → CHAIN DONE) |
| **Z:** | `pool:` union (~20 TiB), mount `Z:` via rclone / `cloud_archiver_hub.py` | **`pool:EMPIRE_HUB` ~764 GiB** — consolidation upload **complete** |
| **Offline disc** | Full E: tree incl. `local_only` | **Not done** — blocks aggressive C:/D: cleanup |

Secrets: `E:\EMPIRE_HUB\00_CORE\local_only\` — **never cloud** (excluded in `config/hub-upload.json`).

**Gap (irreplaceable, not in hub):** ~**719 GiB** Kiwix ZIMs on `F:\AI_ARCHIVE\AI_Archive_Legion\knowledge_bases`; **`pool:ZIM_RESOURCES` ~302 MiB** — separate upload still pending.

Canonical docs: [`docs/BACKUP_CONSOLIDATION.md`](../docs/BACKUP_CONSOLIDATION.md), ESTATE §12, ODYSSEY §14, `E:\EMPIRE_HUB\99_INDEX\`.

## Infra caveat (verified 2026-10-07 on this machine)
- **`V:\Cognee` not mounted**; **`I:\EMPIRE_VHDX` path absent** — `I:`/`G:`/`H:`/`J:` show identical sizes (Drive alias). AGENTS “plug T7 → mount V:” may not apply until remounted.
- Cognee image for backup: 2026-09-27 copy in hub `00_CORE/state/cognee_vhdx/`. Live graph uses Docker Postgres per `config/cognee.env`.

## Prompt budget (key numbers)
- Floor before user speaks ≈ **~4,130 tokens** (post R-03: tool docs in `config/eve-capabilities/tool-docs/`, fetched via `tool_docs`).
- **~94 agent tool files**; **84 MCP** tools; ceilings in `tests/test_prompt_budget.py`.
- Fast mode: **`empire-fast:14b`** (locked); 7B not suitable for multi-card tool reasoning (E-16).

## Cursor / Cline session continuity
- **Memory Bank** (`memory-bank/`) — agent session reset (local, untracked); not Eve runtime memory.
- **graft** — `graft/` graph + MCP `graft` in `.cursor/mcp.json`; run `npx @nanonets/graft build` after large code edits.
- **Read order for fresh sessions:** `docs/DOC_MAP.md` §1 → ESTATE §12 → ODYSSEY §14 → `BACKUP_CONSOLIDATION.md` → REFACTOR_PLAN → `EMPIRE_GUIDE.md`.
- **Portfolio:** `docs/PORTFOLIO.md`; sync checklist `docs/PORTFOLIO_MAINTENANCE.md`.

## Quality gates (before Architect UX smoke)
- `.\scripts\mechanic-green.ps1` (and `-Full` for live workbench).
- `.venv\Scripts\python.exe scripts\smoke-eve-hands.py --eve-chat`
- `python -m pipeline.playbook --coverage`

## Next steps / backlog
- **Backup:** offline disc from E:; plan ZIM → cloud upload; future incremental hub sync after C:/D: changes (see BACKUP_CONSOLIDATION § Future).
- **Space recovery:** C:/D: deletes per `SPACE_RECOVERY.md` only after offline disc (+ ZIM decision).
- **Architect smoke:** T-01 Wiki, T-02 DAZE, T-03 Stem, then T-04…T-09.
- **Refactor:** R-02 resolution semantics (E-13 ambiguity); R-04/R-05 gates in mechanic-green.
- **Optional:** merge `revision-refactor` → `main` when Architect wants GitHub default updated.

## Last memory-bank action
2026-10-08 — Consolidation status locked: hub upload verified; `hub-upload.json` phase `consolidation_complete`; BACKUP_CONSOLIDATION + SPACE_RECOVERY updated. Z: remount is manual after reboot (`cloud_archiver_hub.py`).
