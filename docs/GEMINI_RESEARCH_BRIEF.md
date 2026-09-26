# Gemini research brief — proposing capabilities for EMPIRE

Companion to `docs/LEGO_PROMPT.md`. That file says **how a brick must be shaped**. This file says **what
already exists, what is actually missing, and what evidence you must bring**. A model needs both; the
2026-09-26 deep-research run had only the first, so three of its four proposals described subsystems
EMPIRE already runs. Paste this with `docs/LEGO_PROMPT.md` and `docs/DOC_MAP.md`.

## 1. What EMPIRE already has — do not propose these

Check every proposal against this table first. If your idea is here, either say what the existing
capability fails to do (with evidence) or drop it.

| Capability | What actually runs | Notes that matter |
|---|---|---|
| Local inference | Ollama, `llama3.1`, 24,576-token context, q8_0 KV cache + flash attention | measured 10.5 GB of 16 GB VRAM when loaded |
| Graph + vector memory | Cognee on Postgres + pgvector, datasets `eve_memory` (10,319 files), `eve_core` (curated), `primitives_test` | one store, deliberately; `V:\Cognee` VHDX on the T7 |
| Embeddings | Ollama `nomic-embed-text`, 768 dims, batch 512 | changing the model invalidates every stored vector |
| Task CRUD | PocketBase on :8090 (REST + admin UI), HTMX/Alpine frontend on :8080 | |
| Agent runtime | "Eve" (TypeScript), FastMCP Python servers over stdio, one shared MCP client, playbook limbs read on demand | 7 wrappers consolidated to 1 client, 1,328 → 299 lines |
| Voice / ASR | Speaches on :8000 (CPU, faster-whisper based) — push-to-talk STT and TTS | a second whisper stack would be the third ASR path |
| Web + GitHub search | self-hosted SearXNG container, `searxng_search`, `web_scout`, `github_scout`, `research_*` | |
| Wiki corpus | 5.3M-article snapshot on `D:\wiki_md\2017`, read through the wiki lead path | reference, never embedded |
| Code reach | `read_active_tool` over `03_Active_Tools` + `LEGO_INDEX.md` (flattened codebases) | text-level, not structural — see §2.4 |
| Container execution | Eve sandbox containers (Docker) + `scripts/prune-sandbox-containers.ps1` | `ops` tenancy declared |
| Governance | LEGO contract + `check-legos`, `audit-empire`, capability manifest, `resource_pulse` / `admit_for_goal` | enforced in CI (`mechanic-green`), not by convention |

## 2. What is genuinely open (with the evidence we already have)

Proposals aimed here are worth reading. Everything else needs a strong justification.

1. **Memory content quality — measured, not suspected.** `eve_core` (the set chat recall prefers) holds 75
   entries: **8 registered, 37 reference, 21 forbidden, 9 unregistered**. Cause: keyword scoring in
   `scripts/optimize_eve_memory.py` gives `nlm*` a +55 bonus, so NotebookLM exports outrank project
   knowledge; duplicates (`_1.md`, `X.md.md`) and `unmatched-*` harvest residue pass the threshold. Open work:
   rebuild the set and prove recall names its source.
2. **Batch transcription of ~900 MB of audio** (~88 files in `02_Skills_and_Prompts`). Realtime works;
   file-level batch was never built. Route must use the Speaches endpoint already running.
3. **Container mount containment (CWE-22).** No `Mount`/`bind`/`HostConfig` surface was found in
   `agent/tools/*.ts`, so this may be a non-issue — or the search was too narrow. Verification is open.
4. **Structural code navigation.** Absent (we have text-level reach only). Precondition that currently
   fails: harvested codebases are *flattened*; an AST parser needs real source trees.
5. **Legacy embedded store on `V:\Cognee`** — 2.6 GB (`cognee_graph_kuzu` 2.13 GB + SQLite 451 MB), last
   written 23 Jul, dormant since the move to Postgres. Keep or reclaim: undecided.
6. **Version debt.** cognee 1.4.0 → 1.6.1 (runbook written), PocketBase 0.28.4 → 0.40.4 (a migration, not
   a bump), two `:latest` container tags unpinned.
7. **Standing invariants.** Orphaned MCP child processes were 16 and are now 2 — nothing currently measures
   that they stay at 2.


## 3. Hard constraints, in the units this system actually pays

| Constraint | Number / rule | Why it kills proposals |
|---|---|---|
| Prompt budget | ~11k tokens of a 24,576 window already used (instructions + routing ≈ 5.8k, tool schemas ≈ 5.3k) | every new brick adds tool schemas. A proposal must say what it *displaces* or what its token cost is. "Additive and cheap" is not an option here |
| VRAM | 16 GB card, one GPU tenant at a time (`none`, `chat`, `extract`, `vision`, `ops`), ~10.5 GB used at full context | a second resident model is an OOM, not a feature |
| Memory stores | exactly one (Postgres + pgvector) | a second vector store means two memory systems to curate |
| Ports | MCP servers are stdio and expose none; *declared services* have documented ports (8090, 8080, 11434, 8000) | "zero ports" is not a system law — stating it as one misreads the architecture |
| Network at runtime | none. No cloud API, no keys, no telemetry | non-negotiable |
| Root confinement | tools read/write only inside roots declared in their env | a tool that can escape is rejected before review |
| Re-migration cost | swapping an embedding model invalidates 10,383 stored vectors → full re-embed | "replace X with Y" must carry this cost |

## 4. Evidence standard

1. **No unsourced claim.** Anything asserted as fact needs a link we can open, dated. An upstream CVE or
   benchmark quoted without a checkable source is a hypothesis, and a hypothesis is not a justification.
2. **Measure before recommending.** State the measurement that would *falsify* your proposal. If none
   exists, the proposal is not ready.
3. **Quantify cost** in this system's units: prompt tokens, VRAM, disk, re-embed time, migration risk,
   human review.
4. **Prefer the smallest change that can be measured.** A one-line fix with a test beats an architecture.
5. **A clean "nothing here fits" is a good answer.** It is more useful than a stretch, and it is recorded.

## 5. Required output format per proposal

Beyond `docs/LEGO_PROMPT.md` §2's brick JSON, every proposal must carry these fields:

| Field | Rule |
|---|---|
| `already_exists` | **Required.** Name the closest capability in §1 and why yours is not that. "No close match" is allowed only with the evidence you used to decide |
| `gap_evidence` | a measurement, a repo path, or a logged failure — not an assertion |
| `cost` | tokens, VRAM, disk, migration, review cost |
| `displaces` | what it removes, shrinks, or replaces — or an explicit "adds and displaces nothing" |
| `falsification_test` | the observation that would prove this proposal wrong |
| `fit_argument` | `docs/LEGO_PROMPT.md` §3 checklist, answered plainly |

## 6. Automatic rejections (learned the hard way)

- A proposal whose subject appears in §1 without a named failure of the existing capability.
- A second vector store, a second ASR stack, a second embedding model.
- Capability treated as free: no token or VRAM accounting.
- New always-on prompt rules (guidance belongs in a playbook page or skill, where it costs no context).
- Security claims used as the *primary* justification while remaining unverified.
- "Merge these, they look alike" without measurement — this project has three recorded cases where
  measurement reversed that judgement.

## 7. How to run the task

Give the model: this file + `docs/LEGO_PROMPT.md` + `docs/DOC_MAP.md` (the document index). Ask for:

1. **at most three** proposals, each aimed at a numbered item in §2 — plus
2. **explicit rejections**: things it considered and dropped, with the reason — this is often the most
   valuable part of the answer, and
3. a **one-paragraph answer** to: *"if nothing here justifies new work, say so and say what would change
   your mind."*

Then stop. Proposals are reviewed against `docs/LEGO_CONTRACT.md` and run through `scripts/check-legos.py`;
a conforming brick is the entry ticket, never the argument.
