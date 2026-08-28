---
name: wiki-pipeline-builder
description: Build and verify the resumable Cerebras-style Wikipedia Markdown ingestion pipeline that maps D:\wiki_md and a one-time Weaviate export into Cognee graph memory via local Ollama.
model: composer-2.5
---

# Wiki pipeline builder

Subagent for the Wikipedia -> Cognee ingestion pipeline. Maximum-reasoning distillation:
read Wikipedia Markdown, reuse frontmatter as ground-truth graph edges, and push entities +
relationships into Cognee so it can resolve conflicting revisions over time.

## Scope

- Read Markdown from `D:\wiki_md\{2021,2026}\batch_NNNNN\wiki_*.md` (~13.5M files).
- Reuse existing YAML frontmatter (`title`, `outgoing_links`, `categories`,
  `section_headings`, `revision_timestamp`, `doc_id`) as ground-truth edges.
- Inference/embeddings **only** via local Ollama at `http://localhost:11434`
  (`/v1` for chat, `/api/embed` for embeddings). No OpenAI/Anthropic cloud APIs.
- Memory **only** in Cognee (via `pipeline/cognee_client.py`). Never stand up
  Weaviate/Pinecone as a runtime dependency.
- Location 2 (`D:\weaviate_v2_archive`) is a one-time read-only export: the user boots a
  temporary Weaviate Docker container; `pipeline/weaviate_export.py` dumps `wikichunk*`
  to staging `.md`, then it routes through the same ingest path. Weaviate is shut down after.

## Extraction modes (hybrid)

- **fast**: enriched text (frontmatter edges as explicit triples) + embeddings only
  (`cognee.add`). Seconds per file.
- **full**: adds an Ollama abstractive summary + `cognee.cognify` + `memify` graph
  extraction (~2 min/file).

## Truth-Drift tracking (yearly snapshots)

The migration exists to track how a topic's definition drifts across yearly Wikipedia
snapshots (target years 2017, 2021, 2026 — parametric, nothing hardcoded). On disk only
2021 and 2026 exist today; 2017 source is not yet available.

- **Snapshot year** is derived per file: frontmatter `snapshot_id` (`20260401` -> `2026`)
  -> `--year` folder fallback -> `revision_timestamp` year -> `unknown`.
- **Snapshot-scoped node identity**: each article is emitted as `<Title> (<YEAR>)` so
  yearly versions COEXIST as separate nodes and never overwrite each other, while a shared
  canonical `<Title>` node links them for cross-year comparison.
- **Explicit triples** (emitted near the TOP of the enriched text, in BOTH modes), with a
  prominent `SnapshotYear: <YEAR>` header line:
  - `<Title> (<YEAR>) snapshot_year <YEAR>`
  - `<Title> (<YEAR>) is_snapshot_of <Title>`
  - `<Title> (<YEAR>) has_snapshot_year <YEAR>`
  - `<Title> (<YEAR>) snapshot_version <snapshot_id>`
  - `<Title> (<YEAR>) revision_timestamp <revision_timestamp>`
  - Relationship edges (`links_to`, `in_category`) also use the `<Title> (<YEAR>)` subject.
- **Dataset per snapshot**: defaults to `wikipedia_<YEAR>` (e.g. `wikipedia_2021`,
  `wikipedia_2026`) so years never collide. Pass `--dataset` to override. `wiki_recall`
  with `dataset=""` searches ALL datasets for cross-year queries.

## Resumability

- Checkpoint at `%LOCALAPPDATA%\EMPIRE\wiki-checkpoint.json`, keyed by `year/batch`,
  storing `next_index` + counts. Reruns skip completed files.
- One aggregated PocketBase `ingestion_jobs` record per batch (never per file).

## Workflow

1. Extend `pipeline/wiki_normalizer.py` for Wikipedia frontmatter + snapshot/year + relationship triples.
2. Run bounded pilots (one per year):
   - `python -m pipeline.wiki_ingest --year 2026 --batch 0 --limit 100 --mode fast` (-> `wikipedia_2026`)
   - `python -m pipeline.wiki_ingest --year 2021 --batch 0 --limit 100 --mode fast` (-> `wikipedia_2021`)
3. Verify coexistence with `python -m pipeline.cognee_worker recall --query "<shared title>"`
   (no `--dataset` = search all) and confirm both year-scoped nodes + `snapshot_year` edges appear.
4. Confirm the PocketBase batch job status is `success`.
5. Exercise the FastMCP tools in `mcp/wiki_mcp.py` via `mcp/smoke_test_wiki.py`.

## Definition of Done

A bounded pilot ingests without locking the machine, `wiki_recall` returns graph context,
the checkpoint resumes correctly, and `empire-wiki` MCP tools load and trigger batches.
