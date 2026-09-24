---
name: create_spreadsheet
toolbelt: create_spreadsheet
one_line: Write an Excel (.xlsx) file into eve-output from headers + rows
---

## Description (verbatim from the tool schema, pre-R-03)

Write an Excel (.xlsx) file into eve-output from headers + rows. Blocks formula injection (cells starting =,+,-,@ are escaped). Pure local, offline. Never writes Cognee.

## Parameters

- `filename` — Base filename (no path); .xlsx appended if missing.
- `headers` — Column headers.
- `rows` — Data rows (list of lists).
- `sheet_name` — Worksheet name (default Sheet1).
- `note` — Optional Architect note.

## Usage

Registered by the Toolbelt category `create_spreadsheet`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
