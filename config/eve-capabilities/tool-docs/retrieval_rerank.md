---
name: retrieval_rerank
toolbelt: retrieval_rerank
one_line: Rerank candidate text passages for a query (lexical or optional CrossEncoder)
---

## Description (verbatim from the tool schema, pre-R-03)

Rerank candidate text passages for a query (lexical or optional CrossEncoder). Eval/scratch only — does NOT change Cognee production embeddings (nomic). Requires Retrieval Rerank Toolbelt.

## Parameters

- `query` — (no description)
- `candidates_json` — (no description)
- `top_k` — (no description)

## Usage

Registered by the Toolbelt category `retrieval_rerank`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
