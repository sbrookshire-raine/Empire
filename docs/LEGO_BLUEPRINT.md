# EMPIRE LEGO BLUEPRINT — the handoff document

**Part-A artifact.** Hand this file (or paste §1) to any external model — Gemini, Composer, DeepSeek, whatever —
and it will know **what attaches to EMPIRE, what already exists, and what is honestly open**, in EMPIRE's own
vocabulary, with an output format a machine can check.

- Canonical copy (versioned): `docs/LEGO_BLUEPRINT.md` in `github.com/sbrookshire-raine/Empire`
- Full standard: `docs/LEGO_CONTRACT.md` · Enforced by `scripts/check-legos.py` inside `mechanic-green`
- Maintained alongside: `docs/LEGO_PROMPT.md` (prompt only), `docs/GEMINI_RESEARCH_BRIEF.md` (research mode)
- **Current as of 2026-09-27**

---

## 0. What changed in this version (so an old copy is visibly stale)

Earlier copies of this document carried **the contract but no inventory**. A capable model, told how a brick
must be shaped and nothing about what already runs here, proposed four conforming bricks for capabilities EMPIRE
already had — a semantic memory engine, a container runner, an audio transcriber, and (correctly) one real gap.
Three of four were duplicates. That was a brief defect, not a reasoning defect. This version fixes it:

| Added | Why |
|---|---|
| **§2 What EMPIRE already has** | the section whose absence caused the duplicates |
| **§3 Constraints in real units** | so "cheap" and "additive" are measured in tokens and VRAM, not adjectives |
| **§4 What is genuinely open** | so proposals aim at real problems instead of invented ones |
| **§8 Evidence standard** | two outside runs cited unverified CVEs as their main justification |
| **§9 Corrections** | four repeated errors, each seen at least twice — corrected here so review doesn't have to catch them again |

---

## 1. Copy-paste prompt

> **Context.** EMPIRE is a local-first, meter-free AI workspace: a Windows host running Python, Node,
> PowerShell, Docker and Ollama. Everything runs on this machine — no cloud API calls, no API keys, no
> telemetry at runtime. A local agent ("Eve") uses a fixed set of **limbs**; each limb is a Python MCP server
> plus a thin TypeScript adapter, described by a playbook page and registered in a brick catalog.
>
> **Before you propose anything, read §2.** It lists what already exists. A proposal whose subject is in §2 must
> first say what the existing capability fails to do, with evidence — otherwise it is a duplicate and will be
> rejected without discussion.
>
> **Task.** Propose **at most three** bricks: self-contained capabilities that attach to this system without
> modifying its core — plus, separately, the things you considered and **rejected**, with your reasons. The
> rejections are often the most useful part of a submission. If nothing here justifies new work, say so, and say
> what would change your mind.
>
> **What a brick is.** Four parts, all required:
> 1. `mcp/<name>_mcp.py` — FastMCP tools over stdio. Reads/writes only inside roots declared in its env.
>    Use the SDK this repo uses: `from mcp.server.fastmcp import FastMCP` (the MCP Python SDK's bundled one),
>    **not** the standalone `fastmcp` package.
> 2. `agent/lib/<name>-mcp.ts` — a `createEmpireMcpClient({ label, clientName, script, env })` config plus one
>    thin function per tool, imported from `./mcp-client`. **Do not** import the MCP SDK, manage process
>    lifetime, or parse MCP JSON yourself; a shared client does all of that.
> 3. `config/eve-capabilities/playbook/<limb>.md` — frontmatter (`area`, `one_line`, `tools`, `skills`) and
>    "ask → do → get" pathways. This is how the agent learns to use it, read on demand.
> 4. A brick entry (§5) — `default_on: false` unless it is core, honest `gpu_tenant`, declared `ports`, and the
>    actual tool names.
>
> **Never propose** (automatic rejections):
> - a cloud API, an API key, or any hosted service in the runtime path;
> - **a second copy of something in §2** — including a second vector store, a second ASR engine, a second
>   embedding model, or a second home for job/queue state;
> - a new service or port without an admission entry and start-script wiring;
> - a tool that reads or writes outside its declared roots, or that accepts a path it does not canonicalise;
> - embedding manuals/guides/transcripts into memory (reference material is reached by name, never embedded);
> - a new always-on prompt rule (guidance goes in a skill or playbook page, where it costs no context budget);
> - anything requiring changes to the shared client or the playbook format to bolt on.
>
> **Requirements the system cares about:** declared GPU tenancy (one tenant at a time — `none`, `chat`,
> `extract`, `vision`, `ops`); declared network use; errors returned as `{ ok: false, error }` naming the failing
> server; no secrets in memory in any tier; honest accounting of what the brick costs at runtime.
>
> **Deliverable.** Per brick: the brick JSON (§5), the tool list with one-line purposes, the declarations (GPU /
> network / services / disk), the playbook pathways, and the six required fields in §5. State plainly any
> assumption you made. A clean "nothing here fits" is a better answer than a stretch.

---

## 2. What EMPIRE already has — do not propose these

Check every idea against this table first. These are the capabilities that exist *today*, with the numbers that
matter. If your idea is here, either name what the existing thing fails to do (with evidence) or drop it.

| Capability | What actually runs | Notes that decide proposals |
|---|---|---|
| Local inference | Ollama, `llama3.1`, 24,576-token context, q8_0 KV cache + flash attention | measured ~10.5 GB of 16 GB VRAM when loaded |
| Graph + vector memory | Cognee on Postgres + pgvector; datasets `eve_memory` (~10,300 files), `eve_core` (curated), `primitives_test` | **one store, deliberately.** Memory tiers and rules: `docs/MEMORY_GOVERNANCE.md` |
| Embeddings | Ollama `nomic-embed-text`, 768 dims, batch 512 | a different model is a different vector space → all ~10,400 vectors re-embed |
| **Reranking** | **exists twice**: `pipeline/retrieval_rerank.py` (lexical baseline + optional CrossEncoder A/B, with a control case) and `pipeline/wiki_interpreter.py` (optional `BAAI/bge-reranker-base`, wiki stack currently halted) | "add a reranker" is already answered — the open question is whether reranking *helps*, and the harness now exists to measure it |
| Task / job state | PocketBase `:8090` — tasks, day blocks, `ingestion_jobs` lifecycle (`pending` / `running` / `success` / `failed` / `dead_letter`, plus `retry_count` / `next_run_at` / `failure_reason` for durable retries) | a second queue or job database would be a second source of truth |
| Work orders / approvals | `draft_work_order` writes work orders with `- **Status:** open`, plus the work-orders and resource-queue directories; memories use propose→confirm | staged human approval exists; extend its statuses rather than adding a mailbox |
| Agent runtime | "Eve" (TypeScript), FastMCP servers over stdio via **one shared client** (`agent/lib/mcp-client.ts`), playbook limbs read on demand | adapters stay thin; the shared client owns process lifetime |
| Voice / ASR | Speaches `:8000` (CPU, faster-whisper based) for push-to-talk STT/TTS | realtime exists; **batch** transcription of a file library does not (§4) |
| Web + code search | self-hosted SearXNG, `searxng_search`, `web_scout`, `github_scout`, `research_*` | |
| Containers | Eve sandbox containers (Docker) + `prune-sandbox-containers.ps1` | `ops` tenancy declared |
| Code reach | `read_active_tool` over `03_Active_Tools` + `LEGO_INDEX.md` (flattened codebases) | text-level only; an AST needs real source trees (§4) |
| Wiki corpus | 5.3M-article snapshot on `D:\wiki_md\2017`, read via the wiki lead path | reference, never embedded; stack halted |
| Governance + builder tooling | `check-legos`, `audit-empire`, `check-foundation`, `vault-manifest`, `infra-checks` (deptry / ruff / gitleaks), `pre-commit`, restic backups to the T7, trivy + syft SBOM/scanning | these run in CI; a proposal that ignores them is proposing drift |
| Declared services | Postgres 5432 · PocketBase 8090 · frontend 8080 · Ollama 11434 · Speaches 8000 | documented and admitted — **not** "external daemons" |

## 3. Constraints, in the units this system actually pays

| Constraint | Number / rule | Why it kills proposals |
|---|---|---|
| Prompt budget | ~11k tokens of a 24,576 window already used (instructions + routing ≈ 5.8k, tool schemas ≈ 5.3k) | every brick adds tool schemas. State what your brick **displaces**, or its token cost. "Additive and cheap" is not available here |
| VRAM | 16 GB, one GPU tenant at a time, ~10.5 GB used at full context | a second resident model is an OOM, not a feature |
| Memory stores | exactly one (Postgres + pgvector) | a second store means two things to curate |
| Ports | **MCP servers are stdio-only and expose none.** Declared services have documented ports (§2) | "zero ports" applies to MCP servers, not to the system |
| Network at runtime | none — no cloud API, no keys, no telemetry | non-negotiable |
| Root confinement | tools read/write only inside roots declared in their env, canonicalised and checked | a tool that can escape is rejected before review |
| Re-embedding | swapping the embedding model invalidates ~10,400 stored vectors | any "replace X with Y" carries this cost |
| Runtime cost | a Lens-B limb taxes every single turn; builder-side tooling (Lens A) costs nothing at runtime | say which one you are proposing — see §6 |

---

## 4. What is genuinely open (with the evidence we already have)

Proposals aimed here are worth writing. Everything else needs a much stronger justification.

1. **Memory content quality — measured, not suspected.** `eve_core` (the set chat recall prefers) holds 75
   entries: **8 registered, 37 reference, 21 forbidden, 9 unregistered**. Cause: keyword scoring in
   `scripts/optimize_eve_memory.py` gives `nlm*` a +55 bonus (NotebookLM exports outrank project knowledge), and
   duplicates (`_1.md`, `X.md.md`) plus `unmatched-*` harvest residue passed its threshold. Open work: rebuild
   the set and prove recall names its source.
2. **Is reranking worth it?** Both the rewritten lexical baseline and a cross-encoder score **6/8 on the same
   eight cases**, failing the same two. The harness is honest now (stopwords filtered, candidate order hashed,
   control case present), so the question is real and unanswered: better cases, a bigger model, or a different
   answer.
3. **Batch transcription** of ~900 MB of audio (~88 files) in `02_Skills_and_Prompts`. Realtime works (Speaches);
   file-level batch was never built, and the route should use the service already running.
4. **Canonical path jailing is inconsistent.** Some servers call `.resolve()`; others do not, and **nothing
   enforces `is_relative_to(root)`** across the tool surface — including on any Docker mount path. This is the
   highest-value open item and it needs no new dependency.
5. **No reuse ranking signal.** Nothing records `hit_count` / `last_applied_at`, so recall cannot prefer a fix
   that has worked five times over one that worked once.
6. **No terminal failure state or retry schedule.** Retries are ad-hoc in-process sleeps (fixed 15 s in
   `ingest_workbench.py`); no `next_run_at`, no quarantine record. We do use exponential jitter for LLM calls,
   so the technique exists — the durable schedule does not.
7. **Structural code navigation.** Absent (text-level reach only). Precondition that currently fails: our
   harvested codebases are *flattened*; an AST parser needs real source trees.
8. **Version debt.** cognee 1.4.0 → 1.6.1 (runbook written, unexecuted), PocketBase 0.28.4 → 0.40.4 (a
   migration, not a bump), and 2.6 GB of a dormant legacy store on `V:\Cognee` awaiting a keep-or-reclaim call.

## 5. Required output format

Per brick, the brick JSON:

```json
{
  "id": "short-stable-name",
  "label": "Human Label",
  "toolbelt": "limb_name_or_null",
  "default_on": false,
  "gpu_tenant": "none",
  "ports": { "in": ["text"], "out": ["text"] },
  "tools": ["tool_one", "tool_two"],
  "note": "One sentence: what it does and why it exists."
}
```

Plus these **six required fields** in prose. A submission missing any of them is not ready:

| Field | Rule |
|---|---|
| `already_exists` | **Required.** Name the closest capability in §2 and why yours is not that. "No close match" is allowed only with the evidence you used to decide |
| `gap_evidence` | a measurement, a repo path, or a logged failure — from §4 ideally. Not an assertion |
| `cost` | prompt tokens, VRAM, disk, migration, re-embedding, review cost — in real units (§3) |
| `displaces` | what it removes, shrinks or replaces — or an explicit "adds and displaces nothing" |
| `falsification_test` | the observation that would prove this proposal wrong |
| `fit_argument` | §6's checklist, answered plainly |

## 6. Self-check before submitting

| Question | Must be true |
|---|---|
| All four parts present? | server + adapter + playbook page + brick entry |
| Correct FastMCP? | `from mcp.server.fastmcp import FastMCP` (the SDK's bundled one) |
| Is it in §2? | if yes, you have named what the existing capability fails to do, with evidence |
| Does it declare what it needs? | `gpu_tenant`, `ports`, `network`, `requires_services`, disk |
| Is it local-only? | no cloud endpoints, no keys |
| Is it thin? | no SDK/lifetime/parsing code in the adapter; imports from `./mcp-client` |
| Does it stay out of the always-on prompt? | usage taught via a playbook page |
| Is its data honest? | reference material → a registry line, never an embedding |
| Which lens is it? | **Lens A** (builder-side, zero runtime cost) or **Lens B** (a limb Eve calls, taxed every turn) |
| Would it pass the gate? | conforming to `docs/LEGO_CONTRACT.md` |

## 7. What happens to a submission

It is reviewed against the contract, then the mechanical checks run: brick fields, optional-brick defaults,
adapter thinness, no cloud endpoints, library paths, prompt budget. A piece that fails those **fails the build**
— so a proposal that cannot say how it satisfies §6 is not ready to submit.

Two recent rounds of outside proposals have been reviewed against the running system rather than against the
text. Findings are recorded in `docs/audits/2026-09-26-gemini-brick-proposals-review.md` and
`docs/audits/2026-09-27-gemini-architecture-review.md`, and the outcomes are worth knowing before you write:

- **Three of four bricks in the first round described capabilities EMPIRE already had** — because the handoff
  carried the contract and no inventory. That is what §2 exists to prevent.
- **Mechanisms travelled well; technologies did not.** Every proposal correctly identified a real problem class
  (path containment, retry/quarantine, reuse ranking) and then attached a second stack to it (a broker, a
  second vector store, a second ASR engine, a second job database).
- **One proposal was rejected outright for the right reason**: `fastembed` + `sqlite-vec` would have added a
  second vector store in a different embedding space (384d vs our 768d).

## 8. Evidence standard

1. **No unsourced claim.** Anything asserted as fact needs a link we can open, dated. An upstream CVE or
   benchmark quoted without a checkable source is a hypothesis, and a hypothesis cannot justify a change.
   Two runs cited specific MCP path-traversal CVEs as their primary justification; neither could be verified
   here, and the containment work stood on its own merit anyway.
2. **Measure before recommending.** State the measurement that would **falsify** your proposal. If you have
   none, say you have none.
3. **Quantify cost** in this system's units (§3): prompt tokens, VRAM, disk, re-embed time, migration risk,
   review time.
4. **Prefer the smallest change that can be measured.** A one-line fix with a test beats an architecture.
5. **A clean "nothing here fits" is a good answer.** It is more useful than a stretch, and it is recorded.

## 9. Corrections from outside proposals (each seen at least twice)

1. **Declared services are not "external daemons".** MCP servers are stdio-only and expose no ports. Postgres
   (5432), PocketBase (8090), the frontend (8080), Ollama (11434) and Speaches (8000) are documented, admitted
   services — the memory store among them. Do not propose removing them as "violating the zero-port rule".
2. **Use the FastMCP this repo uses:** `from mcp.server.fastmcp import FastMCP`. Code written against the
   standalone `fastmcp` package (`mask_error_details`, `from fastmcp.exceptions import ToolError`) does not run
   here as written — three submissions have now arrived that way.
3. **Creation vs modification.** A *new* artifact arrives complete and runnable (all four parts). An *existing*
   file is changed by the smallest verifiable edit, never a wholesale rewrite — this project has lost work to
   exactly that. "Always emit the full file" is right for new bricks and wrong for edits.
4. **A defaulted containment root is not containment.** Do not pass `process.cwd()` as the jail root; declare
   explicit roots in the brick's env.
5. **Payloads are an attack surface too.** A tool that canonicalises its own path arguments is still
   unauthorised if a free-form payload can carry a path through it.

And the one that matters most: **propose mechanisms, not technologies.** Name the problem in EMPIRE's
vocabulary (path jailing, retry/quarantine state, reuse ranking, staged approval) — the gate and §2 will tell
you whether we already have it, and in what form.

## 10. Why this shape exists

Three times in this project, "these look alike, merge them" turned out to be wrong when measured (a routing pair
sharing 0 lines; three guide docs sharing 0–1; the one "dead" file being the recipe for a 20 GB corpus).
EMPIRE is coherent but was grown piece by piece. The contract's job is to make the next piece attach cleanly
rather than add a fourth way of doing something — which is why §1 says *reject* more often than it says
*propose*, and why §2 comes before §5.

## 11. Research mode (when the goal is a survey, not a brick)

Give the model this file plus `docs/GEMINI_RESEARCH_BRIEF.md` and `docs/DOC_MAP.md` (the document index), and
ask for:

1. **at most three** proposals, each aimed at a numbered item in §4 — plus
2. **explicit rejections**: what it considered and dropped, with reasons (often the most valuable part), and
3. a one-paragraph answer to: *"if nothing here justifies new work, say so and say what would change your mind."*

Then stop. A conforming brick is the entry ticket, never the argument.



