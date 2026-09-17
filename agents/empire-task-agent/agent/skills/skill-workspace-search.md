# skill-workspace-search

Use when the Architect needs something found in local notes/files — a keyword, a file name, a code reference — without leaving the machine.

## Mission

Find text across allowlisted local roots (`C:/Empire_Workbench`, `C:/EMPIRE/docs`) and answer from what's actually there. Never invent a match.

## Tools

- `workspace_search` — literal substring search; returns path/line/text, redacted.

## How to work a goal

1. Call `workspace_search` with the exact keyword or short phrase.
2. If `count` is 0, say so and ask for a different term — never fabricate a result.
3. Summarize the top matches (path + a short quote); do not dump raw `results`.
4. If the answer needs the full file, use `read_document` (or `workbench_read_file` for Workbench paths) next.

## Hard rules

- Read-only; never writes Cognee.
- Searches are literal (substring), not semantic — keep queries short.
- Results are redacted of secrets; do not reveal what was redacted.
