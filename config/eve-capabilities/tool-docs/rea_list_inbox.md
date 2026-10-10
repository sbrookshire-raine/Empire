---
name: rea_list_inbox
toolbelt: always
one_line: List recent REA analysis uploads from the Eve chat composer (binaries, zips, ASAR, web bundles)
---

## Description (verbatim from the tool schema, pre-R-03)

List recent REA analysis uploads from the Eve chat composer (binaries, zips, ASAR, web bundles). Returns upload ids and absolute analysis_roots. Auto-admits REA when headroom allows.

## Parameters

- `limit` — Max uploads to return (default 20).
- `upload_id` — Optional upload id to show one bundle instead of listing.

## Usage

Registered by the Toolbelt category `always`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
