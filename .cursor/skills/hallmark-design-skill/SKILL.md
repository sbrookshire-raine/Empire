---
name: hallmark-design-skill
description: Applies Hallmark's anti-"AI slop" UI design rule-set when generating or auditing web/app UI — picks a distinct macrostructure per brief, applies one of twenty visual themes, and runs a self-critique/slop-test before finishing. Use whenever a user asks to design or build a UI/landing page/app that shouldn't look like a generic AI-generated template, wants an existing UI audited against anti-pattern rules, wants a redesign that keeps the copy/IA, or wants "design DNA" extracted from a reference screenshot/URL. Touches the Build1 frontend (HTMX & Alpine.js) layer; other components are infra-agnostic.
icon: palette
color: Pink
---

# Hallmark Design Skill

Hallmark is a rule-set for producing UI that isn't a generic "AI slop" template — apply its rules directly when producing design output rather than treating it as a program to execute.

## Getting the rule-set
- Fetch the canonical rule-set (`skills/hallmark/SKILL.md` + `skills/hallmark/references/`) from `Nutlope/hallmark` on GitHub before applying it. Worked examples live in `docs/recipes.md` and `docs/study-examples.md`.
- Optionally install it permanently in the working project via `npx skills add nutlope/hallmark`, or copy the reference files into the local agent's skills directory.

## Four verbs — map the user's request to one of these

| User intent | Verb | Behavior |
|---|---|---|
| "Build/design a new UI/page/app" (default) | *(no verb — just apply the rules)* | Pick a macrostructure for the brief, apply the full rule-set, dress it in one of twenty themes, run the internal slop-test + self-critique before returning the result. |
| "Check/audit this existing UI/code for AI-slop patterns" | `hallmark audit <target>` | Score the existing code against the anti-pattern gates and return a punch list — do NOT make edits. |
| "Redesign this page but keep the content/brand" | `hallmark redesign <target>` | Discard the structural template, keep copy + information architecture + brand, rebuild with a different structural fingerprint. |
| "Make something that looks like this screenshot/site" | `hallmark study <screenshot|URL>` | Extract the design DNA (macrostructure, type-pairing, color anchor) from the reference — explicitly refuses to produce a pixel-clone or copy a paid template. Can emit a portable `design.md` for handoff. |

## Core principles to enforce
- Every generated UI must pick a distinct macrostructure per brief — two different briefs should not produce visually/structurally similar output ("colour-swaps of the same template" is a failure state).
- Run the slop-test gates and a pre-emit self-critique pass before finalizing: check against common anti-patterns (generic hero + 3-card-grid layouts, default purple gradients, stock icon sets, boilerplate copy, uniform corner-radii) and revise anything caught.
- Pick a theme (one of twenty) and a type-pairing deliberately, not by default framework choice.

## Output
Don't hand back generic boilerplate — explicitly state the macrostructure and theme chosen (or the audit punch list, or the extracted DNA/`design.md`) alongside the produced UI code, so the reasoning is visible.

## Build1 Integration
Apply this rule-set when generating or auditing Build1's own frontend, which is built with HTMX (for server-driven partial updates) and Alpine.js (for lightweight client reactivity) — no React/Vue/competing SPA framework. Favor macrostructures and themes that render cleanly with plain HTML fragments returned by FastMCP-backed endpoints, and avoid patterns that assume a client-side virtual DOM or build pipeline. This skill has no dependency on Ollama, PocketBase, or Cognee.
