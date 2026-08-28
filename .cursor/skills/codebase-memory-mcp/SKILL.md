---
name: codebase-memory-mcp
description: Installs and operates codebase-memory-mcp, a fast local MCP server that indexes a codebase into a structural code-intelligence graph (symbols, references, cross-language relationships) for AI coding agents to query. Use when the user wants an agent to deeply understand a large or unfamiliar codebase, needs fast structural code search/navigation across many languages, or asks to "index this project" for better code context. Touches Build1's Nervous System (FastMCP) as a companion local MCP server, distinct from Cognee's conversational/document memory graph.
icon: database
color: Blue
---

# codebase-memory-mcp: local code intelligence MCP server

codebase-memory-mcp is a zero-dependency, pure-C code intelligence engine exposed as an MCP server. It
full-indexes an average repo in milliseconds (reference benchmark: the Linux kernel, ~28M LOC, in ~3
minutes) and supports 158 languages plus a "Hybrid LSP" mode for 10 languages, answering structural
questions (symbol definitions/references, call graphs, cross-file relationships) far faster than plain
grep/embedding search.

## Setup
1. Run the project's one-line install script (macOS/Linux) to fetch the prebuilt binary.
2. Register it as an MCP server in the AI client's MCP config (command + working directory pointing at the
   repo to index).
3. Trigger an initial index of the target codebase; re-index incrementally as files change (check the
   project's docs for a watch/incremental-index flag vs. a manual re-run).

## Usage patterns
- "Index this project" → run the index command against the repo root.
- "Where is X defined / who calls X?" → query symbol definitions/references through the MCP tool calls this
  server exposes, rather than falling back to grep once the index exists.
- Cross-language relationship questions (e.g. a Python FastMCP tool calling into a shared Rust/C module) are
  where this tool adds the most value over plain text search.

## Build1 Integration
- Runs as its own local MCP server, alongside Build1's **FastMCP** tool server and, optionally, Desktop
  Commander MCP — all local, no cloud calls.
- Distinct from **Cognee 1.0**: Cognee holds Build1's conversational/document memory graph; this tool holds a
  purely structural *code* graph (symbols/call graphs) of the Build1 codebase itself. Use Cognee for "what did
  we discuss/decide", use codebase-memory-mcp for "how does this code work/connect."
- Useful when onboarding a local Ollama-driven coding agent onto the Build1 repo so it can navigate
  PocketBase schema code, FastMCP tool definitions, and the HTMX/Alpine frontend without re-reading the whole
  tree each time.
