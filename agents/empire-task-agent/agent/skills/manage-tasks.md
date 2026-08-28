Use when the user wants to create, triage, update, or close tasks in the EMPIRE PocketBase tasks collection.

## Workflow

1. Call `list_tasks` or `search_tasks` to see current work.
2. For new work, call `create_task` with a clear title and optional description, status, and priority.
3. For changes, call `update_task` with the task id and only the fields that change.
4. For removal, confirm with the user, then call `delete_task` (approval gate applies).

## Conventions

- Default new tasks to `status: todo` and `priority: 1` unless the user specifies otherwise.
- Valid statuses: `todo`, `in_progress`, `done`.
- Summarize results as a short bullet list with ids, titles, and statuses.

## If PocketBase is down

Report the error from the tool and tell the user to run `.\scripts\start-pocketbase-background.ps1` from the EMPIRE repo root.
