# EMPIRE Idea Queue

Durable **ideas + verification backlog** for EMPIRE as the project grows.

This is **not**:

| Concept | Where it lives |
|---------|----------------|
| PocketBase **Task** | Workbench Tasks tab — day-to-day todos |
| **Work Order** | `C:\Empire_Workbench\05_Work_Orders\` — Cursor Forge Protocol |
| **This queue** | Ideas, smoke tests, and “do next when ready” — Architect + Mechanic shared list |

**Promote path:** Idea here → (optional) Resource Queue brief → Work Order when ready to forge → delete WO on success → mark queue item `done`.

**Deep store for deferred ideas:** [`docs/ideas/`](ideas/README.md) — one file per idea with intent,
**stack plan**, acceptance test, constraints and open questions, so a Work Order can be written from it
without re-deriving anything. This queue stays the ledger (status + link); the folder holds the
thinking. Index it with `.\venv\Scripts\python.exe scripts\list-ideas.py`; `tests/test_idea_docs.py`
keeps front matter, required sections and rows honest.

**Capability north star:** [EMPIRE Capability Atlas](../.cursor/plans/empire_capability_atlas_00e4868b.plan.md) (plan file may live under user `.cursor/plans/`). Real Cognee memory + Eve partnership first; limbs default OFF; one heavy GPU tenant at a time.

**Clarity (how the space is organized):** [`EMPIRE_CLARITY.md`](EMPIRE_CLARITY.md) — Eve Core vs LEGO products vs session reach; staging memory; Mechanic green before Architect smoke.

---

## How to use

1. Architect (or a pasted doc) adds rows under **Incoming from documents** or the right section.
2. Mechanic keeps **status** and **notes** honest after each session.
3. Testing items stay open until you personally smoke them (or explicitly waive).

### Status legend

| Status | Meaning |
|--------|---------|
| `idea` | Captured; not scheduled |
| `ready` | Clear enough to forge or test |
| `in_progress` | Actively being built or tested |
| `blocked` | Needs path, hardware, or Architect decision |
| `done` | Verified or intentionally closed |
| `parked` | Good idea; deferred on purpose |

---

## Capability Atlas waves

Ordered unlock of stack + RTX 5080 16GB + OSS. Smoke Wave 0 before relying on new limbs in daily chat.

| Wave | Theme | Status | Notes |
|------|-------|--------|-------|
| 0 | Prove LEGO **products** (Truth Drift / DAZE / Stem) as products — not 16 chat limbs | `in_progress` | See [`EMPIRE_CLARITY.md`](EMPIRE_CLARITY.md). Mechanic: `.\scripts\mechanic-green.ps1` before Architect UX. Stem CUDA OK offline 2026-09-06 |
| 1 | Partnership glue (summary, promote, Docling, Fast A/B, Ollama harden) | `done` | Forged 2026-09-06 |
| 2 | Reach (web scout, thought experiments, provenance) | `done` | Forged 2026-09-06 |
| 3 | Senses (voice + vision + GPU lease) | `done` | Forged 2026-09-06; speech server opt-in |
| 4 | Ubiquity + composition (remote, LEGO index, embed A/B) | `done` | Docs + scaffolds; nomic stays production |

### Hard rejects (Bridge / Copilot mismatches)

Do **not** forge: mega FastMCP gateway rewrite, Postgres-as-memory-authority, default `num_ctx` 32k, always-on Weaviate for working docs, near-term ComfyUI/Electron, auto-`cognee_remember` from caches, full Wikipedia → Cognee re-ingest, paid cloud LLM in app code.

---

## Refactor (R)

The structural plan lives in [`REFACTOR_PLAN.md`](REFACTOR_PLAN.md) — diagnosis (measured), the
answer-path spine contract, tool-surface triage, model-promotion gates, non-goals, phased order.
The **evaluation** that backs it (what is actually here, what was leftover junk, the resource map for
PocketBase / Cognee / GUI / MCP / wiki / Ollama / Speaches / capability arms, and the housekeeping
rules) lives in [`REFACTOR_EVAL.md`](REFACTOR_EVAL.md). Re-run `.\scripts\audit-orphans.py` before
adding more scripts. Rows here are the actionable phases; keep their status honest the same way the
`E-*` rows are kept.

| # | Phase | Status | Notes |
|---|-------|--------|-------|
| R-01 | **Phase 0 — Freeze and measure** | `done` | Shipped 2026-09-24: `tests/test_prompt_budget.py` asserts the measured floor (**~11.1k of 16,384** — always-on instructions ~5.8k + enabled schemas ~5.3k), requires **≥4,096 tokens of conversation headroom**, and caps Toolbelt categories at 30; `tests/frontend/test_config_parity.py` kills the Python↔TS↔Modelfile drift class; `scripts/audit-orphans.py` is the re-runnable junk audit. | Evidence and cleanup record: [`REFACTOR_EVAL.md`](REFACTOR_EVAL.md) |
| R-02 | **Phase 1 — Resolution semantics (load-bearing)** | `done` | Shipped 2026-09-24: **ambiguity is a first-class outcome.** `pipeline/wiki_title_dns.family_candidates` flags a bare subject that has no page of its own while its singular family does (`magnets` → `Magnet`/`Magnetism`; `batteries` → `Battery`), returns each reading as its own card with a lead, and the tool rule tells Eve to answer from the matching page *naming it* or to name the candidates and ask. Measures: ~20 ms (PK lookups + one range scan; `LIKE` was 701 ms on the 7.1M-row index), no false positives on `magnetism`/`white stripes`/`kate bush`/`series`/`news`. Question-shaped queries also resolve (kind-phrase strip: 1.8 s miss → 0.58 s hit). A/B on `How do magnets work?`: **14B now presents the three readings and asks** (PASS hygiene, speech 15 → 3 calls); **7B fails** — it emits the call as text then takes 300 s (see E-16). | Acceptance evidence in `eve-audit/r02-*.txt` + the trace summary; regression tests in `tests/pipeline/test_wiki_ambiguity.py` |
| R-03 | **Phase 2 — Tool surface triage / capability registry** | `done` | Shipped 2026-09-24 as **the registry move** (Architect's scope): tool *documentation* left the hot prompt. Schema keeps name + one-line cue + parameter **names**; semantics/gotchas live in `config/eve-capabilities/tool-docs/<tool>.md` (87 docs, harvested by `scripts/build-tool-docs.py` before the trim) and are fetched by the always-registered **`tool_docs`** tool. Measured floor **5,677 → 4,130 tokens (−27%)**: instructions 3,897 → 3,435, default-enabled schema prose 1,780 → 695. Live proof: in a fresh session *"what parameters does wiki_extract take?"* → `tool.requested ['tool_docs']` 62 ms; the wiki and file-search questions still route and answer correctly. | `scripts/measure-prompt-budget.py` (with `--baseline HEAD`) + `pipeline/prompt_budget.py` + `tests/test_prompt_budget.py` ceilings. Still open from the original scope: intent *group* gating (≤3 active) and the archive bucket |
| R-06 | **Intent groups + archive bucket (remaining half of R-03)** | `idea` | R-03 shipped the documentation move; the surface itself is still 87 tools with 25 flat Toolbelt categories and no archive. Remaining: group categories by intent (`research`/`author`/`ops`/`media`), ≤3 active, and a 90-day no-call archive so unused tools leave the registry. Ceiling already asserted: `tests/test_prompt_budget.py::test_enabled_tool_count_is_bounded` |
| R-04 | **Phase 3 — Docs consolidation** | `idea` | Subsystem page = guarantee + verifying command; archive narrative. Extend [`EMPIRE_CLARITY.md`](EMPIRE_CLARITY.md) with the per-subsystem sandbox-vs-product boundary. Exit: L4's three drifts cannot recur undetected |
| R-05 | **Phase 4 — Gates in CI** | `idea` | Wire the model-promotion gates (section 4 of the plan) + the prompt ceiling into `.\scripts\mechanic-green.ps1`. Exit: mechanic-green fails when the floor is exceeded or a promoted model misses a gate |

---

## Testing now (Architect smoke)

**Mechanic gate:** Do not hand items below to the Architect until `.\scripts\mechanic-green.ps1` exits 0 (use `-Full` when Eve live chat is in scope). Architect smoke is optional UX feel, not CI.

These were shipped or partially forged and need **your** hands-on verification when Mechanic is green.

| ID | Item | Status | How to test | Notes |
|----|------|--------|-------------|-------|
| T-01 | **Truth Drift / Wiki Local** | `ready` | `Start-EMPIRE.bat -Weaviate` (or `.\scripts\start-weaviate.ps1`). Enable Toolbelt **Wiki Local**. Ask Eve a cross-year topic (e.g. Cambrai 2017 vs 2026 or AI). Confirm **cards** prefer main articles over disambiguation; cache under `wiki_cache`; **no** auto-Cognee. | Wiki Interpreter (heuristics + optional BGE). Tear down: `.\scripts\stop-weaviate.ps1`. |
| T-02 | **DAZE / Time Reclaim** | `ready` | Open http://127.0.0.1:8080/daze.html. Add overlapping blocks → conflict glow. Enable Toolbelt **Time Reclaim**. Ask Eve what’s free today. | PocketBase `day_blocks`. WO open pending UX OK. |
| T-03 | **Shard of the Division / Stem Factory** | `ready` | Drop a song in `C:\Empire_Workbench\stem_factory\input`. Enable Toolbelt **Stem Factory**. Ask Eve to create stems. Check `stem_factory\output`. | Mechanic: `.venv-cuda` + CUDA device OK offline. Default `limit=1`. |
| T-04 | **Chat continuity** | `ready` | Start stack. Chat several turns, refresh page / reopen chat — Eve should see a short rolling summary prepended server-side. | Wave 1 |
| T-05 | **promote_wiki_cache** | `ready` | After T-01 cache hit, ask Eve to promote a specific `.md` (or MCP `promote_wiki_cache`). Confirm Cognee only on explicit call. | Wave 1 |
| T-06 | **Docling convert** | `ready` | Enable nothing special; ask Eve/`docling_convert` on a local PDF → Resource Queue `.md`. | Needs `pip install docling` in venv |
| T-07 | **Web scout** | `ready` | Enable **Web Scout** limb. Ask Eve to scout a public URL → `04_Thought_Experiments/web_cache/`. | Wave 2 |
| T-08 | **Voice presence** | `ready` | `.\scripts\start-voice.ps1` (or Speaches/Voicebox). Enable **Voice Presence**. Mic blob → transcript in composer. | Wave 3; speech API optional |
| T-09 | **Vision local** | `ready` | `ollama pull qwen3-vl:8b`. Enable **Vision Local**. Ask Eve about a screenshot path. | Wave 3; GPU lease |
| T-10 | **Container Scout** | `ready` | Enable Toolbelt **Container Scout**. Ask Eve to search Docker Hub (e.g. weaviate / vector db). Confirm cache under `04_Thought_Experiments/container_cache/`; **no** auto-Cognee. Optional: ask which `empire-*` containers are running. | See `docs/KUBERNETES_AND_CONTAINERS.md` |
| T-11 | **Smoke A — Operational foundation** | `done` | Follow **Smoke A** in [`EMPIRE_AUTONOMOUS_BUILD_GUIDE.md`](EMPIRE_AUTONOMOUS_BUILD_GUIDE.md). Architect **Smoke PASS Phase 1** 2026-09-09. | Admission audit + release manifest |
| T-12 | **Smoke B — Structured Extract** | `ready` | Follow **Smoke B** in the autonomous build guide (Toolbelt **Structured Extract**). Then `Smoke PASS Phase 2`. | llama.cpp worker; Ollama stays chat |
| T-13 | **Research Partner toggle** | `ready` | `Start-EMPIRE.bat`. Open http://127.0.0.1:8080/eve.html → **More** tab or chat admission bar → enable **Research Partner**. Confirm `GET /api/admission` shows `research_partner: true`. Toggle OFF → partner flag false. | F-29 forged; default OFF in repo template |
| T-14 | **research_orchestrate — GitHub + Product Hunt** | `ready` | With Partner ON, ask Eve: *What's new on Product Hunt today, and find GitHub MCP servers for local DuckDB?* Confirm she uses **`research_orchestrate`** (tool trace or compact multi-source answer). **No** auto-`cognee_remember`. | Same-turn admission bypasses Toolbelt `turn.started` |
| T-15 | **Session capability chips + TTL** | `ready` | During T-14, chat header shows session chips (`github_scout`, `web_scout`, etc.) with TTL countdown. After orchestrator finishes or **Release session** (More tab), chips clear. Optional: wait for TTL expiry. | Polls `/api/admission` every ~30s |
| T-16 | **Research cache artifacts** | `ready` | After T-14, confirm new files under `C:\Empire_Workbench\04_Thought_Experiments\github_cache\` and `web_cache\`. Optional: intake brief in `00_Resource_Queue` for forge-worthy GitHub hits — triage only, no auto-forge. | Provenance footer on cache `.md` |
| T-17 | **Partner OFF guardrail** | `ready` | Partner OFF. Ask the same research question. Eve should **not** silently hit GitHub/Product Hunt; friendly message to enable Research Partner (or manual Toolbelt). | Rings: never auto Cognee / stem / Gumloop |
| T-18 | **Wiki admission preflight (optional)** | `ready` | T7 plugged + Docker available. Partner ON. Ask a cross-year wiki topic (e.g. T-01 style). Confirm admission may run `start-weaviate.ps1` or reports a **clear** error if archive/path missing — no silent full wiki ingest. | Skip if Weaviate archive unavailable |
| T-19 | **GitHub Scout manual limb** | `ready` | Enable **GitHub Scout** on Toolbelt (without Partner). Ask Eve to search repos for `mcp duckdb`. Confirm `github_cache/` only; **no** clone/install/Cognee. Optional: `GITHUB_TOKEN` if rate-limited. | Cursor MCP: `empire-github-scout` |
| T-20 | **Admission CLI smoke** | `ready` | `.\venv\Scripts\python.exe -m pipeline.admission_controller status` → manifest + session + GPU snapshot. `set-research-partner true` → `request github_scout --reason smoke` → `release`. Check `%LOCALAPPDATA%\EMPIRE\` audit append. | Mechanic pre-pass OK; Architect confirms live stack |
| T-21 | **Wiki Phase A — conversational lookup** | `done` | Architect chat 2026-09-11: Stranger Things → Running Up That Hill; Kate Bush bio lead (Catherine Bush / 1958); explicit AI compare 2017 vs 2026 returned AI cards. Smoke: `.\scripts\Run-Wiki-Chat-Smoke.bat` | Mechanic + Architect PASS 2026-09-11; Ollama was yesterday’s lag culprit |
| T-22 | **Wiki calibrate JSONL harness** | `ready` | From repo root: `.\venv\Scripts\python.exe scripts\run-wiki-calibrate.py --tier smoke --injection --retrieval` (or set PYTHONPATH). | Mechanic: smoke 8/8 PASS 2026-09-10 |
| T-23 | **Playwright wiki Eve UI smoke** | `ready` | Stack up + Weaviate. `$env:PYTHONPATH='C:\EMPIRE'; .\venv\Scripts\python.exe scripts\test-wiki-eve-playwright.py` (add `--headful` to watch). | Mechanic PASS 2026-09-10 (~48s); may timeout if Eve busy |
| T-24 | **Embedding stack audit** | `ready` | `.\scripts\audit-embedding-stack.ps1` — confirm **nomic-embed-text** for Weaviate + Cognee; Weaviate reachable optional. | Gap analysis item 7 — audit only, no re-embed |
| T-25 | **Offline survival mirror** | `ready` | While online: `.\scripts\build-offline-mirror.ps1 -PullOllama -Wheelhouse`. Review `D:\empire\MANIFEST.md`. Pull `qwen2.5-coder:7b` if missing. | **Time-sensitive** — gap analysis #1 |
| T-26 | **Wiki glasses (EXTRACT)** | `done` | New chat + Wiki Local ON. Ask Switch specs / Python paradigm / miss `Zxqwy Blorf Band`. Expect EXTRACT table or refuse — no invent. | Shipped `8a03097`; forward plan [`docs/superpowers/plans/2026-09-15-wiki-glasses-forward.md`](superpowers/plans/2026-09-15-wiki-glasses-forward.md) |
| T-27 | **Resource pulse / Eve-managed hands** | `ready` | Stack up. Ask Eve: *What do you have available, and can you turn on GitHub Scout if needed?* Expect `resource_pulse` summary + `admit_for_goal` without Toolbelt clicks. Optional: ask her to release session when done. GPU/Vision should get an ask, not a silent enable. | F-42; no Cognee auto-remember |
| T-28 | **Autonomous wiki retrieval (regex middleware OFF)** | `ready` | New chat + **Wiki Local** ON. Ask *who is Kate Bush?* → expect a `wiki_scout_search` tool call in the trace, no `[[EMPIRE_WIKI_*]]` marker in the prompt, and a grounded answer. Then follow up with **“what else is on that page?”** / **“tell me about their discography”** → Eve must resolve the pronoun herself and re-call a wiki tool. Also try a miss (`Zxqwy Blorf Band`) → refuse, no invent. | Migration 2026-09-23: `EMPIRE_WIKI_MIDDLEWARE` defaults off; legacy injection is the escape hatch. Offline: `.\\venv\\Scripts\\python.exe scripts\\test-wiki-chat-smoke.py` |
| T-29 | **CoT + follow-up hop (reasoning protocol)** | `ready` | Stack up with **16k context** (`curl http://127.0.0.1:11434/api/ps` → `context_length: 16384`). Run `.\\venv\\Scripts\\python.exe scripts\\test-eve-cot-multihop.py --via-frontend` (offline, grades behaviour) and once without the flag (shows raw `<thought>` text). Then do the same two turns by hand in `eve.html`: *Who is Kate Bush?* → *What else is on that page?* — expect **`wiki_read_section`** and a discography answer, **not** the lead paragraph again, and no `<thought>` text visible in the bubble. | Verified PASS both routes 2026-09-23. Block emission is intermittent on the 14B (see E-11); the hop is the requirement |
| T-30 | **Browser voice/reasoning regression** | `ready` | Stack up, **hard-refresh** `eve.html`, hold the mic and ask *What can you tell me about the band the white stripes?* — expect no gibberish in the bubble, a `wiki_scout_search` tool call, and **complete spoken sentences** (no "Ask:/Have:/Next:", no mid-sentence start, no stop after a few words). Mechanic equivalent: `.\\venv\\Scripts\\python.exe scripts\\test-eve-browser-playwright.py` (add `--headful` to watch). | Fixes 2026-09-23: stateful reasoning-stream filter, partial-tag drop, speech-cursor reset, marker + non-Latin strip. Mechanic PASS 2026-09-23 |
| T-31 | **Turn latency + bubble loop** | `ready` | Hard-refresh, ask a wiki question, and watch the transcript: **one** assistant bubble per question and a warm turn in ~6–8 s (first turn after a model load ~16–19 s). Trace it: `$env:EMPIRE_TRACE='1'` on the Workbench + `.\\venv\\Scripts\\python.exe scripts\\trace-eve-browser.py --questions "q1\|q2"` (it prints `bubbles_added` per question). | **Fixed + measured 2026-09-23.** Wiki tool calls 10.7 s → **47–78 ms** (Title DNS missed "white stripes" → 9.5 s LIKE join over 7.1M rows → 12 s rg scan; article-prefix variants + two narrow scans + rg capped at 3 s). Generation capped via the EMPIRE-owned model **`empire-fast:14b`** (`.\\scripts\\build-empire-ollama-models.ps1`, `num_ctx 16384` / `num_predict 512`) because the compat endpoint ignores per-request options — an uncapped degenerate reply was ~90 s. Missing-section loop 15 calls → 2 (`available_sections` + rules). Voice router off by default. One bubble per turn. Server injects `?v=<mtime>` so a normal refresh picks up UI fixes. Follow-up hop PASS (E-10/E-11 remain for intermittency) |

---

## Eve tool-loop / context session (2026-09-23)

Follow-ups from the branch `cursor/eve-context-and-routing-fix` (commits `9a6d3fb`,
`c4544de`). Context: Ollama's OpenAI-compat endpoint ignored `options.num_ctx`, so the
model loaded at 4096 and truncated Eve's prompt — root cause of the empty-response /
hallucinated-refusal failures. Full write-up: [`PROGRESS_REPORT_2026-09-23.md`](PROGRESS_REPORT_2026-09-23.md).

**Fixed and green (do not re-open):** context truncation, `RESOURCE_BLOCK_RE` NameError
crash, catalog-context placement, bare `tell me` wiki false-positive, routing-prompt
loaded from the wrong directory, `defaults_version` `ValueError` risk, startup queue sweep.
Mechanic: 391 tests pass; `scripts/diagnostic.py` 3/3 with real tool calls.

### Ready to forge (Mechanic)

| ID | Item | Status | How to verify / do | Notes |
|----|------|--------|--------------------|-------|
| E-01 | **Verify Deep + Librarian modes load at 16384** | `ready` | Stack up, switch Workbench to **Deep**, then `Invoke-RestMethod http://127.0.0.1:11434/api/ps \| Select -Expand models \| Select name,context_length`. Expect `16384` (not 4096/8192/2048). Repeat for **Librarian** (`command-r:35b`). | **Fast verified 2026-09-23:** model loads at 16384 after `.\scripts\ensure-ollama-parallel.ps1 -NumParallel 1 -ContextLength 16384` (was 4096 → `prompt_eval_count=4098`, truncating Eve's ~11k-token prompt). Deep/Librarian still unverified. Watch 16 GB VRAM — 14B Q4 @16k ≈ 11.9 GB, 27B GSQ ≈ 12 GB |
| E-02 | **Decide fate of `injectOllamaChatOptions` num_ctx** | `done` | **Resolved 2026-09-23 (option a + bake):** the compat endpoint ignores per-request `options` (`num_predict=24` generated 458 tokens; `num_ctx=8192` left the model at 4096), so the limits are baked into an EMPIRE-owned model: `.\\scripts\\build-empire-ollama-models.ps1` creates **`empire-fast:14b`** (`num_ctx 16384`, `num_predict 512`, temp 0.2, top_p 0.9) and Fast uses it (`ollama-config.ts`, `ollama_chat_profiles.py`). Option (c) native `/api/chat` stays open if a per-request override is ever needed. | Also fixed here: `resolve_installed_model` iterated an unordered set, so Fast could resolve to `qwen2.5:32b` (a Deep alias) on some boots — now deterministic (same-tag first) |
| E-03 | **Routing regression battery** | `ready` | Extend `scripts/diagnostic.py` with ~10 prompts spanning catalog / wiki / tasks / memory / files / headroom; assert the expected tool name appears in the `actions.requested` trace. | Now that truncation is gone, tool choice is testable. Earlier runs sometimes picked a plausible-but-wrong tool (e.g. `resource_pulse` beside `check_workbench_health`) |
| E-04 | **Queue retention policy for `.eve/.workflow-data`** | `ready` | Define a retention window for `runs/`, `events/`, `streams/` (was 800 runs + 12k events + 51k streams). Implement prune or document why unbounded is acceptable. | Startup sweep stops re-enqueue; it does not stop growth |
| E-05 | **Delete stray `tests/routing,ps`** | `ready` | `Remove-Item "tests\routing,ps","tests\routing.ps"` (confirm first). The comma looks like a bad redirect typo; neither is collected by `unittest discover`. | Ad-hoc probe scripts, not suite tests |
| E-06 | **Consider continuous stale-run protection** | `idea` | Startup sweep only runs when `start-stack.ps1` actually launches Eve. For runs orphaned *while Eve is up*, add a scheduled task or a `session.completed` hook in the agent. | Not a bug — a deliberate coverage gap. Only if it bites |
| E-09 | **Retire the wiki regex escape hatch** | `idea` | After T-28 passes Architect smoke, delete the legacy path: drop `EMPIRE_WIKI_MIDDLEWARE` + the inject branches from `frontend/wiki_drift_api.py`, the `_wiki_evidence` plumbing in `serve.py`, `pipeline/wiki_lookup_lock.py`, the `isWikiLookupLocked` gates in `agent/tools/wiki_*.ts`, and the `chat_continuity` wiki-marker suppression. Keep `[[EMPIRE_WIKI_ERROR_BOOK]]` / scratchpad. | One release cycle of soak first; `docs/WIKI_SCOUT.md` § Retrieval ownership is the map |
| E-11 | **Harden `<thought>` block compliance (14B)** | `idea` | The protocol is in the prompt and quantifiably active (she quotes rule 1 verbatim; blocks appear in the raw stream), but emission is **intermittent** across turns — measured over ~6 runs, some turns carried no block while the *hop* still happened. Options: (a) accept it (behaviour is the deliverable, the block is scratch and is stripped anyway); (b) enforce at the channel/`defineInstructions` level with a required prefix; (c) switch Fast to a model with native reasoning (qwen3) so the block is first-class. | Do not add regex middleware for this — the block is a means, not the outcome. Evidence: `scripts/test-eve-cot-multihop.py` direct mode |
| E-10 | **One-turn multi-hop “trace” questions** | `ready` | Live smoke evidence (2026-09-23, fast 14B): *“what 80s song became a hit again in the series Stranger Things?”* → Eve calls `wiki_scout_search`, gets the series **lead**, and answers the lead instead of hopping to the song page. Same question phrased as two explicit steps (`first look up the series, then read the song page`) returns **Running Up That Hill** — so the loop, tools, and contracts all allow it; the model just stops. Options: (a) accept the follow-up turn in conversation; (b) restore a hop hint — the Title DNS link web (`pipeline.wiki_title_dns.neighbors`, already CLI-only) could be exposed as an MCP tool so the model can see linked entities (Stranger Things → Kate Bush → song); (c) test Deep / a bigger model. | `scripts/test-wiki-chat-smoke.py` reports these as `WARN known-gap` (not a wiring failure); tools verified to reach the answer, so this is model behaviour + missing hop affordance, not a regression of the middleware removal |

| E-12 | **Fast A/B: 7B vs 14B (decided — keep 14B)** | `done` | Ran the repo's own A/B switch (`%LOCALAPPDATA%\EMPIRE\ollama-fast-ab.json`) with `empire-fast:7b` (new: `config/ollama/Modelfile.empire-fast-7b`, built by `scripts/build-empire-ollama-models.ps1`) against `empire-fast:14b` on identical code/prompts. **Both pass the hard gates** (`scripts/ab-fast-toolcalling.py`: OpenAI tool_calls via the compat proxy, and a **10,022-token** prompt ingested uncut at `num_ctx 16384`). Browser A/B, same 3 questions: 14B **76.9 s** total (22.7/25.9/28.3) vs 7B **25.2 s** (13.8/4.9/6.5) — but the 7B answered *"How do magnets work?"* from **"The Magnets"** (an a cappella group) in 4.9 s with a single search, while the 14B's extra searches corrected course to **magnetism** and followed up on that page. Functionality wins: variant reset to **a**. | Speed is not the gate — grounding is. Keep 7B for cheap non-grounded work (or a smaller Fast slot) only; see E-13 for the real cause |
| E-13 | **Title DNS polysemy: "magnets" → "The Magnets"** | `done` | **Closed by R-02 (2026-09-24).** `family_candidates` now flags exactly this shape (`magnets` has no page of its own; `Magnet`/`Magnetism` do) and returns every reading as a card, so a model can no longer ground a physics question on the band. Verified on the live 7.1M-row index with no false positives (`magnetism`, `white stripes`, `kate bush`, `series`, `news` stay plain hits) in ~20 ms. | Was Phase 1 of [`REFACTOR_PLAN.md`](REFACTOR_PLAN.md); details in [`WIKI_SCOUT.md`](WIKI_SCOUT.md) and the R-02 row |
| E-14 | **Repeat-search hard stop + tool-call-as-text strip + num_ctx alignment** | `done` | Three baseline defects the A/B exposed: (1) the 14B repeated one identical `wiki_scout_search` **7×** (66 s, turn ended in an apology) because the soft hint was ignored → `pipeline/wiki_scout.py` escalates to **strike 3 = refusal** (no cards, `HARD_STOP_REPEAT_HINT`) inside a 180 s window, so a later legitimate question still works; measured 7 → 2 searches, 66 s → 14–26 s. (2) The model wrote a tool call as **prose** ("Called wiki_read_section with object(title=…)") → stripped for bubble *and* speech in `frontend/eve_proxy.py` + `frontend/eve-workbench.js`; both A/B runs measured **0 leaks**. (3) `frontend/ollama_chat_profiles.SHARED_NUM_CTX` was 8192 while `ollama-config.ts` and the baked models said 16384 → aligned (tests updated). Also fixed: question-form extraction (`How does magnetism work?` → `magnetism`; `How do magnets work?` → `magnets`) in `pipeline/wiki_interpreter.py`, which is why the physics question now lands on the wiki. | AGENTS.md requires the two `SHARED_NUM_CTX` values to match. `EMPTY_AFTER_CLEAN_REPLY` replaces an empty bubble when a turn yields only scaffolding |
| E-16 | **Small-model fluency on a multi-card payload (7B)** | `parked` | **Closed by decision 2026-09-24: Fast is locked to `empire-fast:14b`; E-16 is not pursued.** Measured on `empire-fast:7b` with `How do magnets work?`: the tool call is correct (`wiki_scout_search` 46.8 ms → `wiki_read_section` 232.0 ms) but the text step emitted the call it never made (`wiki_read_section("magnetism", section="magnetic_fields_and_theory")`) and two retries ran **301.6 s / 304.7 s**. 7B is not suitable for multi-card tool reasoning in this pipeline; the harness now converts the leak into an honest failure rather than speech. | Evidence: `eve-audit/r02-b-7b-graded.txt`, `eve-audit/r02-trace-summary.txt` |
| E-18 | **Trace has no turn↔session correlation id** | `ready` | `turn.start` records carry model/mode/message but **no session id**, while `tool.requested` / `tool.result` / `stream.end` carry `session` but not the turn. With two browser sessions in flight (tracer + harness, or voice router beside chat) tool events cannot be attributed to a turn — hit while presenting the R-03 trace evidence. Fix: thread a per-request turn id through `serve.py`'s turn.start and the streamed tool events it parses. | Until then, per-turn tool attribution needs single-session runs |
| E-17 | **Leak shapes the sanitizer learned in R-02** | `done` | Three shapes measured live and now stripped in `frontend/eve_proxy.py` + `frontend/eve-workbench.js` (bubble *and* speech, with tests): bare protocol scratch lines (`Ask:howdomagnetswork.` — reached the speaker), bare call expressions (`wiki_read_section("magnetism", section="…")`), and the namespace-restricted form of both so ordinary code the user discusses (`print("hello")`, `df.head()`) is untouched. Turn text is also dropped from the speech queue when a tool step starts, so mid-turn narration ("let's look into the basics of magnetism") is no longer read aloud — speech calls on the magnets turn fell 15 → 3. | Same evidence; tests in `tests/frontend/test_eve_proxy.py` |
| E-19 | **Media limb — local video search, links, transcripts, player (yt-dlp, no vendor API)** | `idea` | **Full plan:** [`ideas/media-limb-yt-dlp.md`](ideas/media-limb-yt-dlp.md). Architect decision 2026-09-24: **yt-dlp, no corporate dependency, no keys, no quota.** Stack: `pipeline/media_scout.py` (+ MCP server) → Toolbelt limb `media_scout`, off by default; kept links in PocketBase `media_links`; Cognee only on confirm; later a `media.html` LEGO page with an embed `<iframe>` player. Acceptance: ask for a video → 2–5 candidates **with links**; keep one → stored + confirmed; later "what was the magnetism video?" → recalled in words. Open: captions-only vs Whisper, page vs dock panel | Deep store convention: [`ideas/README.md`](ideas/README.md) · index: `scripts/list-ideas.py` |
| E-20 | **Eve can list, read, and capture ideas (PocketBase index + proposal path)** | `idea` | **Full plan:** [`ideas/eve-idea-tools.md`](ideas/eve-idea-tools.md). Architect 2026-09-24: ideas must not be lost, and intake (not storage) is the bottleneck — so *say it to Eve* should be enough. Files stay canonical; PocketBase becomes the query index (one-way sync); Cognee only on confirm; Eve may capture at `status: idea` and never promote. Boundaries enforced by `tests/test_idea_docs.py` | Depends on E-19 only for the panel pattern; can be built independently |
| E-15 | **A/B resolver could stay on the alternate after switching back** | `done` | `resolve_fast_model` / `resolveFastAbModel` returned the stored Fast model unchanged, so after a variant-b run the *stored* model was the alternate and switching to `a` silently kept it. Both now return the A baseline when the stored model equals `b_model`. Covered by `tests/frontend/test_ollama_fast_ab.py`. | Found while running the A/B — without it the "variant a" numbers could have been the 7B's |

### Architect smoke (optional feel, not CI)

| ID | Item | Status | How to test | Notes |
|----|------|--------|-------------|-------|
| E-07 | **Confirm push-to-talk survived** | `ready` | Stack up → `http://127.0.0.1:8080/eve.html` → mic button. Also `GET /api/toolbelt` should list `voice_presence`. | `voice_presence` was accidentally stripped during debugging and restored; worth one personal check |
| E-08 | **Wiki Local (Weaviate) is opt-in** | `ready` | Confirm intended: `weaviate:8091` starts only with `-Weaviate`. Normal lookups (Title DNS + lead) still work without it because Eve calls `wiki_scout_search` / `wiki_extract` herself; only Truth Drift (`wiki_scout_compare_years`) needs Weaviate. | Decide whether Operational Phase wants it default-on |

---

## Incoming from documents

Paste or summarize the next document here. Mechanic will triage into Testing / Forge / Parked.

| Date | Source doc | Extracted ideas | Triage |
|------|------------|-----------------|--------|
| 2026-09-06 | Bridge `EVE_OLLAMA_EXPANSION_MANIFEST.md` | Voice, Docling, model A/B, promote cache, provenance, web scout | Folded into Atlas waves; rejects noted above |
| 2026-09-06 | EMPIRE Capability Atlas (Mechanic) | GPU lease, vision limb, thought experiments, LEGO index, embed A/B | Waves 0–4 rows |
| 2026-09-10 | `empire_missed_oss_investigation.md` | kiwix-mcp 3-rung ladder (server-side), FlashRank CPU rerank, promptfoo/JSONL eval, skip Kiwix migration | → F-30–F-33; ladder in `pipeline/wiki_kiwix_ladder.py` |
| 2026-09-10 | `empire_huggingface_specialty_resources.md` | AmbigQA/RedirectQA/FaithDial samples, EMPIRE DriftBench from snapshots, MiniCheck CPU eval later | → `data/eval/wiki_calibrate.jsonl`, `pipeline/wiki_driftbench_seed.py`; HF import parked |
| 2026-09-10 | RAG Stack technical directive (NotebookLM) | Phase A `wiki_read_lead`, slim EVIDENCE, 4 calibration Qs | → T-21; shipped + mechanic smoke PASS |
| 2026-09-10 | `empire_local_capability_gap_analysis.md` | Offline mirror, GLiNER, CPU specialist fleet, PH wind-down, build sequence | → **docs/RESEARCH_CLOSURE.md**; F-35–F-38; T-24–T-25 |

**Intake rule:** When you share a document, add one row above (or ask Cursor to), then split bullets into the sections below with new `I-xx` / `T-xx` / `F-xx` IDs.

---

## Forge / build backlog

Engineering work not yet (or only partially) shipped.

| ID | Item | Status | Manifesto / docs | Notes |
|----|------|--------|------------------|-------|
| F-01 | Web scout (same md contract as wiki_cache) | `done` | Phase 3; `docs/WEB_SCOUT.md` | Local HTTP; Playwright optional later |
| F-02 | `promote_wiki_cache` → Cognee helper | `done` | WIKI_SCOUT | Explicit promote only |
| F-03 | Chat “continue past chat” (short summary into context) | `done` | EMPIRE_GUIDE near-term | `num_ctx` 8192; rolling summary field |
| F-04 | Always-on Weaviate cold-start profile (optional) | `parked` | WIKI_SCOUT | Only if Architect wants wiki up every boot |
| F-05 | Dedicated Cognee `truth_drift` dataset | `done` | WIKI_SCOUT; `config/wiki-promote.json` | Auto-route compare → truth_drift; override allowed |
| F-06 | Stem Factory WO close after live song smoke | `ready` | WO-stem-factory | Depends on T-03 |
| F-07 | DAZE WO close after Architect UX review | `ready` | [`docs/DAZE.md`](DAZE.md) | Forge complete 2026-09-08 — Architect smoke **T-02** |
| F-08 | Model A/B Fast mode only | `done` | Atlas Wave 1 | `%LOCALAPPDATA%\EMPIRE\ollama-fast-ab.json`; Deep/Librarian pinned |
| F-09 | Secure remote access (Tailscale / Cloudflare Tunnel) | `ready` | Phase 6; `docs/REMOTE_ACCESS.md` | Bind localhost until then |
| F-10 | Local voice (STT/TTS) path for composer | `done` | Phase 7; `docs/VOICE_PRESENCE.md` | Toolbelt OFF; OpenAI-compatible speech API |
| F-11 | Docling MCP → Resource Queue markdown | `done` | Atlas Wave 1 | `empire-docling` |
| F-12 | Ollama inventory + loopback harden | `done` | Atlas Wave 1 | Client URL normalize; Fast A/B API |
| F-13 | Thought-experiment limb | `done` | Phase 3 | Notes under `04_Thought_Experiments/` |
| F-14 | Provenance footer on scout caches | `done` | Atlas Wave 2 | `pipeline/provenance.py` |
| F-15 | Vision Local (`qwen3-vl:8b`) | `done` | Atlas Wave 3 | Toolbelt OFF; GPU lease |
| F-16 | GPU lease dashboard surface | `done` | Atlas | `/api/gpu-lease` |
| F-17 | LEGO whiteboard tool index | `done` | Phase 4 | `03_Active_Tools/LEGO_INDEX.md` |
| F-18 | Embedding A/B (`qwen3-embedding:0.6b` test dataset only) | `done` | Atlas Wave 4 | `pipeline/embedding_ab.py`; `scripts/embedding-ab.ps1`; nomic stays production |
| F-19 | Container Scout (Docker Hub + local empire-* status) | `done` | `docs/KUBERNETES_AND_CONTAINERS.md` | Toolbelt OFF; no auto-Cognee; no auto-pull |
| F-20 | Run EMPIRE core on local Kubernetes | `parked` | KUBERNETES_AND_CONTAINERS | Single-host + Ollama VRAM; Compose/scripts win |
| F-21 | Autonomous build guide + Phase 1 foundation | `done` | `EMPIRE_AUTONOMOUS_BUILD_GUIDE.md` | Manifest, admission audit, lineage, fixtures |
| F-22 | Structured Extract (llama.cpp worker) | `done` | `docs/workers/STRUCTURED_EXTRACT.md` | Toolbelt OFF; Mechanic prelim pass; Architect Smoke B |
| F-23 | Retrieval rerank A/B (lexical + optional CE) | `done` | `docs/EMBEDDING_AB.md` | Eval only; nomic stays production |
| F-24 | Playwright allowlisted Browser Local | `done` | Autonomous guide Phase 4 | Toolbelt `browser_local` |
| F-25 | Voice VAD gate + Kokoro path | `done` | `pipeline/voice_vad.py` | Energy/Silero; STT skip if silence |
| F-26 | Vision UI observe (no actuators) | `done` | `pipeline/vision_ui_observe.py` | Under Vision Local toolbelt |
| F-27 | Mechanic SBOM script | `done` | `scripts/empire-sbom.ps1` | Not Eve-exposed |
| F-28 | PaddleOCR specialist | `parked` | Autonomous guide Phase 7 | Only if Docling loses Architect samples |
| F-29 | Research Autopilot (admission + github scout + orchestrator) | `done` | [`docs/RESEARCH_AUTOPILOT.md`](RESEARCH_AUTOPILOT.md) | Forge complete; Architect smoke **T-13–T-20** before daily reliance |
| F-30 | Wiki calibrate JSONL + DriftBench seed + runner | `done` | `data/eval/wiki_calibrate.jsonl`, `pipeline/wiki_driftbench_seed.py`, `scripts/run-wiki-calibrate.py` | 21 seed cases; expand to ~325 with HF samples |
| F-31 | Kiwix-MCP ladder (server-side) | `done` | `pipeline/wiki_kiwix_ladder.py` | `search_with_snippets` → `get_content_summary` → `get_content`; not exposed as MCP |
| F-32 | FlashRank CPU rerank on title+lead | `ready` | missed OSS + HF specialty docs | Phase B — only if calibrate shows title mixups |
| F-33 | HF calibrate sample import (AmbigQA, RedirectQA, …) | `ready` | `empire_huggingface_specialty_resources.md` | `scripts/import-wiki-calibrate-samples.py` not forged yet; 200 placeholder slots optional via `--include-placeholders` |
| F-34 | MiniCheck / FaithCritic CPU offline verifier | `parked` | HF specialty doc | Eval-only after allowlist/GLiNER metrics plateau |
| F-35 | Offline survival mirror + MANIFEST | `done` | `docs/RESEARCH_CLOSURE.md`, `scripts/build-offline-mirror.ps1`, `config/offline-mirror.json` | Architect runs **T-25** while online |
| F-36 | GLiNER CPU entity grounding gate | `done` | `pipeline/wiki_entity_guard.py` | Opt-in: `pip install gliner` + `EMPIRE_GLINER_GROUNDING=1` |
| F-37 | Piper TTS path (vs Speaches) | `parked` | Gap analysis §2 | Speaches already forged (F-10/T-08); compare only if voice quality insufficient |
| F-38 | Ollama JSON-schema article selection | `ready` | Gap analysis §4; structured outputs | Wire `format` for title pick before prose — no second generator |
| F-39 | Wiki glasses forward (filter → tables → sparse remember) | `done` | [`docs/superpowers/plans/2026-09-15-wiki-glasses-forward.md`](superpowers/plans/2026-09-15-wiki-glasses-forward.md) | Battery + filter + multicol + remember pilot 2026-09-15; DuckDB/ZIM stay parked |
| F-40 | Empire Clarity reorg (toolbelt buckets, staging memory, product doors, mechanic-green) | `done` | [`docs/EMPIRE_CLARITY.md`](EMPIRE_CLARITY.md) | Eve Core vs LEGO; `eve_staging` propose/confirm/drop |
| F-41 | Core ready strip (Voice + Wiki header pills) | `done` | [`docs/superpowers/specs/2026-09-16-eve-core-ready-strip-design.md`](superpowers/specs/2026-09-16-eve-core-ready-strip-design.md) | Glasses health + click toggles; out of Tools dock list |
| F-42 | Resource pulse + admit_for_goal (Eve-managed hands) | `done` | [`docs/superpowers/specs/2026-09-16-eve-resource-pulse-design.md`](superpowers/specs/2026-09-16-eve-resource-pulse-design.md) | Policy B; MCP atlas; Architect smoke **T-26** |

---

## Ideas (unsorted growth)

Capture sparks here; promote to Testing or Forge when clear.

| ID | Idea | Status | Source |
|----|------|--------|--------|
| I-01 | LEGO Whiteboard composable UI (beyond markdown index) | `done` | Manifesto Phase 4; http://127.0.0.1:8080/lego.html · recipes + validate + merge apply |
| I-02 | Gumloop limb only after local research fails | `parked` | Manifesto Phase 3 |
| I-03 | Thought-experiment YouTube → research limb | `done` | Manifesto Phase 3 / Atlas |
| I-04 | Rebuild Shard `.venv-cuda` documented in ops cheat sheet | `done` | 2026-09-06 CUDA fix |
| I-05 | **Research discovery closed** | `done` | Gap analysis § Product Hunt wind-down | Authority: **docs/RESEARCH_CLOSURE.md** — DriftBench drives next search |
| I-06 | Personal doc corpus (Docling → Weaviate) | `ready` | Gap analysis §5 | Week 3 build; same `wiki_read_lead` contract on your PDFs |

---

## Session checklist (quick)

When waking EMPIRE to work this queue:

1. `Start-EMPIRE.bat` (or stack script) for Eve / Workbench / PocketBase / Ollama  
2. Weaviate only if doing **T-01** or **T-18**: `Start-EMPIRE.bat -Weaviate` (or `.\scripts\start-weaviate.ps1`)  
3. Voice speech API only if doing **T-08**  
4. **Research Autopilot (T-13–T-17):** enable **Research Partner** in Workbench — no permanent Toolbelt toggles required  
5. Other limbs: enable matching Toolbelt category(s)  
6. Update this file’s status after you test  

---

## Related paths

| Path | Role |
|------|------|
| [EMPIRE_GUIDE.md](../EMPIRE_GUIDE.md) | Collaborator brief |
| [docs/EMPIRE_RESEARCH_SNAPSHOT.md](EMPIRE_RESEARCH_SNAPSHOT.md) | As-built snapshot for research AIs |
| [docs/EMPIRE_AUTONOMOUS_BUILD_GUIDE.md](EMPIRE_AUTONOMOUS_BUILD_GUIDE.md) | Mechanic forge-while-away track |
| [docs/ARCHITECT_TEST_CHECKLIST.md](ARCHITECT_TEST_CHECKLIST.md) | Architect personal smoke list |
| [EMPIRE_MANIFESTO.md](../EMPIRE_MANIFESTO.md) | Phase north star |
| [docs/WIKI_SCOUT.md](WIKI_SCOUT.md) | Wiki Local / Truth Drift |
| [docs/WEB_SCOUT.md](WEB_SCOUT.md) | Web scout cache |
| [docs/VOICE_PRESENCE.md](VOICE_PRESENCE.md) | STT/TTS limb |
| [docs/REMOTE_ACCESS.md](REMOTE_ACCESS.md) | Phase 6 tunnel notes |
| [docs/EMPIRE_USAGE_GUIDE.md](EMPIRE_USAGE_GUIDE.md) | Architect how-to: pages, Toolbelt, recipes |
| [docs/LEGO_WHITEBOARD.md](LEGO_WHITEBOARD.md) | Manifesto Phase 4 LEGO canvas |
| [docs/KUBERNETES_AND_CONTAINERS.md](KUBERNETES_AND_CONTAINERS.md) | K8s vs Compose; Container Scout |
| [docs/CONTAINER_SCOUT.md](CONTAINER_SCOUT.md) | Container Scout limb ops |
| [docs/RESEARCH_AUTOPILOT.md](RESEARCH_AUTOPILOT.md) | Research Partner + admission + orchestrator |
| [docs/DAZE.md](DAZE.md) | DAZE radial day / Time Reclaim |
| [docs/WEAVIATE_HEIST.md](WEAVIATE_HEIST.md) | Weaviate boot / tear-down |
| [docs/RESEARCH_CLOSURE.md](RESEARCH_CLOSURE.md) | **Research phase capstone — read before new tool hunts** |
| `C:\Empire_Workbench\05_Work_Orders\` | Active Forge Work Orders |
| `C:\Empire_Workbench\stem_factory\input` | Stem inbox |
| http://127.0.0.1:8080/daze.html | DAZE radial day |

*Created 2026-09-06. Updated for Capability Atlas. Append freely; do not confuse with PocketBase Tasks.*
