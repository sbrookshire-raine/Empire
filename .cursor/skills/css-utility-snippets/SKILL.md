---
name: css-utility-snippets
description: Consolidated static CSS reference covering entrance/exit animations (Animate.css), atomic utility classes (Basscss), a fixed color palette (clrs.cc), a browser reset (normalize.css), a legacy fixed-width grid (960 Grid System), hover/interaction effects (Hover.css), browser feature-detection snippets (Modernizr), and tileable background patterns (Subtle Patterns). Activate when styling an HTMX + Alpine.js page and the user asks for a specific animation, utility class, hex color, reset behavior, grid layout, hover effect, feature check, or background texture — all are drop-in, no-build-step CSS/JS assets. Touches only the Build1 frontend layer (HTMX & Alpine.js); the other Build1 components (Ollama, PocketBase, Cognee, FastMCP) are not involved.
icon: palette
color: Pink
---

# CSS Utility Snippets

A single reference layer for eight static, no-build CSS/JS libraries commonly used to style lightweight server-rendered frontends like Build1's HTMX + Alpine.js UI. None of these require a bundler, framework, or backend — they are `<link>`/`<script>` includes plus class names. This skill's job is to map a styling request to the right library, class name(s), and copy-pasteable snippet.

## 1. Library catalog

| Library | Purpose | Key classes / usage | Notes |
|---|---|---|---|
| **Animate.css** | ~100 entrance/exit/emphasis/special CSS animations (fade, bounce, zoom, flip, slide, etc.) | `animate__animated animate__bounce` (always pair the base `animate__animated` class with one effect class) | Toggle classes via Alpine (`:class`) or htmx `hx-swap` to trigger on DOM insertion |
| **Basscss** | Atomic/functional CSS: spacing, typography, layout, grid, flexbox, borders, visibility | `.m1`, `.p2`, `.flex`, `.col-4`, `.h1`, `.border`, `.hide` | Compiled, no build step; link `basscss.min.css` |
| **clrs.cc (colors.css)** | Fixed 17-color default web palette | `.bg-navy`, `.navy` (text), `.border--navy`, `.fill-navy`, `.stroke-navy` | Palette: navy #001F3F, blue #0074D9, aqua #7FDBFF, teal #39CCCC, olive #3D9970, green #2ECC40, lime #01FF70, yellow #FFDC00, orange #FF851B, red #FF4136, fuchsia #F012BE, purple #B10DC9, maroon #85144B, white #FFFFFF, silver #DDDDDD, gray #AAAAAA, black #111111 |
| **normalize.css** | Normalizes default browser styling (modern alternative to a full reset) across headings, forms, tables, inputs | No classes — just `<link>` it before your own stylesheet | Explains cross-browser quirks (e.g. button/select font inheritance, sub/sup sizing) |
| **960 Grid System** | Legacy fixed-width (960px) 12/16/24-column layout grid, with RTL variants | `.container_12`, `.grid_1`..`.grid_12`, `.alpha`, `.omega`, `.push_N`, `.pull_N` | Legacy only — for new Build1 pages prefer native CSS Grid/Flexbox (or Basscss's grid classes); use 960 Grid only when replicating an existing fixed-width design |
| **Hover.css** | CSS3 hover/interaction effects for buttons, links, icons (Grow, Pulse, Sink, Rotate, Wobble-*, sweeps, glows, speech bubbles) | Class prefix `hvr-`, e.g. `hvr-grow`, `hvr-underline-from-left`, `hvr-icon-forward` | Icon effects need an inner `<i class="hvr-icon">`; outer element gets the `hvr-icon-*` class |
| **Modernizr** | Runs feature-detect tests (flexbox, webgl, indexeddb, touchevents, css3dtransforms, etc.) | JS: `Modernizr.flexbox`; CSS hook: `.flexbox` / `.no-flexbox` on `<html>` | Async tests need `Modernizr.on('webp', cb)`; build a trimmed custom bundle via `modernizr.build({...})` |
| **Subtle Patterns** | ~350 tileable, subtle background PNG textures (fabric, grunge, denim, paper, argyle, etc.) | `background-image: url(...); background-repeat: repeat;` | CC BY-SA 3.0 — credit the pattern author if used commercially |

## 2. How to answer a request

1. Identify the category (animation, utility spacing/layout, color, reset, grid, hover effect, feature check, or background texture).
2. Pick the matching library from the table and return the exact class name(s) plus a short copy-pasteable snippet (CSS and/or HTML).
3. For **Hover.css**, give the full `.hvr-*` CSS block (not the whole stylesheet) plus the HTML usage example.
4. For **Modernizr**, state whether the test is sync or async, and give both the JS check and the CSS class hook when relevant.
5. For **Subtle Patterns**, match the request to 2-3 likely filename candidates (e.g. "grungy paper" → `asfalt.png`, `bgnoise_lg.png`) rather than inventing a filename; always use `background-repeat: repeat`.
6. If a requested effect/feature/color doesn't exist in the library, say so plainly and suggest the closest real alternative instead of fabricating a class name.

## Example snippets

```css
/* Animate.css trigger */
<div class="animate__animated animate__fadeIn">Loaded via htmx</div>

/* Hover.css Grow effect */
.hvr-grow { display:inline-block; transform:translateZ(0); transition-duration:.3s; transition-property:transform; }
.hvr-grow:hover, .hvr-grow:focus { transform: scale(1.1); }

/* clrs.cc */
.bg-navy { background-color:#001F3F; }

/* Subtle Patterns background */
body { background-image:url("patterns/asfalt.png"); background-repeat:repeat; }
```

## Build1 Integration

All eight libraries are static assets with zero JS-framework dependency — they don't conflict with Alpine.js reactivity or htmx swaps, and add no server load. For a true zero-cloud setup, self-host the CSS/PNG files (e.g. serve them from PocketBase's `pb_public/` static directory) instead of pulling from a third-party CDN. No inference, backend, or memory component is involved — this skill is purely a frontend styling layer.
