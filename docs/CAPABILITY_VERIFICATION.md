# Capability verification — pavement before you test

**One breath:** You should not manually ask “does this work?” until Mechanic has run **`verify-capabilities`** and (optionally) synced the report into **`eve_core`** so Eve **knows** what is proven.

## The contract

| Layer | What it proves | Command |
|-------|----------------|---------|
| **Governance** | Governed arms match schema snapshots | `capability_verification` → `capability_governance` |
| **Playbook** | Every registered Eve tool has worked examples | `pipeline.playbook --coverage` |
| **Tool surface** | ~99 `tool_docs` + Eve bundle ships core tools | `eve_tool_docs`, `eve_build` |
| **Pipeline offline** | Key modules return `ok` (farm, pulse, search, switchboard plan) | battery `offline_pipeline_probes` |
| **MCP** | Every Python MCP script in `.cursor/mcp.json` **imports cleanly** | per-server `mcp:*` checks |
| **Live Eve** (optional) | Real tool-calls on the wire | `-Live` → `smoke-eve-hands`, `test-eve-tools-playwright` |

Architect UX (clicking `eve.html`) is **feel and product**, not “is the tool there?”

## Run order

```powershell
.\scripts\mechanic-green.ps1          # units + governance + stack (when Docker ok)
.\scripts\verify-capabilities.ps1      # all tools + MCP pavement (offline)
.\scripts\verify-capabilities.ps1 -Live   # + Eve must call github_scout / resource_farm
.\scripts\verify-capabilities.ps1 -Live -SyncCognee   # + remember report in eve_core
```

Report files:

- `tmp/capability_verification_report.json`
- `data/curated_primitives/raw_materials/EVE_VERIFIED_CAPABILITIES.md`
- `%LOCALAPPDATA%\EMPIRE\eve_hands_verified.json` (injected on capability / resource-farm questions via pulse)

## How Eve learns it

1. **On demand (preferred):** `cognee_recall("verified capabilities what works", dataset="eve_core")` after `-SyncCognee`.
2. **On capability questions:** frontend injects `[[EMPIRE_RESOURCE_PULSE]]` including `verified_hands_snippet` when fresh.
3. **Deep syntax:** `playbook` + `tool_docs` — unchanged; verification does not replace them.

Do **not** auto-remember chat transcripts. Only the mechanic markdown is promoted to `eve_core`, with provenance in the file front matter.

## Extending coverage

Edit `config/diagnostics/capability-verification-battery.json`:

- Add `offline_pipeline_probes` rows (`module` + `call`).
- Add `live_stack_probes` scripts when a tool needs a live Eve turn.

Re-run verify; commit updated `EVE_VERIFIED_CAPABILITIES.md` when the report changes materially.

Related: [PLAYBOOK.md](PLAYBOOK.md), [MEMORY_GOVERNANCE.md](MEMORY_GOVERNANCE.md), [RESOURCE_FARM_AND_CATALOG.md](RESOURCE_FARM_AND_CATALOG.md).
