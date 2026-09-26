# Tool versions — measured baseline and upstream watchlist

Measured 2026-09-26 on this machine, with upstream state read from each project's own releases page.
Purpose: make upgrades **deliberate**. A version that moves by accident changes behaviour under Eve
with no checkpoint and no test — which is exactly what the cognee floor pin was risking.

## Baseline vs upstream

| Tool | Ours | Upstream latest | Gap | Action |
|---|---|---|---|---|
| **cognee** | **1.4.0** | **1.6.1** (24 Sep) | 2 minor | **Pinned to `==1.4.0` today.** Upgrade is worth planning: 1.5.0.dev4 "Dataset Indexing & Search Relevance", 1.5.3 "search relevance + interrupted uploads resume", 1.6.0 "keyless workflows" |
| **docling** | 2.115.0 | **2.130.0** (22 Sep) | 15 minor | Worth updating — it converts our PDFs; the gap is mostly PDF/Markdown/docx correctness fixes |
| **PocketBase** | 0.28.4 | **0.40.4** (12 Sep) | 0.28 → 0.40 | **Treat as a migration, not an update**: major-version jump with schema/API changes. Plan + test on a branch |
| **Ollama** | 0.34.3 | 0.34.4 stable (0.40.0-rc0 is Apple-Silicon MLX) | 1 patch | Low urgency; rc is irrelevant to us |
| **MCP Python SDK** | 1.28.1 | (not checked) | — | Check before adding a limb that uses newer transport features |
| Python | 3.11.9 | — | — | Fine; cognee 1.4 is happy here |
| Node / npm | 24.14.1 / 11.11.0 | — | — | Fine for the Eve runtime |
| Docker | 29.8.0 | — | — | Fine |

## Unpinned things (same hazard class as the cognee floor)

| Item | Current | Risk |
|---|---|---|
| `searxng/searxng:latest` | `:latest` | a pull can change search behaviour silently |
| `ghcr.io/speaches-ai/speaches:latest-cpu` | `:latest` | a pull can change voice/STT behaviour silently |
| `pgvector/pgvector:pg16` | major-pinned | acceptable — `pg16` is the boundary that matters |

Recommendation: pin the two `:latest` images to explicit tags (or digests) when voice/search next get
touched, and record the change here. Not urgent, but it is the same failure mode we just closed.

## The unlock: the inventory we thought was missing already exists

Cognee's Python API documents what our MCP limb lacked:

| Capability | API |
|---|---|
| **List / create / fetch / delete datasets** | `cognee.datasets` |
| **Delete data with the unified v1.0 API** | `forget()` |
| **Delete stored data / reset system state** | `prune` |
| **Cross-check a dataset's graph and vector stores for integrity** | `validate()` |
| Graph insight report | `report()` |
| Apply pending schema migrations | `run_migrations()` |
| REST surface | `/api/v1/*` (search history, activities, sessions, provenance delete planning) |

So curation does **not** require inventing an instrument — it requires exposing `cognee.datasets` (read
only, to start) through our limb, or calling it from a script. `validate()` is a bonus: it answers
"is this dataset internally consistent?" before anyone prunes it.

## Storage backends (DuckDB / FalkorDB / pgGraph) — recommendation: do not switch

- Our stack is **Postgres + pgvector** (`pgvector/pgvector:pg16`), with **LanceDB** already present in
  cognee 1.4's dependency set. That is upstream's supported path.
- The community adapters exist (`cognee-community-hybrid-adapter-duckdb`, `-falkor`,
  `cognee-community-graph-adapter-pggraph` — the last explicitly **experimental**).
- **Our bottleneck is memory content, not storage.** Recall is diluted by harvest bulk, not by the
  engine. Swapping backends means a full re-ingest, a schema migration, and unknown failure modes, in
  exchange for a capability we have not shown we lack.
- The improvements we actually want (search relevance, ingestion resume) arrive from **version
  upgrades**, not backend swaps.
- **Condition to revisit:** if recall is still poor *after* curation and an upgrade, then evaluate
  FalkorDB/DuckDB/pgGraph with a measurement, not a preference.

## Upgrade discipline (applies to every row above)

1. Checkpoint branch first (`pre-<tool>-<date>`).
2. Read the release notes for breaking changes; name them in the commit.
3. Update on the branch, run `mechanic-green` (which now includes the audit and contract validators).
4. Record the new version here — a version without a date is folklore.
