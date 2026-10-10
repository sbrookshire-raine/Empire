---
name: browser_capture_screenshot
toolbelt: always
one_line: Capture a Playwright screenshot of an allowlisted localhost EMPIRE URL or a local HTML file (under REA inbox …
---

## Description (verbatim from the tool schema, pre-R-03)

Capture a Playwright screenshot of an allowlisted localhost EMPIRE URL or a local HTML file (under REA inbox or Empire_Workbench). Observation only — no clicks. Auto-admits Browser Local when headroom allows.

## Parameters

- `url` — Allowlisted http(s) URL (e.g. http://127.0.0.1:8080/eve.html).
- `html_path` — Absolute path to a local .html file under Workbench or REA inbox.
- `full_page` — Capture full scrollable page (default false).
- `note` — (no description)

## Usage

Registered by the Toolbelt category `always`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
