---
name: visual-designer
description: Build visual node editors and interactive HTML pipeline tools, using a design-pattern knowledge base drawn from ComfyUI, React Flow, LiteGraph, Drawflow, and Flowise. Activate for "build a node editor", "visual pipeline tool", "what color should wires be", "design this as a graph UI". Frontend-facing skill for Build1: renders as plain HTML/CSS/JS wired to HTMX/Alpine.js rather than a heavy SPA framework.
icon: layout
color: Pink
---

# Visual Designer

## Activate when

'build a node editor' · 'visual pipeline' · 'node graph UI' · 'design a canvas' ·
'wire colors' · 'bezier curves' · 'Sound Blocks style'

## Knowledge base — read `references/` on demand

Keep each source's full token dump as its own file under `references/` rather than
inline in this document:

| Source | File | Contains |
|---|---|---|
| ComfyUI | `references/comfyui.json` | Slot colors, card shape, execution glow `#ffcc00`, 80+ CSS tokens |
| React Flow (n8n-style) | `references/reactflow_n8n.json` | Bezier calcOffset, handle CSS, ghost paths, animated edges |
| LiteGraph / Drawflow | `references/drawflow_litegraph.json` | Grid snap, shadow reset, port protrusion, slot height |

## Scripts (place under `scripts/`)

`ui_tools.py` — `bezier_path`, `type_color`, `design_tokens`, `node_card_html`,
`edge_svg_html`, `snap_to_grid`. See `references/10_ui_design.md` for full signatures.

## Quick start

1. Pick the reference palette/behavior closest to what the user wants (ComfyUI-style
   slots, n8n-style bezier edges, or LiteGraph-style grid-snap canvas).
2. Generate the node/edge HTML with `ui_tools.node_card_html` / `ui_tools.edge_svg_html`,
   plain CSS for styling, and small `ui_tools.snap_to_grid` logic for drag behavior.
3. Wire interactivity (drag, connect, select) with **Alpine.js** components and use
   **HTMX** for anything that needs to round-trip to the backend (saving a pipeline,
   loading a saved graph) instead of a client-side SPA framework.

## Build1 Integration

Persist saved node graphs (nodes/edges/positions as JSON) in **PocketBase**. If the
canvas represents an actual AI pipeline, the pipeline's execution/tool-calling logic
should be served by **FastMCP** and run against the local **Ollama** model — this skill
only covers the visual editor, not pipeline execution.
