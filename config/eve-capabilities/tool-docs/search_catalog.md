---
name: search_catalog
toolbelt: always
one_line: Search the local EMPIRE capability catalog for tools by capability, description, category, or name
---

## Description (verbatim from the tool schema, pre-R-03)

Search the **external intake catalog** (`catalog.db` — OSS/MCP repository rows). Read-only. For Eve's **own** tools and limbs, use **`capability_route`** first; do not use this tool to discover `wiki_scout_search`, tasks tools, etc.

## Parameters

- `query` — Capability or tool search, for example minimax or decision making.
- `limit` — Maximum catalog results.

## Usage

Registered by the Toolbelt category `always`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
