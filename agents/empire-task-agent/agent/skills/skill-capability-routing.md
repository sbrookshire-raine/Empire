# skill-capability-routing

Use when choosing which arm to call for a task. Prefer the least-powerful, most-local option; only escalate when the cheaper tool cannot answer.

## Order of preference

1. **Read-only over write** — `workspace_search` / `read_document` / `query_data` before `create_spreadsheet` / `author_code`.
2. **Local over web** — `workspace_search`, `query_data`, `read_document`, Cognee recall before `web_scout` / `github_scout`.
3. **Light service before GPU tenant** — PocketBase/frontend (`switchboard_ensure`) before vision/stem/voice/extract (`switchboard_tenant`).

## Arm → use when

| Arm | Use when |
|-----|----------|
| `workspace_search` | Find text/files locally (keyword, code reference) |
| `query_data` | Pull answers from local CSV/JSON/Parquet/SQLite |
| `read_document` | Read a local PDF/DOCX/XLSX/HTML/markdown |
| `create_spreadsheet` | Produce an `.xlsx` the Architect can open |
| `author_code` | Write/change code (disposable worktree, reviewable diff) |
| `python_verify` | Check code before sharing (syntax + lint + tests) |
| `switchboard_*` | Start/stop services or serialize GPU tenants for a task |

## Hard rules

- Every arm carries provenance and is scratch-only; never auto-Cognee.
- Writes go only to `eve-output` / `eve-worktrees`; never outside.
- Mutating service/GPU actions: dry-run first, then only on headroom green.
