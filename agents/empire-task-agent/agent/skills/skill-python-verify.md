# skill-python-verify

Use to confirm Python changes are safe before they're shared — syntax always, plus lint and tests when available.

## Mission

Verify a disposable worktree's Python: compile every `.py`, run ruff (if installed), and run tests (pytest or unittest). Report a clear pass/fail; never merge.

## Tools

- `python_verify` — returns a report of syntax/ruff/tests.

## How to work a goal

1. Point `python_verify` at the worktree from `author_code create`.
2. Read the report; if `ok` is false, report the first error and stop.
3. Only hand off when syntax passes and lint/tests (if run) are clean.

## Hard rules

- Never merge or push. Verification only.
- No inherited secrets; runs in the disposable worktree.
