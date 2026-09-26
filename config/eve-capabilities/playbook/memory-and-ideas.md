---
area: memory-and-ideas
one_line: Recall and store memory, curated primitives, thought experiments, the decoded ledger, ideas.
tools: cognee_recall, cognee_remember, propose_remember, confirm_remember, cognee_improve, cognee_forget, primitive_lookup, thought_experiment_capture, thought_experiment_read, loom_status, loom_process_shell, architect_now_update
skills: recall-ingested-context, skill-companion, skill-loom-intake, skill-thought-experiments
---

# Memory, ideas and the ledger — worked pathways

Two different stores, never confused: **Cognee** is long-term memory (datasets `eve_core`, `eve_memory`,
`primitives_test`), and the **ledger/scratch** is the Architect's own decoded thinking. Promotion to
Cognee happens only when he agrees.

## Recall
Use when: "what do you know about…", "my interests/projects", "do you remember…".

- **Ask:** "what are my interests?" → **Do:** `cognee_recall(query, dataset="eve_core")` (fallback `eve_memory`) → **Get:** grounded answers from what was ingested, not training memory.
- **Ask:** "what projects do I have in memory?" → **Do:** `cognee_recall("projects")` → **Get:** the list as stored; never create tasks from this.
- **Ask:** "what did we decide about the wiki limb?" → **Do:** `cognee_recall("wiki limb decision")` → **Get:** the stored decision or an honest "not in memory".
- **Ask:** "recall the curated primitives about restraint" → **Do:** `cognee_recall("restraint", dataset="primitives_test")` → **Get:** the curated primitive passages.
- **Ask:** "is anything in memory about the drums lesson?" → **Do:** `cognee_recall("drums")` → **Get:** hits or a plain absence.

## Storing (with consent)
Use when: something is worth keeping for future turns.

- **Ask:** "remember that I prefer dry answers" → **Do:** `propose_remember(text)` → ask the Architect → `confirm_remember(id)` → **Get:** one Cognee entry, no silent writes.
- **Ask:** "keep this whole report in memory" → **Do:** `propose_remember(summary)` → **Get:** a proposal he can accept or drop.
- **Ask:** "that ingest made recall worse" → **Do:** `cognee_improve()` → **Get:** a re-index/repair pass, then re-query.
- **Ask:** "forget the stale boot notes" → **Do:** `cognee_forget(scope)` **only when he says so** → **Get:** the removal confirmed by name.
- **Ask:** "remember that the Cognee graph lives on the VHDX" → **Do:** `cognee_remember("Cognee graph storage: VHDX at I:\\EMPIRE_VHDX\\empire_cognee.vhdx")` → **Get:** it stored straight away, because his instruction *is* the consent (when he did not ask, use `propose_remember` first).
- **Ask:** "update my current facts card" → **Do:** `architect_now_update(text)` → **Get:** the living card refreshed (facts about him only — never instructions).

### What may be remembered — tier rules (full policy: docs/MEMORY_GOVERNANCE.md)

Before proposing anything, answer three questions:

1. **Knowledge or reference?** *Knowledge* = standing preferences, house rules, decisions **with their
   rationale**, corrections to you, vocabulary, the Architect's primitives → eligible for `eve_core`,
   which stays small on purpose. *Reference* = manuals, vendor guides, tutorials, transcripts, big
   exports → **never embed**; the place for them is a Library access point line in `config/library.json`.
2. **Durable?** Still true and useful in a month — or it belongs to this conversation only.
3. **Provenance?** Name the source file, or the conversation with its date. No provenance, no entry.

Never in memory, in any tier: secrets (keys, tokens, passwords), harvested bulk and byte-identical
duplicates, code and zips, game/harvest noise. Harvest scratch stays in `04_Thought_Experiments` until
he promotes it.

When you recall, cite `source_file` plus its date, and say plainly whether it was **"you told me"**
(recall) or **"I looked it up"** (a path, a URL, an article).

## Thought experiments (his practice, formalized)
Use when: "does X apply to Y", "take inspiration from A and try it on B", or he says "thought experiment".

- **Ask:** "does the pencil eraser idea apply to code review?" → **Do:** `primitive_lookup("eraser reversibility")` → **Get:** his own row (`pencil (eraser end)` → `Iterative Reversibility`, sibling: a birthday candle) as the evidence.
- **Ask:** "which primitives does juggling share with drumming?" → **Do:** `primitive_lookup("juggling drumming")`; if no row matches → **Get:** the ledger's vocabulary (`Timing & Sync`, `Sensory Feedback`) to name the closest as the Architect's-inference mapping, labelled as such.
- **Ask:** "write this one down" → **Do:** `thought_experiment_capture(topic, notes)` → **Get:** a note under `04_Thought_Experiments` (scratch; not Cognee).
- **Ask:** "what did we try before about X?" → **Do:** `thought_experiment_read()` → list, then read one → **Get:** the previous mapping so this turn builds on it.
- **Ask:** "test the claim before you write it down" → **Do:** `author_code` + `python_verify` → `thought_experiment_capture(notes=<result + what would falsify>)` → **Get:** a tested claim with a falsifier.
- **Ask:** "which rows in my ledger are about feedback loops?" → **Do:** `primitive_lookup(primitive="Sensory Feedback")` → **Get:** every decoded thing carrying it, with siblings.
- **Ask:** "how much of the ledger is decoded?" → **Do:** `primitive_lookup(text=...)` → **Get:** `rows_total` and `rows_distinct` (501 / 247 on this machine).

## Loom intake (raw dumps → primitives)
Use when: he drops a NotebookLM/Obsidian CSV export, or says "run the Shell".

- **Ask:** "here's my new export — fold it in" → **Do:** `loom_status()` → `loom_process_shell("/path/to/export.csv")` → **Get:** gated rows in `primitive_ledger.csv` (max 7 promoted per cycle; overflow stays in buffer).
- **Ask:** "how big is the ledger, and where's the Seeker prompt?" → **Do:** `loom_status()` → **Get:** row counts + the paths.
- **Ask:** "a single articulated idea, no CSV" → **Do:** `primitive_lookup` + synthesis (skip the Shell — it is for dumps) → **Get:** primitive names and a mapping.
- **Ask:** "never delete ledger rows" → **Do:** nothing — that is the Mechanical Ratchet rule; say it → **Get:** a refusal to prune.

## The composite pathway (what a real session looks like)
- **Ask:** "use my ledger: what does the pencil teach me about anything else?" → **Do:** `primitive_lookup("pencil")` → `thought_experiment_read()` → `primitive_lookup(primitive="Sacrificial Attrition")` → **Get:** his row, past experiments on it, and every sibling domain that shares the mechanism — then capture the new mapping.
- **Ask:** "learn something with me about X" → **Do:** `wiki_scout_search(<bare title>)` → hop with `wiki_read_section` → `cognee_recall` for what we already built → **Get:** grounded explanation + our prior work, then one next step.
- **Ask:** "is this idea already in my ledger or my notes?" → **Do:** `primitive_lookup(text)` → `thought_experiment_read()` → `workspace_search(text)` → **Get:** a single answer that covers ledger, experiments, and files.
