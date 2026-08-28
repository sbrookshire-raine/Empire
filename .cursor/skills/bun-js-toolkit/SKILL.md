---
name: bun-js-toolkit
description: Runs Bun, an all-in-one fast JavaScript/TypeScript runtime, package manager, test runner, and bundler (single executable `bun`) that is a drop-in replacement for Node.js. Use when a user wants to install dependencies, run a script, execute/bundle a TS or JS file, run tests, or execute a package one-off (bunx) for a JavaScript/TypeScript project, or explicitly asks to use Bun instead of npm/yarn/pnpm/Node. Infra-agnostic JS tooling; useful as the local dev/build tool for Build1's HTMX/Alpine.js frontend assets and for scripting a FastMCP server's supporting Node tooling, if any.
icon: zap
color: Yellow
---

# Bun — JavaScript/TypeScript Toolkit

Repo `oven-sh/bun` ships a single binary `bun` that replaces Node.js, npm/yarn/pnpm, a
test runner, and a bundler. It has fast startup and native TS/JSX support (no separate
transpile step needed).

## Install

Supports Linux (x64/arm64, kernel >= 5.6), macOS (x64/Apple Silicon), Windows
(x64/arm64). Install via the official installer script, then verify with `bun --version`.

## Common commands

1. Install dependencies: `bun install`
2. Run a script/file: `bun run <script>` or `bun <file.ts>` directly (TS/JSX run
   without a separate build step).
3. Bundle for production: `bun build ./src/index.ts --outdir ./dist`
4. Run tests: `bun test`
5. One-off package execution: `bunx <package>`

## Build1 Integration

Entirely infra-agnostic tooling with no direct tie to Ollama/PocketBase/Cognee/
FastMCP. Since Build1's frontend is **HTMX + Alpine.js** (no SPA framework, minimal JS
by design), use Bun sparingly — mainly to bundle/minify the small amount of Alpine.js
glue code or run any Node-based build/lint scripts a FastMCP or PocketBase tooling
project needs, not to introduce a heavier JS framework.
