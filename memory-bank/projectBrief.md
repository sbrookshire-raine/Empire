# Project Brief — EMPIRE

## Core requirements & goals
EMPIRE is a **meter-free, local AI workbench** on Windows 11 — not SaaS, not a React SPA.

- **Eve** — Autonomous Knowledge Refinery and Cognitive Co-Designer (local Ollama orchestrator).
- Helps the Architect triage tools, remember local knowledge, manage tasks, and hand forge work to Cursor.

## Non-negotiables (runtime)
1. No React/Next/Vue SPA; no Firebase/Supabase in app code.
2. No paid cloud LLM APIs in application code.
3. Node/npm only in `agents/empire-task-agent/`.
4. Loopback binding by default; remote via Tailscale/Cloudflare later — not open LAN.
5. Tasks ≠ Work Orders.
6. No silent full-wikipedia Cognee ingest; staging memory needs confirmation.

## Operational estate (2026-10)
Backup and hub work added a **cloud copy tier** (`pool:` / `Z:`) and **`E:\EMPIRE_HUB`** staging — documented in `docs/ESTATE_INVENTORY.md` and `docs/ODYSSEY.md` §14. This does **not** change the runtime rule: Eve still uses local Ollama and loopback services.

## Vision phases (EMPIRE_MANIFESTO.md)
1. Intake & Triage — working  
2. Evaluation — in progress  
3. Thought Experiments — in progress  
4. LEGO Whiteboard — working  
5. Time Reclamation (DAZE) — working  
6. Remote access — planned  
7. Voice — scaffold  

## Canonical repo
- GitHub: https://github.com/sbrookshire-raine/Empire  
- **Active branch:** `revision-refactor` (ahead of `main` as of 2026-10-07)  
- Local root: `C:\EMPIRE`

See also: [productContext.md](productContext.md), [systemPatterns.md](systemPatterns.md).
