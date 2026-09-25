---
name: research_start
toolbelt: web_research
one_line: Start a research job (query + URLs) and return a job id immediately
---

## Description (verbatim from the tool schema, pre-R-03)

Start a research job (query + URLs) and return a job id immediately. Use for slow or multi-page research instead of blocking the turn; read it back later with research_read.

## Parameters

- `query` — What the research is for — one line.
- `urls` — Page URLs to fetch. Without one there is nothing to fetch yet (no search tool).

## Usage

Registered by the Toolbelt category `web_research`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
