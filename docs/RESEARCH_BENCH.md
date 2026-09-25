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

## Live mode — measured 2026-09-25 (1/8), and why

The baseline mode measures *capability existence*. Live mode asks the harder question — do real turns
through the Workbench actually use the limb? First full run, stack up (8080 / 2000 / 8090, SearXNG up):

```
  rb_01..rb_07  FAIL  tools=none      rb_08  pass  tools=none
  passed=1/8   per_need={'search': {'pass': 0, 'fail': 2}, 'github': ..., 'archive': {'pass':0,'fail':2}, ...}
```

`rb_05` detail: `{"tools": [], "cited_url": false, "chars": 321}` — **she answered in 321 characters of
prose with no tool calls at all.** Not an empty response (so not E-30), and not a search-specific
failure: `rb_05`/`rb_06` expect `wiki_local` / `github_scout` tools. Two findings, in order of weight:

1. **Live turns are not using tools — including enabled ones.** `wiki_local` *is* in the local Toolbelt
   (`%LOCALAPPDATA%\EMPIRE\eve-toolbelt.json` → `active_tools: ["wiki_local"]`) and `wiki_scout_search`
   is gated on it, yet no tool ran. So the Workbench path is either not offering tool schemas, not
   surfacing the results, or she is choosing parametric answers. This affects *every* capability in the
   UI, so it outranks the bench's own verdict and needs its own investigation.
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

Re-run live mode with `.\venv\Scripts\python.exe scripts\run-research-bench.py --live --case rb_05 --json`.

**Corroborated on the browser path, 2026-09-25, with the gate open.** After `admit web_research`
(light hand — session grant active, 30 min, `searxng_search` enabled): `scripts/trace-eve-browser.py
--question "search the web for the latest yt-dlp release notes and tell me what version it is"` produced
**one bubble in 25.1 s** (healthy) whose answer was prose — and **no query ever reached SearXNG**
(`docker logs empire-searxng`, 10-minute window). So the chain is now fully isolated:

| Link | State |
|---|---|
| Search service | ✅ live (`empire-searxng`, 36 results for a probe query) |
| Tool invoked directly | ✅ works (`pipeline.search_scout` + a live query-only desk job → 9,298-char digest) |
| Capability gate | ✅ open (`admit web_research` → `ok: true`, listed under "Can admit now") |
| **Her turn calling the tool** | ❌ **no tool call — E-43** |

That makes E-43 the single blocker between "the capability exists" and "she uses it". To see the
per-turn tool list, start the Workbench under `EMPIRE_TRACE=1` (the trace above reports
*"(no records after the mark — start the Workbench with EMPIRE_TRACE=1)"*).


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
