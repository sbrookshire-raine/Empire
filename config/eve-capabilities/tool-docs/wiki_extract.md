---
name: wiki_extract
toolbelt: wiki_local
one_line: Extract structured facts from a local Wikipedia page (Title DNS)
---

## Description (verbatim from the tool schema, pre-R-03)

Extract structured facts from a local Wikipedia page (Title DNS). Returns fields, tables, and lists — not a lead dump. Use for dates, numbers, specs, table rows, lists; pass a self-contained subject (resolve pronouns yourself first). If EXTRACT is empty, refuse — do not invent. Does NOT write Cognee. If [[EMPIRE_WIKI_EXTRACT]] or [[EMPIRE_WIKI_LOOKUP]] is already in the turn (legacy middleware), answer from that instead of calling this.

## Parameters

- `subject` — Encyclopedia title or subject.
- `year` — Snapshot year (default 2026).
- `need_hint` — Optional hint to rank fields/tables (e.g. release date, population).
- `section` — Optional H2 section name.
- `question` — Full user question for ranking.

## Usage

Registered by the Toolbelt category `wiki_local`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
