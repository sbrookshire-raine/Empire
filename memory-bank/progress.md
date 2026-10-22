# Progress — What works, what's left, current status
# Progress — What works, what's left, current status
## 2026-10-22 — The wiki limb is whole: full index, live hop, bounded prefetch

**Working (872 passed / 1 skipped / 0 failed):**

| Thing | Before | Now |
|---|---|---|
| Title DNS titles | 4,095,795 (57%) | **7,138,751 (all 143 batches)** |
| `wiki_extract_battery` | skipped by the gate | **runs: 11/11, 0 skipped** |
| Wiki chat smoke | 3 known-gaps + 3 failures, exit 1 | **PASS** (7 live + 5 injection) |
| Live routing battery | 7/7 (fragile) | **7/7** |
| Memory ask (session create) | **110 s** (6 sequential recalls) | **~21 s** (one bounded recall) |

**E-10 is closed.** The gap was never the model: the index did not have the
page ("Stranger Things" resolved to the ABC *song*) and the link web was
empty, so Eve was reporting the wrong page faithfully. The index is rebuilt
and the hop affordance is live — `ensure_links` (a page's own outgoing links,
scanned on demand), `related_titles` (titles that contain the subject),
`hop_titles` (one rule both callers ask), and the hop evidence carries the
page's section and its outline, so three song sections sit next to their own
season instead of one prose wall.

**The gate now asks the runtime where the corpus is** (`scripts/wiki-index-path.py`)
instead of hardcoding `I:\`, and the battery is corpus-aware: a case whose
page is not in the corpus is a loud SKIP, not a FAIL.

**Still open:**
- The chat prefetch still costs ~20 s (one Cognee recall ≈ 15 s on this
  machine). It is bounded now, but it is the slowest thing in a chat turn.
- The bulk link web is still unbuilt (14.5 h at 136 pages/s). The on-demand
  scan covers the pages that are actually visited.
- Weaviate (`:8091`) is still opt-in; the wiki limb works without it.
- `empire-fast:7b` still cannot do native tool calls — a model property.

## 2026-10-21 — Phase 2 closed (green suite + calibrated ceilings + model evaluation)

**Working:** the whole suite is green (**849 passed / 1 skipped / 0 failed**),
the green gate passes offline *and* with the enforced live tier, the
prompt-budget ceilings are calibrated against a live measurement, and the
7B/14B promotion decision is now *measured* rather than inherited.

**The seven pre-existing failures are fixed** (root causes in
`activeContext.md`). The non-obvious one: the workbench theme rule ("every
colour lives in a `:root` token") was broken by 8 literal `oklch()` values in
the limb meter, and the workbench was running a second background loop (an 8 s
limb-meter poll) that the polling guard forbids.

**Prompt budget:** the live measurement is **6,688 real tokens** against a
6,410-token chars/3.8 estimate (**+4.3%**).
`pipeline.prompt_budget.LIVE_OVER_ESTIMATE` carries that calibration and the
ceilings in `tests/test_prompt_budget.py` are now written in real tokens.

**Model decision (E-12):** `empire-fast:14b` **promoted** (6/6 gates).
`empire-fast:7b` **not promoted** — it fails the live routing battery (5/7):
it writes tool calls as JSON prose in the message body, so no tool runs and the
task is never created. The proxy gate passes for it, which is exactly why the
live battery exists. Evidence: `eve-audit/promotion-2026-10-21/gates.txt`.

**Not done / deferred:** Title DNS rebuild (57% coverage) and Weaviate stay out
of scope. The 7B's native-tool-calling gap is a model property, not a code bug.

## 2026-10-21 — Live tier exercised (Phase 2)
## 2026-10-21 — Live tier exercised (Phase 2)

**Working:** the live tier now runs against a real stack and proves two
things the offline tier cannot: that each ask reaches a tool *its route*
implies (E-03 battery, 7/7 measured), and what the model is *actually*
charged for the prompt (6,669 real tokens vs 6,388 estimated).

**New:** `pipeline/live_probe.py` (structured turn evidence + correct-tool
assertions), `config/diagnostics/live-routing-battery.json`,
`scripts/verify-live-routing.py`, `scripts/measure-live-prompt.py`,
`pipeline/intent_codex.load_intents()`.

**Fixed (real defects the live tier found):**
- a stray `</translation>` with no opener survived sanitization and reached
  the bubble and the speaker;
- every `tool.result` trace line recorded `"tool": null` (wrong field path);
- the live harnesses proved tool calls by grepping the raw blob, which
  passes when the model merely *mentions* a tool.

**Test state:** 754 tests, the same 7 known pre-existing failures (was
734/7 -- 20 added, no regressions). Browser harness 17/17.

**Not done / deferred:** the 7B/14B sequential evaluation (E-12/E-16) and
the Title DNS rebuild (57% coverage) stay parked; Weaviate stays out of
scope. Prompt-token *budgeting* is next: the live number is 4.4% above the
chars/3.8 estimate, so the static ceilings are slightly optimistic.
## 2026-10-21 — Shared route classifier + enforced live gate (Phases 0–1)

**Working:** one classifier decides wiki / memory / task / other, and every
caller agrees with it; the green gate can now *require* the live tier and
fails if it did not run; the capabilities report names the always-on tools.

**Test state:** 734 tests, 7 failures (baseline was 678 / 8 — one fixed, 56
added, no regressions). The 7 are the known pre-existing set: 2
`eve_workbench_static`, 2 `wiki_drift_api` (`extract_search_query` band
extraction, unrelated to routing), 1 thin playbook area, 2 prompt-budget
ceilings.

**New:** `pipeline/route_classifier.py`, `docs/ROUTE_CLASSIFIER.md`,
`POST /api/route/classify`, `tests/pipeline/route_corpus.py` (~50 cases
shared by the classifier test and the caller-parity test).

**Fixed along the way (all pre-existing defects, not new features):**
- the live harnesses were posting a nested toolbelt that the toolbelt path
  never read — every live measurement was against the wrong surface;
- `context_block()` overrode the codex with a second wiki rule, so
  `resolve()` and `context_block()` could pick different routes;
- the browser carried a third copy of the routing rules;
- a stalled stream sat silent for 600 s and then reported a generic
  "disconnected" that named no cause;
- `cognee_recall` never appeared in the report that lists what Eve can call.

**Not done / deferred:** the live tier has never been exercised here (no
Ollama/Eve/frontend stack in this environment), so `mechanic-green.ps1
-Live` is implemented and enforced but unrun. The live harness rewrite
(structured `tool.requested` events, correct-tool selection, measured prompt
tokens, 7B promotion criteria) is still outstanding. Title DNS rebuild
(57% coverage) and Weaviate remain out of scope.

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