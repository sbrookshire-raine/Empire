---
name: author_code
toolbelt: author_code
one_line: Author code in a disposable Git worktree
---

## Description (verbatim from the tool schema, pre-R-03)

Author code in a disposable Git worktree. `create` makes a fresh worktree; `apply` writes one file and returns a reviewable diff; `remove` deletes a worktree. Never pushes, merges, or touches the production tree. Never writes credential files.

## Parameters

- `action` — Operation to perform.
- `worktree` — Worktree path (required for apply/remove).
- `relative_path` — File path inside the worktree (apply only).
- `content` — File content (apply only).
- `note` — Optional note (create only).

## Usage

Registered by the Toolbelt category `author_code`. The model sees the name, the
one-line cue and the parameter names in its schema; this document is the deep syntax it
can fetch with `tool_docs` when a call needs more than the cue.
