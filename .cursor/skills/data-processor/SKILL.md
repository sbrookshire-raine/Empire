---
name: data-processor
description: Process CSV/Excel files, extract from PDFs, query databases, and transform data. Activate for "process this file", "extract from PDF", "read this CSV", "query the database", "analyze this spreadsheet". Infra-agnostic data-wrangling toolkit; when the target database is Build1's own store, prefer the SQLite/PocketBase connector over Postgres/MySQL/MongoDB.
icon: database
color: Blue
---

# Data Processor

## Activate when

- "Process this CSV / Excel / spreadsheet"
- "Extract text / tables from this PDF"
- "Query the database"
- "Join / pivot / filter this data"
- "Read this file and summarize"

## How to use this skill

1. Identify the data source type (CSV/Excel, PDF, or a live database) and pick the
   matching script below, kept under this skill's `scripts/` directory.
2. Read `references/03_data.md` for the full function signatures before calling
   anything — keep the exhaustive parameter catalog there rather than inline here.
3. For any database target, connect with `db_connectors.py`; when the target is
   Build1's own backend, connect to the **PocketBase SQLite** file directly (or via
   PocketBase's REST/JS SDK) rather than standing up Postgres/MySQL/MongoDB unless the
   user explicitly has one of those as a separate data source.
4. Return a concise summary/result table to the user, not raw dumps, unless they ask
   for the full export.

## Script catalog

| Script | Purpose |
|---|---|
| `data_tools.py` | CSV/Excel read/write, filter, pivot, describe |
| `database_tools.py` | SQL query/execute/insert, schema inspection |
| `db_connectors.py` | PostgreSQL, MySQL, MongoDB, SQLite connectors |
| `pdf_tools.py` | Text + table extraction, merge, split |
| `vector_tools.py` | Embed, index, semantic search |
| `audio_tools.py` | Transcribe audio files |

## Build1 Integration

- **Backend (PocketBase/SQLite):** default to the SQLite connector in
  `db_connectors.py` when the data lives in a Build1 project's own PocketBase database.
- **Memory/RAG (Cognee):** if `vector_tools.py`'s embed/index step is meant to build
  long-term memory rather than a one-off search, route it through **Cognee** instead of
  a standalone vector store, and generate embeddings with the local **Ollama** model
  rather than a cloud embedding API.
- **Nervous system (FastMCP):** expose any of these data operations as FastMCP tools if
  they need to be callable by the agent repeatedly, rather than one-off scripts.
