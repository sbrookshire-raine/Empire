---
name: graphify-codebase-graph
description: Installs and drives Graphify (PyPI package graphifyy, CLI command graphify), a tool that builds and maintains a live dependency/knowledge graph of a codebase for AI coding assistants, auto-updates via a git post-commit hook, and powers PR review/triage and conflict-risk analysis. Use when a user wants an AI assistant to understand a large codebase's structure/dependencies, wants to keep a code graph in sync with commits, or wants graph-informed PR triage, review-order, or merge-conflict-risk analysis. Mostly infra-agnostic dev tooling; can complement Cognee if the user wants Build1's own memory graph to also hold codebase structure.
icon: git-branch
color: Purple
---

# Graphify — Codebase Graph for AI Assistants

Graphify builds and maintains a dependency/knowledge graph of a codebase so AI coding assistants (Claude,
Cursor, Codex, and 20+ others) can reason about structure without re-reading the whole tree, and uses that
graph for PR review/triage and merge-conflict-risk analysis.

## Install (package name differs from CLI command)
1. Install the PyPI package: `pip install graphifyy` (note the double `y` — this is intentional, distinct
   from the `graphify` CLI command it installs).
2. Verify the CLI is on PATH: `graphify --version`.

## Setup and usage
1. Run `graphify init` (or the project's documented init command) inside the target repo to build the
   initial dependency/knowledge graph.
2. Install the git post-commit hook Graphify provides so the graph auto-updates after every commit, keeping
   it in sync without manual re-runs.
3. Point the AI coding assistant at Graphify's graph output/query interface so it can look up
   dependencies/relationships before editing unfamiliar code.
4. For PR workflows, use Graphify's triage/review-order/conflict-risk commands to rank which PRs to review
   first or flag files likely to merge-conflict, based on graph proximity rather than diff size alone.

## Build1 Integration
Mostly infra-agnostic — Graphify assists development *of* the Build1 codebase itself and has no runtime
dependency on Ollama, PocketBase, Cognee, or the HTMX/Alpine frontend. If desired, its post-commit graph can
be periodically exported and ingested into **Cognee 1.0** so Build1's own memory graph also carries
structural codebase knowledge alongside conversational/document memory — treat this as optional, not
required, since Graphify already works standalone via its git hook.
