# Review — Gemini architectural chat ("LEGO architecture, RabbitMQ, DLX, episodic memory")

Date: 2026-09-27 · Reviewer: Cursor (mechanic) · Status: **review + plan; no code changed yet.**
Source: an externally generated chat transcript supplied by the Architect (message-bus/microservices patterns,
then a "EMPIRE-compliant" retrofit of those patterns, then advice for the coding model).

Every claim below was checked against the running repository, not assessed in the abstract.

## Verdict in one line

The chat is **most useful where it names missing *mechanisms* and least useful where it proposes *technology*** —
and its own retrofit is already closer to EMPIRE than its first half. Three of its five "compliant" upgrades are
genuinely absent here; two are things we already do, and one is wrong for this stack in a way that must not be
adopted.

## Already ours (no action; recorded so it is not re-litigated)

| Proposal | Where it already lives |
|---|---|
| Four-part brick rule (server + thin adapter + playbook page + brick JSON) | `docs/LEGO_PROMPT.md` §1, enforced by `scripts/check-legos.py` in the gate |
| "Never propose" list (no cloud API/keys, no undeclared service, no always-on prompt rule, no second copy) | `docs/LEGO_PROMPT.md` §1, `docs/LEGO_CONTRACT.md` |
| Teach capability via demand-loaded playbook, never prompt bloat | `docs/OPERATING_CONTRACT.md` §4; measured prompt budget ~11k/24,576 |
| Structured errors `{ok:false, error}`, no stack traces to the prompt | `docs/OPERATING_CONTRACT.md` §5 (implementation gap noted below) |
| Path canonicalisation on tool inputs | Partial — see gap 1; `work_order_mcp.py` resolves, `cognee_mcp.py` resolves, others do not |

## Wrong for this stack (explicitly rejected — do not adopt)

1. **"No external database daemons (no RabbitMQ, Redis, Pinecone, or Postgres)."** **Postgres is EMPIRE's
   memory store.** It is a *declared service* with a documented port (5432) in `AGENTS.md`, wired into the
   capability admission manifest, and the reason `config/cognee.env` says `DB_PROVIDER=postgres`,
   `VECTOR_DB_PROVIDER=pgvector`. The real rule is narrower and is the one we already follow: **MCP servers are
   stdio-only and expose no ports; services must be declared, documented and admitted.** The chat conflates the
   two, and taking its rule literally would delete our memory layer.
2. **`from fastmcp import FastMCP` / `mask_error_details=True` / `from fastmcp.exceptions import ToolError`.**
   That is the *standalone* `fastmcp` package. Every server here uses the MCP Python SDK's bundled FastMCP:
   `from mcp.server.fastmcp import FastMCP` (verified across `mcp/*.py`). The snippet would not run as written.
3. **"FULL SCRIPTS ONLY: never partial diffs."** Rejected as a universal rule. Our verified practice is small,
   reviewable edits plus a gate; whole-file rewrites are how content gets silently lost (the CRLF/hash incident
   of 2026-09-26 is this project's worked example). It *is* correct for new artifacts — a new brick should arrive
   complete — so it is adopted for creation, not for modification.
4. **Unverified CVEs** (CVE-2025-68143 / CVE-2026-57442) again used as justification. Same standing rule: a
   claim without a checkable source is a hypothesis, not a reason. The containment work stands on its own merit.
5. **`agent/lib/empire-mcp-client`** — our shared client is `agent/lib/mcp-client.ts` (`createEmpireMcpClient`).
   Minor, but a model following the chat literally would create a duplicate client.

## Verified gaps (these are the useful part)

1. **Canonical path jailing is inconsistent.** `cognee_mcp.py` and `work_order_mcp.py` call `.resolve()`;
   several path-taking servers do not, and **nothing enforces `is_relative_to(root)`** anywhere. There is no
   shared helper. This is the same gap flagged as F2 in `docs/GAPS`-era notes, now confirmed by grep. **Real.**
2. **No ranking signal for reuse.** No `hit_count` / `last_applied` / usage weighting exists in memory or
   tooling (`primitive_lookup.py` has field weights, which is a different thing). Recall cannot prefer a
   solution that has worked five times over one that worked once. **Real and unused.**
3. **No terminal-failure state.** Retries exist ad hoc (`MAX_RETRIES = 3` in `scripts/ingest_workbench.py`,
   instructor retries in `cognee_client.py`) and `ingestion_jobs` records exist in PocketBase (with a cleanup
   script for rows stuck in `running`) — but there is **no dead-letter concept**: repeatedly failing work has no
   terminal, reviewable state. **Real.**
4. **`ToolError` is never used** in `mcp/*.py`; our error contract is satisfied today only by structured return
   values. Whether we adopt `ToolError` (in the SDK's namespace) is an open decision, not an obvious win.

## The one idea worth taking seriously, in a different form

**Episodic "solution recipe" memory** (store a verified problem→root-cause→fix; retrieve by similarity) is a good
idea for Eve. The chat's *implementation* is not: `fastembed` + `sqlite-vec` + `BAAI/bge-small-en-v1.5` would be a
**second vector store** with a **different embedding space** (384d vs our nomic 768d), which our one-store rule
and the measured curation findings both reject.

The EMPIRE-compliant form is a **new Cognee dataset plus tools** (`store_recipe` / `find_recipe`), governed by
`docs/MEMORY_GOVERNANCE.md` (propose → confirm, never silent writes), with the usage counter from gap 2 as its
ranking tie-break. Same value, zero new infrastructure, one store.

## Plan to incorporate (phased, smallest verifiable step first)

**Phase 1 — canonical path jailing (do first; ~an hour, no new dependency).**
Add one shared helper (e.g. `mcp/lib/security.py`) exposing `resolve_within(raw, root)` that canonicalises with
`Path.resolve()` and raises a structured, actionable error unless `is_relative_to(root)`. Apply it to every tool
that accepts a path or a Docker mount (`cognee_mcp`, `work_order_mcp`, `docling_mcp`, `browser_local_mcp`, the
workbench/active-tools readers). **Acceptance:** a test per server proving `..\..\Windows\System32\config\SAM`
and a symlink escape are both refused, and that legitimate paths still work. This also closes the open F2 item
and needs no new port, service, or dependency.

**Phase 2 — error discipline, standardised (small).**
Decide once whether `ToolError` (MCP SDK namespace) is used, then make it uniform: Python raises a structured
failure that carries a *reason*, adapters keep returning `{ok:false, error}`. Record the decision in
`OPERATING_CONTRACT.md` §5 so the next brick copies it instead of inventing a third style.

**Phase 3 — terminal failure state (small, in the store we already run).**
Add a `dead_letter` status + `failure_reason` + attempt count to `ingestion_jobs` (PocketBase), and a
`scripts/review-dead-letters.ps1` that lists quarantined rows. `cleanup-stale-ingestion-jobs.ps1` learns the
difference between *stuck* and *failed*. This is the outbox/DLQ value with none of the broker.

**Phase 4 — episodic recipe memory as a dataset (medium; needs a decision, not a dependency).**
Design `eve_recipes` as a Cognee dataset with two tools (`store_recipe`, `find_recipe`), a playbook limb, and the
MEMORY_GOVERNANCE propose/confirm path — then measure it with the repaired rerank harness before trusting it.
Explicitly **not** SQLite/FastEmbed.

**Phase 5 — usage-frequency ranking (medium; depends on Phase 4 for a real target).**
Store `hit_count` + `last_applied_at` and use them as a *tie-break* after similarity, not as a replacement for
it. Where the metadata lives (a sidecar row set vs a PocketBase collection) is a decision to make with the
Phase 4 design, not before.

**Phase 6 — AST validation of generated patches (candidate, gated).**
Tree-sitter/`ast-grep` refusing `(ERROR)`/`(MISSING)` nodes before a patch is written is a good builder-side
safety net, but it is gated on the same de-flattening question as the code-intelligence brick, and it partly
overlaps tools we now run (`ruff`, the gate). Keep on the list; do not start before the precondition is met.

## Corrections to fold into the handoff documents

`docs/LEGO_PROMPT.md` is what a coding or proposing model receives, so the four corrections above belong in it
rather than only in this audit:

1. **Services vs MCP servers.** Add one line: *MCP servers are stdio-only; declared services (Postgres 5432,
  PocketBase 8090, frontend 8080, Ollama 11434, Speaches 8000) are documented and admitted. Never propose
  removing them as "external daemons".*
2. **Which FastMCP.** Add the import we actually use (`from mcp.server.fastmcp import FastMCP`) so snippets do
  not arrive written against the standalone package.
3. **Creation vs modification.** State the rule precisely: new artifacts arrive complete; existing files are
  changed by smallest verifiable edit. This is the one place where the chat's blanket "full scripts only" would
  actively harm the project.
4. **Evidence standard** (already in `GEMINI_RESEARCH_BRIEF.md` §4): carry the same sentence into the brick
  prompt, since this chat cited unverified CVEs as justification a second time.

## Honest note on value

Roughly a third of this transcript is already our contract restated, a third is a retrofit that correctly
rejects its own first half (RabbitMQ → in-process, PostgresSaver → file-backed), and the remaining third names
four mechanisms we genuinely lack. **The mechanism-level items are worth having; the technology-level items are
worth refusing** — which is exactly the pattern this project keeps meeting, and the reason the LEGO gate exists.

