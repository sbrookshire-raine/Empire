---
name: capability_route
toolbelt: always
one_line: Keyword route to tools, limbs, and playbook areas with load hints
---

# capability_route

Search Eve's **internal** capability index (tools, Toolbelt limbs, playbook areas).

## When to use

- "What tool should I use for …?" / "Do you have a way to …?"
- Before enabling a heavy limb or calling GPU/network tools.
- **Not** for mining the OSS repo catalog — use `search_catalog` for `catalog.db` rows.

## Parameters

- `query` — Intent or keywords (required).
- `limit` — Max hits (default 5, max 10).

## Follow-up protocol

1. `capability_route(query)` — pick id + read `load` / `next_steps`.
2. `playbook(area)` — worked examples; `tool_docs(tool)` — parameters.
3. `resource_pulse()` then `admit_for_goal(category)` if the limb is off.

## Notes

Registered as **always on**. Index is built from tool docs, playbook front matter, and `capability-manifest.json` — no prompt stuffing.
