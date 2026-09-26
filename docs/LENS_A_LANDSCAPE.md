# Lens A landscape — infrastructure that makes EMPIRE run better and is never called by Eve

Surveyed 2026-09-26 via authenticated `gh search repos` on this machine. Stars / last push / licence are as
observed that day — **they age, re-check before acting**. Two queries returned name collisions (`restic`,
`inspect_ai`) and were re-run scoped to their owners; the corrected numbers are what appear here.

Why this document exists: `docs/GAP_LENSES.md` separated builder instruments from Eve's runtime capability
because their costs are not comparable. This is the deep pass on the first lens — tools that are **adopted
once and cost nothing forever after**: no prompt tokens, no VRAM, no limbs, no new services Eve must reach.
The criterion for inclusion is not "popular"; it is **our recorded defect class**, named per row.

Judged for adoption only where a defect class already bit us.

## 1. Supply chain — what we depend on without declaring

| Candidate | Evidence | Defect class | Our recorded instance |
|---|---|---|---|
| `osprey-oss/deptry` | 1,484★ MIT, 2026-09-26 | undeclared / unused / transitive deps | **docling was installed but absent from `requirements.txt`** (found by hand 2026-09-26); a fresh setup would have silently lost PDF conversion |
| `pypa/pip-audit` | 1,370★ Apache-2.0, 2026-09-26 | known CVEs in installed packages | no dependency audit has ever run on this venv |
| `gitleaks/gitleaks` | **29,497★ MIT**, 2026-09-23 | secrets committed or stored on disk | our policy says *secrets never in memory, in any tier* — and **no mechanism enforces it** anywhere, including the 14,652-file vault. `betterleaks/betterleaks` (2,033★ MIT, 2026-09-26) is a rising fork worth watching |

## 2. Code hygiene — defects in what we write

| Candidate | Evidence | Defect class | Our recorded instance |
|---|---|---|---|
| `astral-sh/ruff` | **49,803★ MIT**, 2026-09-26 (Rust, fast) | lint + format, one tool | Python is our largest surface and has no enforced style/lint baseline |
| `PyCQA/bandit` | 8,286★ Apache-2.0, 2026-09-21 | insecure Python patterns | we write subprocess, path and SQL code by hand |
| `semgrep/semgrep` | 16,773★ **LGPL-2.1**, 2026-09-25 | pattern-based bug variants, custom rules | would let us encode rules like "no cloud endpoint", matching `check-legos` at the code level |
| `jendrikseipp/vulture` | 4,823★ MIT, 2026-09-25 | dead code | **three** "this looks dead" calls reversed by measurement |
| `kucherenko/jscpd` | **6,275★ MIT**, 2026-09-26 (Rust engine, 220+ langs) | copy/paste clones | we consolidated **7 near-identical MCP wrappers** into one client — the clone class that produced them has no detector |

## 3. Test strength — whether the arbiter can actually see defects

| Candidate | Evidence | Defect class | Our recorded instance |
|---|---|---|---|
| `boxed/mutmut` | 1,453★ BSD-3, 2026-09-12 | tests that pass but would not catch a defect | the gate is the arbiter (598 tests, 38 s); its *strength* has never been measured. A rotted harness sat unrun until 2026-09-24 |
| `HypothesisWorks/hypothesis` | 9,021★, 2026-09-25 | property-based testing | our parsers/decoders (encoding chain, CRLF hash stability, graph-payload sanitisers) are ideal property targets |
| `pytest-dev/pytest-cov` | 2,065★ MIT, 2026-09-21 | uncovered paths | 598 tests, no coverage map — we cannot say which code never runs |

## 4. Measurement — the class of question we keep answering by hand

| Candidate | Evidence | Defect class | Our recorded instance |
|---|---|---|---|
| `sharkdp/hyperfine` | **28,908★ Apache-2.0**, 2026-04-30 | CLI/startup benchmarking with statistics | cold start 75 s → 24.6 s was measured by hand; nothing makes it repeatable |
| `benfred/py-spy` | 15,516★ MIT, 2026-08-14 | sampling profiler, no restart needed | the MCP process investigation (16 → 2 processes) was done by counting, not profiling |
| `bloomberg/memray` (+ `pytest-memray`) | 15,240★ Apache-2.0, 2026-09-23 (+424★) | Python memory profiling | python footprint 862 MB → 412 MB was inferred from process counts, not measured |

## 5. Text and data repair — the corpus keeps surprising us

| Candidate | Evidence | Defect class | Our recorded instance |
|---|---|---|---|
| `rspeer/python-ftfy` | 4,065★, pushed 2024-10-30 (stable, old) | mojibake / Unicode glitches **after the fact** | our decode chain (UTF-8 → cp1252 → latin-1) recovered 66 files; ftfy repairs the text *content* the chain can only guess at |
| `pkolaczk/fclones` | 2,950★ MIT, 2025-03-03 (Rust) | duplicate files, fast | vault duplicates still unswept (see `czkawka` 33,742★ / `text-dedup` 762★ in the OSS audit) |


## 6. Backup and recovery — the largest gap found, and the least glamorous

We have a **manifest** of the vault (14,652 files / 2,814.8 MB / 0 errors) — that is proof of what exists,
not a copy of it. The live store is a Postgres container plus `V:\Cognee`, and the workbench holds the only
copy of everything else. A disk failure currently costs all of it.

| Candidate | Evidence | Fit |
|---|---|---|
| `restic/restic` | **36,272★ BSD-2**, 2026-09-25 — fast, encrypted, deduplicating, snapshot-based | **Recommended.** Single binary, no service, no port, works against local/VHDX targets. Deduplication matters at 2.8 GB of mostly-markdown vault |
| `borgbackup/borg` | 13,775★, 2026-09-26 — deduplicating archiver with encryption | Equivalent capability; heavier on Windows without WSL. Second choice |

Cost: dev-time only. Nothing in Eve's runtime changes. This is the one item here that protects against a loss
that is otherwise unrecoverable.

## 7. Container and image hygiene — our unpinned supply chain

| Candidate | Evidence | Defect class | Our recorded instance |
|---|---|---|---|
| `aquasecurity/trivy` | **38,085★ Apache-2.0**, 2026-09-25 | vulns + misconfig + secrets + SBOM in one tool | two images run on `:latest` (`searxng/searxng`, `ghcr.io/speaches-ai/speaches:latest-cpu`) — a pull can change behaviour with nothing measuring it |
| `anchore/syft` | 9,613★ Apache-2.0, 2026-09-25 | SBOM generation | we cannot say what is inside the images we run |
| `wagoodman/dive` | 54,611★ MIT, 2025-12-15 | image layer inspection | useful when a pulled image surprises us |
| `hadolint/hadolint` | 12,431★ **GPL-3.0**, 2026-09-25 | Dockerfile linting | **conditional** — we consume images, we do not build them; only relevant if that changes |

## 8. Making all of it automatic

| Candidate | Evidence | Fit |
|---|---|---|
| `pre-commit/pre-commit` | 15,595★ MIT, 2026-08-17 | The mechanism that turns §1–§4 from intentions into habits. Same pattern that already works here: `mechanic-green`, `check-legos`, `audit-empire` are wired, so they run. Tools not wired are tools not used |
| `newren/git-filter-repo` | 13,333★, 2026-07-09 | History rewriting when a repo-scale mistake needs undoing; relevant given how many checkpoint branches we now carry |

## 9. Reading our own traces

| Candidate | Evidence | Fit |
|---|---|---|
| `tstack/lnav` | 10,703★ BSD-2, 2026-09-26 | Navigate `eve-trace.jsonl` and audit logs interactively instead of hand-parsing. Dev-time only — she never sees it |

## 10. Evaluating Eve's behaviour without taxing her

| Candidate | Evidence | Fit |
|---|---|---|
| `promptfoo/promptfoo` | **25,477★ MIT**, 2026-09-26 | Test prompts, agents and RAGs declaratively, with red-teaming. **Replaces the hand-run bench** (8/8 baseline, 4/8 live behavioural) with a repeatable suite |
| `UKGovernmentBEIS/inspect_ai` | 2,862★ MIT, 2026-09-26 (+ `inspect_evals` 683★) | Framework from the UK AI Security Institute; more rigorous, more ceremony |

Both are **Lens A**: they exercise her from outside, at dev time. No prompt tokens, no limbs, no VRAM.

## 11. Vector infrastructure without a second store

| Candidate | Evidence | Fit |
|---|---|---|
| `supervc-stack/VectorChord` | 1,802★, 2026-08-06 — pgvector successor + `VectorChord-bm25` (379★) | Improves **the store we already run** — faster, disk-friendlier ANN, plus native BM25 for hybrid retrieval |
| `timescale/pgvectorscale` | 3,135★ PostgreSQL licence, 2026-09-07 — DiskANN | Complements pgvector for performance at scale |

Both are Postgres **extensions**, so adoption means rebuilding the container image and re-running the recall
test. Conditional, but this is the legitimate way to chase recall speed/quality at the infrastructure layer —
distinct from the "second memory store" proposals that were rejected.

## Adoption shortlist (small → large, all runtime-free)

| # | Tool | Why first | Wire into |
|---|---|---|---|
| 1 | **gitleaks** | enforces a written policy that currently has no mechanism | pre-commit + a repo/vault scan |
| 2 | **deptry** | proven today: it would have caught the docling hole | `mechanic-green` |
| 3 | **restic** | the only item preventing an unrecoverable loss | scheduled job, verified restore |
| 4 | **trivy** + **syft** | two `:latest` images are unmeasured supply chain | a stack audit step |
| 5 | **ruff** (+ **bandit** or **semgrep**) | our largest code surface has no enforced baseline | pre-commit |
| 6 | **pre-commit** | makes 1–5 automatic instead of remembered | repo root |
| 7 | **promptfoo** | turns Eve's behavioural bench into a suite | `mechanic-green` (dev-side) |
| 8 | hyperfine + py-spy + memray | the measurement trio for questions we answer by hand | on demand |
| 9 | jscpd | detector for the clone class that produced 7 wrappers | reported measurement |
| 10 | VectorChord / pgvectorscale | infra-level recall performance | rebuild + recall test |

## Coverage honesty

**Not surveyed here** (so this is a landscape, not a claim of completeness): `uv`/`pip-tools` for lockfiles and
resolution, prose/link tooling (`vale`, `typos`, `markdownlint`, `lychee` — its stats still unverified),
Windows-specific file/disk utilities, service supervision (`nssm`, `winsw`), and scheduler options for the
automation in rows 1–4. Also not covered: anything requiring a runtime daemon, since that would be Lens B by
definition.

**Licence notes carried forward:** semgrep LGPL-2.1, hadolint GPL-3.0, rmlint GPL-3.0, universal-ctags GPL-2.0.
All fine as locally-run developer tools; each is a consideration if ever bundled or redistributed.
