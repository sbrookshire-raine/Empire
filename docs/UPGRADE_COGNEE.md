# Upgrading Cognee — runbook (prepared, deliberately not yet executed)

**Why upgrade at all.** `1.4.0 → 1.6.1` buys, in upstream's own words: `validate()` (cross-check a
dataset's graph and vector stores for integrity), `report()` (graph insight report), *"Dataset Indexing
& Search Relevance"* (1.5.0.dev4), *"interrupted uploads can resume and large files are processed
faster"* (1.5.3), and *"keyless workflows"* (1.6.0). Read-only data-set inventory (`cognee.datasets`)
and `prune` already exist in 1.4.0, so **the upgrade is an improvement, not a prerequisite** — nothing
blocks curation while we wait.

**Why this is a runbook and not a shell command I ran.** Our memory store is the one asset where a
half-finished change is worse than an old version:

- `run_migrations()` alters the Postgres schema. **Re-pinning the package does not undo that.**
- Three of our files touch Cognee directly: `mcp/cognee_mcp.py` (five tools), `pipeline/cognee_subprocess.py`
  (worker operations), `config/cognee.env` (providers, batching, graph prompt).
- Dependency drift is real: the upgrade can pull newer `litellm` / `openai` / `pydantic`, which our
  adapters and the MCP SDK 1.28.1 also depend on.

## Preconditions (all of them, in this order)

1. **Postgres backup of the memory store** — the durable knowledge lives there:
   `docker exec empire-cognee-postgres pg_dump -U <user> <db> > I:\EMPIRE_DATA\backups\cognee-<date>.sql`
2. **Graph store snapshot** — `V:\Cognee` (the T7 VHDX). A copy or VHDX snapshot; no snapshot, no upgrade.
3. **Checkpoint branch** — `pre-upgrade-20260926` exists on origin as of 2026-09-26.
4. **A quiet window** — no ingest, no `optimize-eve-memory` run in flight.

## Steps

| # | Action | Verify |
|---|---|---|
| 1 | Backups from the preconditions | files exist, non-trivial size |
| 2 | `.\venv\Scripts\python.exe -m pip install "cognee[postgres-binary]==1.6.1"` | `pip show cognee` → 1.6.1; note every other package that moved |
| 3 | Restart the stack (`Stop-EMPIRE.bat` → `Start-EMPIRE.bat`) | `audit-empire.py` contract satisfied |
| 4 | Apply migrations via `cognee.run_migrations()` | completes without error; record output |
| 5 | Smoke: list datasets, then remember → recall a scratch marker on a throwaway dataset | marker recalled, dataset then pruned |
| 6 | `python scripts/check-legos.py` and `mechanic-green -Full` | both green (578+ tests) |
| 7 | Expose the new capability: `validate()` and dataset listing in `mcp/cognee_mcp.py` | playbook limb updated, coverage `ok` |
| 8 | Update `docs/TOOL_VERSIONS.md` and the contract's placement/version notes | dated row |

## Rollback

1. Re-pin and reinstall: `pip install "cognee[postgres-binary]==1.4.0"`.
2. **If step 4 ran, restore the Postgres backup** — the package rollback alone is not enough.
3. Restore `V:\Cognee` from the snapshot if the graph store was touched.
4. Re-run `audit-empire.py` + gate; record what broke and why in `docs/TOOL_VERSIONS.md`.

## Do at the same time

Our own logs report `auth posture: authentication=required, multi_tenant=enabled (default (no env vars
set))`. For a single-user local install that is probably the wrong posture — Cognee's warning line names
the switch (`ENABLE_BACKEND_ACCESS_CONTROL=false`). Check `config/cognee.env` during step 3, before
anything is written.

## After the upgrade, the curation that was waiting

`cognee.datasets` (already available) → per-dataset inventory → deliberate `Foundation/` set → recall
test → `prune`/`forget` test data and rebuild `eve_memory` curated-only. Only then does `validate()` get
run on the survivor, to prove the dataset is internally consistent.
