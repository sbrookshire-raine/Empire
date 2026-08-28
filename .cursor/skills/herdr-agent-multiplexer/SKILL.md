---
name: herdr-agent-multiplexer
description: Installs and operates herdr, a single-binary Rust terminal workspace manager (agent multiplexer, tmux-like) for running and monitoring multiple AI coding agent sessions in parallel panes that persist across detach/reattach and SSH sessions. Use when a user wants to run several agent sessions simultaneously in one terminal, monitor agent status (blocked/working/done) at a glance, detach/reattach to long-running sessions, or have agents programmatically spawn/read/coordinate panes via herdr's socket API. Infra-agnostic developer tool — not coupled to any specific Build1 component, but useful for managing parallel Ollama-backed coding-agent sessions while building Build1 itself.
icon: terminal
color: Grey
---

# herdr — Terminal Workspace Manager for AI Coding Agents

`herdr` (ogulcancelik/herdr) is a Rust CLI/TUI (single binary, no Electron) that works like tmux but is purpose-built around AI coding agent sessions: it shows real terminal views (not a summarized interpretation) for each agent, lets sessions survive detach/restart/SSH, and exposes a socket API so agents can spawn panes and coordinate with each other.

## Install
```bash
# via cargo
cargo install herdr

# or download the prebuilt single binary for your platform from the releases page
```

## Usage
1. Launch `herdr` in the project directory to open the workspace manager.
2. Spawn a new pane per agent session (e.g. one pane running a local coding agent against the Build1 repo, another running tests).
3. Detach with the standard multiplexer detach key; the sessions keep running. Reattach later, including over SSH, to resume monitoring.
4. Check the pane status indicators (blocked/working/done) to see which agent needs attention without switching into each pane.
5. For programmatic coordination, use herdr's socket API to let one agent spawn or read another agent's pane output.

## Build1 Integration
Infra-agnostic — herdr manages terminal sessions, not application runtime. It's most useful while *developing* Build1: run one pane per local coding-agent session (each possibly calling local Ollama models) so multiple parts of the stack (backend, FastMCP tools, frontend) can be worked on in parallel panes without losing session state on disconnect.
