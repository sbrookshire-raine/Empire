# Research Bench

**One breath:** the eval that decides whether Eve can work *outside her own archive*. It names, from
the repo, which of the Architect's asks no tool can serve — and it scores real turns, so "she got
better at research" is a number rather than a feeling.

**Why it exists.** [`RESEARCH_CLOSURE.md`](RESEARCH_CLOSURE.md) closed discovery: *"future
architecture changes require a measured DriftBench regression, not a new README."* The Architect then
named one capability he wants and does not have — *"let her search the internet if I need her to"* —
which is a **proven hole**, so it gets a bench before it gets a tool.

```
.\venv\Scripts\python.exe scripts\run-research-bench.py --baseline      # no model needed
$env:EMPIRE_TRACE='1'
.\venv\Scripts\python.exe scripts\run-research-bench.py --live --out eve-audit\research-bench-live.json
```

## Baseline, measured 2026-09-24 (`eve-audit/research-bench-baseline.json`)

| Case | Need | Verdict | Why |
|---|---|---|---|
| `rb_01` | search | **blocked** | "no callable tool for a 'search' ask (tried: web_search, web_fetch, searxng_search, web_search_local)" |
| `rb_02` | search | **blocked** | same |
| `rb_03` | github | ready | `github_scout_search` / `github_scout_readme` (after admission) |
| `rb_04` | fetch | ready | `web_scout` / `browser_local_fetch` — **given** a URL |
| `rb_05`, `rb_06` | archive | ready | `wiki_*` (resident once `wiki_local` is on) |
| `rb_07` | artefact | ready | `create_spreadsheet` / `author_code` (after admission) |
| `rb_08` | none | ready | open-ended ask, answered in prose by design |

**6 ready · 2 blocked — both blocked cases are public web *search*.** `research_orchestrate` does not
close the gap: it orchestrates archive + GitHub + the Product Hunt feed + **one URL you name**, not a
query-based web search. `web_search` / `web_fetch` are `export default disableTool()` (the
provider-managed path hung local Ollama) — so the absence is structural, not an oversight.

**Update 2026-09-25 — the hole is closed (E-35).** A self-hosted SearXNG instance with its JSON API
enabled (`scripts/start-searxng.ps1`, `config/searxng/settings.yml`) plus the gated `searxng_search`
tool took the bench to **8/8 ready, `blocked_needs: none`, `--require-ready` exit 0**. A live desk job
given only a query searched, took the top 3 results, fetched them and wrote a digest — no URL supplied.
`rb_01` / `rb_02` now resolve through `searxng_search`; the tool states its own failure modes (instance
down → names `start-searxng.ps1`; JSON disabled → names the settings key) rather than fabricating.

## Live mode — measured 2026-09-25, and a false alarm worth keeping

The baseline mode measures *capability existence*. Live mode asks the harder question — do real turns
through the Workbench actually use the limb? **It is only meaningful when the Workbench runs with
`EMPIRE_TRACE=1`**, because `serve.py` writes `eve-audit/eve-trace.jsonl` only then, and that file is the
only honest source of "which tool ran".

**The first run read 1/8 with `tools=none` on every case — and it was wrong.** The frontend had been
started by `start-stack.ps1` *without* tracing, so no `tool.requested` records were written. The bench's
only guard was "does the trace file exist?", and a **stale** file from earlier sessions did exist
(24,340 records, 136 of them `tool.requested`) — so blindness went **silent** and every case was graded
as a missing tool call. That was recorded as E-43, *"live turns make no tool calls"*, which was **not
true**: it was the instrument, not Eve.

Same stack, same cases, tracing on:

```
  rb_01  pass  tools=['searxng_search']
  rb_02  FAIL  tools=['searxng_search']  ['no source URL in the answer']
  rb_03  FAIL  tools=['research_orchestrate', 'admit_for_goal', 'request_capability', ...]
  rb_04  FAIL  tools=none                ['no expected tool ran', 'empty reply']
  rb_05  pass  tools=['wiki_scout_search', 'wiki_read_section']
  rb_06  pass  tools=['wiki_scout_compare_years']
  rb_07  FAIL  tools=['wiki_scout_compare_years', 'wiki_read_section', ...]
  rb_08  pass  tools=none
  passed=4/8
```

So **tool calling works**, including the capability this bench was built to gate: `rb_01` called
`searxng_search` and passed. The live score is behavioural, not structural:

1. `rb_02` / `rb_07` — the right *class* of tool ran (search; wiki reads) but the answer carried neither
   the source URL nor the artefact the case asks for: follow-through, not capability.
2. `rb_03` — she reached for `research_orchestrate` + `admit_for_goal` + `request_capability` instead of
   the github tool. Defensible route; the case's expectation is narrower than what she did.
3. `rb_04` — **`empty reply` with no tool call**: the E-30 class, now caught in a repeatable harness.
4. `rb_08` — pass with no tools, exactly as designed.

**The instrument is now honest by construction.** `run-research-bench.py` treats "no trace records for
this turn" as **unverifiable**: it prints `???? no trace records (WORKBENCH NOT TRACING — not a verdict)`,
counts `unverified`, and exits non-zero. A blind run can no longer masquerade as a capability failure,
and a stale trace file no longer hides it (the check is per-turn records, not file existence).

2. **`web_research` was Architect-only — fixed 2026-09-25 by the Architect's call.** The manifest had
   `web_research: {auto_enable: false, session_ttl_min: 0, gpu_tenant: "none"}`, so
   `pipeline/resource_pulse admit web_research` refused with *"ask the Architect before enabling. Do not
   force the Toolbelt."* — while its own `gpu_tenant: "none"` recorded that search costs no GPU. A
   CPU-only HTTP call was being gated like a Demucs run, which left `searxng_search`, `research_start`,
   `research_status` and `research_read` **unreachable in a default stack**, and made the playbook's
   "admit Web Research first" something she could not do unaided. Now `auto_enable: true` with a
   30-minute session TTL, i.e. the ordinary **light-hand** route (`resource_pulse` → `admit_for_goal`),
   matching the manifest's own `gpu_tenant: "none"`. Gate: `is_light = auto_enable and gpu_tenant in
   {"", "none", "idle"}` (`pipeline/resource_pulse.py:236`). The Architect still flips the *Toolbelt*
   when he wants it always-on; this only restores her ability to admit it for a bounded session.

Run live mode with the Workbench tracing:
`.\venv\Scripts\python.exe scripts\run-research-bench.py --live --case rb_01 --json`.

**The browser-trace observation, read correctly.** `trace-eve-browser.py` on *"search the web for the
latest yt-dlp release notes…"* gave one healthy bubble (25.1 s) in prose, and **no query reached
SearXNG** (`docker logs empire-searxng`, 10-minute window). Taken at the time as "she does not search",
and read beside the blind bench, it looked systemic. With `rb_01` passing on the same capability — and
the frontend's own trace showing `tool.requested: searxng_search` — the honest reading is much narrower:
**that phrasing did not trigger a search in that turn.** One no-tool turn is a data point about a
question, not a verdict about a limb; re-run it with tracing on before concluding anything.

| Link | State |
|---|---|
| Search service | ✅ live (`empire-searxng`, 36 results for a probe query) |
| Tool invoked directly | ✅ works (`pipeline.search_scout`; live query-only desk job → 9,298-char digest) |
| Capability gate | ✅ open (`admit web_research` → `ok: true`, now the light-hand route) |
| **Her turn calling the tool** | ✅ **works** — live `rb_01`: `tools=['searxng_search']`, case passed |


## The contract

| Rule | Where |
|---|---|
| Every case names a `needs` value that maps to callable tools | `pipeline/research_bench.py` (`NEED_TOOLS`) |
| A need with no callable tool is reported **blocked**, derived from `pipeline.tool_registry` — a disabled tool can never satisfy a need | `capability_baseline()` |
| A graded turn must show the expected tool, cite a source URL when the fact is external, avoid fabricated-evidence phrases, and produce a **real** artefact (the limb ran — chat text is not a document) | `grade()` |
| The hole stays visible: `--require-ready` exits 1 while a need is blocked | `scripts/run-research-bench.py` |
| Cases must stay valid and span the needs | `tests/pipeline/test_research_bench.py` |

## Extending it

1. Add a line to `data/eval/research_bench.jsonl`: `id`, `needs`, `query`, `expect_tool_any`,
   and whichever rules apply (`must_cite_source`, `must_contain`, `must_mention_any`,
   `expect_title_any`, `expect_artefact`, `must_not_mention`).
2. Keep some cases that already pass — a bench that only fails cannot show progress.
3. `--baseline` to see the capability verdict, `--live` (with `EMPIRE_TRACE=1`) to grade real turns.

## Limits

- **The live mode needs the Workbench running**; the baseline does not (it reads the registry).
- **Tool evidence comes from the trace**, so a run without `EMPIRE_TRACE=1` grades pessimistically —
  the script says so out loud rather than quietly passing everyone.
- **Grader, not a judge**: it checks tool evidence, citations, forbidden claims and artefact
  production. Whether an answer is *good* still needs eyes.

## Related

- [`RESEARCH_CLOSURE.md`](RESEARCH_CLOSURE.md) — the discovery gate this bench is the ticket for
- [`EMPIRE_IDEA_QUEUE.md`](EMPIRE_IDEA_QUEUE.md) — E-34 (this bench), E-35 (the search limb it unblocks)
- [`PLAYBOOK.md`](PLAYBOOK.md) — what she reads to *use* a capability once it exists
- The **research desk** (`pipeline/research_desk.py`, E-37) is the pickup half: a job returns a id
  immediately, a detached worker fetches on CPU, and `research_read` returns a bounded digest — the
  long-pass answer to a window that only holds about one long article.
