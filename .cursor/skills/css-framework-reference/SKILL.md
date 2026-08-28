---
name: css-framework-reference
description: Consolidated CSS component/markup reference spanning Bootstrap, Flat UI, Foundation for Sites, daisyUI, Ratchet, and Photon. Given a requested UI component (button, card, modal, navbar, grid, switch, off-canvas, carousel, etc.), returns the correct classes/markup for that framework. Activate when building or styling pages for the Build1 Frontend (HTMX & Alpine.js); no code execution, this is a lookup skill.
icon: layout-grid
color: Purple
---

# CSS Framework Component Lookup

Reference/snippet lookup across six CSS toolkits. There is nothing to run — map the user's requested
component to the right markup below, or point to the framework's own docs/live component reference for
anything not covered here.

## 1. Pick the framework
| Framework | Best for | Notes |
|---|---|---|
| **Bootstrap 5** (twbs/bootstrap) | General-purpose components, 12-col grid | `data-bs-*` attrs, widest ecosystem |
| **Flat UI** (designmodo/Flat-UI) | Flat-design restyle of Bootstrap + extra widgets (switch, slider, tags input) | Built ON TOP of Bootstrap — same markup for standard components |
| **Foundation for Sites** | XY Grid (Flex-based), off-canvas, reveal modal, orbit carousel | `data-*` attrs, `Foundation.init()` |
| **daisyUI** | Tailwind-based utility components | Requires Tailwind CSS installed first |
| **Ratchet** | Mobile-app-style prototypes in plain HTML | Static, use a tagged release not `master` |
| **Photon** | Electron desktop app chrome (toolbars, panes, window controls) | CSS/markup only, no JS behavior |

## 2. Component → markup quick table
| Component | Bootstrap | Foundation | daisyUI | Flat UI / Ratchet / Photon |
|---|---|---|---|---|
| Button | `<button class="btn btn-primary">` | `<a class="button primary">` | `<button class="btn btn-primary">` | Flat UI: same as Bootstrap. Ratchet: `<button class="btn btn-primary">` |
| Card | `.card > .card-body > .card-title/.card-text` | `.card > .card-divider/.card-section` | `.card > .card-body > .card-title` | Photon: `.pane-group > .pane` for panels |
| Modal | `.modal.fade` + `data-bs-toggle="modal"` | `.reveal[data-reveal]` + `data-open="id"` | `.modal` + `<label>` trigger pattern | Ratchet: `.modal` |
| Nav/Toolbar | `.navbar > .navbar-brand/.collapse` | `.top-bar > .top-bar-left/.top-bar-right` | `.navbar > .navbar-start/.navbar-end` | Ratchet: `.bar.bar-nav`. Photon: `.toolbar-header` |
| Grid | `.container > .row > .col-md-6` | `.grid-x.grid-margin-x > .cell.medium-6` | Tailwind `grid grid-cols-2` | — |
| Switch/Toggle | (utility only, no native switch) | `.switch` | `.toggle` | Flat UI: `.switch` (signature component) |
| Carousel/Slider | `.carousel[data-bs-ride]` | `.orbit[data-orbit]` | `.carousel` | Flat UI: `.slider` (range input) |
| Off-canvas / Drawer | `.offcanvas` | `.off-canvas[data-off-canvas]` | `.drawer` | Ratchet: `.slider` push nav |

If a request isn't in this table, check the framework's own live docs (getbootstrap.com, get.foundation,
daisyui.com/components, or the repo's `docs/`/`components.html`) rather than guessing exact class names.

## 3. Setup (pick the simplest option for the user's stack)
- **CDN** (fastest, no build step): link the framework's official CSS `<link>` in `<head>`; use the version-specific
  URL from that framework's own docs site rather than guessing one.
- **npm**: `npm install bootstrap` / `foundation-sites` / `daisyui` (as a Tailwind plugin) / clone Ratchet or Photon
  and use their `dist/` compiled assets.
- Flat UI and Ratchet ship compiled CSS/JS in `dist/`; Photon ships `css/photon.css` + a `fonts/` icon font.

## Build1 Integration
Build1's frontend is **HTMX + Alpine.js** — there is no competing JS framework to remove, but avoid double-driving
interactivity:
- Use these toolkits **for CSS classes only**. Do not wire up each framework's own JS bundle (`bootstrap.bundle.js`,
  `foundation.js`, Ratchet's `push.js`) for interactive behavior — that duplicates what Alpine.js already does.
- Drive show/hide, toggles, and tab state with **Alpine.js** (`x-data`, `x-show`, `:class`) instead of
  `data-bs-toggle` / `data-open` / `data-orbit` JS init.
- Drive data fetching/form submission with **HTMX** (`hx-get`, `hx-post`, `hx-target`) against FastMCP-backed or
  PocketBase-backed endpoints instead of any framework's AJAX helpers.
- Photon is only relevant if Build1 ships an Electron desktop shell; for a browser-served HTMX/Alpine frontend,
  skip it unless explicitly building a desktop wrapper.
