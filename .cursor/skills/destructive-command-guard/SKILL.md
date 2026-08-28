---
name: destructive-command-guard
description: Installs and configures dcg (Destructive Command Guard), a Rust CLI hook that intercepts and blocks destructive shell commands (recursive deletes, force pushes, disk wipes) before AI coding agents can execute them. Use when a user wants to protect their filesystem/repo from accidental destructive commands run by an AI coding assistant working on the Build1 codebase, or asks about configuring dcg's allow/deny rules. Infra-agnostic dev-safety tool — protects the local machine regardless of which Build1 component is being edited.
icon: shield
color: Orange
---

# Destructive Command Guard (dcg)

dcg is a Rust binary that acts as a pre-execution hook for AI coding agents. It inspects shell commands the
agent is about to run and blocks destructive ones (e.g. `rm -rf /`, `git reset --hard`, disk-wiping, force
operations) based on a configurable rule set (`config.toml` / `config.schema.json`), then installs itself
into each supported agent's native hook mechanism.

## Supported agents
Claude Code, Codex CLI (0.125.0+), Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Cursor IDE, Hermes
Agent, Grok (native + Claude-compat), Antigravity CLI (`agy`), OpenCode (community plugin), Aider (git hooks
only), Continue (detection only).

## Install
1. Use the project's auto-detecting installer script — it detects platform, downloads the right binary, and
   configures hooks for every supported agent it finds installed on the machine.
2. Review the generated `config.toml` and tighten/loosen the deny rules for the project (e.g. always deny
   `rm -rf` outside a scratch dir, always deny force-push to `main`).
3. Re-run the installer after adding a new coding agent to the machine so its hook gets registered too.

## Configuration
- Rules live in `config.toml`, validated against `config.schema.json`.
- Prefer an explicit deny-list for genuinely destructive patterns plus a narrow allow-list for known-safe
  exceptions, rather than one broad rule that might block legitimate work.

## Build1 Integration
Infra-agnostic — dcg protects the local dev machine itself, independent of which Build1 layer (Ollama,
PocketBase, Cognee, FastMCP, or the HTMX/Alpine frontend) an AI coding agent is currently editing. Recommend
installing it once per developer machine when any AI coding assistant is used to modify the Build1 repo,
since local-first development means agents have direct filesystem access with no cloud sandboxing net.
