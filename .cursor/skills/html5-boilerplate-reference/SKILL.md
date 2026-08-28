---
name: html5-boilerplate-reference
description: Reference guide to the HTML5 Boilerplate static front-end starter template (its index.html head/meta setup, css/js structure, and docs). Use when a user asks for a quick front-end project scaffold, boilerplate HTML head/meta tags, default CSS helper classes, or a specific snippet (robots.txt, site.webmanifest, print styles, 404 page). Frontend-adjacent: use only as a plain HTML skeleton, then wire the Build1 HTMX/Alpine.js frontend on top of it rather than any other JS framework.
icon: layout-template
color: Grey
---

# HTML5 Boilerplate — reference lookup skill

HTML5 Boilerplate is a static starter template (no build tooling required at runtime).
This is NOT an app to execute — treat it as a **catalog of files/snippets** to quote or
scaffold from. The published project lives in `/dist` (mirrored in `/src`); everything
else in the repo (gulpfile, tests) only builds `/dist` and isn't part of the template
itself.

## How to get the project

- Fastest: `npx create-html5-boilerplate new-site && cd new-site && npm install && npm run start`
- Or `npm install html5-boilerplate`, then copy `node_modules/html5-boilerplate/dist/*`
  into the project.
- Or download the release zip and unzip it.
- Only clone this repo directly if the user wants to *contribute to* html5-boilerplate
  itself.

## File map for lookup requests

- `src/index.html` — the canonical HTML skeleton: doctype, `<html class="no-js" lang="">`,
  viewport meta, title, Open Graph placeholder comments, stylesheet/script includes at
  the end of body.
- `src/css/` — base normalize-style resets, print styles (`@media print`), and helper
  classes: `.hidden`, `.visuallyhidden`, `.visuallyhidden.focusable`, `.invisible`, and
  the micro clearfix `.clearfix`.
- `src/404.html` — a standalone placeholder 404 page.
- `src/favicon.ico`, `src/icon.png`, `src/icon.svg` — default icon set.
- `src/site.webmanifest` — default web app manifest (name, icons, theme_color, display).
- `src/robots.txt` — default permissive robots file.
- `src/js/` — placeholder JS entry point.
- `docs/` — full documentation split by topic: `docs/html.md`, `docs/css.md`,
  `docs/js.md`, `docs/misc.md`, `docs/usage.md`, `docs/extend.md`, `docs/faq.md`;
  `docs/TOC.md` indexes them all.

## Answering a user request

1. Identify which artifact they want (head boilerplate, a CSS helper class, robots.txt,
   manifest, print styles, etc.).
2. Quote the exact snippet from the matching `src/` file above, or point to the
   matching `docs/*.md` section for the rationale.
3. If they want to start a new project, give the `npx create-html5-boilerplate new-site`
   quick start instead of raw file contents.
4. Browser support = Browserslist "defaults" (see `.browserslistrc`/README) — mention
   this if asked about compatibility.

## Build1 Integration

Use this template only for its neutral HTML head/meta/CSS scaffold. Do **not** wire in
`src/js/` as a general-purpose app entry point — for Build1, replace it with
**HTMX** attributes for server-driven interactivity and **Alpine.js** for lightweight
client state, served by whatever backend renders the FastMCP/PocketBase-backed pages.
No inference (Ollama) or memory (Cognee) involvement for this skill.
