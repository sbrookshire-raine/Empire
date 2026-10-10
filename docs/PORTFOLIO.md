# Portfolio — local-first systems, trustworthy retrieval, and learning tools

<!--
  synced_from_odyssey: 2026-10-08 (content drawn from ODYSSEY.md through §14 + MOTIVATION.md §1–2)
  maintainer: see docs/PORTFOLIO_MAINTENANCE.md when ODYSSEY.md changes
  canonical audit: docs/ODYSSEY.md
-->

## Demonstration hub (not the EMPIRE runtime)

This folder is a **story layer** for a **web-based portfolio** — the narrative of how **EMPIRE** and **Eve** came to be. It is **not** the operational stack (no PocketBase/Cognee/Eve install here). Canonical history lives in **[ODYSSEY.md](ODYSSEY.md)**; this page and [`data/framer-portfolio/`](../data/framer-portfolio/) are the **public-facing extract** (Framer CMS CSVs, slide copy, case studies).

**Architect · builder · educator-adjacent systems**  
~3 years (2024–2026): ranking and retrieval, local AI orchestration, document and audio pipelines, and preserved exports when platforms shut down.

**Thesis** (same as [ODYSSEY §1](ODYSSEY.md#1-the-problem-in-one-sentence)):  
**Rank the trustworthy thing above the popular thing — and keep that knowledge local, unmetered, and verifiable over time.**

**Deep audit (full journey, apps, file evidence):** [ODYSSEY.md](ODYSSEY.md)  
**Why (short):** [MOTIVATION.md](MOTIVATION.md)

---

## Executive summary

I build **bounded, verifiable knowledge systems** on my own hardware: weighted retrieval instead of hype, contracts instead of hope-the-model-behaves, and checkpoints instead of monolithic ingests. The thread runs from a **2024 YouTube educational filter** (explicit scores, engagement as likes/views, threshold 0.6) to **2026 EMPIRE** (local Eve agent, wiki scout, Cognee memory, MCP tools, measured CI gates).

Parallel threads: **teaching and students** (co-op class idea → Thinking Coordinator → Eve as co-worker), **music production** (Stem Factory / Moises-class pipeline at library scale), and **product-side experience** (Hatch canvas beta, Playful TestFlight — then export and own the IP when the platform died).

I document work as **audits with corrections kept visible**, not polished fiction. This page is the **portfolio extract**; the growing source log is ODYSSEY.

---

## Timeline (selected beats)

| When | What | Portfolio note |
|------|------|----------------|
| 2024-11 | PDF → learning hub (`learning_hub` logs, four script iterations in days) | Document intake instinct |
| 2024-12 | **IRENE** / **Aporia** — weighted YouTube refiltering; Flask progress tracker | First working “rank trustworthy” code |
| 2025-01 | **rAIne** named; PythonAnywhere → local IDE | Cloud-to-local pivot |
| 2025-03 | **Zet** capture pipeline; **Thinking Coordinator** research | Intake + peer-coaching model |
| 2025-04 | **Living Book Worlds** (large design — extraction, vectors, card templates) | Ancestor of structured_extract / LEGO cards |
| 2025-08 | **Raine blueprint** — simulate personality and architecture before code; friction doc | Eve’s design method |
| 2025-11 | **IRENE 2.0**; Hatch **education presentation** project bookmarked | |
| 2025–26 | **Hatch** — 13+ apps (~25k LOC) exported before platform shutdown | Preservation + product beta story |
| 2026-05 | **Raine Abacus** — dockerised agents, Weaviate, resource pipeline | Direct EMPIRE ancestor |
| 2026-07 | **EMPIRE** repo; Build1 docs describe stack before fully built | PocketBase, MCP, HTMX/Alpine |
| 2026-07 | Wiki corpus scale wall — ingest halted bounded (~71k / 46M) | Checkpointed scale lesson |
| 2026-09 | Eve, LEGO governance, mechanic-green, estate audits | Ship discipline |
| 2025–26 | **Stem Factory / Shard** — Demucs pipeline, practice tracks, MCP limb | Shipped creative tool |
| 2026-10 | **EMPIRE_HUB** + rclone pool — consolidation backup architecture | Ops / consolidation phase |

*Full dated table:* [ODYSSEY §2–§4, §14](ODYSSEY.md).

---

## Case studies

### 1. Trustworthy ranking (IRENE → Wiki Scout)

**Problem:** Popular ≠ useful for learning; raw view counts lie.  
**Approach:** Over-fetch candidates → **weighted heuristics** → **threshold** → flag usable / refuse to invent. Implemented for YouTube (2024) with explicit weights and likes/views engagement; same pattern for Wikipedia scout (2026).  
**Outcome:** One architectural lineage across two years, not a rewrite.  
**Evidence:** [ODYSSEY §1–§2](ODYSSEY.md), [MOTIVATION §1](MOTIVATION.md), [WIKI_SCOUT.md](WIKI_SCOUT.md).

---

### 2. PREVaiL → Eve (learning style as product)

**Problem:** Generic AI responses ignore how someone actually learns.  
**Approach:** PREVaiL (“learning style-based AI response system”) explored VARK-style profiles and feedback; carried into Eve’s persona directives (Scanner / Pattern-Weaver, co-worker not chatbot).  
**Outcome:** Personality and routing treated as **engineered**, not prompt luck.  
**Evidence:** [ODYSSEY §8 PREVaiL](ODYSSEY.md), [ODYSSEY §9.1](ODYSSEY.md) (engagement: unlocks vs grind).

---

### 3. Hatch exports (platform risk and IP)

**Problem:** Built heavily on **Hatch** canvas; company shut down; successor **Playful** tested (TestFlight, onboarding) and declined.  
**Approach:** Export **13+ projects**, master index, ~25k lines — documented as **your IP**, not the platform’s.  
**Outcome:** Local-first is **earned** (see MOTIVATION §2), not ideology. Product beta experience: small teams, pivots, preservation.  
**Evidence:** [ODYSSEY §8 Hatch register + blockquote](ODYSSEY.md).

**Highlighted apps (names only — detail in ODYSSEY):** Energia productivity system, idea-farm (production data, org partnerships), student-advisor dashboards, 80s Synth / Aporia task manager, Anamchara.

---

### 4. Failures → contracts (EMPIRE governance)

**Problem:** 2025 build pain — env hell, CORS, schema mismatches, “chasing the ball” mid-build ([roadblocks doc](ODYSSEY.md)).  
**Approach:** Each failure class mapped to a **contract**: sandbox containers, port/service operating contract, LEGO manifest + capability registry, fix-before-add work order.  
**Outcome:** mechanic-green gates, playbook coverage, prompt-budget tests — design from scar tissue.  
**Evidence:** [ODYSSEY §9](ODYSSEY.md), [OPERATING_CONTRACT.md](OPERATING_CONTRACT.md), [LEGO_CONTRACT.md](LEGO_CONTRACT.md).

---

### 5. EMPIRE (local-first agent stack)

**Problem:** Need a **meter-free**, local orchestrator for memory, tasks, research limbs, and forge handoff to IDE — without SPA complexity or cloud LLM rent.  
**Approach:** **Eve** on Ollama; **PocketBase** tasks; **Cognee** memory; **FastMCP** tools; **HTMX/Alpine** workbench; Toolbelt-gated “LEGO” products (Wiki, DAZE, Stem Factory). Spec’d in Raine blueprint (2025) and witnessed in Build1 docs (2026) before full implementation.  
**Outcome:** Working workbench, measured audits, refactor plan for explicit answer-path (intent → resolution → evidence → answer).  
**Still open (by design):** student-facing blueprint items (adaptive tutor, unified student dashboard) — original 2024 classroom thread.  
**Evidence:** [ODYSSEY §4, §10](ODYSSEY.md), [EMPIRE_MANIFESTO.md](../EMPIRE_MANIFESTO.md), [manifest/README.md](manifest/README.md), GitHub: [Empire](https://github.com/sbrookshire-raine/Empire) (`revision-refactor` branch).

---

### 6. Stem Factory / Shard (audio at library scale)

**Problem:** Commercial stem tools don’t match custom practice workflows (focus mixes, missing-stem tracks, library batch).  
**Approach:** Reverse-engineered processing goals; **Demucs** pipeline, drum analysis, practice generator, scheduled batch runs, MCP server → EMPIRE Toolbelt limb.  
**Outcome:** **Shipped capability** integrated into EMPIRE (not only a side repo); large derived library on estate (see ODYSSEY §8 Stem row).  
**Evidence:** [ODYSSEY §8 Stem Factory](ODYSSEY.md), EMPIRE `stem_factory` MCP + tools.

---

### 7. Living Book Worlds (structured worlds from books) — optional depth

**Problem:** Turn fiction and non-fiction into **interactive, structured worlds** with extraction, vector store, API, card templates.  
**Approach:** Large 2025 design (entities, sensory detail, voice cues, n8n chunking plan).  
**Outcome:** Architectural ancestor to EMPIRE extraction / structured cards; good follow-up for a **creative systems** portfolio angle.  
**Evidence:** [ODYSSEY §8 Living Book Worlds](ODYSSEY.md).

---

## What I learned (transferable)

From [ODYSSEY §5](ODYSSEY.md) — abbreviated:

- **Narrow scope, keep the core** (Rails → refiltering still served the class idea).  
- **Bounded, resumable jobs** beat heroic full ingests.  
- **Write continuity where the work lives** — this audit exists because rebuilds happened.  
- **Protect before optimize** — backups and hub consolidation before deleting terabytes.  
- **Small verified wins** beat perfect design.  
- **Document the real day** — constraints become methods (voice journaling on walks, etc.).

**How to present work to me:** progress as **accumulating unlocks**, not opaque grind ([ODYSSEY §9.1](ODYSSEY.md)).

---

## Skills (derived from work, not every tool touched)

| Area | Examples |
|------|----------|
| **Retrieval & ranking** | Weighted scoring, thresholds, rerank, ambiguity/refusal |
| **Local AI ops** | Ollama, context budgets, voice (Speaches), GPU placement |
| **Agent tooling** | MCP, capability registry, prompt-budget governance |
| **Data / corpus** | Wikipedia markdown corpus, wiki scout, checkpointed ingest |
| **Document pipelines** | PDF hub → Docling/read_document → workbench ingest |
| **Audio DSP** | Demucs stems, batch library processing, practice-track generation |
| **Full-stack (local)** | Python services, PocketBase, zero-build HTMX UI, Node agent runtime |
| **Reliability** | Docker sandboxes, integration gates, operating contracts |
| **Backup / estate** | rclone union pool, tar-first hub, verify-before-delete |
| **Product / beta** | Hatch/Playful testing, export on shutdown |
| **Education-adjacent design** | Co-op class origin, coordinator model, student dashboards (Hatch) |

---

## Assets that survived three years

From [ODYSSEY §6](ODYSSEY.md):

- Frozen **corpus** (wiki snapshots, ZIMs, meta-history recon — truth/drift motivation).  
- **Design pattern:** pool → heuristics → threshold → usable flag.  
- **Collaboration model:** AI specified in dialogue (2025) → **Eve** (2026).  
- **Writing preserved:** OneNote, Obsidian, Heptabase exports — enables this audit.

---

## How to read more

| Need | Document |
|------|----------|
| Full project register (every attempt) | [ODYSSEY §8](ODYSSEY.md) |
| Heptabase era, Indie Art Hub | [ODYSSEY §12](ODYSSEY.md) |
| Backup / hub chapter | [ODYSSEY §14](ODYSSEY.md), [BACKUP_CONSOLIDATION.md](BACKUP_CONSOLIDATION.md) |
| Updating this page after ODYSSEY edits | [PORTFOLIO_MAINTENANCE.md](PORTFOLIO_MAINTENANCE.md) |
| Framer site or slide deck layout | [PORTFOLIO_FRAMER.md](PORTFOLIO_FRAMER.md) |
| Vault + dialogue depth | [audits/2026-09-28-vault-and-dialogue-digest.md](audits/2026-09-28-vault-and-dialogue-digest.md) |

---

## Contact / code

- **Repository:** https://github.com/sbrookshire-raine/Empire (active development on `revision-refactor`)  
- **Live stack (local):** Eve workbench `http://127.0.0.1:8080/eve.html` when EMPIRE is running  

*Last portfolio sync: 2026-10-08 — update via [PORTFOLIO_MAINTENANCE.md](PORTFOLIO_MAINTENANCE.md) when [ODYSSEY.md](ODYSSEY.md) changes.*
