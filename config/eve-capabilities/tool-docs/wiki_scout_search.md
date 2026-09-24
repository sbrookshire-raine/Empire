---
name: wiki_scout_search
toolbelt: wiki_local
one_line: Local Wikipedia lookup (Title DNS + article lead) for a subject you name
---

## Description (verbatim from the tool schema, pre-R-03)

Local Wikipedia lookup (Title DNS + article lead) for a subject you name. Returns the article **lead only** — it usually will NOT contain songs, albums, dates, or table rows. Resolve pronouns and follow-ups yourself first — pass a

## Parameters

- `query` — Search query for Wikipedia.
- `year` — Snapshot year: 2017, 2021, or 2026 (default 2026). Use other years only when the user asks.
- `limit` — Max ranked cards to keep after interpret (default 5).

## Usage

Registered by the Toolbelt category `wiki_local`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
