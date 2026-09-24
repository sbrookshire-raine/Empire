# Wikipedia Workbench Eval

Offline-first acceptance suite for **work**, not trivia Q&A.

**Architect one-liner:** Trivia dies when Wikipedia is a navigable library with memory of the path; it stays trivia when every turn is “embed → paste lead → answer.”

## Rules

| Setting | Value |
|---------|--------|
| Weaviate | **Off** (no existence gate, no `:8091` speech) |
| Wiki Local | On |
| Cognee | Not required for pass |
| Primary mode | `--injection` (Title DNS + markdown evidence) |

## Suite file

[`data/eval/wiki_workbench.jsonl`](../data/eval/wiki_workbench.jsonl) — 11 cases (`tier: workbench`).

## Run

```powershell
cd C:\EMPIRE
$env:PYTHONPATH = "C:\EMPIRE"
$env:EMPIRE_WIKI_WEAVIATE_FALLBACK = "0"
.\venv\Scripts\python.exe scripts\run-wiki-calibrate.py --suite workbench --injection
```

Baseline report (optional):

```powershell
.\venv\Scripts\python.exe scripts\run-wiki-calibrate.py --suite workbench --injection --baseline data\eval\wiki_workbench_baseline.json
```

## Pass / fail rubric

These injection cases cover the **legacy escape hatch** (`EMPIRE_WIKI_MIDDLEWARE=1`); the
harness sets it locally. In the default autonomous mode there is no injected block, so
grade the reply against `wiki_scout_search` / `wiki_extract` tool output instead
(see [WIKI_SCOUT.md § Retrieval ownership](WIKI_SCOUT.md)).

A case **PASS**es injection when:

1. `[[EMPIRE_WIKI_LOOKUP]]` (or clear miss/disambig contract) is present when expected.
2. Every `must_contain` needle appears in the injected message (case-insensitive).
3. No `must_not_contain` / `must_not_mention` strings (Weaviate, Docker, 8091, Cult following, …).
4. If `must_titles` is set: at least one expected title appears in evidence (`Title:` / hop / related).
5. If `expect_ask_disambiguation`: injection asks which title / lists candidates (or turn-2 resolves after fork).
6. If `expect_miss`: miss contract without inventing a fake page.
7. If `expect_escalate_web`: injection or CONTRACT notes local insufficiency / weather / future device — **not** a Weaviate boot speech.

Live Eve (`--live-eve`) is optional and not required for Phase 0 baseline.

## Roadmap mapping

| Case | Unlocks with |
|------|----------------|
| wb_01 Casting Hop | Phase 1 aliases + Phase 2 Cast/Filmography sections |
| wb_02 Soundtrack Trace | Phase 2 Discography/Charts + link hops |
| wb_03 Ingredient Origin | Link hops + History section |
| wb_04–05 Synthesis | Phase 3 scratchpad |
| wb_06 Cast Table Merge | Phase 2 Cast section (two titles) |
| wb_07 One-Letter Fork | Phase 4 follow-up router |
| wb_08 Persistence | Decade parsing + Phase 3 scratchpad |
| wb_09 Error Book | Phase 3 Error Book |
| wb_10–11 Escalation | Skill/CONTRACT (web boundary) |

## Deferred

ZIM / openzim-mcp and GBNF stay deferred until kill criteria in [`WIKI_SCOUT.md`](WIKI_SCOUT.md) trip.
