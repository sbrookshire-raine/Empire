# Phase 2 First Step — Resource Pulse + Eve-Managed Admit

**Date:** 2026-09-16  
**Status:** Building  
**North star:** Architect should not push a series of tool buttons. Eve manages the capability space when safe; the right dock stays a display window (DAZE, etc.). LEGO project work waits until she proves she can manage resources.

## First step (this build)

1. **`resource_pulse`** — diagnostics Eve (and MCP) can call: RAM/disk, GPU lease, service probes, inventory (manual + session), light skills safe to admit, GPU skills that need Architect OK, plain-English `summary`.
2. **`admit_for_goal`** — Eve requests a capability for a task reason:
   - Light (`auto_enable` in capability manifest) + headroom OK → session admit **without** requiring Research Partner toggle (Architect is not the button).
   - GPU / non-auto → `{ need_architect: true }` — ask, do not force.
   - Fail closed on bad headroom / busy GPU / session cap.
3. Eve tools + atlas MCP + routing/skill: pulse first, then admit or ask.
4. No Cognee auto-remember. No UI redesign required for this step (dock thinning later).

## Later (not this step)

- Thin Tools dock to display-only  
- Official LEGO project expansion  
- Full autopilot GPU without asking  
