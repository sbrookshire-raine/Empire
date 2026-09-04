Use when the user asks whether the Workbench is healthy, how much disk space remains, how many Active Tools are present, or wants a quick EMPIRE Workbench diagnostic.

## Mission

Run a local health check on `C:/Empire_Workbench` and report the result in plain language. Do not invent numbers — call the tool.

## Tool

Call `check_workbench_health` (no arguments).

## How to answer

1. Say whether status is **online**, **degraded** (low free space), or **error**.
2. Mention free space vs total (GB).
3. Mention Active Tools count.
4. Optionally note Resource Queue / Work Orders counts if useful.
5. If `low_free_space` is true, warn briefly that free space is under the threshold.

## Hard rules

- Local Windows only — never claim a cloud/sandbox filesystem.
- Do not delete or move Workbench files during a health check.
- Keep the spoken reply short and easy to listen to.
