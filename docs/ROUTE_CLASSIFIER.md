# The shared route classifier — one decision, one place

**One breath:** `pipeline/route_classifier.py` decides whether a message is a
**wiki** ask, a **memory** ask, a **task** ask, or something **else**. Every
caller asks it. Nobody keeps their own copy of the rules.

## Why it exists

Four places used to answer "is this an encyclopedia ask or a memory ask?"
independently:

| Caller | What it did |
|---|---|
| `frontend/wiki_drift_api.py::is_wiki_lookup_query` | its own regexes |
| `frontend/memory_api.py::is_memory_chat_query` | its own regexes *and* its own copy of the wiki check |
| `frontend/eve-workbench.js::isMemoryQuery` | a **third** set of regexes, in the browser |
| `pipeline/intent_codex.py::context_block` | scored the codex, then **overrode** the result with a wiki rule |

Four answers to one question is four ways to be wrong, and they were wrong in
different directions:

- **"what is my disk space"** was a *wiki* ask. The bare verb "what" matched
  a wiki trigger, so Eve was sent to look up the disk space on Wikipedia.
- **"what can you tell me about my memory of the project"** was an
  *encyclopedia* ask. Same bare verb, plus "about".
- The browser's copy could not see the server's rules at all, so it
  disagreed with the server **on purpose** — it did not even try to agree.

## The contract

```python
from pipeline import route_classifier

route_classifier.classify("Who is Kate Bush?")   # -> "wiki"
route_classifier.classify("what do you know about me")  # -> "memory"
route_classifier.classify("list my tasks")       # -> "task"
route_classifier.classify("what is my disk space")  # -> "other"
route_classifier.explain("Who is Kate Bush?")     # -> {"route": ..., "reason": ...}
```

Four labels: `wiki`, `memory`, `task`, `other`.

## Precedence

The order is the whole point of the module.

1. **Explicit wiki signal** — the message names Wikipedia, the wiki archive,
   a page, an article, a discography, or asks to compare years. This wins
   even over a memory anchor: *"look up the wikipedia article we discussed"*
   is a wiki ask, because the wiki verb names the archive.
2. **Memory anchor** — the message is about the Architect's own context
   (memory, interests, uploads, projects, notes, or past work: *"did we
   already build this"*). This wins over the generic wiki verbs: *"what do
   you know about my notes"* is memory, not an encyclopedia ask.
3. **Task** — the message is about the PocketBase task list.
4. **Encyclopedic subject** — a media noun (*"what albums did X release?"*).
5. **Generic wiki verb** — *"who is X"*, *"what is X"*, *"tell me about X"*,
   but only with a real encyclopedic subject and no stack subject.
6. Otherwise: **other**.

The rule that makes step 5 safe: a generic wiki verb needs a subject, and it
is suppressed by a stack subject. *"what is my disk space"* has neither.

## Who asks it

| Caller | How |
|---|---|
| `pipeline/intent_codex.py` | `resolve()` applies the route; `context_block()` uses the same result, so the two cannot disagree |
| `frontend/wiki_drift_api.py` | `is_wiki_lookup_query()` — the classifier can **veto**; the module's own regexes are a *fallback* for messages it does not recognise |
| `frontend/memory_api.py` | `is_memory_chat_query()` |
| `frontend/wiki_green_path.py` | the green path only prefetches archive evidence for a wiki ask |
| `frontend/serve.py` | `/api/route/classify` — the browser's window onto the classifier |
| `frontend/eve-workbench.js` | `isMemoryQuery()` calls the endpoint; it no longer carries any routing rules |

### The browser fails open

The browser calls `/api/route/classify` and, on **any** error — endpoint
missing, network down, classifier broken, bad JSON — it treats the message as
*not* a memory query and sends it to Eve. A classifier outage must never stop
a message from reaching her.

The endpoint itself **fails closed** (`503`) when the classifier raises, so
the failure is visible in the server log rather than silent.

## The corpus

`tests/pipeline/route_corpus.py` holds ~50 cases, grouped by the rule meant
to fire. Two test files read the *same* corpus:

- `tests/pipeline/test_route_classifier.py` — the classifier itself.
- `tests/frontend/test_route_classifier_parity.py` — every caller must agree
  with it.

So a change to one caller cannot silently reintroduce a second opinion.

## Changing the rules

Edit `pipeline/route_classifier.py`, then add the case to
`tests/pipeline/route_corpus.py` with the route you expect. If a caller
disagrees, the parity test names it.

**Do not** add routing rules to a caller. The only rules a caller may own are
the *stateful* ones the classifier cannot see: the page currently being
discussed, the Title DNS disambiguation prompt.

## The route is only half the claim

The classifier decides the route. Whether Eve then *reaches for that route's
tool* is a separate fact, and it is only observable on the live stack.

`scripts/verify-live-routing.py` (the E-03 battery) runs each prompt from
`config/diagnostics/live-routing-battery.json` as a real turn and reads the
framework's **structured** events:

- `actions.requested` -> `data.actions[].toolName` (the request)
- `action.result`     -> `data.result.toolName` + `data.status` (the outcome)

The old live harnesses grepped the raw NDJSON blob for a tool name. That
passes when the model merely *mentions* a tool in prose, and it cannot tell
the right tool from a plausible-but-wrong one. The battery reads the events
instead, so "Eve called a tool" means a tool call was actually issued.

The expected tool is derived at run time from the same classifier and codex
the running system uses, so the battery cannot assert something the system
does not itself claim.

### "No tool called" is sometimes correct

A case may set `require_tool: false`. The server's **green path**
(`frontend/wiki_green_path.py`) prefetches an archive extract for common wiki
phrasings and tells Eve to skip the tool call -- so for those asks, *no tool
call is the right answer*, and only a **foreign** tool (one belonging to
another route) is a failure.

That distinction was found by running the battery: the first version
asserted "a tool must be called" and failed two wiki cases that were in fact
answered correctly from prefetched evidence. The contract now has two halves:

1. **No foreign tool** -- a route never reaches into another route's tools.
   This is the regression the classifier fixed: "what is my disk space" used
   to go to the encyclopedia.
2. **Right tool when one is due** -- and only when the server did not already
   prefetch the answer.

### Measured on the live stack (2026-10-21)

7/7 cases routed correctly against `empire-fast:14b`: wiki (served from
prefetched evidence or `wiki_read_section`), memory (`cognee_recall`), task
(`list_tasks` / `create_task`), and the two `other` cases, which reached no
encyclopedia tool.
