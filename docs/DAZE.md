# DAZE — EMPIRE Time Reclaim (Phase 5)

Local **24-hour radial day** for the Architect. PocketBase `day_blocks` + HTMX/Alpine UI — no Firebase, no React.

Visual language follows the [daze-murex.vercel.app](https://daze-murex.vercel.app/) reference: deep `#040814` canvas, cyan ticks/rings, neon sector colors, red-pink now needle.

## Open

http://127.0.0.1:8080/daze.html

Compact layout: dial left, blocks/editor right. **Embed** (Eve dock carousel): http://127.0.0.1:8080/daze.html?embed=1

**Eve dock screens** (› arrow): **Dial** → **Schedule** → **Blocks**. Reusable pattern lives in `frontend/tool-dock.css` (blueprint for other tools).

In Eve Workbench, enable **Time Reclaim**, open the **DAZE** dock tab, swipe **›** for schedule & appointments. Eve receives which screen is visible.

## Features

| Feature | Notes |
|---------|--------|
| Radial dial | Midnight at top, clockwise; 24 hour ticks (labels every 3h, major every 6h) |
| Planned + actual | Dual rings (outer planned, inner actual) or single-phase view |
| Conflict glow | Overlapping blocks in the same phase glow red |
| Live clock | Center **HH:MM** readout on today's date (updates every 30s) |
| Now needle | White spoke + dot on today's date |
| Free windows | Gaps ≥30 minutes (planned when viewing both) |
| Kind colors | focus / body / admin / creative / rest / other |

## Eve (Toolbelt **Time Reclaim**, default OFF)

| Tool | Purpose |
|------|---------|
| `daze_list_day` | Blocks + conflicts for a date |
| `daze_upsert_block` | Add or update a block (minutes 0–1440) |
| `daze_free_windows` | Free arcs for coaching |
| `daze_compare_phases` | Planned vs actual summary + coaching hints |

Skill: `skill-daze-time.md` · MCP: `empire-daze` · Cursor `.cursor/mcp.json`

## API (Workbench proxy)

| Route | Method |
|-------|--------|
| `/api/daze/day?date=&phase=planned\|actual\|both` | GET |
| `/api/daze/free?date=&phase=&min_minutes=` | GET |
| `/api/daze/compare?date=` | GET |
| `/api/daze/block` | POST (upsert; include `id` to update) |
| `/api/daze/block?id=` | DELETE |

Direct PocketBase remains at `http://127.0.0.1:8090/api/collections/day_blocks/records` but the UI uses the proxy.

## PocketBase schema

Collection `day_blocks`: `date`, `title`, `start_minute`, `end_minute`, `kind`, `phase` (`planned`|`actual`), `notes`, `color`.

Migration: `backend/pocketbase/pb_migrations/1700000002_day_blocks.js`

## Live product reference

The React/Firebase Daily OS at https://daze-murex.vercel.app/ is a **design reference only**. EMPIRE does not sync to it.

Product profile + ingest: `scripts/ingest-daze-product.ps1` → Cognee dataset (optional).

## Smoke (Architect T-02)

1. Add two overlapping planned blocks → red conflict on dial + banner
2. Enable **Time Reclaim** → ask Eve "What's free today?"
3. Toggle **Planned + actual** view → inner/outer rings
4. Optional: `daze_compare_phases` for drift coaching
