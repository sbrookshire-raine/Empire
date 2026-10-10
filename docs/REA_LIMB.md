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

## Chat uploads (no fixed folder)

On **http://127.0.0.1:8080/eve.html**, use the **📎** button in the chat composer. Allowed types include `.zip`, `.exe`, `.dll`, `.asar`, `.apk`, `.js`, `.wasm`, `.html`, and related binaries (up to **200 MiB** each, **8** files per upload). Files land under:

`C:/Empire_Workbench/rea_inbox/<upload_id>/`

Zips are extracted automatically. Eve receives absolute `analysis_roots` on the next message (and can call `rea_list_inbox` later).

## Eve tools (Toolbelt **REA** — auto-admits on first call)

| Tool | Purpose |
|------|---------|
| `rea_doctor` | Host readiness |
| `rea_list_inbox` | Recent chat uploads + paths |
| `rea_analyze_javascript` | Static JS/Electron app analysis |
| `rea_invoke` | Any REA MCP tool by name |
| `browser_capture_screenshot` | Playwright screenshot (allowlisted URL or local HTML) |
| `app_visual_observe` | Screenshot + qwen3-vl UI regions (how a page/app looks) |

Visual tools admit **Browser Local** and **Vision Local** when headroom allows. They do **not** launch arbitrary EXEs or drive clicks — use them for uploaded HTML, unpacked web bundles, or allowlisted Workbench URLs (e.g. a page you are already serving locally).

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

## Disassembly catalog (Heptabase)

One card per RE play session → local files → optional publish to the **EMPIRE Disassembly Catalog** whiteboard (colors + dependency links). See [DISASSEMBLY_CATALOG.md](DISASSEMBLY_CATALOG.md).
