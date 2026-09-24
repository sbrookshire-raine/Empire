---
name: query_data
toolbelt: query_data
one_line: Run a read-only SQL query (DuckDB) over a local CSV/JSON/Parquet/SQLite file
---

## Description (verbatim from the tool schema, pre-R-03)

Run a read-only SQL query (DuckDB) over a local CSV/JSON/Parquet/SQLite file. Pass data_file (allowlisted local path) and query against table `data`; or pass a full SELECT with no file. No network, no writes, no extensions. Caps rows/bytes/time.

## Parameters

- `sql` — SQL query, e.g. 'SELECT * FROM data WHERE age > 40 LIMIT 20'.
- `data_file` — Optional allowlisted local data file to register as table `data`.
- `max_rows` — Max rows to return (default 1000).

## Usage

Registered by the Toolbelt category `query_data`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
