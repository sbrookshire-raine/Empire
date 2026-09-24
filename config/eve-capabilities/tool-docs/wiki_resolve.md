---
name: wiki_resolve
toolbelt: wiki_local
one_line: Resolve whether a Wikipedia title exists in the local Title DNS phone book
---

## Description (verbatim from the tool schema, pre-R-03)

Resolve whether a Wikipedia title exists in the local Title DNS phone book. Pass a self-contained title — resolve pronouns/context from the conversation first. Returns exact/alias/ambiguous/missing. Does NOT extract page content. If the turn already carries [[EMPIRE_WIKI_LOOKUP]] / [[EMPIRE_WIKI_EXTRACT]] evidence (legacy middleware), answer from it instead of calling this. Does NOT write Cognee.

## Parameters

- `subject` — Title or subject to resolve.
- `year` — Snapshot year (default 2026).
- `question` — User question for disambiguation hints.

## Usage

Registered by the Toolbelt category `wiki_local`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
