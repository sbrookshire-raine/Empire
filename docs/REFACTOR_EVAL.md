# Refactor Evaluation (2026-09-24)

Scope: the `revision-refactor` branch. Companion to [`REFACTOR_PLAN.md`](REFACTOR_PLAN.md) — the plan
says *what is structurally wrong and in what order*; this document says *what is actually here, what
connects, what is leftover, and what was changed as a result*.

Method: reference-graph audit with `scripts/audit-orphans.py` (every candidate source file, references
counted across the repo and split by referrer: code / tests / scripts / docs / other). Files wired
from **outside** the repo (Windows Task Scheduler, `.cursor/` hooks, `.bat` entry points) were then
verified by hand — a zero in-repo reference count is a question, not a verdict.

---

## 1. Findings

### 1.1 Modules are healthy

`pipeline/` (78 files), `frontend/` (26) and `mcp/` (24) returned **zero orphans and zero
docs-only files**. Every module is referenced by code. The problems in this project are not dead
modules — they are prompt budget, tool-surface count and documentation drift (§3 of the plan).

### 1.2 Scripts: most "orphans" are wired outside the repo

The audit flagged 12 non-test files. Hand verification classified them:

| File | Wired to | Verdict |
|------|----------|---------|
| `scripts/install-upgrade-workers.ps1`, `start-memory-watchdog.ps1`, `start-research-scavenger.ps1`, `stop-upgrade-workers.ps1`, `status-upgrade-workers.ps1`, `remove-upgrade-workers.ps1` | Windows Task Scheduler tasks **`EMPIRE-AmbientMemoryWatchdog`** and **`EMPIRE-ResearchScavenger`** (both registered and running `config/eve-capabilities/*.py`) | **Keep** — a complete ops family (install/start/stop/status/remove) for two live workers. Undocumented in the repo, which is why it looked dead. Documented §2.3 |
| `scripts/capability-kill-switch.ps1` | the capability-governance system (`verify_capability()` fail-closed; `mechanic-green` has a governance step) | **Keep** — governance kill switch is the *fail-closed* control; removing it would leave no way to disable arms fast |
| `scripts/build-project-catalog.ps1` | `frontend/project_catalog.save_project_catalog` (live module) | **Keep** — it is that module's builder entry point |
| `scripts/ingest-workbench.ps1` | calls `scripts/ingest_workbench.py`, and pre-validates venv + `V:\Cognee` mount + `nomic-embed-text` | **Keep** — it is the safe front door for the memory ingest |
| `scripts/run-graft-build.ps1` | `graft/` (generated) and `.cursor/hooks/graft-hooks.cjs`, `.cursor/rules/graft.mdc` | **Keep** — dev-navigation tooling; it is the sanctioned `npx` exception (build-time, not app code) |
| `scripts/stop-voice.ps1` | pairs with `start-voice.ps1` (11 references); stops the Speaches container | **Keep** — asymmetric before: `start-voice` documented, `stop-voice` not. Documented §2.3 |
| `scripts/test-wiki-librarian-vs-fast.py` | posts to `/api/eve/session` with an explicit `mode` (Fast vs Librarian reply comparison) | **Keep** — the *mode* A/B is not covered by the Fast-model A/B switch. Endpoint verified present; the script's behaviour has not been re-run since the model change, so its first run is its acceptance check |
| `UPGRADE/{5 × .zip}` | unpacked into `eve-skills/<skill>/` (5 skills × 18 files present on disk) | **Removed** — redundant archives |
| `UPGRADE/discovery-router.py`, `UPGRADE/seed-catalog.py` | superseded by the grown, tested copies in `config/eve-capabilities/` (6.3 KB vs 4.7 KB, 9.1 KB vs 3.8 KB; covered by `tests/pipeline/test_discovery_catalog.py` and `test_capability_seed.py`) | **Removed** — two-copies drift risk |
| `tests/routing,ps`, `tests/routing.ps` | nothing (not collected by pytest; already queued as E-05) | **Removed** |
| `config/eve-capabilities/seed_catalog.py` | referenced by a test only; reads `UPGRADE/osint-catalog.json` → `catalog.db` | **Keep** — the capability catalog's seeder; documented §2.3 |

Test files appearing as orphans are normal: pytest wires them by discovery. The only tests that are
*not* wired are the two stray `routing` files (removed).

### 1.3 Generated state in git adds noise, not value

| Path | Status | Recommendation |
|------|--------|----------------|
| `config/ollama-active-model.json` | tracked, rewritten whenever a mode/model changes → shows up as a diff in every commit | Leave tracked (it is the cross-process source of truth) but expect churn; do not hand-edit |
| `config/eve-capabilities/catalog.db` (+ `-wal`, `-shm`) | tracked SQLite | Keep the `.db`; consider ignoring `-wal`/`-shm` |
| `backend/pocketbase/pb_public/dashboard/status.json` | generated, untracked | Add to `.gitignore` (it reappears in `git status` after every dashboard refresh) |
| `eve-audit/`, `tmp/`, `graft/` | gitignored | correct as-is |

---

## 2. What changed in this pass

### 2.1 Removed (all recoverable from git history)

- `UPGRADE/*.zip` (5 files) — superseded by the unpacked `eve-skills/<skill>/` trees.
- `UPGRADE/discovery-router.py`, `UPGRADE/seed-catalog.py` — superseded drafts; live copies are in
  `config/eve-capabilities/`.
- `tests/routing,ps`, `tests/routing.ps` — stray, uncollected probe files (queue **E-05**).

### 2.2 Added — machinery that keeps this evaluation honest

| Addition | Why it exists |
|----------|---------------|
| `scripts/audit-orphans.py` | Re-runnable reference-graph audit; the method behind §1. Run it after any cleanup so "is this junk?" is a command, not an opinion |
| `tests/frontend/test_config_parity.py` | **Kills the L4 drift class.** Parses `ollama-config.ts` and every `config/ollama/Modelfile.*` and asserts the Python `SHARED_NUM_CTX`, each mode's model, and every baked `num_ctx` agree. The 8192-vs-16384 drift is now a build failure, not a discovery |
| `tests/test_prompt_budget.py` | **Refactor plan R-01.** Turns the measured floor (~11.1k of 16,384: instructions ~5.8k + schemas ~5.3k) into an asserted invariant, including ≥4,096 tokens of conversation headroom and a ceiling on Toolbelt categories (30) |
| `UPGRADE/README.md` | Makes the remaining folder self-describing: it is a provenance bundle plus one live data source (`osint-catalog.json` → `catalog.db`), not a build area |

### 2.3 Documented so they connect (nothing removed)

The ops family around the two scheduled workers, and the manual tools that had no in-repo
reference, are now named in one place — this section — with the command each one runs:

| Command | Does |
|---------|------|
| `scripts\install-upgrade-workers.ps1` | registers `EMPIRE-AmbientMemoryWatchdog` + `EMPIRE-ResearchScavenger` |
| `scripts\start-memory-watchdog.ps1` / `start-research-scavenger.ps1` | runs the registered task now |
| `scripts\status-upgrade-workers.ps1` / `stop-upgrade-workers.ps1` / `remove-upgrade-workers.ps1` | inspect / stop / unregister |
| `scripts\capability-kill-switch.ps1` | fail-closed governance: stop arms, empty the snapshot so every `verify_capability()` check refuses |
| `scripts\build-project-catalog.ps1` | rebuild the projects catalog from workbench harvest |
| `scripts\ingest-workbench.ps1` (+ `ingest_workbench.py`) | validated Workbench → `eve_memory` Cognee ingest (checks venv, `V:\Cognee`, `nomic-embed-text`) |
| `scripts\stop-voice.ps1` | stop the Speaches voice container (`start-voice.ps1` starts it) |
| `scripts\test-wiki-librarian-vs-fast.py` | mode A/B: same questions through Fast vs Librarian via `/api/eve/session` |
| `scripts\run-graft-build.ps1` | rebuild the Cursor wiring graph (build-phase only; the one sanctioned `npx` at repo root) |
| `scripts\remote-build-lighten.ps1` | slow-remote-day relief: stops Superwhisper + `audiodg`, stops Weaviate, switches the Cursor MCP profile to Remote (`switch-cursor-mcp.ps1 -Profile Remote`), kills stray MCP python processes, then restart Cursor |
| `scripts\audit-orphans.py` | re-runnable reference audit behind the findings in section 1 |

Convention that emerged from this list: **a script that is a one-time installer or an ops control is
legitimate — but it must be named somewhere a human will look.** Otherwise it becomes E-05 class.

---

## 3. Resource map — what we have and how Eve should use it well

The instruction from the Architect: **do not remove skills; use the resources we already own well.**
This section is the honest inventory: what each resource is genuinely good at, how Eve reaches it
today, and where the value is still on the table.

### 3.1 The backbone insight

**MCP is the seam that makes Cursor and Eve the same system.** `mcp/` (24 files, 84 tools) is thin
FastMCP wrappers over `pipeline/`; Eve's agent tools (`agents/.../agent/tools/`, 86 files) call the
same python. One backend, two consumers: Cursor during the build phase, Eve at runtime. That is the
strongest architectural asset in EMPIRE and the reason the components fit — invest in the pipeline
(`pipeline/` = 20.8k lines of the real logic) and both surfaces benefit.

### 3.2 PocketBase (`:8090`)

- **What it is / real strength:** zero-ops SQLite + REST + admin UI + migrations. Perfect fit for
  local-first: no server to babysit, inspectable data, `/_/` admin for repair.
- **How Eve uses it:** `create_task`, `list_tasks`, `update_task`, `delete_task`, `search_tasks`
  (+ work-order / active-tool records), through `agent/lib/pocketbase.ts` and the Tasks tab.
- **Underused:** it is a genuine small operational database, not just a todo list. Work orders,
  capability/catalog records and chat-history state could live beside tasks with the same backup story.
- **Use it well:** keep it the *state* store (things that must survive a reboot and be editable by
  hand) and keep Cognee the *meaning* store. Do not make it a vector store.

### 3.3 Cognee (`V:\Cognee` on the VHDX)

- **What it is / real strength:** graph + vector memory with dataset separation and a single-process
  lock making MCP and CLI safe together — real recall, not prompt stuffing.
- **How Eve uses it:** `cognee_recall` / `cognee_remember` / `cognee_improve` / `cognee_forget`;
  datasets `eve_core` (fast curated recall), `eve_memory`, `eve_staging` (Architect-gated permanence),
  `eve_ambient` (bounded watchdog facts); `scripts/optimize-eve-memory.ps1` curates `eve_core`.
- **Underused:** memory is consulted but rarely *written* deliberately — `propose_remember` →
  `confirm_remember` is the strongest trust loop in the system and should be the reflex for anything
  the Architect says twice.
- **Use it well:** recall first for anything about the Architect's world; propose (never auto-promote)
  research; keep `eve_core` small so fast chat stays fast.

### 3.4 The GUI (Workbench `eve.html` + companions)

- **What it is / real strength:** zero-build HTMX/Alpine pages over the same local APIs — instant
  iteration, no bundler, inspectable in DevTools, and cache-busted (`?v=<mtime>`).
- **How Eve uses it:** chat + voice push-to-talk, Tasks, Memory (ingest/optimize), Models (mode + Fast
  A/B), History; companions `dashboard.html`, `wiki.html`, `daze.html`, `lego.html`,
  `primitives.html`, `architect-smoke.html`.
- **Underused:** the GUI is the only place the Architect sees *evidence* — tool traces, which model
  answered, which page grounded the answer. Today that lives in `eve-audit/*.jsonl`.
- **Use it well:** treat the Workbench as the *trust surface*: mode, model and grounding visible per
  turn is worth more than another tab.

### 3.5 Ollama (`:11434`)

- **What it is / real strength:** local inference with mode slots (fast / deep / librarian), an
  owned-model strategy (`empire-fast:14b`, limits baked in) and a documented promotion gate.
- **How Eve uses it:** through the agent; the frontend composes modes, the A/B switch swaps Fast only,
  and `resource_pulse` / `admit_for_goal` keep one heavy tenant in 16 GB VRAM.
- **Underused:** `deep` / `librarian` are rarely exercised in anger — the mode A/B script exists for
  exactly that and has not been re-run since the model change.
- **Use it well:** one promoted model per slot, gates before promotion
  (`scripts/ab-fast-toolcalling.py`), and let tool-surface discipline keep prompts small enough that a
  14B stays reliable.

### 3.6 Wiki (Title DNS + Weaviate + cache + Truth Drift)

- **What it is / real strength:** offline Wikipedia as a *resolvable* corpus — SQLite title index
  (0.03–0.62 s exact hits), `D:\wiki_md` sections, Weaviate on demand, markdown cache with provenance,
  Truth Drift year comparison, scratchpad + Error Book for multi-hop work.
- **How Eve uses it:** `wiki_scout_search` → `wiki_read_section` / `wiki_extract` / `wiki_resolve`;
  refusal and repeat-refusal rules keep loops bounded; `wiki_remember` promotes a lead deliberately.
- **Underused:** the link web (`pipeline.wiki_title_dns.neighbors`, CLI-only) — the hop affordance the
  multi-hop gap (E-10) needs.
- **Use it well:** it is the *evidence* arm. Ambiguity must be a first-class resolution outcome
  (E-13 / R-02), so a small model can be right instead of fast and wrong.

### 3.7 Voice — Speaches (`:8000`)

- **What it is / real strength:** local STT/TTS, no cloud, push-to-talk in the Workbench; spoken text
  is sanitized so scratch never reaches the speaker (measured: 0 leaks).
- **Underused:** `voice_speak` / `voice_transcribe` are usable as tools but voice is mostly a chat
  affordance; the voice *router* was retired for cost and could return as a cheap intent classifier.
- **Use it well:** keep speech hygiene as a contract, and prefer push-to-talk for anything the
  Architect should not have to type.

### 3.8 Capability arms & governance (`config/eve-capabilities/`)

- **What it is / real strength:** a real registry (`capability-registry.json` / `.yaml`), a catalog DB
  (`catalog.db` seeded from `UPGRADE/osint-catalog.json`), micro-skills under `eve-skills/` each with
  its own SKILL.md, a discovery router, two bounded ambient workers, and a fail-closed kill switch.
- **How Eve uses it:** `capability_status`, `request_capability`, `release_capabilities`,
  `admit_for_goal`, plus `skill_triage_manifest` / `search_catalog` for "what can you do?".
- **Underused — the single biggest lever for the tool-surface problem:** the registry already holds
  structured knowledge about every capability, while that knowledge currently sits *in the prompt*
  (5.3k of schemas plus skill text). Progressive disclosure was a direction; the registry makes it
  concrete — **advertise a small surface, let Eve look up the rest on demand.**
- **Use it well:** registry = the tool expert's memory; prompt = the shortlist.

---

## 4. Eve's four roles, mapped to the resources above

| Role | Uses | Today's gap to close |
|------|------|----------------------|
| **Orchestrator** | `resource_pulse`, `admit_for_goal`, GPU lease, Toolbelt groups, one heavy tenant | Goal-driven admission works but the *tool surface* is still hand-curated per session; intent groups (R-03) are what make orchestration cheap |
| **Builder** | `author_code`, `python_verify`, `create_spreadsheet`, work orders → Cursor, `eve-skills/` micro-skills, `tool_forge` | Forge work still leaves the local loop; the capability registry is the natural place to record what was built and how to invoke it |
| **Tool expert** | `search_catalog`, `skill_triage_manifest`, `capability_status`, MCP tool families | The expert knowledge is mostly in the prompt. Move it to the registry/catalog and look it up (R-03), then the answer to "what can you do?" is grounded and cheap |
| **Advisor** | Cognee recall + propose/confirm, wiki glasses, Truth Drift, DAZE, resource pulse | Advice is strong on memory and wiki, weakest on *showing its evidence*; surfacing grounding per turn in the Workbench closes that (§3.4) |

## 5. Next actions (unchanged plan, now with evidence)

1. **R-01 (ready):** ceiling test — **done in this pass** (`tests/test_prompt_budget.py`), including
   the ≥4,096-token conversation-headroom assertion.
2. **R-02 (ready):** resolution semantics — make `ambiguous` a legal outcome with candidates, then
   re-run the browser A/B and check whether a small model can answer the "magnets" case correctly.
3. **R-03:** tool triage — Core ≤ 15, intent groups (≤ 3 active), archive. Use
   `tests/test_prompt_budget.py::test_enabled_tool_count_is_bounded` as the tripwire.
4. **R-04:** docs consolidation — subsystem pages state guarantees + verifying commands; this document
   and `REFACTOR_PLAN.md` are the first two that already follow the rule.
5. **R-05:** wire the parity + budget tests and the model-promotion gates into
   `scripts/mechanic-green.ps1` so the floor cannot rise unnoticed.

## 6. Housekeeping conventions from this pass

1. **New script rule:** every script either (a) is called by another file, (b) is a documented ops
   command in this document or AGENTS.md, or (c) does not get committed. Run
   `scripts/audit-orphans.py` before adding more.
2. **Constants rule:** a value that exists in two languages must have a parity test
   (`tests/frontend/test_config_parity.py` is the template).
3. **Generated-state rule:** if a file is machine-written, it is gitignored or explicitly declared as
   tracked-with-churn (§1.3) — never silently mixed into a source commit.

---

## Related

- [`REFACTOR_PLAN.md`](REFACTOR_PLAN.md) — diagnosis, spine contract, phases R-01..R-05
- [`EMPIRE_CLARITY.md`](EMPIRE_CLARITY.md) — Core / LEGO / Session reach bounding box
- [`EMPIRE_IDEA_QUEUE.md`](EMPIRE_IDEA_QUEUE.md) — `R-*` and `E-*` rows
- `scripts/audit-orphans.py` — re-run the audit this document is based on
