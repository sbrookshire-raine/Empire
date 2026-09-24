---
name: container_scout_search
toolbelt: container_scout
one_line: Search Docker Hub by keyword; cache markdown under 04_Thought_Experiments/container_cache
---

## Description (verbatim from the tool schema, pre-R-03)

Search Docker Hub by keyword; cache markdown under 04_Thought_Experiments/container_cache. Auto-admits Container Scout when headroom allows. Does NOT pull images or write Cognee.

## Parameters

- `query` — Search keywords (e.g. weaviate, vector database).
- `limit` — Max results (default 10).
- `note` — Optional Architect note.

## Usage

Registered by the Toolbelt category `container_scout`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
