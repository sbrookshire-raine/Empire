# skill-thought-experiments

Phase 3 thought experiments: take inspiration from one thing and test whether it transfers to
another. **Capture alone is not the skill — the connection is the deliverable.**

## Tools

| Tool | When |
|------|------|
| `primitive_lookup` | Find the mechanism a thing shares with another domain (returns `primitives` + a `sibling`), and the ledger's own vocabulary |
| `thought_experiment_read` | List or read past experiments **before** starting a new one |
| `thought_experiment_capture` | Write the experiment down at the end (topic + optional URL/notes) |

## Protocol (in order — steps 1, 2 and 4 are not optional)

1. **Ground both terms.** `wiki_scout_search` the bare title of each side (`Juggling`, `Drum kit`),
   then hop with `wiki_read_section` / `wiki_extract` when the lead lacks the mechanism. Outside the
   archive: `web_scout`, `github_scout_*`. Never ground a side in training memory.
2. **Name the mechanism in the Architect's vocabulary.** `primitive_lookup` with the shared words
   (e.g. `"timing rhythm coordination"`). The row's `primitives` is the join key and its `sibling` is
   a second domain where the same mechanism already appears — that is the evidence transfer is real,
   not decorative. No match → say so, then retry **once** using the returned `vocabulary` names.
3. **State the mapping in one sentence** — the mechanism, what it becomes in the target domain, and
   **where it breaks**. The break is the interesting part; keep it.
4. **Test what is testable.** `author_code` + `python_verify` for anything numeric or structural
   (periods, duty cycles, counts, schedules). A tested claim beats three paragraphs.
5. **Label provenance:** what came from a tool (name the title), what is your inference, what is
   general knowledge.
6. **Write it down.** `thought_experiment_capture` with the mapping, the test result, and one line
   saying what would falsify it. Offer Cognee promotion only if the Architect asks.

## Boundaries

- Scratch only: notes land under `04_Thought_Experiments`; never auto-Cognee.
- No tool, no claim: an ungrounded side is reported as ungrounded, not invented.
- Eve is **not** The Keeper at runtime — plain synthesis, no ceremonial greeting.

