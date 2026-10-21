# Progress — What works, what's left, current status

## 2026-10-21 — REA Bin-1 integration (working, live-verified)

**Working:** six REA skills (`rea_skills` tool) + the claim-ledger MCP
(`claim_ledger` tool), both as opt-in Toolbelt limbs. 678 unit tests (35 new;
clean-HEAD baseline is 643/8), `verify-capabilities -Live` 36/36, `verify-stack`
19/19, `audit-empire` clean.

**Fixed along the way (all pre-existing bugs, not new features):**
- claim-ledger: Windows drive-letter root parsing, always-true cwd guard,
  shell selection (a bare `cmd.exe` failed because `executable=` does no PATH
  lookup), and a missing DB directory.
- `pipeline/eve_operating_context.py`: the proven-tool list was written twice,
  pushing the always-on prompt over its ceiling. Now 4940 tokens (was 5033).
- `pipeline/capability_index.py`: UTF-8 stdout guard (the CLI died with
  UnicodeEncodeError on a cp1252 console).

**Known pre-existing failures (8, unchanged by this work):** two
`eve_workbench_static` assertions, two `wiki_drift_api` lookups, one
`intake-and-legos` thin playbook area, and the two prompt-budget ceilings
(`default_schema_weight` 1447 > 1220 at HEAD and now; `floor` 6481 at HEAD,
6387 now — this work *lowered* it but not below the 6250 ceiling).

**Not done / deferred:** the 16 Bin-3 skills are deliberately absent (a test
asserts it). `forkdive`/`discover` have not been run against the live network.
`verify-capabilities -Live -SyncCognee` was not run (it writes to `eve_core`).

## Git / GitHub (2026-10-08)
| Branch | Role |
|--------|------|
| `revision-refactor` | Active development; pushed through docs/estate/hub work + mid-branch engineering (P2–P13, plan accuracy) |
| `main` | **Stale on GitHub** (~145 commits behind); last tip: Eve Clarity (resource pulse, verification green) |

Tracked in git: `memory-bank/` (6 files). Untracked locally: `.clinerules`
(Cline Memory Bank rules) — not on GitHub unless explicitly added.

## What works
- **Eve Core:** chat, PocketBase tasks, Cognee recall, staging→confirm memory, companion profile / architect_now.
- **LEGO:** Truth Drift (wiki scout + `D:\wiki_md` read path), DAZE, Stem Factory (Shard / Demucs limb).
- **LEGO Whiteboard:** `lego.html`.
- **Capability system:** Toolbelt, resource pulse, admit_for_goal, playbook + `tool_docs` (R-03).
- **Packaged skills:** `eve-skills/` (five local packages with tests); 33 `agent/skills/*.md` still inert (E-29).
- **Docs:** `DOC_MAP`, `ESTATE_INVENTORY`, `BACKUP_RUNBOOK`, `BACKUP_CONSOLIDATION`, `ODYSSEY` (§14 hub), `REFACTOR_PLAN`, operating contract + audits.
- **Code graph:** `graft/` wiring cards; MCP graft server configured.

## Oct 2026 deliverables (estate / backup)
- **EMPIRE_HUB** on `E:\` — **staging complete**; index, restore, SPACE_RECOVERY; ~797 GiB.
- **`pool:EMPIRE_HUB` on Z:** — **~764 GiB uploaded**; consolidation check green with `hub-upload.json` excludes (2026-10-08).
- **Cloud pool** `Z:` (rclone union, ~2.45 TiB used / 20 TiB); remount after crash via `E:\cloud_archiver_hub.py`.
- **Stem factory outputs** (~519 GB on `G:\…\Music\stem_factory`) documented; gap-chain `05_stem_factory_T8` queued.
- **Wiki layer audit** documents 20 GB `D:\wiki_md` corpus; Weaviate drain-only.

## Phases status (EMPIRE_MANIFESTO.md)
| # | Phase | Status |
|---|-------|--------|
| 1 | Intake & Triage | Working |
| 2 | Evaluation | In progress |
| 3 | Thought Experiments | In progress |
| 4 | LEGO Whiteboard | Working |
| 5 | Time reclamation | Working |
| 6 | Secure remote access | Planned |
| 7 | Real-time voice | Scaffold (Speaches :8000) |

## What's left / in progress
- **Offline disc** copy of full `E:\EMPIRE_HUB` (incl. secrets).
- **ZIM library** (~719 GiB on F:) — not in EMPIRE_HUB; cloud upload to `pool:ZIM_RESOURCES` not done.
- Refactor **R-02..R-05** exit criteria.
- Architect smoke **T-01..T-09**.
- C:/D: space recovery per `SPACE_RECOVERY.md` (hub cloud gate satisfied; disc + ZIM still block big deletes).
- Remount or repoint Cognee if `V:\Cognee` required on this machine layout.
- E-29 skill packaging cleanup.

## Health checks
```powershell
.\scripts\mechanic-green.ps1
.\scripts\mechanic-green.ps1 -Full
.\venv\Scripts\python.exe scripts\smoke-eve-hands.py --eve-chat
```

## Current status
2026-10-08 — Hub consolidation upload verified; docs and memory bank aligned. See `techContext.md` for last mechanic-green on this machine.
