# WORK PLAN — everything proposed, in execution order

Single list of all outstanding work, ordered by one rule: **fix what exists before adding what does not, and
measure before adopting.** Status: `DONE` · `NEXT` · `TODO` · `WAITING` (owner decision) · `GATED` (precondition).

Consolidates: the audit→contract programme, the Lens A/Lens B surveys, the memory-curation work, and three rounds
of outside proposals reviewed in `docs/audits/2026-09-27-gemini-architecture-review.md`.

## P1 — Canonical path jailing  → **DONE** (2026-09-27)

- **Shipped:** `pipeline/paths.py` (`resolve_within` / `is_within`) applied to `mcp/cognee_mcp.py`,
  `mcp/work_order_mcp.py`, `mcp/workbench_mcp.py` and the docling staging output. 28 tests across
  `tests/test_paths.py` and `tests/test_mcp_path_jailing.py`, all green (suite 625).
- **Two live holes were closed, not hypothetical ones:** `cognee_ingest_mock_file` had **no containment at all**
  (any `.json`/`.md` on the machine could be read and pushed into graph memory), and `docling_convert` wrote
  Markdown to **any path the model named**, with `mkdir(parents=True)`.
- **Not at `mcp/lib/security.py`,** as outside advice suggested: this repo's top-level `mcp/` collides with the MCP
  SDK's own `mcp` package, so that import would resolve inside the SDK. `pipeline/` is the real package home.

- **Why:** some servers call `.resolve()`, others do not, and **nothing enforces `is_relative_to(root)`** across
  the tool surface — including any Docker mount path. Independently identified by both reviewers.
- **Shape:** one helper (`mcp/lib/security.py`) exposing `resolve_within(raw, root)`; apply it to every
  path-taking tool (`cognee_mcp`, `work_order_mcp`, `docling_mcp`, `browser_local_mcp`, workbench/active-tools).
- **Acceptance:** a test per server proving `..\..\Windows\System32\config\SAM` **and** a symlink escape are
  refused while legitimate paths still work.
- **Cost:** no new dependency. **Risk:** a legitimate path the tests miss gets refused — so the tests come first.

## P2 — Error discipline, decided once  → **DONE** (2026-09-27)

- **Decision:** tool-call failures return `{ok: false, error}`; exceptions remain correct for **startup/config**
  failures, where refusing to boot is the desired behaviour. `pocketbase_mcp._require_env` is the model case — a
  missing credential must be loud, not a silent default.
- **Audit:** every `raise` in `mcp/*.py` inspected. `wiki_mcp`'s two `mode` validations were raising and are now
  returned (`{ok:false,error,mode}`); the only remaining raise is the credential guard. No third style anywhere.

`ToolError` is never used in `mcp/*.py`; the contract is met today by structured returns. Decide once (SDK's
`ToolError` vs `{ok:false,error}` only), apply uniformly, and record it in `OPERATING_CONTRACT.md` §5 so the next
brick copies rather than inventing a third style.

## P3 — Retry schedule + quarantine  → **DONE** (2026-09-27)

- **Shipped:** migration `1700000003_ingestion_job_retries.js` (adds `retry_count`, `max_retries`, `next_run_at`,
  `failure_reason`, and `dead_letter` to the status vocabulary) · `pipeline/job_schedule.py` (pure policy, 21 tests,
  exponential-with-jitter expressed as an *absolute timestamp* because a durable schedule must outlive its process)
  · wired into `pipeline/ingest_local.py` · `scripts/requeue-stale-jobs.py` behind the existing
  `cleanup-stale-ingestion-jobs.ps1` command.
- **Verified against the live database,** not assumed: migration applied, `dead_letter` + all four fields present,
  and the 14 rows stuck in `running` were requeued to `pending` with jittered `next_run_at` values (16:30:06–16:30:09
  rather than in lockstep). `running` is now 0 of 544.
- **Deliberately a script, not a Toolbelt tool** (Lens B discipline): an operator path on CPU, and Eve can already
  act on these rows through the generic `pb_update_record` — a new limb would have cost her prompt budget.

- **Why:** retries are ad-hoc in-process sleeps (fixed 15 s in `ingest_workbench.py`); no `next_run_at`, no
  terminal state. We already use exponential jitter for LLM calls — the technique exists, the durable schedule
  does not.
- **Shape:** extend PocketBase `ingestion_jobs` with `retry_count`, `max_retries`, `next_run_at`, `last_error`,
  `failure_reason` and a `dead_letter` status; a review tool/script for quarantined rows; cleanup learns
  *stuck* ≠ *failed*.
- **Not:** a new queue database (that would be a second home for job state).

## P4 — Memory curation rebuild  → **WAITING (prune sign-off)**

Strip the `nlm*` +55 bonus and add duplicate/residue guards in `scripts/optimize_eve_memory.py`; rebuild
`eve_core` from `config/foundation.json`; then prove it with a recall test that names `source_file`. Measured
baseline: 8 registered / 37 reference / 21 forbidden / 9 unregistered of 75. Pruning needs explicit approval.

## P5 — Rerank expansion (8 → ~50 real cases)  → TODO

Both backends score 6/8 on the same eight synthetic cases. Harvest **real queries** (`eve-audit/eve-trace.jsonl`
with `EMPIRE_TRACE=1`, plus workbench chat history), re-run both backends, and either justify reranking or drop it
permanently. Best idea to come out of the outside review.

## P6 — Recipe memory as a dataset  → TODO

Episodic "problem → root cause → fix" memory as a **Cognee dataset** with `store_recipe` / `find_recipe` under the
propose→confirm path. Explicitly **not** sqlite-vec/FastEmbed (second store, different embedding space).

## P7 — Usage-frequency tie-break  → TODO (after P6)

`hit_count` + `last_applied_at` as a tie-break *after* similarity. Stored in a **sidecar table we own** — never by
altering Cognee's tables, which its own migrations own and which the 1.6.1 upgrade will rewrite.

## P8 — Batch transcriber brick  → TODO (after P3)

89 files / 923.6 MB measured; **one file is 0 KB**, so skip-invalid is mandatory. First step is to verify the
Speaches `:8000` transcription endpoint (down at review time — the premise is unmeasured). The brick must declare
`requires_services: speaches:8000`, and it needs P3 to survive partial failures.

## P9 — Structural code reach  → GATED

Tree-sitter/`ast-grep` needs real source trees. Future harvests can preserve directory trees; the *existing*
flattened corpora need a re-clone from recorded source URLs, and `read_active_tool` + `LEGO_INDEX.md` are built
around the flat form.

## P10 — Version debt  → TODO, one item WAITING

cognee 1.4.0 → 1.6.1 (runbook `docs/UPGRADE_COGNEE.md`; its backup precondition is **now met** — first verified
restic snapshot 2026-09-26 — the Postgres dump is still its own step) · PocketBase 0.28.4 → 0.40.4 (a migration)
· **2.6 GB dormant legacy store on `V:\Cognee`: keep or reclaim — owner call.**

## P11 — Lens B measurement: document format census  → TODO

Which formats actually fail today? That measurement gates OCR (`surya`), `marker` and `markitdown`. Without it, a
document brick is a guess.

## P12 — Carries and remaining Lens A

Index the new documents in `DOC_MAP.md` · reconcile the dataset inventory (`--with-data`) · `new-brick.ps1`
scaffold · one live MCP wrapper call · `promptfoo`/`inspect_ai` (behavioural eval) · `hyperfine`/`py-spy`/`memray`
(measurement trio) · `jscpd` (clone detection) · `VectorChord`/`pgvectorscale` (conditional on a rebuild).

## Owner decisions outstanding

1. **P4 prune sign-off** — what may be removed from `eve_core`.
2. **P10 keep-or-reclaim** the 2.6 GB legacy store on `V:`.
3. **Escrow the restic password** (`%LOCALAPPDATA%\EMPIRE\restic-pass.txt`) somewhere physical — losing it loses
   every backup.
4. **Reload Cursor's MCP servers** so the PocketBase hands use the rotated password.
5. **Rotate the Weaviate key** if the wiki stack ever returns (it was live in a public repo).

## Already automated (so it does not depend on memory)

`mechanic-green` runs unit tests, capability governance, `check-legos`, `check-foundation` (advisory), infra checks
(deptry/ruff/gitleaks, advisory), the wiki battery, the UI harness, `verify-stack` and `audit-empire` ·
`pre-commit` installed with both hooks · container images pinned by digest · **LEGO blueprint auto-synced to the
Desktop with rolling backups** (`scripts/sync-lego-blueprint.ps1`; verified — keeps the newest 3, prunes the
oldest, and warns when a structural inventory has changed since the document was written).

