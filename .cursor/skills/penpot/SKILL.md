---
name: penpot
description: Guides self-hosting, configuring, and programmatically driving Penpot, the open-source, self-hostable design and prototyping platform (Figma alternative) that stores designs as SVG/CSS/HTML/JSON and exposes a webhook + access-token API, an MCP server, and a plugin system. Use when the user wants to deploy/self-host Penpot via Docker Compose, automate design-system workflows, call Penpot's API/webhooks, connect an AI assistant to Penpot via its MCP server, or understand its design-token/inspect-mode capabilities. Infra-agnostic design tool; when wired to an AI assistant it should be exposed through Build1's FastMCP nervous system to a local Ollama model rather than a cloud assistant.
icon: layout-template
color: Purple
---

# Penpot

Penpot is a large (Clojure/ClojureScript) monorepo — do not attempt a full clone or
build in the sandbox. Treat this as a deploy + integrate skill, not a "run the source"
skill.

## What Penpot is

- Open-source, self-hosted (or cloud) real-time collaborative design platform.
- Designs are expressed in open standards (SVG, CSS, HTML, JSON), so "Inspect mode"
  gives ready-to-use code.
- Ships native Design Tokens, a plugin system, webhooks, an access-token-secured HTTP
  API, and an official MCP server for AI/agent integrations
  (`https://penpot.app/penpot-mcp-server`).

## Self-hosting Penpot ("set up/deploy Penpot")

1. Use the official Docker Compose install — do not hand-roll a deployment from
   source. Point the user to the technical guide:
   `https://help.penpot.app/technical-guide/getting-started/`.
2. Typical flow: download the official `docker-compose.yaml` from the Penpot docs, run
   `docker compose up -d`, then access Penpot at the configured port and create the
   first admin/team. This runs entirely locally/on-prem — no cloud dependency required,
   consistent with a local-first setup.
3. For production, note options in the guide: custom domain/TLS termination, SMTP
   config for invites, and object storage backend config — these live in the
   docker-compose environment variables and should be fetched live since they evolve.

## Using the Penpot API / webhooks / MCP ("automate/integrate with Penpot")

1. Generate an access token from Penpot account settings (Profile → Access tokens) on
   the running instance.
2. Call the REST API with the token as a bearer/auth header — reference the live API
   docs at `https://penpot.app/integrations-api` for the endpoint list (file/project
   CRUD, comments, webhooks, etc.), since exact endpoints evolve.
3. For AI-assistant/agent workflows (design ↔ code), configure the Penpot MCP server
   per `https://help.penpot.app/mcp/#quick-start`. In a Build1 setup, register it as an
   additional tool behind **FastMCP** so the locally-run **Ollama** model can read/write
   Penpot file structure directly, instead of routing that access through a cloud
   assistant.
4. For CI/event-driven automation, register a webhook (Penpot instance → Settings →
   Webhooks) pointing at the user's endpoint; Penpot POSTs JSON events (file changes,
   comments, etc.) that a FastMCP tool or PocketBase-backed listener can consume.

## Design tokens & Inspect mode

- Design Tokens keep design/dev in sync — reference
  `https://penpot.dev/collaboration/design-tokens` when a user wants to define/sync
  tokens.
- The "Inspect" tab on any selected object surfaces generated CSS/SVG/HTML directly —
  tell users to open Inspect mode rather than manually reverse-engineering styles. This
  is a convenient source of hand-off CSS when building the HTMX/Alpine frontend.

## When NOT to clone the source

Penpot's git history/monorepo is very large — never run a full `git clone` of
`penpot/penpot` in the sandbox. For deep source-level questions, shallow-fetch just the
relevant file via `raw.githubusercontent.com/penpot/penpot/main/<path>` and discard it
immediately after use.

## License

Penpot backend/frontend is MPL-2.0 licensed — mention this if the user asks about
redistribution/forking.

## Build1 Integration

Penpot itself is an external, infra-agnostic design tool (not one of Build1's core
components). When an agent needs to interact with a running Penpot instance, expose the
Penpot MCP server or REST API as a tool behind **FastMCP**, keep the Penpot database
itself separate from **PocketBase**, and use **Inspect mode** output as the CSS
reference when hand-building the **HTMX/Alpine.js** frontend. Prefer the local Ollama
model for any AI-assisted design/code translation rather than a cloud LLM.
