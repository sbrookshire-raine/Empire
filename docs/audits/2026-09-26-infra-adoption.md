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

## ADDENDUM 2026-09-26 — public-repo credential exposure (found by gitleaks, then by `gh repo view`)

The canonical repo `sbrookshire-raine/Empire` is **PUBLIC** (`isPrivate: false`). That turns the
gitleaks triage from "probably benign" into a real exposure:

- `.cursor/mcp.json` and `.cursor/mcp.full.json` carried `empire-wiki-scout.WEAVIATE_API_KEY` (36 chars,
  high-entropy — the classifier could not call it a placeholder) and `empire-pocketbase.POCKETBASE_ADMIN_*`
  credentials, committed across ~190 commits of history. Anyone who scraped the repo has them.
- **Action taken:** both files untracked (`git rm --cached`), added to `.gitignore` with the reason, and
  replaced by sanitized `.cursor/mcp.example.json` / `.cursor/mcp.full.example.json` with every
  key/token/secret/password value set to `REPLACE_ME` — verified programmatically: **0 high-entropy
  values remain** in the examples.
- **Action still required (Architect):** *rotate* the Weaviate key and the PocketBase admin password.
  The history is already public, so untracking does not undo it — rotation is the only effective remedy.
  Purging history (`git-filter-repo`) is possible but rewrites a public repo; rotate first, then decide.

## Addendum — backups exist now (restic)

- Repository: `I:\EMPIRE_BACKUP\restic` on the **T7 Shield (I:)**, chosen by evidence rather than
  assumption: `Get-Volume` shows I: as a separate physical device from C:, 3725.7 GB with 2327.6 GB free.
  Caveat stated, not hidden: I: is **exFAT** (no journaling), which is exactly why the restore test is
  mandatory rather than optional.
- Password: `%LOCALAPPDATA%\EMPIRE\restic-pass.txt` — outside the repo, never committed. Losing it means
  losing every backup: that file is now the system's real single point of failure and should be escrowed
  somewhere physical.
- Runner: `scripts/backup-empire.ps1` (with `-VerifyRestore`), first snapshot of `C:\Empire_Workbench`.
- Acceptance rule recorded: a backup that has never been restored from is not a backup.

## Tranche 2 (2026-09-26 late) — pre-commit, image pinning, vuln scan, coverage

**pre-commit (the wiring).** `pre-commit 4.6.2` installed. `.pre-commit-config.yaml` holds **one** local
hook that calls `scripts/infra-checks.ps1` — the same script `mechanic-green` runs, so there is a single
source of truth for how each tool is invoked (binary resolution, report paths, advisory semantics).
Hook installed at `.git/hooks/pre-commit` and verified: `pre-commit run --all-files` → *"EMPIRE infra
checks (deptry, ruff, gitleaks - advisory) ... Passed"*. Advisory, so it reports without blocking;
`git commit --no-verify` for WIP.

**Images pinned by digest (the real fix for `:latest`).**

| Image | Digest | File |
|---|---|---|
| `searxng/searxng` | `sha256:5286edb3…a6dfb6` | `scripts/start-searxng.ps1` |
| `ghcr.io/speaches-ai/speaches` | `sha256:21e3df06…53ef8` | `scripts/start-voice.ps1` |
| `pgvector/pgvector` | `sha256:1d533553…79f0fb` | `docker-compose.yml` |

Trade-off stated rather than hidden: **a pin freezes known CVEs too.** It must be paired with a periodic
comparison of the pinned digest against current upstream, or we trade "silent change" for "silent rot".

**First vulnerability scan ever (trivy).**

| Image | HIGH + CRITICAL | Detail |
|---|---|---|
| `searxng/searxng` | **0** | clean at those severities |
| `speaches` (voice, :8000) | **47 — 2 CRITICAL, 45 HIGH** | pillow ×13, cryptography ×4, urllib3 ×4, starlette ×3 |

Risk framing, not alarm: Speaches binds `127.0.0.1` only, so this is **not remote-exploitable today**. It
matters if :8000 is ever exposed, and it matters for hostile *input* (media parsed by pillow/starlette).
Recommendation: try a newer upstream image before deciding anything — and note that the digest pin now
freezes this vulnerable build in place until someone updates it deliberately. SBOMs captured with syft
(`eve-audit/sbom-*.json`) so the inventory exists when that happens.

**First coverage map ever.** `598 passed` in 43.61 s, **TOTAL 32%** (18,603 statements, 12,615 never
executed in-process). The caveat matters more than the number: scripts the gate runs as *subprocesses*
(verify-stack, the wiki battery, vault-manifest) report **0% by construction** — coverage cannot see into
a child process. So 32% understates real execution and overstates the gap in `pipeline/` and `mcp/`.
Report: `eve-audit/coverage.txt`.

**Correction to a Lens B recommendation.** `pipeline/retrieval_rerank.py` **already exists** and is a
reranking A/B harness: lexical token-overlap scorer always available, `sentence_transformers.CrossEncoder`
optional behind `EMPIRE_RERANK_MODEL`, cached, fixtures in `data/eval/retrieval`, and explicitly *"eval
only — never swaps production Cognee embeds (nomic)"*. My FlashRank recommendation was therefore wrong in
an important way: this is not a missing capability, it is an **existing harness that was never run**. The
next step is to run the A/B we already own, not to adopt a new library.
