---
name: design-researcher
description: Research and extract visual design patterns from any app, repo, or tool, outputting structured JSON design tokens for reuse. Activate for "research how X is designed", "mine design patterns from this app", "extract CSS tokens from this repo". Infra-agnostic research skill; its output tokens are consumed when styling Build1's HTMX/Alpine.js frontend.
icon: eye
color: Teal
---

# Design Researcher

## Activate when

"research how X is designed" · "mine design patterns from this repo" · "what design
decisions does X make" · "extract CSS tokens" · "source design patterns for my UI"

## Workflow

1. Identify the target app/repo/tool and the specific design surface to study (colors,
   spacing, typography, component shapes, motion, etc.).
2. Fetch only the relevant source files (CSS/SCSS/design-token JSON, component
   markup) or Inspect-mode output rather than the whole codebase.
3. Extract concrete values (hex colors, spacing scale, font stacks, border-radius,
   shadow/elevation values, transition timings) into a structured JSON design-token
   object.
4. Save the token set under this skill's `references/` directory (e.g.
   `references/<source>.json`) so future lookups don't re-scrape the same source.
5. Summarize the key patterns for the user and hand back the JSON tokens directly.

## Build1 Integration

Infra-agnostic research step with no dependency on Ollama/PocketBase/Cognee/FastMCP.
Feed the resulting JSON design tokens into the CSS used by Build1's **HTMX + Alpine.js**
frontend (e.g. as CSS custom properties or a small Tailwind/vanilla-CSS token file) so
the same visual language mined from the reference app is reused consistently there.
