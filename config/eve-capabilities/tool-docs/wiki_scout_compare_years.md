---
name: wiki_scout_compare_years
toolbelt: wiki_local
one_line: Truth Drift compare with Wiki Interpreter across local Wikipedia years (2017/2021/2026)
---

## Description (verbatim from the tool schema, pre-R-03)

Truth Drift compare with Wiki Interpreter across local Wikipedia years (2017/2021/2026). Only when the user explicitly asks to compare years / Truth Drift. Resolve the topic yourself, including pronouns (pass a self-contained topic). Returns cards_by_year — you MUST answer from those card titles/snippets only. Do not invent year-by-year 'key findings' or maturity narratives without card text. Archive years are not hypothetical futures. Does NOT write Cognee. Requires Wiki Local Toolbelt.

## Parameters

- `query` — Topic to compare across years.
- `years` — Comma-separated years, default 2017,2021,2026.
- `limit_per_year` — Max ranked cards per year after interpret (default 4).
- `tool` — (no description)

## Usage

Registered by the Toolbelt category `wiki_local`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
