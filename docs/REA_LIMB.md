# REA limb (Reverse Engineer Anything)

[REA](https://github.com/morluto/rea) (`rea-agents` on npm) exposes a local MCP server for reverse-engineering workflows. EMPIRE pins it under `tools/rea/` and wires it for **Cursor** and **Eve** (Toolbelt category `rea`).

## Install / update

```powershell
cd C:\EMPIRE
.\scripts\ensure-rea.ps1
```

This runs `npm install` in `tools/rea` (pinned `rea-agents@6.3.0`). Node **22.19+**, **24.11+**, or **26+** is required by REA.

Optional bundled agent skill (Cursor / other CLIs):

```powershell
node C:\EMPIRE\tools\rea\node_modules\rea-agents\scripts\rea.mjs setup --yes --skill
```

Restart Cursor after MCP changes.

## MCP (Cursor)

Registered in `.cursor/mcp.json` as **`rea`**: Node runs `tools/rea/node_modules/rea-agents/scripts/rea.mjs mcp` (stdio). Evidence cache default:

`C:/Empire_Workbench/04_Thought_Experiments/rea_cache`

Override with env `REA_EVIDENCE_ROOT`.

## Eve tools (Toolbelt **REA** — default off)

| Tool | Purpose |
|------|---------|
| `rea_doctor` | Host readiness |
| `rea_analyze_javascript` | Static JS/Electron app analysis |
| `rea_invoke` | Any REA MCP tool by name |

Enable **REA** on the Workbench Toolbelt (Session) or ask Eve to admit the limb, then use natural language ("reverse engineer this Electron app at …").

## Native analysis engines

JavaScript/.NET static paths work without extra installs. **Hopper, Ghidra, or IDA** are optional and required for deep native binary work. Configure per [REA installation docs](https://github.com/morluto/rea/blob/main/docs/installation.md) (`GHIDRA_INSTALL_DIR`, etc.).

Check readiness:

```powershell
node C:\EMPIRE\tools\rea\node_modules\rea-agents\scripts\rea.mjs doctor
```

## Rebuild Eve after tool changes

```powershell
cd C:\EMPIRE\agents\empire-task-agent
npm run build
```

Or restart via `.\scripts\start-eve.ps1` when the stack is up.
