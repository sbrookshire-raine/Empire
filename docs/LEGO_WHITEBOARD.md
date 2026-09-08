# LEGO Whiteboard

Manifesto Phase 4 — compose forged EMPIRE limbs as short-name bricks on a local canvas.

**URL:** http://127.0.0.1:8080/lego.html

## What it does

- Palette of bricks from [`config/lego-bricks.json`](../config/lego-bricks.json)
- Drag / place bricks; connect **out → in** ports
- **Save** board JSON under `C:/Empire_Workbench/03_Active_Tools/lego_boards/default.json`
- **Apply to Toolbelt** turns on optional limbs for enabled bricks (writes `%LOCALAPPDATA%/EMPIRE/eve-toolbelt.json`)
- Core bricks (`memory`, `tasks`, `docling`, `gpu`) are never Toolbelt-gated

## What it does not do

- No React / tldraw / Excalidraw
- Edges do **not** auto-run Eve or auto-`cognee_remember`
- Harvested `*_flattened.txt` files are not palette bricks (use Tool Forge)

## API

| Method | Path | Role |
|--------|------|------|
| GET | `/api/lego/bricks` | Catalog |
| GET | `/api/lego/board` | Load default board |
| PUT | `/api/lego/board` | Save board body |
| POST | `/api/lego/apply-toolbelt` | Sync enabled optional limbs |

## Smoke

1. Open LEGO page (stack frontend running)
2. Place `wiki` + `extract`, connect an edge, Save
3. Apply to Toolbelt → Eve Toolbelt shows those limbs ON
4. Reload LEGO → board restores
5. Confirm Memory was not auto-written

## Human index

[`C:/Empire_Workbench/03_Active_Tools/LEGO_INDEX.md`](file:///C:/Empire_Workbench/03_Active_Tools/LEGO_INDEX.md)
