---
name: opencut-dev-setup
description: Sets up and runs the in-progress OpenCut monorepo rewrite (web, api, desktop apps; Rust core) for local development using proto and moon, and clarifies when to redirect a user to the stable opencut-classic app instead. Use when a user wants to build/run this OpenCut rewrite locally, understand its planned Editor API/MCP server/plugin architecture, or just wants a working video editor today. Infra-agnostic — a standalone video-editor project, not a Build1 stack component.
icon: film
color: Orange
---

# OpenCut — dev environment setup (rewrite branch)

**Important context to give the user first:** the `OpenCut-app/OpenCut` repository is a from-scratch rewrite
of OpenCut, a free/open-source video editor. It is **not yet usable as an editor** and is **not accepting
outside contributions** while the architecture is being designed. The rewrite adds: an Editor API, a
plugin-first architecture, a shared Rust core across desktop/mobile/browser, an MCP server for AI agents,
headless/automation batch rendering, and an in-editor scripting tab.

- If the user wants a **working video editor now**, point them to the stable app: `opencut-app/opencut-classic`
  (also what powers the public opencut.app site).
- If the user wants to **follow along with or run the rewrite locally**, use the steps below.

## 1. Install the toolchain
1. Install `proto` (the toolchain version manager this monorepo pins tool versions with).
2. Use `proto` to install the pinned Node/Rust toolchain versions declared in the repo's `.prototools`.
3. Install `moon` (the monorepo task runner) via `proto` as well.
4. Run `moon` project setup/bootstrap tasks (e.g. `moon run :install` or the equivalent declared task) to
   pull dependencies for the `web`, `api`, and `desktop` workspaces plus the Rust core.

## 2. Run locally
- Use the monorepo's declared `moon` tasks (e.g. `moon run web:dev`, `moon run api:dev`) rather than invoking
  each workspace's package manager directly, so task dependencies/build order stay correct.
- Expect an incomplete/changing feature set — this is pre-alpha rewrite code.

## Build1 Integration
Infra-agnostic. OpenCut is an unrelated open-source video editor; it does not integrate with Ollama,
PocketBase, Cognee, FastMCP, or the HTMX/Alpine frontend. Only relevant if a user is separately building or
contributing to OpenCut itself.
