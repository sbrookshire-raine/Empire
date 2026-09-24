---
name: wiki_scratch_read
toolbelt: wiki_local
one_line: Read the Wikipedia research scratchpad (bridging facts) and optional Error Book misses
---

## Description (verbatim from the tool schema, pre-R-03)

Read the Wikipedia research scratchpad (bridging facts) and optional Error Book misses. Only for multi-hop briefs after you already have page evidence from a wiki tool. If [[EMPIRE_WIKI_EXTRACT]] or [[EMPIRE_WIKI_LOOKUP]] is already in the turn (legacy middleware), answer from that instead of calling this. An empty scratchpad is normal for single-page extracts. Does NOT write Cognee.

## Parameters

- `session_id` — Chat session id if known.
- `include_errors` — If true, include recent Error Book misses.
- `chat_reply_rule` — (no description)

## Usage

Registered by the Toolbelt category `wiki_local`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
