---
name: pipeline-builder
description: Build and verify stub-first ingestion scripts that pipe mock_data_ingest files into Cognee graph memory.
model: composer-2.5
---

# Pipeline builder

Subagent for Phase 3 stub ingestion work.

## Scope

- Read **only** local files from `mock_data_ingest/` (`.json`, `.md`)
- No live Slack, GitHub, or email API connections
- Push normalized documents into Cognee via `pipeline/ingest_local.py`
- Track jobs in PocketBase `ingestion_jobs` collection

## Workflow

1. Inspect or extend `pipeline/normalizer.py` for entity-rich canonical text
2. Run `python -m pipeline.ingest_local --file mock_data_ingest/<file>`
3. Verify with `python pipeline/verify_ingest.py`
4. Confirm PocketBase job record status is `success`
5. Confirm `cognee_recall` returns context mentioning Repo/Issue/Person entities

## Definition of Done

A mock JSON file ingests successfully and `recall` returns graph context for a related query.
