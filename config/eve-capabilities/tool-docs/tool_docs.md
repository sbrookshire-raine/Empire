---
name: tool_docs
toolbelt: always
one_line: Look up deep syntax for one tool (parameters, semantics, gotchas) when a call needs more than its one-line cue
---

## Description (verbatim from the tool schema, pre-R-03)

Look up deep syntax for one tool (parameters, semantics, gotchas) when a call needs more than its one-line cue.

## Parameters

- `name` — Tool name to document, e.g. wiki_read_section. Omit to list all…

## Usage

Registered by the Toolbelt category `always`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
