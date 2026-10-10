---
name: app_visual_observe
toolbelt: always
one_line: Visually observe how a page or local HTML app looks: Playwright screenshot, then qwen3-vl structured UI regio…
---

## Description (verbatim from the tool schema, pre-R-03)

Visually observe how a page or local HTML app looks: Playwright screenshot, then qwen3-vl structured UI regions. Use for Electron/web UIs the Architect uploaded or serves locally. Does not launch arbitrary EXEs or click controls. Auto-admits Browser Local and Vision Local when headroom allows.

## Parameters

- `url` — Allowlisted http(s) URL to open in headless Chromium.
- `html_path` — Absolute path to HTML under REA inbox or Empire_Workbench.
- `full_page` — (no description)
- `note` — What to look for in the UI.

## Usage

Registered by the Toolbelt category `always`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
