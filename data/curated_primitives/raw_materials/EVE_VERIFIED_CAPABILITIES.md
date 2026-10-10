---
source: capability_verification
kind: eve_operating_contract
dataset: eve_core
memory_status: foundation
promote: mechanic_only
verified_at: 2026-10-10T16:48:32+00:00
---
# EVE verified capabilities (mechanic report)

This document is **written by Mechanic** (`pipeline.capability_verification`). Eve should treat it as authoritative for *what is proven to work* on this machine. Do not tell the Architect a tool is broken without checking this report age and re-running `scripts/verify-capabilities.ps1`.

- Offline checks: **33** (33 pass, 0 fail)
- Live stack checks run: **False**
- Eve tool-doc registry: **33+** named tools (see `tool_docs` / `playbook`)
- MCP servers import-clean: **24**

## How Eve should use this

1. **Recall first:** `cognee_recall("verified capabilities what works", dataset="eve_core")`.
2. **Route second:** `capability_route` → `playbook` → `tool_docs` for parameters.
3. **Call tools** — optional limbs auto-admit via `resource_pulse` / `admit_for_goal`; never claim you lack GitHub/internet if the tool is listed below as proven.
4. **Workbench Tools dock** is read-only status; you manage admits.

## Proven MCP servers (import / wiring)

- `empire-artifact`
- `empire-atlas`
- `empire-browser-local`
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
- **eve_build** — `eve_runtime` (offline)
- **resource_farm_catalog** — `catalog_status` (offline)
- **resource_pulse** — `pulse` (offline)
- **workspace_search** — `search` (offline)
- **switchboard_plan** — `plan` (offline)
- **capability_route** — `route` (offline)
- **mcp:empire-artifact** — `empire-artifact` (mcp)
- **mcp:empire-atlas** — `empire-atlas` (mcp)
- **mcp:empire-browser-local** — `empire-browser-local` (mcp)
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

## Refresh

```powershell
.\scripts\verify-capabilities.ps1
.\scripts\verify-capabilities.ps1 -Live -SyncCognee
```

