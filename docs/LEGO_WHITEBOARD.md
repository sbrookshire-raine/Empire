# LEGO Whiteboard

Manifesto Phase 4 — compose forged EMPIRE limbs as short-name bricks on a local canvas.

**URL:** http://127.0.0.1:8080/lego.html

## What it does

- Palette of bricks from [`config/lego-bricks.json`](../config/lego-bricks.json)
- **Workflow recipes** from [`config/lego-recipes.json`](../config/lego-recipes.json) — Research Partner, Truth Drift, Morning Coach, Document Intake
- Drag / place bricks; connect **out → in** ports (auto-picks compatible port kind)
- **Validate** — unknown bricks block Apply; port mismatches show warnings
- **Save** board JSON under `C:/Empire_Workbench/03_Active_Tools/lego_boards/default.json`
- **Apply to Toolbelt** — optional **merge** keeps limbs already ON in Toolbelt
- Core bricks (`memory`, `tasks`, `docling`, `gpu`) are never Toolbelt-gated

## What it does not do

- No React / tldraw / Excalidraw
- Edges do **not** auto-run Eve or auto-`cognee_remember`
- Harvested `*_flattened.txt` files are not palette bricks (use Tool Forge)
- Research Partner session mode is Eve Workbench-only (not a LEGO brick)

## API

| Method | Path | Role |
|--------|------|------|
| GET | `/api/lego/bricks` | Catalog |
| GET | `/api/lego/recipes` | Recipe list |
| POST | `/api/lego/recipe` | Instantiate recipe `{ id }` |
| GET | `/api/lego/board` | Load default board |
| PUT | `/api/lego/board` | Save board body |
| POST | `/api/lego/validate` | Validate nodes/edges |
| POST | `/api/lego/apply-toolbelt` | Sync enabled optional limbs `{ merge: true }` optional |

## Smoke

1. Open LEGO page (stack frontend running)
2. Load **Research Partner** recipe → Validate → Save
3. Apply to Toolbelt with **Merge** checked → Eve Toolbelt shows wiki/github/web ON (and keeps other limbs)
4. Reload LEGO → board restores
5. Confirm Memory was not auto-written

## Human index

[`C:/Empire_Workbench/03_Active_Tools/LEGO_INDEX.md`](file:///C:/Empire_Workbench/03_Active_Tools/LEGO_INDEX.md)
