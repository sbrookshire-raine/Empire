# The Capability Playbook

**One breath:** the playbook is what Eve reads when she needs to *do* something — per capability, the
tool names and 3–7 worked examples written as **ask → tools → artefact**, so a known route is reused
instead of a tool being reached for at random. It is her runtime answer to *"how do I use this?"*;
`tool_docs` answers *"what are this tool's parameters?"*.

**Why it exists.** `agent/instructions.ts` builds the system prompt from `eve_instructions.md` +
`empire-routing.md` only — so the 33 `agent/skills/*.md` files never entered context and every
routing line saying "Load **skill-x**" pointed at text that was never loaded (E-29). The playbook is
the on-demand replacement, in the same spirit as R-03's tool-docs move: the prompt keeps the name and
a one-line cue, the depth is fetched when it is needed.

## Where it lives

| Piece | Path |
|---|---|
| Content (her playbook) | `config/eve-capabilities/playbook/<area>.md` — 8 areas, ~43 KB, 40+ sections |
| Registry / lookup | `pipeline/playbook.py` — `index()`, `topic()`, `thin_sections()`, `coverage()` |
| The tool | `agents/empire-task-agent/agent/tools/playbook.ts` — always registered |
| Deep syntax | `config/eve-capabilities/tool-docs/playbook.md` (fetched with `tool_docs`) |
| Routing line | `agent/empire-routing.md`: "Call `playbook` for the route, `tool_docs` for syntax." |
| Contract tests | `tests/pipeline/test_playbook.py`, `tests/pipeline/test_playbook_coverage.py` |

Each file carries front matter — `area`, `one_line`, `tools:`, `skills:` — then one `## <capability>`
section per capability:

```markdown
## Local Wikipedia lookup
Use when: who/what/when questions, cast lists, briefs.
- **Ask:** "what album has Seven Nation Army?" → **Do:** `wiki_scout_search("The White Stripes")`
  then `wiki_read_section("Elephant")` → **Get:** the album+track answer with the page named.
```

## The guarantee (and how to check it)

`python -m pipeline.playbook --coverage` — exits 0 only when all of these hold, and
`tests/pipeline/test_playbook_coverage.py` fails the build when they do not:

| Check | Meaning |
|---|---|
| `missing_tools` | every tool in the R-03 registry is claimed by an area — no tool without examples |
| `unused_tools` | every claimed tool actually appears in a worked example (a claim with no example is decoration) |
| `ghost_tools` | no area promises a tool that does not exist |
| `missing_skills` | every `agent/skills/*.md` file is claimed by exactly one area (E-29) |
| `ghost_skills` | no claimed skill lacks a file behind it |
| `thin_sections` (test) | every section carries ≥ 3 examples, or an explicit "not enough real uses yet" note |

Measured 2026-09-24, after the cleanup this contract forced: **81 tools — all claimed and all shown —
and 33/33 skill files mapped**, `ok: true`.

## Extending it

1. Add or edit `config/eve-capabilities/playbook/<area>.md`, keeping ≥ 3 examples per section.
2. A new tool must be added to the `tools:` front matter **and** used in an example.
3. Run `python -m pipeline.playbook --coverage` and `.\scripts\mechanic-green.ps1`.

`scripts/build-tool-docs.py` regenerates the tool registry; it skips `export default disableTool()`
files, so a switched-off tool can no longer acquire a doc (nine such phantom docs used to promise
tools she could not call — see E-32).

## Limits

- **On demand, not resident.** The routing line nudges her to call `playbook`, and a browser run
  showed she does (77.7 ms), but nothing forces it. Uncallable-by-construction was never the goal;
  *available and correct* was.
- **Front matter is a claim; the bodies are the truth.** Coverage checks that a claimed tool appears
  in an example, but only a human review can say the example is *good*.
- **The 33 `agent/skills/*.md` files are still inert** — the playbook now subsumes their subjects, so
  the E-29 decision (compile them into `eve-skills/` packages, or fold and delete) is a folder
  cleanup rather than a capability risk.

## Related

- [`EMPIRE_IDEA_QUEUE.md`](EMPIRE_IDEA_QUEUE.md) — E-29 (inert skills), E-32 (phantom docs + ghost routes)
- [`REFACTOR_PLAN.md`](REFACTOR_PLAN.md) — R-03 (tool docs out of the hot prompt) · R-05 (gates in CI)
- [`EMPIRE_USAGE_GUIDE.md`](EMPIRE_USAGE_GUIDE.md) — the Architect-side how-to
