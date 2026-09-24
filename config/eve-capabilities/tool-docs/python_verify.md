---
name: python_verify
toolbelt: python_verify
one_line: Verify Python code in a disposable worktree: syntax check (always) plus optional ruff lint and pytest/unittest
---

## Description (verbatim from the tool schema, pre-R-03)

Verify Python code in a disposable worktree: syntax check (always) plus optional ruff lint and pytest/unittest. Never merges, pushes, or mutates production. Returns a report; if ok is false, do not merge.

## Parameters

- `worktree` — Worktree path to verify.
- `run_tests` — Run tests too (default true).

## Usage

Registered by the Toolbelt category `python_verify`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
