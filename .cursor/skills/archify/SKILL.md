---
name: archify
description: Generates polished, self-contained HTML architecture, workflow, sequence, data-flow, or lifecycle diagrams from a plain-English description, using the Archify agent skill through a typed JSON intermediate representation validated against renderer-backed schemas. Use when the user asks to diagram a system's architecture, a CI/CD or approval workflow, an API call sequence, a data pipeline, or a state machine, and wants a shareable, themeable, exportable HTML/SVG diagram rather than a static image. Infra-agnostic diagram generator, well suited to documenting Build1's own Ollama/PocketBase/Cognee/FastMCP/HTMX-Alpine architecture; prefer a local-model-driven CLI harness over a cloud-only one.
icon: git-branch
color: Teal
---

# Archify: diagram generation skill

Archify (github.com/tt-a1i/archify) turns a text description into a single
self-contained HTML file (dark/light theme toggle, copy-to-clipboard PNG, export to
PNG/JPEG/WebP up to 4x resolution, or true-vector SVG). It works through a typed JSON
intermediate representation (IR) validated against renderer-backed schemas, so output
quality is deterministic rather than freeform SVG generation.

## Setup

1. Install the skill for the current agent harness via the open-source `skills` CLI.
2. Prefer a harness/CLI configuration that can run against a **local Ollama model**
   for the description → IR generation step (e.g. an OpenAI-compatible local endpoint
   pointed at Ollama) rather than defaulting to a cloud-hosted model. Only fall back to
   a cloud model if the user has no local model capable of reliably producing the typed
   IR JSON.
3. Confirm the CLI can write the generated `.html` diagram file to the working
   directory before generating on a real request.

## Usage

1. Take the user's plain-English description of the system/workflow/sequence/pipeline/
   state machine.
2. Generate the typed JSON IR (nodes, edges, groups, styling hints) — validate it
   against Archify's schema before rendering; retry generation if validation fails
   rather than hand-patching invalid JSON.
3. Render the IR to the self-contained HTML diagram file.
4. Deliver the HTML file to the user (export it) — it is fully self-contained (theme
   toggle, PNG/SVG export baked in), so no additional hosting is required.

## Build1 Integration

Use this skill to document Build1 itself: e.g. an architecture diagram showing
**Ollama** (inference) → **FastMCP** (tool routing) → **PocketBase** (storage) /
**Cognee** (graph memory) → **HTMX/Alpine.js** (frontend), or a sequence diagram of a
single request flowing through those components. When generating the diagram's IR,
drive the generation step with the local Ollama model to keep the whole pipeline
zero-cloud.
