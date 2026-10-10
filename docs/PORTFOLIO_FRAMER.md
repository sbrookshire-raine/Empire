# Framer / slide deck — export from PORTFOLIO

**Source of truth for copy:** [`PORTFOLIO.md`](PORTFOLIO.md) (sync from [`ODYSSEY.md`](ODYSSEY.md) via [`PORTFOLIO_MAINTENANCE.md`](PORTFOLIO_MAINTENANCE.md)).

**Import into Framer (CSV):** [`data/framer-portfolio/`](../data/framer-portfolio/) — see [`README`](../data/framer-portfolio/README.md). Verify with `.\scripts\export-framer-portfolio.ps1`.

**This file:** Framer-ready structure — section order, progression narrative, slide deck, and **image placeholders**. When PORTFOLIO changes, update matching blocks here and the CSV pack (same `synced_from_odyssey` date in PORTFOLIO comment).

---

## Does PORTFOLIO adapt to Framer?

**Yes.** [`PORTFOLIO.md`](PORTFOLIO.md) is already organized as:

- One **thesis** (hero)
- **Timeline** (progression 2024 → now)
- **Case studies** (Problem → Approach → Outcome — maps to Framer “project” cards)
- **Skills** (icon grid or tags)

For Framer you add **visuals** (screenshots, diagrams, photos) that markdown deliberately omits. ODYSSEY holds paths to artifacts; this doc lists **what to capture**.

**Two Framer patterns that work well**

| Pattern | Use when |
|---------|----------|
| **Long scroll** | One URL: Hero → Timeline (sticky horizontal) → Case study sections → Skills → Contact |
| **Slide-style sections** | Full-viewport blocks (100vh each) with scroll snap — feels like a deck without PDF |
| **Separate deck** | Export the slide list below to Pitch, Google Slides, or Framer “presentation” template |

---

## Progression arc (beginning → current)

Use this as the **spine** for timeline and slides. Same story as PORTFOLIO timeline, grouped into **eras** for visuals.

```
2024  ORIGIN     Documents + classroom idea → narrow to ranking (IRENE/Aporia)
2025  NAMING     rAIne, simulate-before-code, PREVaiL, Hatch apps, friction lessons
2026  EMPIRE     Local stack shipped; corpus bounded; governance gates; backup hub
NOW   CONSOLIDATE  E: hub → cloud pool; GitHub; portfolio (you are here)
```

**Framer component idea:** horizontal timeline with four era bands; click/scrub expands milestone cards (dates from PORTFOLIO timeline table).

---

## Framer page map (recommended sections)

Copy headings and body from PORTFOLIO; paste into Framer text layers.

| # | Section ID | Framer layout hint | Source in PORTFOLIO |
|---|------------|-------------------|---------------------|
| 1 | `hero` | Full bleed + one line thesis + subtitle | Thesis + tagline (lines 9–13) |
| 2 | `summary` | 2 columns text + optional portrait | Executive summary |
| 3 | `progression` | Horizontal scroll timeline | Timeline table + era arc above |
| 4 | `pattern` | Diagram: Pool → Score → Threshold → Usable | Case study 1 (one graphic reused) |
| 5 | `project-irene` | Image left, text right | Case study 1 |
| 6 | `project-prevail` | Image right, text left | Case study 2 |
| 7 | `project-hatch` | Grid of 4–6 app thumbnails | Case study 3 |
| 8 | `project-governance` | Before/after or bullet + dashboard screenshot | Case study 4 |
| 9 | `project-empire` | Workbench screenshot + stack icons | Case study 5 |
| 10 | `project-stem` | Waveform or stem UI + pipeline strip | Case study 6 |
| 11 | `lessons` | 5–7 cards | What I learned |
| 12 | `skills` | Tag cloud or 2×5 grid | Skills table |
| 13 | `roadmap` | Short list (student dashboard, tutor — from ODYSSEY §10) | Optional honesty slide |
| 14 | `contact` | GitHub + email + “full audit” link to ODYSSEY PDF/export later | Contact block |

**CTA line for footer:** “Full three-year audit available on request” or link to public GitHub readme — avoid dumping `K:\` paths on the site.

---

## Slide deck (15 slides)

Use as Framer full-height sections or export to slides. **Headline / Body / Visual** per slide.

### Slide 1 — Title
- **Headline:** Rank the trustworthy thing above the popular thing  
- **Body:** Three years building local, verifiable knowledge systems — from classroom idea to EMPIRE.  
- **Visual:** Abstract or personal photo; no code.

### Slide 2 — Thesis
- **Headline:** Local · unmetered · verifiable  
- **Body:** I build on my own hardware: weighted retrieval, explicit contracts, checkpointed jobs — not infinite cloud ingest.  
- **Visual:** Simple three-icon row (laptop, lock, checkmark).

### Slide 3 — Where it started (2024)
- **Headline:** 2024 — Documents first, then YouTube  
- **Body:** PDF learning hub (Nov 2024). Then IRENE: re-rank YouTube for education — likes/views, not raw views; threshold 0.6. Aporia Flask tracker.  
- **Visual:** Screenshot of filter code snippet or Aporia UI if available; else diagram “PDF → hub”.

### Slide 4 — The pattern (still used in 2026)
- **Headline:** Same architecture, two years apart  
- **Body:** Over-fetch → weighted heuristics → threshold → refuse to invent. YouTube 2024 → Wikipedia scout 2026.  
- **Visual:** One flow diagram (reuse on website § `pattern`).

### Slide 5 — 2025 — Design before code
- **Headline:** Simulate, then build  
- **Body:** Raine blueprint: stress-test logic and personality in dialogue before shipping. PREVaiL: learning-style responses. Thinking Coordinator: co-worker, not chatbot.  
- **Visual:** Heptabase or blueprint excerpt (blur sensitive); or stylized quote card.

### Slide 6 — 2025 — Hatch & platform risk
- **Headline:** 13 apps, then the platform died  
- **Body:** Beta-tested Hatch canvas; exported ~25k lines when it shut down. Tried Playful (TestFlight); kept my IP and went local-first for real.  
- **Visual:** Collage: Energia, idea-farm, student dashboard — 3–4 Hatch screenshots.

### Slide 7 — Friction → discipline
- **Headline:** Failures became contracts  
- **Body:** Env hell, schema mismatches, CORS — documented Aug 2025. Answer: sandboxes, operating contract, LEGO manifest, mechanic-green gates.  
- **Visual:** Dashboard or `mechanic-green` pass screenshot; optional red→green simple graphic.

### Slide 8 — 2026 — EMPIRE
- **Headline:** EMPIRE — local agent workbench  
- **Body:** Eve on Ollama; PocketBase tasks; Cognee memory; MCP tools; HTMX workbench. Toolbelt limbs: Wiki, DAZE, Stem Factory.  
- **Visual:** `eve.html` workbench screenshot (Neon Storm UI).

### Slide 9 — Scale with boundaries
- **Headline:** Stop the ingest, keep the corpus  
- **Body:** Wiki work halted at ~71k / 46M pages — bounded checkpoint, not abandoned idea. Frozen snapshots for truth/drift.  
- **Visual:** Timeline fork: “unbounded ✗” vs “checkpointed ✓”.

### Slide 10 — Stem Factory (shipped creative tool)
- **Headline:** Music at library scale  
- **Body:** Moises-class pipeline: Demucs stems, practice tracks, batch runs — integrated as EMPIRE Toolbelt limb.  
- **Visual:** Stem stages diagram or practice-track screenshot; waveform optional.

### Slide 11 — Living Book Worlds (optional depth)
- **Headline:** Books → structured worlds  
- **Body:** 2025 design: extraction, vectors, card templates — ancestor of today’s structured extract / LEGO cards.  
- **Visual:** Concept art or card mockup; skip slide if site is tight.

### Slide 12 — What I learned
- **Headline:** Lessons that transfer  
- **Body:** Narrow scope, keep core · Bounded jobs · Write continuity · Protect before optimize · Small verified wins · Real-day documentation · Progress as unlocks.  
- **Visual:** 7 small cards (Framer components).

### Slide 13 — Skills
- **Headline:** What I work on  
- **Body:** Retrieval · Local AI ops · Agents/MCP · Document/audio pipelines · Reliability · Backup estate · Product beta · Education-adjacent UX.  
- **Visual:** Skills grid from PORTFOLIO table.

### Slide 14 — Now — consolidation
- **Headline:** 2026 — One hub, two backups, one repo  
- **Body:** EMPIRE_HUB on E:; rclone pool to cloud; GitHub Empire; offline disc planned. Workspace moving from fragmented drives to one story.  
- **Visual:** Simple hub diagram (E → cloud Z → disc); no secret paths.

### Slide 15 — Close
- **Headline:** Let’s build verifiable systems  
- **Body:** GitHub: sbrookshire-raine/Empire · Open to teaching-adjacent product · Full audit: ODYSSEY (on request).  
- **Visual:** QR or link button; portrait optional.

---

## Image & media checklist (gather for Framer)

| Asset | Suggested source | Used on |
|-------|------------------|---------|
| Eve workbench | `http://127.0.0.1:8080/eve.html` screenshot | Slides 8, 14; `project-empire` |
| Dashboard / health | `dashboard.html` | Slide 7 |
| DAZE dial | `daze.html` | Optional “time reclamation” |
| LEGO whiteboard | `lego.html` | Optional “composable tools” |
| Hatch exports | Heptabase / PROJECT HUB folders | Slide 6, `project-hatch` |
| idea-farm / Energia | Hatch export screenshots | Hatch grid |
| IRENE / code | Repo or archive screenshot | Slides 3–4 |
| Wiki scout / drift | `wiki.html` or cache card | Case study 1 |
| Stem pipeline | Shard docs or output folder (no huge library) | Slide 10 |
| Personal | Photo, music, teaching context | Hero, Slide 1 |
| Timeline graphic | Build in Framer from era arc | `progression` |

**Rights:** Hatch/React exports are your IP (ODYSSEY §8). EMPIRE screenshots are yours. Avoid Google Drive paths in public filenames.

---

## Framer workflow (maintenance)

1. Edit **ODYSSEY** → sync **PORTFOLIO** ([checklist](PORTFOLIO_MAINTENANCE.md)).  
2. Update **this file** only where Framer copy diverges (slide headlines, image list).  
3. Paste updated paragraphs from PORTFOLIO into Framer — keep thesis wording **identical** to §1.  
4. Optional: one Framer CMS collection “Case studies” with fields: `slug`, `problem`, `approach`, `outcome`, `image`, `year` — populate from PORTFOLIO case studies.

**Deck vs site:** Same content; deck = slides 1–15 full viewport; site = sections 1–14 with deeper case study pages later.

---

## Related

- [`PORTFOLIO.md`](PORTFOLIO.md) — copy source  
- [`PORTFOLIO_MAINTENANCE.md`](PORTFOLIO_MAINTENANCE.md) — when ODYSSEY changes  
- [`ODYSSEY.md`](ODYSSEY.md) — evidence and dates for footnotes  
