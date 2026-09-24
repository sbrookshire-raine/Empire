---
name: skill_triage_manifest
toolbelt: tool_forge
one_line: Inventory SKILL.md files and run Build1 3-Bin heuristic triage
---

## Description (verbatim from the tool schema, pre-R-03)

Inventory SKILL.md files and run Build1 3-Bin heuristic triage. Writes skill_triage_manifest.json + SKILL_TRIAGE_MANIFEST.md under harvest_cache. Requires Tool Forge Toolbelt.

## Parameters

- `paths` — Comma-separated zip files or directories to scan (optional).
- `include_installed` — Also scan C:/EMPIRE/.cursor/skills (default true).

## Usage

Registered by the Toolbelt category `tool_forge`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
