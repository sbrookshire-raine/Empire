---
source: capability_verification
kind: eve_operating_contract
dataset: eve_core
memory_status: foundation
promote: mechanic_only
verified_at: 2026-10-22T02:33:55+00:00
---
# EVE verified capabilities (mechanic report)

This document is **written by Mechanic** (`pipeline.capability_verification`). Eve should treat it as authoritative for *what is proven to work* on this machine. Do not tell the Architect a tool is broken without checking this report age and re-running `scripts/verify-capabilities.ps1`.

- Offline checks: **35** (35 pass, 0 fail)
- Live stack checks run: **False** — _not run; offline report only_
- Always-on tools: **31** (registered in every session, no admit needed)
- On-by-default gated tools: **8** (`wiki_local`)
- Eve tool-doc registry: **35+** named tools (see `tool_docs` / `playbook`)
- MCP servers import-clean: **25**

## How Eve should use this

1. **Always-on:** `eve-operating-context.md` in system prompt + `[[EMPIRE_RESOURCE_PULSE]]` every turn.
2. **Route:** `capability_route` → `playbook` → `tool_docs` for parameters.
3. **Call tools** — optional limbs auto-admit via `resource_pulse` / `admit_for_goal`; never claim you lack GitHub/internet if the tool is listed below as proven.
4. **Workbench Tools dock** is read-only status; you manage admits.

## Always-on tools (call these without asking)

These are registered in every session — no Toolbelt click, no admit, no `resource_pulse` round trip. If the Architect asks about memory, tasks, or the catalog, use them directly.

- `admit_for_goal`
- `capability_route`
- `capability_status`
- `check_workbench_health`
- `cognee_forget`
- `cognee_improve`
- `cognee_recall`
- `cognee_remember`
- `create_task`
- `delete_task`
- `disassembly_card_write`
- `gpu_lease_status`
- `intake_to_lego_run`
- `list_tasks`
- `pb_health`
- `playbook`
- `rea_analyze_javascript`
- `rea_doctor`
- `rea_invoke`
- `rea_list_inbox`
- `release_capabilities`
- `remember_wiki_lead`
- `request_capability`
- `resolve_intent`
- `resource_farm_run`
- `resource_pulse`
- `search_catalog`
- `search_tasks`
- `tool_docs`
- `update_task`
- `wiki_remember`

### On by default (switch off via the Toolbelt)

- `promote_wiki_cache`
- `wiki_extract`
- `wiki_read_section`
- `wiki_resolve`
- `wiki_scout_compare_years`
- `wiki_scout_search`
- `wiki_scratch_read`
- `wiki_scratch_upsert`

## Proven MCP servers (import / wiring)

- `empire-artifact`
- `empire-atlas`
- `empire-browser-local`
- `empire-claim-ledger`
- `empire-cognee`
- `empire-container-scout`
- `empire-daze`
- `empire-discovery`
- `empire-docling`
- `empire-evidence`
- `empire-github-scout`
- `empire-heptabase`
- `empire-loom-intake`
- `empire-pocketbase`
- `empire-retrieval-rerank`
- `empire-stem-factory`
- `empire-structured-extract`
- `empire-switchboard`
- `empire-tool-forge`
- `empire-web-scout`
- `empire-wiki-scout`
- `empire-work-orders`
- `empire-workbench`
- `graft`
- `rea`

## Proven checks (sample tools / subsystems)

- **playbook_coverage** — `playbook` (offline)
- **capability_governance** — `capability_registry` (offline)
- **eve_tool_docs** — `tool_docs` (offline)
- **always_on_tools** — `cognee_recall` (surface)
- **eve_build** — `eve_runtime` (offline)
- **resource_farm_catalog** — `catalog_status` (offline)
- **resource_pulse** — `pulse` (offline)
- **workspace_search** — `search` (offline)
- **switchboard_plan** — `plan` (offline)
- **capability_route** — `route` (offline)
- **mcp:empire-artifact** — `empire-artifact` (mcp)
- **mcp:empire-atlas** — `empire-atlas` (mcp)
- **mcp:empire-browser-local** — `empire-browser-local` (mcp)
- **mcp:empire-claim-ledger** — `empire-claim-ledger` (mcp)
- **mcp:empire-cognee** — `empire-cognee` (mcp)
- **mcp:empire-container-scout** — `empire-container-scout` (mcp)
- **mcp:empire-daze** — `empire-daze` (mcp)
- **mcp:empire-discovery** — `empire-discovery` (mcp)
- **mcp:empire-docling** — `empire-docling` (mcp)
- **mcp:empire-evidence** — `empire-evidence` (mcp)
- **mcp:empire-github-scout** — `empire-github-scout` (mcp)
- **mcp:empire-heptabase** — `empire-heptabase` (mcp)
- **mcp:empire-loom-intake** — `empire-loom-intake` (mcp)
- **mcp:empire-pocketbase** — `empire-pocketbase` (mcp)
- **mcp:empire-retrieval-rerank** — `empire-retrieval-rerank` (mcp)
- **mcp:empire-stem-factory** — `empire-stem-factory` (mcp)
- **mcp:empire-structured-extract** — `empire-structured-extract` (mcp)
- **mcp:empire-switchboard** — `empire-switchboard` (mcp)
- **mcp:empire-tool-forge** — `empire-tool-forge` (mcp)
- **mcp:empire-web-scout** — `empire-web-scout` (mcp)
- **mcp:empire-wiki-scout** — `empire-wiki-scout` (mcp)
- **mcp:empire-work-orders** — `empire-work-orders` (mcp)
- **mcp:empire-workbench** — `empire-workbench` (mcp)
- **mcp:graft** — `graft` (mcp)
- **mcp:rea** — `rea` (mcp)

## Live stack checks

_Not run._ The live tier proves real tool calls on the wire; run `.\scripts\verify-capabilities.ps1 -Live` for that. Do not claim a tool works on the wire from this report alone.

## Refresh

```powershell
.\scripts\verify-capabilities.ps1
.\scripts\verify-capabilities.ps1 -Live -SyncCognee
```

