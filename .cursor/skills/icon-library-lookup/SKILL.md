---
name: icon-library-lookup
description: Consolidated icon/flag lookup covering five static SVG sets — Bootstrap Icons, Heroicons, Ionicons, Tabler Icons, and Flag Icons. Maps a plain-English icon or country-flag request to the correct icon name, CSS class, or inline snippet. Use whenever a user building the Build1 HTMX/Alpine.js frontend asks for an icon, glyph, or flag. Touches: Frontend (HTMX & Alpine.js) only — infra-agnostic with respect to Ollama, PocketBase, Cognee, and FastMCP.
icon: shapes
color: Bronze
---

# Icon & Flag Library Lookup (5 sets, consolidated)

These are static, offline-friendly SVG/webfont libraries — no build step, no server, no LLM call required. Your job is reference/lookup: map a concept to the right name, verify it exists in the chosen set, and hand back a snippet the HTMX/Alpine frontend can drop in directly. Never invent a name that isn't in the set.

## 1. Pick the right library

| Library | Repo | Size | Variants | Naming | Best for |
|---|---|---|---|---|---|
| Bootstrap Icons | twbs/icons | 2,000+ | outline / `-fill` | kebab-case | general UI, webfont class |
| Heroicons | tailwindlabs/heroicons | 300+ | 24px outline+solid, 20px solid, 16px solid | kebab-case (svg) | Tailwind-flavored UIs |
| Ionicons | ionic-team/ionicons | ~1,300 | filled (default) / `-outline` / `-sharp` | kebab-case | `<ion-icon>` web component — pairs well with HTMX since it needs no build |
| Tabler Icons | tabler/tabler-icons | 6,000+ | `outline/` (default) / `filled/` | kebab-case, check `aliases.json` for renames | largest catalog, stroke icons |
| Flag Icons | lipis/flag-icons | 250+ countries + regional (`eu`, `un`, `gb-eng`, etc.) | 4:3 rect / `1x1` square | ISO 3166-1-alpha-2 lowercase code | country/region flags |

If the project already uses one library, stay consistent — don't mix multiple icon sets in the same UI unless asked.

## 2. Resolve request → name

1. Extract the concept ("delete"→trash, "settings"→cog/settings/adjustments, "user"→user/user-circle, "search"→search/magnifying-glass, "close"→x/x-mark, "home"→house/home, "add"→plus).
2. Verify the name exists in the chosen set (browse the repo's icon directory or the library's own search site — heroicons.com, tabler.io/icons — before answering). For Tabler, also check `aliases.json` for renamed icons.
3. Pick a style variant appropriate to context: outline for general UI, filled/solid for emphasis or small/dense UI, `-off`/negated variants (Tabler) for disabled states.
4. If unsure between 2-3 close candidates, present them rather than guessing one that may not exist.

## 3. Output snippets (plain HTML — fits HTMX/Alpine, no framework build step)

**Bootstrap Icons — webfont class:**
```html
<i class="bi bi-trash"></i>
```
Or sprite `<use>`: `<svg><use href="bootstrap-icons.svg#trash"></use></svg>`

**Heroicons — inline SVG** (copy from repo's `optimized/24/outline/<name>.svg`):
```html
<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
  <!-- path(s) from the matching heroicon file -->
</svg>
```

**Ionicons — web component** (no build needed, works great with HTMX-rendered fragments):
```html
<script type="module" src="https://unpkg.com/ionicons@latest/dist/ionicons/ionicons.esm.js"></script>
<ion-icon name="heart-outline"></ion-icon>
```

**Tabler Icons — webfont or sprite:**
```html
<i class="ti ti-trash"></i>
<!-- or sprite -->
<svg><use href="tabler-sprite.svg#tabler-trash"></use></svg>
```

**Flag Icons — CSS class span:**
```html
<span class="fi fi-us"></span>          <!-- 4:3 -->
<span class="fi fi-us fis"></span>      <!-- square -->
<div class="fib fi-de" style="width:40px;height:30px;"></div>  <!-- background-image variant -->
```

## 4. Self-host, don't CDN-depend

Build1 is zero-cloud/local-first. Prefer downloading each library's font/sprite/CSS files once and serving them as static assets alongside the HTMX/Alpine frontend, rather than pointing `<script src>`/`<link href>` at jsdelivr/unpkg CDNs. This keeps the UI fully functional offline/on a LAN with no external network dependency.

```bash
# Example: vendor Bootstrap Icons locally
curl -LO https://github.com/twbs/icons/releases/latest/download/bootstrap-icons-<ver>.zip
unzip bootstrap-icons-<ver>.zip -d frontend/static/icons/bootstrap-icons
```
Repeat the same pattern (download release asset → `frontend/static/icons/<lib>/`) for Heroicons, Ionicons, Tabler, and Flag Icons.

## Build1 Integration

Icons/flags are pure static frontend assets — they don't touch Ollama, PocketBase, Cognee, or FastMCP. Vendor the chosen library's files under the frontend's `static/` directory (served by whatever serves your HTMX pages) and reference them via class/`<use>`/`<ion-icon>`. Alpine.js can toggle an icon's name/class reactively (`:class`, `x-bind`) purely client-side with zero network round-trips, which fits the local-first design. If icon names are user-configurable data (e.g. a per-user favorite icon), store just the icon *name string* in PocketBase and resolve it to markup client-side using this lookup — don't store rendered SVG blobs in the database.

For the full per-icon name catalog of any set, consult that library's own repo/site rather than trying to enumerate thousands of names here — this file intentionally stays a resolution *process*, not an exhaustive index.
