---
name: stem_run
toolbelt: stem_factory
one_line: Run Demucs stem separation + practice focus tracks on songs in the stem inbox (default C:/Empire_Workbench/st…
---

## Description (verbatim from the tool schema, pre-R-03)

Run Demucs stem separation + practice focus tracks on songs in the stem inbox (default C:/Empire_Workbench/stem_factory/input). Writes to stem_factory/output. Default limit=1. GPU preferred; may take minutes. Requires Stem Factory Toolbelt.

## Parameters

- `limit` — Max songs to process (default 1).
- `device` — cuda or cpu (default cuda, auto-falls back).
- `overwrite` — Reprocess even if outputs exist.

## Usage

Registered by the Toolbelt category `stem_factory`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
