---
name: desktop-commander-mcp
description: Installs and configures Desktop Commander MCP, an MCP server (npm package @wonderwhy-er/desktop-commander) that gives MCP-compatible AI clients terminal command execution, process management, file search/edit, and in-memory code execution (Python/Node.js/R) plus instant CSV/JSON/Excel analysis on the user's own machine. Use when a user wants to give a local MCP client the ability to run shell commands, edit/search files, or analyze local data files. Touches Build1's Nervous System (FastMCP) — this is an additional MCP server that can run alongside FastMCP's own tools, fully local.
icon: monitor
color: Blue
---

# Desktop Commander MCP

An MCP server (built on the MCP Filesystem Server) that lets any MCP-compatible AI client run terminal
commands (including long-running/interactive processes), search and edit files, execute code in memory
across Python/Node.js/R without saving files, and analyze CSV/JSON/Excel data on request — all on the user's
own machine, with no cloud API token cost.

## Install (choose based on client and OS)
1. **npx, auto-updating (requires Node.js):** configure the MCP client to launch the server via
   `npx @wonderwhy-er/desktop-commander`, following the client's own "add an MCP server" config format
   (command + args entry in its MCP config file).
2. **Global npm install (pinned version, no auto-update):** `npm install -g @wonderwhy-er/desktop-commander`,
   then point the client config at the installed binary path instead of `npx`.
3. Restart the MCP client after editing its config so it picks up the new server.

## Usage patterns
- Terminal execution: ask the connected agent to run a shell command; it is executed via this MCP server on
  the local machine.
- File search/edit: request file edits/searches by path; the server exposes filesystem tools directly.
- In-memory analysis: ask for CSV/JSON/Excel summaries without writing intermediate scratch files.

## Build1 Integration
- This is a second, general-purpose local MCP server — it can run **alongside** Build1's own **FastMCP**
  tool server, both exposed to the same local Ollama-driven agent client, without conflicting (each server
  registers its own tool names).
- Use it for ad-hoc terminal/file tasks during Build1 development; keep Build1's actual product-facing
  tools (PocketBase queries, Cognee memory calls, etc.) inside the project's own FastMCP server rather than
  bolting them onto Desktop Commander.
- No cloud dependency — matches Build1's zero-cloud requirement as-is.
