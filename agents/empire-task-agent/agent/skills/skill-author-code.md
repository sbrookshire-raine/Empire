# skill-author-code

Use when the Architect asks you to write or change code — always in a disposable worktree, always as a reviewable diff, never a silent self-merge.

## Mission

Author code with the Architect: every change is a visible diff in a disposable Git worktree under `eve-worktrees/{run-id}`. Never push, merge, or mutate the production tree.

## Tools

- `author_code` (action=create/apply/remove) — create a worktree, write a file + get its diff, remove the worktree.
- `python_verify` — syntax + lint + tests on the worktree before anything is shared.

## How to work a goal

1. `author_code create` → get a `worktree` path.
2. For each file, `author_code apply` with `relative_path` + `content`; show the returned `diff`.
3. `python_verify` the worktree; only report it as done when `ok` is true.
4. Present the diff to the Architect for review. Remove the worktree when finished (or leave it for review).

## Hard rules

- Never write `.env`, keys, or credential paths.
- Never push or merge. Never mutate the production repo.
- `relative_path` must stay inside the worktree (no `..`, no absolute paths).
