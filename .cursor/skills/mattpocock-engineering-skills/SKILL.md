---
name: mattpocock-engineering-skills
description: Installs Matt Pocock's collection of small, composable software-engineering agent skills (planning, ticket triage, systematic debugging loop, etc.) via the community skills.sh installer. Use when the user wants a lightweight, adaptable engineering workflow skill set — as opposed to a monolithic "vibe coding" framework — for planning work, triaging tickets, or debugging systematically. Infra-agnostic: applies to engineering process regardless of which Build1 component (Ollama, PocketBase, Cognee, FastMCP, HTMX/Alpine) the work touches.
icon: wrench
color: Grey
---

# mattpocock/skills: Real-Engineering Skill Pack

A collection of small, composable agent skills for day-to-day software engineering (github.com/mattpocock/skills, MIT), distributed via the community `skills.sh` installer rather than a single monolithic process-owning framework.

## Setup

1. Run the installer from the target project:
   ```bash
   npx skills@latest add mattpocock/skills
   ```
2. When prompted, select the desired skills and target coding agent, **making sure to select `/setup-matt-pocock-skills`**.
3. Inside the coding agent, run:
   ```
   /setup-matt-pocock-skills
   ```
   This asks: which issue tracker to use (GitHub, Linear, or local files — used by the triage/ticket skills) and what labels are applied when triaging tickets. For a fully local Build1 workflow, prefer **local files** as the issue tracker to keep the loop zero-cloud.

## Mapping a request to a skill

- **Debugging a bug systematically** → `/diagnosing-bugs` (`skills/engineering/diagnosing-bugs/SKILL.md`) — wraps a best-practice loop (reproduce → isolate → hypothesize → test → fix → verify) instead of ad hoc guessing.
- **Triaging/labeling issues** → `/triage`, applying the labels configured during setup, against the configured tracker.
- **Other skills** are organized under `skills/` by category — inspect the installed skill's own `SKILL.md` for exact invocation syntax once selected, since skills are added individually during interactive install.
- Skills are intentionally small and meant to be hacked on — if the user wants different behavior, edit the installed skill's file directly rather than treating it as a black box.

## Output
After invoking a skill, report the concrete engineering artifact produced (a debugging report with root cause and fix, a triaged/labeled ticket list, etc.) and note which skill/config (issue tracker, labels) was used so results are traceable back to setup choices.

## Build1 Integration
Purely a process/workflow skill pack — it does not call Ollama, PocketBase, Cognee, or FastMCP directly. Use it to plan or debug work on any Build1 component; when triaging Build1-specific tickets, prefer the local-files tracker option to keep the toolchain zero-cloud.
