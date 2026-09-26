# Infra adoption — first Lens A tools installed and run

Date: 2026-09-26. Scope: the highest-upside rows of `docs/LENS_A_LANDSCAPE.md`, adopted and **executed**,
not just recommended. Everything here is dev-time only — no prompt tokens, no VRAM, no limb, nothing Eve
can reach.

## Installed

| Tool | Version | How | Why it was first |
|---|---|---|---|
| `deptry` | 0.25.1 | `pip` (venv) | the class we were bitten by hours earlier: **docling installed but undeclared** |
| `ruff` | 0.16.9 | `pip` (venv) | our largest code surface had no lint baseline at all |
| `pytest-cov` | 7.1.0 | `pip` (venv) | 598 tests, no coverage map |
| `gitleaks` | 8.x | `winget` | a written policy ("secrets never in memory, any tier") with **no mechanism** |
| `restic` | 0.19.1 | `winget` | we hold a vault **manifest**, not a copy of the vault |

Pinned in `requirements-dev.txt`. `scripts/infra-checks.ps1` runs the three that produce findings and is
wired into `mechanic-green` as an **advisory** step.

## Findings — deptry: 51 issues

Beyond the known docling hole, three classes appeared:

- **`DEP001` missing from declarations**: `gliner` (used by `pipeline/wiki_entity_guard.py`) and
  `optimize_eve_memory` (imported by `scripts/ingest_nlm_batch.py`). A fresh setup breaks these paths.
  **Open question for the Architect:** the wiki is halted per AGENTS.md — is `gliner` intentionally absent,
  or is this drift? Not fixed silently.
- **`DEP003` imported but only transitive** (fragile — a parent package update removes them): `playwright`,
  `tenacity`, `psutil`, `sentence_transformers`, `torch`, `yaml`. Note `sentence_transformers`/`torch` are
  used by `pipeline/retrieval_rerank.py`, which bears on the FlashRank question: **a reranking stage may
  already exist** in the repo and needs reading before any new reranker is considered.
- **`DEP002` declared but unused in our code**: `pydantic`, `psycopg2-binary`, `asyncpg`, `pgvector`,
  `transformers`, `matplotlib`. Some of these are legitimately declared for Cognee's own use — DEP002 will
  need a documented ignore list rather than blanket action.

## Findings — ruff: not clean, and that is the point

Findings grouped by rule (report at `eve-audit/ruff.txt`): regex-flag aliases (~162), unsorted imports (78),
printf-style formatting (76), **blind `except` (67)**, unused unpacked variables (63), **`try/except: pass`
(49)**, collapsible ifs (25), unused imports (25), **`subprocess.run` without `check` (22)**, unused noqa
(19). The blind-except and silent-pass counts are the ones worth acting on eventually: they are exactly how
a defect becomes invisible. Report-only for now — a first lint pass must not be a gate.

## Findings — gitleaks: 79 findings, triaged by rule and file

Rules: 54 `generic-api-key`, 19 `curl-auth-header`, 5 `curl-auth-user`, 1 `jwt`.

| File | Count | Verdict |
|---|---|---|
| `docs/reference/*` (Gumloop, Cursor, FlutterFlow, Dify, Magic Patterns guides) | ~30 | **False positives** — vendor documentation quoting upstream examples. Allowlisted in `.gitleaks.toml` with a stated reason |
| `.cursor/mcp.full.json` | 15 | **UNRESOLVED — needs the Architect.** Tracked in HEAD, present on disk, **not** gitignored, and the same values reoccur across many commits. If any key is real: rotate first, then purge history (`git-filter-repo`, already on the Lens A list) |
| `tmp/diag_following_gql.py`, `tmp/diag_following_like.py` | 28 | Files are now **gitignored and untracked** — these findings live in *history* only. Same purge question, lower immediacy |
| `data/practice/my-first-memory.md` | 1 | single finding, worth a look (practice fixture) |

No secret values are reproduced anywhere in this record — the scan was run with `--redact`.

## Deliberately not done yet

- **`restic` is installed but no repository is initialised** — that needs a target decision from the
  Architect. A backup on the same physical device it protects is not a backup, so the obvious default
  (`I:`, which also hosts the VHDX file) is a compromise worth stating rather than assuming. A backup that
  has never been restored from is not a backup either; the restore test is part of the acceptance.
- `trivy`/`syft` (two `:latest` images), `pre-commit` (wiring the above into habits), coverage run,
  `hyperfine`/`py-spy`/`memray`, `jscpd` — next tranche, in that order.
