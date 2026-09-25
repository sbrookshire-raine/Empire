# Constrained output on local Ollama — measured, not assumed

**One breath:** `format` (JSON schema) **works and is fast** on this box, an `enum` is honoured exactly,
a bad schema **fails loudly in 0.02 s** instead of degrading silently — and **`format` + `tools` cannot
be combined**: the grammar wins and the tool call vanishes. That last one decides E-36's question.

Measured 2026-09-25 with `scripts/probe-constrained-output.py` on `empire-fast:14b` via native
`/api/chat` (the path the agent uses). E-36 put reliability before capability on record and asked for
this evaluation before wiring anything.

## Results

| # | Probe | Result | Time |
|---|---|---|---|
| 1 | baseline, no constraint | ANSWERED (`ready`) | 3.67 s |
| 2 | `format: "json"` | **VALID JSON** `{"status":"ok","n":3}` | **0.39 s** |
| 3 | schema with `enum` of 5 candidate titles | **VALID JSON**, `{"title":"White Stripes (disambiguation)","confidence":0.6}`, **member of the enum** | 1.11 s |
| 4 | malformed schema (`enum` as a string) | **HTTP 400** — *"enum must be a non-empty array"* | **0.02 s** |
| 5 | tool call **and** `format` together | VALID JSON `{"title":"White Stripes"}`, **`tool_calls: 0`** | 0.63 s |

## What this buys us

- **Structured output is available and cheap** — 0.39–1.11 s, i.e. below the prose path and far below
  the 3.4 s turn floor. There is no cost argument against using it.
- **A closed choice is structurally closed.** Probe 3 could not invent a title: the enum is enforced, so
  a nonexistent page is *unrepresentable*, not merely unlikely.
- **Misconfiguration is loud.** Probe 4 shows a bad schema rejected at request time with the exact
  reason. Wiring `format` therefore cannot create a silent hang — the failure mode E-30 is about.

## What it does NOT buy us (the two decisive findings)

1. **Grammar-constrained tool calling is not available: `format` suppresses `tools`.** Probe 5 asked a
   prompt that should have called `wiki_scout_search`; with `format` set it returned the JSON object and
   **zero tool calls**. So E-36's hope — *"structured decoding makes a malformed call structurally
   impossible"* — **does not hold on this server.** It is either/or: constrain the output, or allow tool
   calls. Malformed tool calls must be prevented elsewhere (argument validation + one bounded retry in
   the harness), not by `format`.
2. **Constrained syntax is not constrained meaning.** Probe 3 answered correctly *by shape* and **wrong
   by content**: for *"a spreadsheet of the White Stripes studio albums"* it picked
   **`White Stripes (disambiguation)`**, not `The White Stripes` — and reported confidence 0.6. An enum
   guarantees the answer is *one of the candidates*; it cannot guarantee the candidate list is good, nor
   that the pick is the best member. This is also the honest context for E-30: the pick step is where a
   confidently wrong title is born, which is why `pick_lead_target()` carries explicit ladders.

## How to re-measure

```powershell
.\venv\Scripts\python.exe scripts\probe-constrained-output.py
.\venv\Scripts\python.exe scripts\probe-constrained-output.py --model empire-fast:7b
```

## Where this leaves F-38

F-38 reads *"wire `format` for title pick before prose — no second generator"*. Re-grounded on the code:
**there is no model title pick to constrain** — `pipeline/wiki_read_lead.py:pick_lead_target()` is
deterministic Python (topic resolver + explicit ladders + first-hit fallback), and the only
structured-output user in the repo is `structured_extract.py`, which already does the
`json_schema` → `format: "json"` fallback dance.

So F-38's evaluation half is **done** and its wiring half is now a smaller, better-posed decision:

- If a model pick is ever wanted (replacing the ladders), `format` + `enum` is the right tool, and
  probe 3 shows it is enforceable — but it must be given a **pre-filtered candidate list**, because
  probe 3 also shows it will pick a plausible wrong member with confidence.
- The measured pick (**disambiguation page for a studio-albums ask**) is *worse* than the deterministic
  path today, so there is no case for swapping the ladders out on evidence.
- **Never** set `format` on a turn that must be able to call a tool (probe 5).

## Related

- [`EMPIRE_IDEA_QUEUE.md`](EMPIRE_IDEA_QUEUE.md) — E-36 (sequencing), F-38 (this measurement), E-30 (the pick's neighbourhood)
- [`RESEARCH_CLOSURE.md`](RESEARCH_CLOSURE.md) — "Constrained output | Ollama `format` | F-38"
- [`PLACEMENT.md`](PLACEMENT.md) — the other measured probe (`scripts/measure-placement.py`)
