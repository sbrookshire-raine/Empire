---
name: wiki_read_section
toolbelt: wiki_local
one_line: Read a local Wikipedia markdown page by title (Title DNS)
---

## Description (verbatim from the tool schema, pre-R-03)

Read a local Wikipedia markdown page by title (Title DNS). Optional section: cast, discography, filmography, charts, history, reception, plot, production. Use when the landing lead is too thin for the question; pass the self-contained title. If [[EMPIRE_WIKI_LOOKUP]] / [[EMPIRE_WIKI_EXTRACT]] evidence is already in the turn (legacy middleware), answer from that instead of calling this. Does NOT write Cognee.

## Parameters

- `title` — Exact encyclopedia title.
- `year` — Snapshot year (default 2026).
- `section` — Optional H2 section key: cast, discography, filmography, charts, history, reception, plot, production.
- `question` — User question for section preference when section omitted.

## Usage

Registered by the Toolbelt category `wiki_local`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
