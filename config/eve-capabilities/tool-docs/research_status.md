---
name: research_status
toolbelt: web_research
one_line: Check a research job's state (or list open jobs when called with no id)
---

## Description (verbatim from the tool schema, pre-R-03)

Check a research job's state (or list open jobs when called with no id). Cheap; safe to call every turn.

## Parameters

- `job_id` — Job id from research_start; omit to list open jobs.

## Usage

Registered by the Toolbelt category `web_research`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
