# Active Context — Current work focus & next steps
# Active Context — Current work focus & next steps
## 2026-10-21 — Phase 2 closed: 7 baseline failures fixed, ceilings calibrated, 7B/14B measured

**The seven known pre-existing failures are gone.** The suite is now
**849 passed / 1 skipped / 0 failed** (was 842 passed / 7 failed).

| Failure | Root cause | Fix |
|---|---|---|
| `eve_workbench_static` — CSS colour rule | 8 lines in the limb meter used literal `oklch(...)` outside the `:root` token block | hoisted into `--tone-*` tokens |
| `eve_workbench_static` — `setInterval` count | the limb meter polled every 8 s — a second background loop | poll removed; the meter now refreshes on tab switch, turn, tool step and admission change |
| `wiki_drift_api` ×2 — `extract_search_query` | the album-discography pattern swallowed the quoted subject ("The band 'the white stripes discography") | `_ROLE_QUOTED_RE`: a role word + quoted phrase is an explicit title and wins |
| `test_playbook` — thin sections | `intake-and-legos` carried 1 and 0 worked examples | 5 and 5 examples, written from the tool docs |
| `test_prompt_budget` ×2 | the ceilings were written in *estimate* space (chars/3.8), which undercounts by 4.3% | ceilings are now **real** tokens; `prompt_budget.LIVE_OVER_ESTIMATE` carries the calibration |

### The calibration
Measured live (2026-10-21, `empire-fast:14b`): **6,688 real prompt tokens**
against a 6,410-token static estimate → **+4.3%**. `LIVE_OVER_ESTIMATE = 1.044`
maps the estimate onto the real scale, and the calibrated estimate (6,692) lands
4 tokens from the truth. The ceilings moved to 5,300 / 1,575 / 6,800 real
tokens. `scripts/measure-live-prompt.py` is the tool that takes the measurement.

### Gates
- `mechanic-green.ps1` — every step PASS.
- `mechanic-green.ps1 -Live` — PASS, and the live tier is **enforced**
  (`live_ran=true`; a stale report cannot satisfy it).
- Browser harness 17/17; `verify-stack` 19/19; `audit-empire` contract satisfied.

### Model promotion (E-12/E-13) — measured, not inherited
Six gates: **14B 6/6 PASS**, **7B 5/6 FAIL**. The 7B passes the proxy
tool-calling gate but **fails the live routing battery (5/7)**: on
`memory_recall` and `task_create` it writes the tool call into the message
*body* as JSON prose instead of emitting a native `tool_calls` payload, so the
sanitizer strips it and **the task is never created**. Evidence:
`eve-audit/promotion-2026-10-21/gates.txt`. The Fast A/B variant was reset to
**a** (`empire-fast:14b`).

### Next
- Architect UX smoke is unblocked (the gate is green).
- The 7B stays a candidate; it would need native tool calling in the live agent.
- Title DNS rebuild (57% coverage) and Weaviate remain out of scope.

## 2026-10-21 — Live tier exercised (Phase 2): routing battery + real prompt tokens
## 2026-10-21 — Live tier exercised (Phase 2): routing battery + real prompt tokens

**The stack was up.** Last session the live tier was blocked with no
Ollama/Eve/frontend; this session all four services answered. That turned
"the live tier is implemented but unrun" into a tier that ran -- and it
found three real defects on the first pass.

### What the live tier now proves

- **`scripts/verify-live-routing.py`** (E-03 battery) reads the framework's
  **structured** events (`actions.requested` -> `data.actions[].toolName`,
  `action.result` -> `data.result.toolName`) instead of grepping the raw
  blob for a tool name. The old string match passed when the model merely
  *mentioned* a tool. Expectations come from the shared classifier + codex
  at run time, so the battery cannot assert what the system does not claim.
- **`scripts/measure-live-prompt.py`** reports the prompt the model is
  *actually* charged: **6,669 real tokens vs 6,388 estimated (+4.4%)**,
  17,907 tokens of headroom in the 24,576 window.
- Both are wired into `config/diagnostics/capability-verification-battery.json`
  as live probes, so `verify-capabilities -Live` and `mechanic-green -Live`
  enforce them. The live tier has now run clean: 4/4 live checks, 39 total.

### The contract the battery taught us

"No tool was called" is **sometimes correct**: the server's green path
prefetched the archive extract and told Eve to skip the tool call. The
battery therefore asserts two things -- **no foreign tool** (a route never
reaches into another route's tools) and **the right tool when one is due**.
The first version asserted "a tool must be called" and failed two wiki
cases that were answered correctly. That was a wrong assertion, not a
system bug. Measured live: **7/7 cases route correctly**.

### Three defects found and fixed

1. **Stray `</translation>` reached the bubble and the speaker.** A closing
   tag with no opener survived sanitization (the paired-block rule needs
   both). Fixed in `frontend/eve_proxy.py` for both the stateless stripper
   and the streaming filter -- re-verified live: 0/4 leaks (was 1/3).
2. **Every `tool.result` trace line said `"tool": null`.** The name is on
   `data.result.toolName`, not `data`. Fixed in `frontend/serve.py`.
3. **The model sometimes emitted its tool call as content, not a call.**
   Not a code bug -- but the battery now *measures* it instead of hiding it.

### Test state

754 tests, the same **7** known pre-existing failures (was 734/7 -- 20 added,
no regressions). Browser harness 17/17.

### Next

- Prompt-token budgeting: the live number is 4.4% above the chars/3.8
  estimate, so the static ceilings are slightly optimistic.
- Sequential 7B/14B evaluation (E-12/E-16) -- still parked. The promotion
  gates are now written down and executable (see `docs/CAPABILITY_VERIFICATION.md`).
- Title DNS rebuild (57% coverage) and Weaviate remain out of scope.

## 2026-10-21 — Shared route classifier + enforced live gate (Phases 0–1)

Two defects that made routing unprovable are fixed. **Baseline was 678 tests /
8 failures; now 734 / 7** (one baseline failure fixed, 56 tests added, no
regressions). The 7 remaining failures are the known pre-existing set.

### Phase 0 — the gate now proves things

- **`scripts/mechanic-green.ps1` has `-Live`** and **enforces** it: the live
  tier's report (`tmp/capability_verification_report.json`) must say
  `live_ran: true`, else the gate FAILS. A stale report is deleted first, so
  a previous run cannot satisfy it.
- **Capabilities report** (`pipeline/capability_verification.py`) now names
  the **always-on tools** (31, incl. `cognee_recall`) and the `wiki_local`
  default-on set, and says plainly whether the live tier ran. New offline
  check `always_on_tools`; the always-on set is defined **once** in
  `pipeline/tool_registry.py::always_on_tools()`.
- **Toolbelt shape**: the toolbelt path only ever read a **flat**
  `active_tools`; the live harnesses posted **nested**
  `{"toolbelt": {"active_tools": [...]}}`, which was silently dropped — so
  every live routing measurement was taken against a toolbelt that was never
  applied. `frontend/eve_toolbelt.py::extract_active_tools()` now reads both
  (flat wins); the harnesses send flat lists and restore the operator's
  toolbelt afterwards (`temporary_active_tools`).
- **No more 600-second silence**: `frontend/eve_proxy.py` now has two
  deadlines — a first-event deadline (90 s, the model never started) and a
  steady-state one (300 s, stalled mid-turn) — and reports *which*:
  `STREAM_NO_EVENTS_MESSAGE` / `STREAM_STALLED_MESSAGE` / (clean EOF)
  `STREAM_ENDED_EMPTY_MESSAGE`, each naming the check to run.

### Phase 1 — one classifier for wiki / memory / task

- **New: `pipeline/route_classifier.py`** — `classify()` returns
  `wiki | memory | task | other`. Precedence: explicit wiki signal → memory
  anchor → task → encyclopedic subject → generic wiki verb → other.
  Documented in [`docs/ROUTE_CLASSIFIER.md`](../docs/ROUTE_CLASSIFIER.md).
- **`intent_codex.context_block()` no longer overrides** the codex with a
  wiki rule; `resolve()` applies the route and reports it, and
  `context_block()` uses the same result. `min_score` aligned (4).
- **Callers now agree**: `is_wiki_lookup_query` (classifier can veto; the
  legacy regexes are a fallback), `is_memory_chat_query`, the wiki green
  path, and the browser.
- **The browser no longer carries routing rules**: `isMemoryQuery()` calls
  the new `POST /api/route/classify` endpoint and **fails open to Eve** on
  any error. The endpoint itself fails closed (503) so the fault is visible.
- **Corpus**: `tests/pipeline/route_corpus.py` (~50 cases) is read by both
  `test_route_classifier.py` and `test_route_classifier_parity.py`, so the
  classifier and every caller are held to the same contract.

### Known remaining failures (7, all pre-existing)

2 `eve_workbench_static`, 2 `wiki_drift_api` (`extract_search_query` band
extraction — unrelated to routing), 1 thin playbook area, 2 prompt-budget
ceilings.

### Next (not done)

- **Live tier never ran here**: no stack (Ollama/Eve/frontend) in this
  environment. `mechanic-green.ps1 -Live` is implemented and enforced but
  needs a live stack to exercise.
- **Live harness rewrite** (structured `tool.requested` events, correct-tool
  selection, real prompt-token measurement, 7B promotion criteria) — deferred
  to Phase 1's live half; the offline toolbelt fix is in.
- Title DNS rebuild (57% coverage) and Weaviate are still **out of scope**.

## 2026-10-21 — REA Bin-1 integration landed (live, verified)

Six Gumloop REA skills + the claim-ledger MCP are now in EMPIRE, gated behind
two new Toolbelt limbs (`rea_skills`, `claim_ledger`).

- **Runner:** `pipeline/rea_skills.py` — allowlist of exactly 6, paths jailed to
  `eve-output/rea-skills`, upstream tree copied to scratch before running
  (never modified), interpreter resolved explicitly (`python3` is a broken
  Store alias on this host).
- **Vendored upstream:** `vendor/rea-skills/` (byte-identical to the bundle).
  The other 16 skills are deliberately absent and a test asserts it.
- **EVE surface:** `rea_skills` + `claim_ledger` tools, `skill-rea-skills` +
  `skill-claim-ledger` skill files, playbook examples in
  `config/eve-capabilities/playbook/reverse-engineering.md`.
- **Claim ledger:** `mcp/claim_ledger_mcp.py` — three upstream Windows bugs
  fixed (drive-letter root parsing, always-true cwd guard, shell selection).
- **Rollback:** `scripts/rollback-rea-integration.ps1` (one command, `-WhatIf`
  supported).
- **Docs:** `docs/rea-integration/probe-log.md` (evidence) and
  `approval-matrix.md` (Bin-1/Bin-3 split + safety invariants).

Verified live: Eve called both tools on the wire; `verify-capabilities -Live`
36/36; `verify-stack` 19/19; `audit-empire` "contract satisfied".

**Key host facts learned (do not re-derive):**
- `python3` is a Microsoft Store alias stub — unusable. Use the repo venv.
- EVE rejects unknown frontmatter keys: the upstream skills' `icon:`/`color:`
  make them unloadable, hence EMPIRE-authored skill files.
- The installed `rea-agents` is **6.3.0** while the bundle targets 6.5.0; some
  readers the skills document do not exist in the live 139-tool list.
- `objdump`, `gdb`, `tshark`, `binwalk`, `adb`, `frida` are all absent.
- `pipeline.capability_index` needed a UTF-8 stdout guard on this console.

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
- Floor before the user speaks: **6,688 real tokens** (measured live 2026-10-21) of a 24,576 window — 17,888 tokens of headroom. The static chars/3.8 estimate says 6,410; `LIVE_OVER_ESTIMATE = 1.044` bridges the two.
- Ceilings in `tests/test_prompt_budget.py` are in **real** tokens (5,300 / 1,575 / 6,800). Re-measure with `scripts/measure-live-prompt.py` before raising one.
- **~94 agent tool files**; **84 MCP** tools; tool detail lives in `config/eve-capabilities/tool-docs/`, fetched via `tool_docs` (R-03).
- Fast mode: **`empire-fast:14b`** (promoted, 6/6 gates); 7B not promotable — it writes tool calls as prose, so no tool runs (E-12).

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
2026-10-21 — Phase 2 closed: the seven known pre-existing failures are fixed (849 tests,
0 failures), the prompt ceilings are calibrated on a live measurement (6,688 real vs 6,410
estimated, +4.3%), the green gate passes with the live tier enforced, and the 7B/14B
promotion decision is measured — 14B 6/6, 7B 5/6 (fails the live routing battery).
