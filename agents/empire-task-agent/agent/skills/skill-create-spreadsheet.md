# skill-create-spreadsheet

Use when the Architect wants a table turned into an actual `.xlsx` file they can open — reports, exports, lists, comparisons.

## Mission

Write clean `.xlsx` files into `eve-output` from headers + rows, with formula-injection protection, and tell the Architect where the file landed.

## Tools

- `create_spreadsheet` — headers + rows → `.xlsx` under `C:/EMPIRE/eve-output`.

## How to work a goal

1. Turn the data into a `headers` list and a `rows` list-of-lists.
2. Call `create_spreadsheet` with a short `filename` (no path).
3. Report the returned `path` and row count.

## Hard rules

- Only writes under `eve-output` — never elsewhere, never Cognee.
- Cells starting with `= + - @` are escaped as text (never executed as formulas).
- Keep tables bounded (≤200 columns, ≤20000 rows).
