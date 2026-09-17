# skill-query-data

Use when the Architect wants a concrete answer pulled from a local CSV / JSON / Parquet / SQLite file — counts, filters, totals, joins.

## Mission

Run read-only SQL over a local data file and answer from the actual rows. Never write, never network, never install extensions.

## Tools

- `query_data` — pass a `data_file` (registered as table `data`) + SQL, or a full inline `SELECT`.

## How to work a goal

1. Confirm the file exists under an allowlisted root (`C:/Empire_Workbench`, `C:/EMPIRE/data`).
2. Call `query_data` with `data_file` and a `SELECT ... FROM data ... LIMIT`.
3. Answer from the returned `columns` + `rows`. State the row count and any truncation.

## Hard rules

- Only `SELECT`/`WITH` — no DELETE/UPDATE/ATTACH/COPY/http.
- Caps: max 10000 rows, 2 MB result, 30s. Add `LIMIT` to stay small.
- Read-only; never writes Cognee.
