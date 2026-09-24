---
name: container_scout_detail
toolbelt: container_scout
one_line: Docker Hub repo detail + recent tags (e.g
---

## Description (verbatim from the tool schema, pre-R-03)

Docker Hub repo detail + recent tags (e.g. semitechnologies/weaviate). Auto-admits Container Scout when headroom allows. Cache only — never pull/run.

## Parameters

- `repo` — Image repo: namespace/name or official short name (redis).
- `tag_limit` — Max tags to list (default 15).
- `note` — Optional Architect note.

## Usage

Registered by the Toolbelt category `container_scout`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
