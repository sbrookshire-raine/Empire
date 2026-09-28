# ESTATE INVENTORY — what exists, what it is, and where it should live

Written 2026-09-27. This document exists because the estate is bigger than the repository, and two things have
already gone wrong by *assuming* rather than looking: a dormant Cognee store was nearly discarded as "public,
re-derivable" data, and a drive letter (`E:`) turned out to name a different physical disk than it had hours
earlier. **Rule one: identify before changing. Rule two: nothing is called disposable until its contents have been
read.** Everything in this document is measured on the machine, not inferred from folder names.

## 1. Drives — identified by serial, never by letter

Letters move when hardware is swapped. Serials do not.

| Letter | Device | Media | Size GB | Free GB | Used GB | FS |
|---|---|---|---|---|---|---|
| **C** | SKHynix `HFS001TEJ9X115N` (internal NVMe) | SSD | 951.6 | 267.5 | 684.1 | NTFS |
| **D** | SKHynix `HFS001TEJ9X115N` (internal NVMe) | SSD | 953.9 | **174.7** | 779.1 | NTFS |
| **E** | ~~WD My Passport **25E1** `WX41AA69RHTD`~~ → **now WD My Passport 2627 `WX32D10DE684`** | **HDD** USB | 3726 | **3725.6 — blank** | 0 | NTFS |
| *(detached)* | WD My Passport **25E1** `WX41AA69RHTD` — its letter was taken | **HDD** USB | 1863 | 1017.4 (when mounted) | 845.6 | NTFS |
| **H** | Samsung T7 Shield `E843119X0SNFS6S` (T7 #2) | SSD USB | 3725.9 | 1291.7 | 2434.2 | exFAT |
| **I** | Samsung T7 Shield `M471025W0JNFS6S` (T7 #1) | SSD USB | 3725.7 | 1860.1 | 1865.6 | exFAT |
| **V** | VHDX file *inside* `I:\EMPIRE_VHDX\empire_cognee.vhdx` | — | 2048 | 2044.4 | 3.6 | NTFS |
| **G** | Google Drive FS (client running) | cloud | quota **unreadable this way** | — | — | — |
| *(detached)* | WD My Passport **2627** `WX32D10DE684` | **HDD** USB | 3726 | **3726 — wiped blank** | 0 | NTFS |

Notes that matter:

- **Letters moved on 2026-09-27 — read paths with care.** The blank 2627 (`WX32D10DE684`) was attached after the
  25E1 was ejected, and it **took the freed letter `E:`**. So today **`E:` is the 2627 (blank backup target)**, and
  every `E:\wikipedia`, `E:\enwiki…xml`, `E:\AI_PROJECTS` path in this document now refers to the **detached 25E1**.
  This is the same class of event as the 2026 drive-letter swap that Rule one exists for.

- **`V:` is not a disk.** It is an NTFS volume inside a VHDX *file* that lives on `I:`. Clearing it frees nothing on
  C: or D:, and frees nothing on I: unless the VHDX is compacted. Mount/detach: `scripts/mount-cognee-vhdx.ps1`
  (and `-Detach`, which needs elevation).
- **`G:` reports the same size as `C:` (951.7 GB)** — that is the Drive FS mirroring the system volume, **not** your
  Drive quota. Ask the Drive UI, or `rclone about`.
- ~~**No SMART from either HDD's USB bridge.**~~ **Corrected 2026-09-27: SMART is readable on every attached drive.** `smartctl -d sat` reads the WD 2627 and `-d sntasmedia` reads both T7s (raw reads need elevation). Windows "Healthy" is still a shallow status — read the counters instead, per §6 item 5.
- Measured E: sequential **read** throughput: **104.8 MB/s** (1,843.9 MB in 17.59 s) — USB 3, no read-side collapse.
  **Write** speed is unmeasured and is the number that predicts a 525 GB mirror (both WD portables are likely SMR).
- `.dropbox.device` markers exist on E:, H: and the detached 2627. Dropbox is not installed or running, so they are
  inert — but reinstalling Dropbox could reclaim those drives.

## 2. Timeline — the evolution of ideas, from file creation dates

This is not one project. It is **four successive architectures**, and each survived into the next. The dates below
are filesystem creation times, so they show when work actually happened.

### 2024-11 → 2024-12 — **IRENE** (first attempt)

| Date | Artifact | What it is |
|---|---|---|
| 2024-11-21 | `E:\AI_PROJECTS\` | the earliest AI workspace: `IRENE`, `IRENE BASED PROJECT WORKING FOLDER`, `Empower`, `DL_PROJECT_BOLT`, `bolt install`, `Gadget_phase_tracker`, `markdown_combo_pdf`, `2nd_run_file_processor` |
| 2024-11-24 | `E:\gutenberg_books_txt`, `H:\gutenberg_books_txt` | Project Gutenberg text corpus (the first "local library") |
| 2024-11-27 | `E:\transfer_112724`, `E:\AI_stuff_backup` | machine-migration snapshots |
| 2024-12-12 | `H:\Inception_of_Dreams\01_IRENE` | IRENE carried forward to a second location |
| 2024-12-21 | `E:\workpc backup` | work-PC backup |
| 2024-11→12 | `E:\wikipedia\*.zim` (16 files, 461 GB) + `E:\enwiki-20241001-…multistream.xml` (97 GB) | **the frozen offline knowledge base** — Kiwix ZIM library + raw XML dump |

**Reading:** `IRENE` is the origin point. `markdown_combo_pdf` is an early document-conversion attempt — the
ancestor of today's docling/doc path. The 2024 Wikipedia + Gutenberg material shows the same *frozen-snapshot*
instinct that later became Truthdrift: capture knowledge while it is still pre-contamination.

### 2024-12 → 2026-01 — **AI Factory** (second attempt)

| Date | Artifact | What it is |
|---|---|---|
| 2025-11-24 | `H:\AI_ARCHIVE\` | archive root for the AI Factory era |
| 2025-11-26/27 | `E:\dropbox_backup_misc`, `E:\AI_stuff_backup`, `E:\github_desktop_project_folder` (now empty) | consolidation |
| **2025-12-04** | **`D:\AI_Factory\`** | a full stack attempt: `agent-zero`, `affine`, `memori`, `n8n_data`, **`qdrant_storage`**, `knowledge_bases`, `master_documents`, `models`, `repos`, `workspace` + `AI_FACTORY_GUIDE.md`, `IMPLEMENTATION_PLAN.md`, `MANIFEST.md` |
| 2026-03-23 | `H:\AI_MODELS_2026` | model collection: Llama-3.3-70B-Abliterated, Magnum-v4-72B, BGE-reranker-v2-m3, Whisper-Large-V3, XTTS-v2, Flux-Uncensored-V2, Depth-Anything-V2 |

**Reading:** AI Factory is the first *assembled* stack — agent framework + workflow automation (n8n) + knowledge
bases + **a vector store (Qdrant)**. Its `master_documents`/`knowledge_bases` are the direct ancestors of today's
Cognee datasets. It was abandoned, not disproven.

### 2026-04 → 2026-05 — **Raine / v2 markdown pipeline** (third attempt: the Wikipedia era)

| Date | Artifact | What it is |
|---|---|---|
| **2026-04-03** | `H:\AI_ARCHIVE\v2_markdown_pipeline\` (real git repo: `.git`, `forge/`, `git_collection/`, `dashboard/`, `docs/`, `docker/`, `config/`, `backups/`, `chrome-lens-extension/`) | the pipeline that turned Wikipedia into markdown and embedded it |
| 2026-04-07 | `C:\wiki_md`, `C:\wiki_runs`, `C:\wiki_dumps` | **first working copies on C:** |
| 2026-04-08 | `D:\wiki_md\2026`, `D:\wiki_runs\2026`, `D:\wiki_dumps\2026`, `…\v2_markdown_pipeline\raine` | the Raine material proper |
| **2026-04-09** | **`D:\weaviate_v2_archive\`** | the vector store: `wikichunk` + `wikichunk2021` |
| 2026-04-11 | `wikichunk2026` | third snapshot year complete |
| 2026-04-14/16 | `D:\wiki_runs\2017`, `I:\weaviate_v2_archive`, `I:\wiki_md` | 2017 added; copies pushed to the T7 |
| 2026-04-19/21 | `D:\wiki_dumps\2026_meta_history` | **the full revision-history dump** |
| 2026-05-06 | `MASTER_RAINE_TO_EMBED` | the curated set staged for embedding |
| 2026-05-10 | `RAINE_ABACUS_PROJ_FOLDER\runtime\weaviate` (docker, run from the OneDrive Desktop) | Raine Abacus ran **its own** Weaviate instance |

**Reading:** this is where the hard-won corpus was built — **46,251,388 embedded chunks** across 2017/2021/2026
(12,501,004 + 15,214,782 + 18,535,602), plus the meta-history dump that makes *edit-level* drift analysis possible.
"Raine" is this era.

### 2026-07 → today — **EMPIRE** (fourth attempt, current)

| Date | Artifact | What it is |
|---|---|---|
| **2026-07-20** | `C:\EMPIRE` | the current repository |
| 2026-07-21 | `I:\EMPIRE_DATA`, `I:\EMPIRE_VHDX`; `media-weaviate` (docker volume `cursor_hol_weaviate_data`) | Cognee storage era begins; another abandoned vector store |
| 2026-07-22 | `D:\wiki_md\2017` | 2017 markdown completed |
| 2026-07-23 | `H:\colibri`; `V:\Cognee` last write | Colibri (local inference engine) downloaded; **Cognee wiki ingest halted here** |
| 2026-09-01 | `C:\Empire_Workbench`, `D:\Empire_Workbench`, `_github_staging\{sbrookshire-raine,sbx2020}` | the Workbench + **repos already cloned**: `academic_hub`, `Empire`, `notie` |
| 2026-09-10 | `D:\empire\MANIFEST.md`, Desktop research docs | plan/review artifacts of this era |
| 2026-09-14 | `empire-weaviate-heist-2017` container | the *working* Weaviate, mounted from `I:` |
| 2026-09-25 | *(failure)* | it died: `failed to read disk usage: input/output error` on `/var/lib/weaviate` |
| 2026-09-26 | `I:\EMPIRE_BACKUP` (restic) | first verified backup — of `C:\Empire_Workbench` only, 2.6 GB |
| 2026-09-27 | `I:\HDD_MOVE_TEMP` | the 2627's contents moved off that HDD, which is now blank |

**The through-line:** IRENE (isolated scripts) → AI Factory (agent + workflow + vector DB) → Raine (a knowledge
corpus, embedded) → EMPIRE (task loop + Cognee memory + MCP limbs + Eve). Each attempt kept the previous one's best
idea and dropped its machinery. **The corpus is the one asset that survived all four.**

### From the Obsidian notes — the 2025 thread the folders couldn't show (added 2026-09-27)

The vault notes carry dates in filenames, so they recover a year that the folder hierarchy alone hid. This is the
**idea layer** beneath the four build attempts: several of these were designed in detail and never shipped.

| Date | Note | The idea |
|---|---|---|
| 2025-01-12 | *(oldest note in both live vaults)* | the notes begin here — six months before the first corpus work |
| 2025-01-18 | `Abacus - related.md` | **Abacus** — the first named system |
| **2025-01-19** | **`rAInE - Raine AI Expression (or exchange).md`** | **the origin of the name "Raine"** — an *AI expression/exchange* concept, not a codename |
| 2025-02-19 → 03-12 | `6. testing with abacus.md`, `ABACUS - prompt changes.md` | Abacus in active prompting |
| 2025-03-14 | `Synthesis.md` | synthesis of the above |
| **2025-03-22 → 03-26** | `Zettelkasten, Severance, and the Cold Harbor Project.md` · `Zettel Template.md` · `Zed learning process notes.md` · `2a. Youtube Zeded.md` · `3A - ZED2RSS.md` · **`MASTER- Gemini Zet God script.md`** · `MASTER - Shortened Notegpt Zet prompt.md` · `7A - agentic code for ripping and zet summarizing from consolex.ai.md` | **"Zet" = Zettelkasten (Zed)**: an automated *capture → summarize → zettel* pipeline — YouTube, RSS, ConsoleX and Gemini feeding structured notes |
| 2025-03-31 | `Possible job - Thinking Coordinator.md` | an idea for the work itself |
| 2025-04-09 → 04-18 | `Gemini Learning hub project summary (project save point)`, `gemini ui research`, `Learning home (possible next step)`, `041825 - Workflow success with Cove AI…` | a **learning hub**, and the first automation win (Cove AI) |
| 2025-08-15 → 08-18 | `08-15-2025 - Raine blueprint.md` · `raine roadblocks - clear paths` · **`08_16_25_rAIne non n8n_MVP_v1 setup.md`** · `RAINE DEV CHAT PT1/PT2` · `rAIne Oauth` | the **Raine blueprint**, its blockers, and the decision to build an MVP **without n8n** |
| **2025-11-18** | `IRENE 2.0 1/2/3` | **IRENE revived** — a year after the 2024-11 scripts |

**Reading:** the documented arc is *Abacus → rAInE (AI expression) → Zet/Zed (knowledge capture) → learning hub →
Raine blueprint & non-n8n MVP → IRENE 2.0 → the 2026 markdown pipeline → EMPIRE*. **`Zet` is the unbuilt ancestor of
EMPIRE's intake logic**: the same instinct that later became `wiki_scout` (capture → structure → retrieve), designed
in March 2025 and never finished.

**Vault inventory**

| Vault | Notes | Oldest → newest | State |
|---|---|---|---|
| `…\Documents\RESYNC_2026` | **497** | 2025-01-12 → 2026-06-29 | **the live vault**; folders `0.EVOLVE 5_18_26`, `1_SBX`, `1. GADGET FOCUS`, `2. PAST LIVES`, `Clippings`, `Excalidraw`, `Zettelkasten (Zed)` |
| `…\Desktop\SBX_Vault` | **474** | 2025-01-12 → 2026-05-18 | earlier sibling of the same tree (overlapping dates) |
| `…\Documents\SBX_Vault` | **0** | — | **empty shell** — folder structure only |
| `…\Documents\Obsidian Vault` | **0** | — | **empty shell** — only `.obsidian` |

`2. PAST LIVES\Zettelkasten (Zed)` holds the Zed system proper: `Experiments`, `Guides`, `Learning Notes`,
`Reference Notes`, `Templates`, **`ZED Notes`**.

Two consequences: the vaults live **inside OneDrive**, so a cloud copy likely exists already — but OneDrive sync is
*not* a backup (deletions and account problems propagate), so the notes belong in the backup plan as their own tier.
And three of the four vaults are duplicates or empty shells, which is why the note count looked ambiguous until each
was counted.

### Unlocated — must be found before archiving anything

- **`RAINE_ABACUS_PROJ_FOLDER`** — its container mounted
  `C:\Users\m69nr\OneDrive\Desktop\RAINE_ABACUS_PROJ_FOLDER\runtime\weaviate` in May 2026; that path no longer
  exists. There is a Desktop folder `R_UNIVERSAL SYNTHESIS ARCH` (2026-08-30) — **hypothesis only, unverified.**
  **RESOLVED 2026-09-28 by direct check:** it lives at `…\OneDrive\Desktop\PROJECT HUB\RAINE_ABACUS_PROJ_FOLDER\` and
  is **present — 70,861 files / 3.48 GB**. (The digest's §I.2 finding was right; this line had simply never been
  updated.)
- **`media-weaviate`** used docker volume `cursor_hol_weaviate_data` — **identified 2026-09-27:** compose project `cursor_hol`, and the volume is 994.5 kB (§6 item 3).

**Verified absent, 2026-09-28:** **`C:\Users\sbrookshire\` does not exist** — the only profile on this machine is
`m69nr` (+ Default/Public). So **the "old machine" is not reachable from here at all**: the `AI_PROJECTS` material that
did migrate is all there is. Likewise **`D:\repos` and `I:\repos` do not exist**, so the plan to re-home the cloned
repos has not happened — and the repos that *are* staged sit in **`D:\Empire_Workbench\_github_staging\`**.
**`E:\wikipedia` is absent** because `E:` is now the 2627; the 16 ZIMs are on the detached 25E1.
- **`E:\wikipedia\*.zim`** — 16 Kiwix ZIM archives, 461 GB. Intactness unverified (ZIM carries internal checksums).

## 3. How the legacy assets can be converted or placed to serve EMPIRE

The test applied to each: *does this feed a capability EMPIRE actually has or is planning?* Assets that don't get
archived, not integrated — the estate is large enough to drown in.

| Asset | What it is | Conversion / placement into EMPIRE |
|---|---|---|
| **ZIM library** `E:\wikipedia\*.zim` (461 GB) | 16 offline Kiwix encyclopedias (Wikipedia Jan-2024, WikiSource 2022, Wikibooks 2021, Wiktionary 2024, Gutenberg 2023, medlineplus, iFixit, mutopia/openmusictheory/tonedear, survivorlibrary 232 GB) | **Highest-leverage unclaimed asset.** `zimdump`/`kiwix-tools` (Lens A, dev-time) extracts each to text; those enter the **existing** pipeline — normalize → markdown → title registry → the same `wiki_scout` read path. No new limb, only a new source. Adds domains EMPIRE lacks: **medical** (medlineplus), **music theory** (openmusictheory/mutopia/tonedear — aligned with your music work), repair (iFixIt), plus more frozen pre-2025 snapshots for Truthdrift. Decide `survivorlibrary` (232 GB) on re-downloadability first. |
| **`enwiki…multistream.xml`** (97 GB, E:) | raw English Wikipedia, Oct 2024 | Parse → markdown via the existing path. Provenance for the 2026 snapshot; keep as source-of-record, cold. |
| **`D:\wiki_dumps\2026_meta_history`** | revision-history dump (Apr 2026) — **on disk it is only two truncated `.part` slices, ~1.67 GB, page ranges p2955–3418 and p9479–10061** (see [`audits/2026-09-27-ideas-and-evidence-digest.md`](audits/2026-09-27-ideas-and-evidence-digest.md) §C) | **The Truthdrift engine's real fuel** — this recon is what started the whole thread. Convert to per-page revision timelines in a structured store (Postgres, *not* Cognee: relational, not semantic). Any plan must first account for **re-acquiring the complete multi-part dump**. |
| **`D:\wiki_md`** (18.76M files) | page-level markdown, 2017/2021/2026 | Already EMPIRE's runtime retrieval path, and it must stay on internal storage. Needs per-year **title registry/index** (the error book shows live misses: *"not in title registry"*) and **packing** for backup. |
| **Weaviate store** (D: 524.6 GB + I: working copy) | 46,251,388 chunks × 768-dim, with `snapshot_id`/`page_id`/`body_sha256` provenance | Keep as the **precomputed semantic index** and archival record — deliberately not a runtime dependency. The provenance fields are what make systematic cross-year diffing possible. |
| **Repos** — `_github_staging\{sbrookshire-raine,sbx2020}` (**already cloned**), `E:\AI_PROJECTS`, `E:\github_desktop_project_folder` (empty) | both GitHub accounts, staged 2026-09-01 | Re-home to a stable `D:\repos\<account>\<repo>` and treat as **the P9 source of truth**: real trees → tree-sitter/`ast-grep` reach, and `read_active_tool` stops depending on flattened harvests. `academic_hub` may carry reusable scraping code. |
| **`D:\AI_Factory`** (30.4 GB, Dec 2025) | agent-zero, affine, memori, **n8n_data**, **qdrant_storage**, knowledge_bases, master_documents + 3 planning docs | Mine before archiving: `master_documents`/`knowledge_bases` are candidate corpora; `n8n_data` is automation prior art; **`qdrant_storage` may hold embeddings already paid for** (reuse beats recompute); the `AI_FACTORY_*.md` docs are prior architecture thinking worth ingesting as reference. |
| **`v2_markdown_pipeline`** (H:, Apr-2026 git repo) | the Raine pipeline: `forge/`, `git_collection/`, `dashboard/`, `docker/`, `docs/` | Direct ancestor of EMPIRE's `tool_forge`/`stem_factory` and the wiki ingest. Read `docs/` + `forge/`, port what the current code lost, archive as prior art. |
| **Desktop research docs** — `EMPIRE RAG Stack evaluation`, `EMPIRE_WIKI_ARCHITECTURE_STRATEGY`, `EMPIRE_WIKI_STORAGE_RESEARCH_REPORT`, `empire_local_capability_gap_analysis`, `empire_missed_oss_investigation`, `nlm extention evaluation`, `empire_huggingface_specialty_resources`, `CONFIG API RULES.MD` | Sept 2026 analysis of *these same problems* | **Exactly the material Cognee exists for.** Move to `docs/reference/` and/or ingest into the curated `primitives`/`eve_core` path — otherwise the same research gets redone. |
| **Desktop folders** — `DAZE`, `PROJECT HUB`, `SBX_Vault`, `RESEARCH THOUGHT EXPERIMENT FILE HUB`, `TOOL_FACTORY_GUMLOOP*`, `TOOLBOX_GUMLOOP_PROJECT`, `Repo_ripper Agent`, `cursor_git`, `cursordocs`, `kb extract`, `R_UNIVERSAL SYNTHESIS ARCH`, `zebra`, `tool-factory*.zip` (v1–v4) | assorted attempts; **`DAZE` already exists as `daze_mcp.py`** | Identify → archive as `legacy/` on the cold HDD. The tool-factory ZIPs show the `tool_forge` lineage. |
| **`H:\colibri`** | Colibri local inference engine (CPU) | Hold as a **fallback runtime option** if Ollama becomes the bottleneck (Lens B; not needed today). |
| **`H:\AI_MODELS_2026`** (2.4 TB) | GGUF + Transformer models | Mostly **re-downloadable — no backup**. Exception: `BGE-reranker-v2-m3` (wiki interpreter), `Whisper-Large-V3`/`XTTS-v2` (voice) are referenced by EMPIRE. |
| **`H:\Heptabase backup 4_7_26`** | knowledge-tool backup | Inspect for notes worth ingesting, then archive. |
| **Music libs** (`EZDrummer`, `Toontracks`, `Superior`, samples) | music production | **Not EMPIRE.** Leave in place; exclude from backup scope. |
| **Obsidian vaults** — `…\Documents\RESYNC_2026` (497 notes) + `…\Desktop\SBX_Vault` (474), plus two empty shells | Jan-2025 → Jun-2026, dates in filenames | **The idea layer, and EMPIRE's "why".** Curated knowledge worth ingesting into the `primitives`/reference path after curation — but *read first*: `08-15-2025 - Raine blueprint.md`, `raine roadblocks - clear paths`, `08_16_25_rAIne non n8n_MVP_v1 setup.md`, `MASTER- Gemini Zet God script.md`. Those recover designed-but-unbuilt work. Back up as its own tier (§4): OneDrive sync is not a backup. |
| **`Zet` / Zettelkasten (Zed)** — Mar 2025, never shipped | an automated *capture → summarize → zettel* pipeline fed by YouTube, RSS, ConsoleX and Gemini; `2. PAST LIVES\Zettelkasten (Zed)\{Experiments, Guides, Learning Notes, Reference Notes, Templates, ZED Notes}` | **The unbuilt ancestor of EMPIRE's intake logic** — same instinct as `wiki_scout` and the learn-from cache. Review `3A - ZED2RSS.md`, `7A - agentic code for ripping and zet summarizing from consolex.ai.md`, `MASTER - Shortened Notegpt Zet prompt.md`, then **register it in `EMPIRE_IDEA_QUEUE`** rather than let it be redesigned again. |
| **`H:\llama.cpp`**, `SteamLibrary` | tooling/games | Regenerable; no backup. |

## 4. Backup tiers and placement

Ranked by irreplaceability, not size. **Rule: the runtime copy is never the backup copy.**

| Tier | Contents | Size (measured) | Copies today |
|---|---|---|---|
| **T0 sources** | `enwiki…xml` 97 · `wiki_dumps` 44 · meta-history · ZIM library 461 | ~602 GB | 1 each |
| **T1 markdown** | `D:\wiki_md` (18.76M files) + ~~`I:` copy~~ | 80.7 GB | **1 today, not 2** — measured 2026-09-27: `I:\wiki_md` is an **empty tree** (0 files, only an empty `2017` folder). The runtime corpus is **single-copy**, and its three year-directories (2017/2021/2026) are deliberate snapshots, not duplicates |
| **T2 Weaviate** | `D:` original + `I:` working copy | 524.6 GB | 2, one machine |
| **T3 personal** | `I:\HDD_MOVE_TEMP` | **423.3 GB** | **1 — on an SSD, post-migration** |
| **T4 system** | `C:\EMPIRE` 5.1 · `C:\Empire_Workbench` · `%LOCALAPPDATA%\EMPIRE` · Postgres dump | ~10 GB | restic: 1 snapshot, Workbench only |
| **T5 regenerable** | models 2.4 TB, Steam, most ZIMs | — | **do not back up** |
| **T6 legacy** | Raine/v2 pipeline, AI Factory, IRENE, Desktop projects, tool-factory ZIPs | GBs | archive as-is |
| **T7 notes** | **three documentation eras, all located:** OneNote (`ONENOTE BACKUP PREOBSIDIAN.md`, 383,846 B / 8,339 lines, **Dec 2024 → 2025**) · Obsidian (497 + 474 notes) · Heptabase (`All-Data.json` 25.3 MB + `Card Library` + `Journal` + `Whiteboard`) — plus Desktop note folders (`DAZE`, `PROJECT HUB`, `HIDDEN`, `TOOL_FACTORY_GUMLOOP*`) | ~1.5 GB | OneNote + Obsidian live **in OneDrive** (sync ≠ backup); the Heptabase export sits on `H:`. **Update 2026-09-28: Heptabase is now THREE exports, not one** — `H:\Heptabase backup 4_7_26\` (2026-04-08, 749 cards, copied + verified) plus **`C:\Users\m69nr\Downloads\Heptabase-Data-Backup-2026-05-09…` (1,009 cards) and `…2026-07-24…` (1,290 cards)**, and the live library at **1,574**. The two newer exports are **in no backup tier yet** — they were found by a filename sweep, not by design. Also in `Downloads`: `recall_backup_12_15_25\` (a knowledge-graph export with `Book/Game/Technology/AI/Organization` folders, including `Organization\DeepSeek.md`). **Copy the two exports into this tier** (small; ~1.5 GB). Growth is a dated series: 749 → 1,009 → 1,290 → 1,574. **First copy made 2026-09-27** → `E:\EMPIRE_BACKUP_2026-09-27\01_notes_T7\` — 2,036 files / 929.9 MB, **verified identical by relative path + size** (`scripts/compare-trees.py`, 0 differences). **Finding:** the live `Seth @ FVCC` notebook holds only `OneNote_RecycleBin` — it is **empty** — so `ONENOTE BACKUP PREOBSIDIAN.md` is the *only* OneNote-era record on this machine; the `.onepkg` sits on the detached 25E1. See digest §H |

**Placement**

| Destination | Holds | Why |
|---|---|---|
| **WD 2627** (3.7 TB, blank, clean) | T3 personal (423) + T0 (602 basic) + T2 mirror (525) + T1 packed (~80) + T6 legacy ≈ **1.7 TB** | clean, cold, sequential-friendly; ~2 TB headroom |
| **E:** (WD 25E1, 1.0 TB free) | second copies of the tiers that cannot be replaced: **T3**, **T1-2017**, **T0 meta-history** | a *different physical device* — this is what makes it 3-2-1 |
| **Google Drive `G:`** | **T1-2017 packed + manifest** (small, most irreplaceable) | cloud only where it's proportionate; quota must be read from the Drive UI |
| **I:** | keeps Weaviate *working* copy + VHDX + restic repo | already there |
| **H:** | unchanged (models/apps); candidate for the restic replica | fast SSD |

**Copy-first (Architect, 2026-09-27):** *"i dont want you deleting anything unnecessary. i have an external hdd empty
that can hold backup data."* So the empty 3.7 TB external drive **removes the reason any of this had to be a move**:
**back up by copying, verify, and keep every original.** The deletions in §5 and in steps 4–10 of §7 are demoted to
*optional, last, and only after a verified backup exists* — and none of them is required to make the backup. Nothing
in this document authorises deleting a source, a snapshot, or a copy; the space-recovery column is now a convenience,
not a justification.

**T1 packing cost — measured 2026-09-27.** The "~100–170 h" above is for *loose-file* copying; the real bottleneck is
**compression**, not the copy. Probe: two real batch directories from `D:\wiki_md\2021` (each exactly **50,000 files**),
1,403 MB of source:

| Method | Time for 100,000 files | Rate | Extrapolated to 18.76M files / 81 GB |
|---|---|---|---|
| `tar -czf` (gzip) | ~13 min | **~130 files/s** | **~40 hours** |
| **`tar -cf` (no compression)** | **57.8 s** | **1,729 files/s, 24.3 MB/s** | **~3 hours**, archive ≈ **85 GB** |

**T1 timing — corrected by the real run (2026-09-28 11:05).** The "~3 hours" above was measured with the probe writing to
**`C:` (NVMe)** — the real job writes to the **USB HDD**, and with millions of tiny files that is ~20× slower:
**`2017` alone took 5 h 40 m** (24.8 GB archive, ~1.2 MB/s, ~600 files/s). So the estimate was destination-bound, not
source-bound: the corpus *read* was never the problem. Revised: `2021` ~1.5–2 h and `2026` ~2 h follow, total ~9–10 h.
Lesson: **a throughput probe is only valid if it writes to the destination medium** — same lesson as the 2 GB write
test that was too small to expose SMR.

**Also: `%TIME%` in a `cmd` `for` block is expanded once at parse time.** The T1 log shows every timestamp identical to
the second. Exit codes (via `!ERRORLEVEL!` with delayed expansion) are correct; the timestamps are not. Use `!TIME!`.

**Status 2026-09-28 11:05 — copied 579.8 GB of 3725.6.** `wiki_md_2017.tar` complete (24.8 GB, exit 0),
`wiki_md_2021.tar` running, `2026` queued. **`User_Files` (781,163 files / 1.67 GB) is still missing** — bsdtar failed
on it instantly, exactly as it did on the restic repo; it needs Python `tarfile`. Everything else in `09_i_drive_leftovers`
is present: `EMPIRE_DATA` (44.03 GB loose, `weaviate_dump` partial), `EMPIRE_VHDX` (4.04 GB), `EMPIRE_BACKUP.tar`
(3.83 GB), `weaviate_dump.tar` (712.9 MB, completed 05:20:59).

**Backup progress (2026-09-27, copy-first, destination `E:` = the 2627 `WX32D10DE684`):**

| # | Tier | Destination | Copied | Verified |
|---|---|---|---|---|
| 1 | **T7 notes** | `01_notes_T7\` | 2,036 files / 929.9 MB | **identical** (path + size) |
| 2 | **T4 system** — `C:\Empire_Workbench` + `%LOCALAPPDATA%\EMPIRE` | `02_system_T4\` | 14,653 files / 2.69 GB and 270 files / 10.9 GB | **identical** (path + size) |
| 3 | **T3 personal** — `I:\HDD_MOVE_TEMP` | `03_personal_T3\` | **439.4 GB** — finished 22:27:57 | verification running at wrap-up |
| 4 | **T6 legacy** (curated: v2 pipeline code+docs, Legion docs, IRENE, AI_Factory, all Desktop projects) | `07_legacy_T6\` | finished 22:46:57 | v2 pipeline compared: **320 files, 0 differences** |
| 5 | **Docker-era volumes** — 13 volumes (Cognee `pgdata` 8.0 GB, open-webui ×3, postgres ×3, n8n ×3, cursor_hol) | `08_volumes\` | **26 files / 12.39 GB** | **identical** (path + size) |
| 6 | **I: leftovers** — `EMPIRE_DATA` (incl. the 2017 dump), `EMPIRE_VHDX`, `EMPIRE_BACKUP` (restic), `User_Files` | `09_i_drive_leftovers\` | **running** — `EMPIRE_I_LEFTOVERS` | pending |

**Operational findings, 2026-09-27 — earned the hard way, worth not rediscovering:**

| Finding | Consequence |
|---|---|
| **`docker run` fails inside a Windows scheduled task** | Docker Desktop needs an interactive session. The Docker-volume job died silently there (task went `Ready`, no container, no log line, no `CHAIN DONE`). **Run Docker jobs from an interactive shell**; scheduled tasks are fine for plain `robocopy`. |
| **USB drives are not bind-mountable into Docker** | `-v E:\path:/dst` → `invalid reference format` (the drive-letter colon), and with forward slashes it mounts but **writes fail** (`Wrote only 6144 of 10240 bytes`) because the WSL2 VM has no automount for removable drives. **Fix that worked: tar to `C:` staging, then `robocopy` to the backup drive** (13 volumes → 11.53 GB of tars → verified identical). |
| **A long job launched as a child of an agent shell is killed when that shell's job closes** | The drive self-test lost its log this way and needed a second elevated call. Long jobs go through `schtasks` (`EMPIRE_T3_COPY`, `EMPIRE_T6_COPY`, `EMPIRE_I_LEFTOVERS` pattern), and they survive the session. |
| **`smartctl` installs without elevation but *reads* need it** | `start-process -Verb RunAs` for reads; `-d sat` for the WD bridge, `-d sntasmedia` for the T7s' USB-NVMe bridges. |
| **`robocopy /L` is the cheap way to size a filtered copy** | It prints the exact file/byte totals that *would* copy without writing anything — used to size T6 before committing to it. |
| **`robocopy` grinds pathologically on huge tiny-file trees** | `I:\EMPIRE_DATA\weaviate_dump` (289,945 tiny files) burned **20,716 s of CPU for 1.4 GB** — ~2–3 files/s, **no errors logged**, `MT:4` threads spinning. `User_Files` (781,163 files) is the same shape. **Cure: a tar.** Measured 1,729 files/s on the same class of tree (500× faster) and it leaves the destination holding a few big files instead of ~800,000 tiny ones — which also matters for later enumeration on a USB disk. `robocopy /L` remains the right *sizing* tool, just not the right *copying* tool for this shape. |
| **`tar.exe` (bsdtar) crashes on the restic repo** | Exit **-1073741819 (0xC0000005, access violation)**, sometimes only after writing part of the archive: `I:\EMPIRE_BACKUP` reproduced it **twice** (attempts both died; one left a 580 MB partial). **Cure: Python `tarfile`** — added all **14,727 files in 114 s** with no crash. Prefer `tarfile` (or robocopy) for the `I:\EMPIRE_BACKUP` tree specifically; `tar.exe` was fine on `D:\wiki_md` and the Docker staging trees. |
| **Windows path colons break Docker `-v`; USB drives break it harder** | Covered above: forward slashes fix the parse, staging on `C:` fixes the mount. |
| **`Get-ChildItem`/`Get-Item` can return a stale size while a file is being written** | A 0 MB reading for a tar that `[System.IO.FileInfo]` reported as 257 MB. When watching a growing file, use `FileInfo` and take **two samples 30 s apart** before concluding anything has stalled — I nearly called a working job dead. |
| **Do not run two jobs at one USB disk** | SMR portables thrash. All copy jobs here were serialised (chains waiting on DONE markers) for exactly that reason. |

**Finding — `%LOCALAPPDATA%\EMPIRE` is mostly regenerable.** Of its 10.9 GB, **`models` 8,584.7 MB + `bin` 2,277 MB =
10.86 GB** is re-downloadable model and binary cache. The *unique* state is ~30 MB: `chat-history` (184 files),
`eve-trace.jsonl`, `wiki-error-book.jsonl`, `gpu-lease.json`, `eve-toolbelt.json`, the ollama profiles — the answer to
§8.3's "what Eve was actually asked and answered". Also present: **`restic-pass.txt`, a credential** — back it up,
never ingest it.

**T6 scoped by measurement (2026-09-27) — most of "legacy" is not data, it is regenerable:**

| Source | Measured | Unique part |
|---|---|---|
| `H:\AI_ARCHIVE` — **1,154 GB** | `AI_Archive_Legion` **1,054 GB** of models / datasets / docker images / python+node packages / binaries / runtimes / embeddings (a Nov-2025 offline-RAG toolset); `v2_markdown_pipeline` **89 GB**, of which **`data` is 54.9 GB of DERIVED corpus in 5.45M files** and `.git` is 3.8 GB; `ai_factory_workspace` 10.9 GB | **~30 MB** of v2 code + docs, the Legion's inventory docs / prompts / scripts, `_old_docs`, `_old_scripts` |
| `D:\AI_Factory` — 30.4 GB | `.venv` 2.5 + `models` 27.3 = **29.8 GB regenerable** | **~1.3 GB**: agent-zero, affine, knowledge_bases, repos, n8n_data, and the six `AI_FACTORY_*.md` planning docs (§8.3 wanted those read) |
| `H:\Inception_of_Dreams` | 120 MB | all of it — **IRENE** |
| Desktop projects | ~51 GB — `HIDDEN` 17.4 · `PROJECT HUB` 17.9 · `FROM EXHDD` 12.9 · `INSPIRATION COVE` 1.3 · rest < 0.7 each | all unique |
| **curated T6** | | **≈ 53 GB, not ~1.2 TB** — a 95% reduction with no unique data dropped |

**CORRECTION (same session, better measurement): the 2017 source *is* on disk.** `I:\EMPIRE_DATA\wiki_xml_20170301\`
holds **`enwiki-20170301-pages-articles.xml.bz2` (12.81 GB)** plus `convert_2017.log` / `.err` / `.pid` from 2026-07-22
— i.e. the dump *and* the conversion run that produced `wiki_md/2017`. So **`wiki_md/2017` is re-derivable locally
after all** (as is 2021, whose dump is on `D:\wiki_dumps`), and the argument above for packing T1 out of
irreplaceability does not hold. The statement that "2017 is gone from dumps.wikimedia.org and not cheaply
re-derivable" was true about *Wikimedia's* index and false about *this machine* — the third time in this session that
measuring beat a confident inference. What the finding really does is **move the priority to `I:\EMPIRE_DATA` itself**:
13 GB of 2017 dump + **31.2 GB of `wiki-reports`** (the title registry / priority reports used at runtime) are sitting
**unprotected on the fault drive**. Still worth packing T1 (~3 h, uncompressed) as insurance — but as convenience, not
as rescue.

Two mechanical facts that shape all of this: **`wiki_md` cannot be copied as files** (18.76M × ~4 KB → ~100–170 h per
copy; pack it first), and both WD portables are likely **SMR** — sustained writes can collapse, so large jobs run
deliberately, not unattended.


## 5. Recovering working space on C: and D:

**Optional, and last — see the copy-first note in §4.** Nothing here is needed to make a backup, and nothing here
authorises deleting a source or a snapshot. Freeing space is a convenience; the backup comes first, verified, with the
originals intact.

| Move | Recovers | Notes |
|---|---|---|
| **`D:\weaviate_v2_archive` (563 GB) → external drive** | D: 174.7 → ~699 GB free **only if you later choose to delete** | **Copy and verify first** (durable index files, after a clean Weaviate shutdown). The archive is irreplaceable and its three snapshots are by design — deletion is optional and last, never a prerequisite |
| `D:\wiki_dumps` (44.2) + `D:\wiki_runs` (27.4) → 2627 | D: → ~770 GB free | optional; both are cold |
| **`C:\wiki_md` + `C:\wiki_runs` + `C:\wiki_dumps`** (created 2026-04-07) | **nothing — measured empty 2026-09-27** | ~~C: up to ~150 GB if they are stale duplicates~~ **CORRECTED:** all three hold **0 files / 0 GB**, so there is no C: win here and nothing left to compare. The estimate above came from dates alone — the first row in this document disproved by looking |
| **`docker_data.vhdx` (101.2 GB) → D:** | C: → ~368 GB free | Docker Desktop → Settings → Resources → Advanced → *Disk image location*; stop Docker first; do it *after* D: is freed |
| Reconcile `C:\Empire_Workbench` vs `D:\Empire_Workbench` | small | **RESOLVED 2026-09-27, then CORRECTED 2026-09-28.** The first reading called `D:` a "2-entry stub" — that counted *top-level* entries only. Measured properly: **`C:` is 14,653 files / 2.82 GB** (the live vault) and **`D:` is 11,313 files / 1.27 GB** — not a stub at all: it holds **`_github_staging\`** (the staged GitHub repos, the P9 source trees) plus `04_Infrastructure`. **Neither copy is in the backup yet** — T4 copied `C:` only. The stub can go later **if you choose** — optional, and not needed for any backup |

Keep on internal D:: `wiki_md` (81 GB) — it is the runtime corpus and wants SSD latency.

## 6. Open items — verify before touching

1. ~~**`RAINE_ABACUS_PROJ_FOLDER`**~~ **RESOLVED 2026-09-27** — never missing: it lives at `…\Desktop\PROJECT HUB\RAINE_ABACUS_PROJ_FOLDER\` (May 2026), containing a dockerised agent system with `agent_resource_pipeline/`, its own Weaviate `runtime/`, cloned resource repos and a `MANUAL.md`. Read `MANUAL.md` + `agent_resource_pipeline/` first. See digest §I.2.
2. ~~**`C:\wiki_*`** — sizes unknown; must be compared against D: before any deletion.~~ **RESOLVED 2026-09-27 — they are empty.** `C:\wiki_md`, `C:\wiki_runs` and `C:\wiki_dumps` each hold **0 files / 0 GB** (verified to depth 2 with `-Force`). No comparison was needed because there is nothing there. **The §5 space-recovery row is corrected accordingly** — a reminder that the 2026-04-07 creation dates were evidence of a *plan*, not of content.
3. ~~**`media-weaviate` volume** `cursor_hol_weaviate_data` — unidentified.~~ **RESOLVED 2026-09-27.** Docker is running (29.8.0), so it could finally be read: the volume belongs to compose project **`cursor_hol`** (created 2026-06-08, label `com.docker.compose.project: cursor_hol`), confirming the digest §H.3 hunch that it matches the **`cursor_HOL`** repo in the staged repos — and it is **994.5 kB**, a stub, not lost data. The same read turned up something more important:
   - **`docker_data.vhdx` (101.2 GB) is not junk.** It holds ~12 GB that exists nowhere else: **`empire_empire_cognee_pgdata` 8.418 GB** (the live Cognee memory database), **`open-webui` + `ai_factory_open-webui` + `agent-zero_open-webui-data` ≈ 3.2 GB** (prior-era chat history, three copies), `agent-zero_postgres-data` 238.1 MB, `v2-markdown-pipeline_v2_dify_postgres_data` 139.3 MB, `docker_postgres_data` 80.8 MB, plus n8n storages and ~640 MB build cache.
   - **Consequence:** §4's tiers do not account for these, and step 8 of §7 relocates the VHDX without reading it. Treat the Cognee `pgdata` as **T4 system** — the `pg_dump` in step 6 is the right tool but needs Postgres **running** (the container is currently exited) — and the open-webui / agent-zero / dify volumes as **T6 legacy**. **Do not run a general `docker system prune` before these are copied**; `prune-sandbox-containers.ps1` remains safe (sandbox containers only).
4. **ZIM integrity** — **corrected 2026-09-28: there are TWO ZIM libraries, ~1.06 TB, not one of 461 GB.** A census
   (`eve-audit/zim-census.py`) found **49 ZIMs / 595.4 GB on `H:\AI_ARCHIVE\AI_Archive_Legion\knowledge_bases\`** —
   including **`survivorlibrary.com_en_all_2024-09.zim` at 249.50 GB**, `wikipedia_en_all_maxi_2024-01.zim` 109.89 GB,
   `stackoverflow.com_en_all_2023-11.zim` 80.48 GB, `gutenberg_en_all_2023-08.zim` 76.84 GB — plus a distinct set of
   **music-theory ZIMs** (`openmusictheory.com` 0.16 GB, `mutopiaproject.org` 6.64 GB) and a devdocs/StackExchange
   cluster. The **16 archives / 461.4 GB on the 25E1** (`E:\wikipedia`, detached, so absent from the census) are a
   *different* set with partial overlap. **Consequence:** my earlier statement that the ZIMs "exist only on
   `E:\wikipedia`" was wrong — it came from a top-level-only check that never looked inside `H:\AI_ARCHIVE`. ZIMs are
   re-downloadable, so this is not an emergency, but `H:`'s 595 GB is single-copy today, and my T6 copy **deliberately
   excluded `knowledge_bases`**.
5. ~~**HDD health** — no SMART from either WD; read real counters before entrusting T3/T0/T2.~~ **RESOLVED 2026-09-27 for every attached drive — and the old claim was wrong.** `smartmontools` 7.5 (installed by winget, no elevation needed) reads **all** of them: `-d sat` for the WD USB bridge, `-d sntasmedia` for the T7s' USB-NVMe bridges. **Raw device reads do need elevation** — it runs via `Start-Process -Verb RunAs`, output at `eve-audit/smart-report.txt`. Measured:
   - **2627 (`E:`, `WDC WD40NDZW-11MR8S1`, `WD-WX32D10DE684`) — PASSED and essentially a new drive:** **81 power-on hours**, Start/Stop 263, Load_Cycles 1276, and **zero on every damage counter** — Reallocated 0 · Current_Pending 0 · Offline_Uncorrectable 0 · UDMA_CRC 0 · Raw_Read_Error 0 · Spin_Retry 0 · Multi_Zone 0. 25 °C, 5400 rpm, TRIM available. **Caveat: no self-test has ever been logged**, so its surface has never been validated (extended test ≈ 29 min).
   - **T7 #1 (`/dev/sdc`, NVMe serial `S6SFNJ0W520174M`) is the concerning one: 912 unsafe shutdowns** across **11,138 power-on hours** (8.19 TB written, 0 media errors). It is exFAT with no journaling, and it is the drive holding **T3 personal and the restic repo** — so T3's second copy is the highest-value work here.
   - T7 #2 (`/dev/sdf`, `S6SFNS0X911348E`): PASSED, 2,633 h, 30 unsafe shutdowns, 0 media errors. Both T7s report "self-tests not supported".
   - Internal `C:`/`D:` (SKHynix): PASSED, 2,317/2,322 h, 9 unsafe shutdowns each, **0 media errors**; `C:` runs warm at 54 °C.
   - Still unmeasured: **the WD 25E1** (detached).
   - **Serial duality, worth knowing before identifying anything:** each T7 reports a **USB-bridge** serial to Windows (`M471025W0JNFS6S`, `E843119X0SNFS6S`) and a **different NVMe** serial to SMART (`S6SFNJ0W520174M`, `S6SFNS0X911348E`). The `/dev/sdX` order follows physical-drive order with the VHDX (`PD3`) absent, so `sdc` = `PD2` = `I:` and `sdf` = `PD5` = `H:`.
6. **`I:\wiki_md` + `I:\weaviate_v2_archive`** (dated 2026-04-16) — complete or stale? Answered **2026-09-27, by file-level comparison** (`scripts/compare-trees.py`, `eve-audit/weaviate-diff-classify.py`) — and it corrected this document's own first attempt at the answer:
   - **`weaviate_v2_archive`: the durable data is the same on both copies.** 1,430 paths are shared and **1,128 durable index files match with 0 differing**. Every difference is *write-ahead traffic*: 456 `.wal` + 42 LSM only on `D:`, 403 `.wal` + 24 LSM only on `I:`, 2 `hnsw.commitlog` files that differ in size — **~37 MB vs ~2 MB out of 563 GB**. **Correction:** an earlier edit here called the `I:` copy *"71 files / ~30 MB short — verifiably incomplete."* That was wrong twice over: the 71 was a net coincidence between 498 and 427 differing paths, and *every one of those paths is an ephemeral log*, not archive content. The right conclusion: the copy is **not short, it is non-quiescent** — its WALs were mid-rotation when the copy was taken.
   - **`I:\wiki_md` is an empty tree: 0 files, 0 GB** (only an empty `2017` folder exists). **There is no `I:` copy of the wiki corpus at all.** `D:\wiki_md` holds the corpus: `2017` (535 entries), `2021` (126), `2026` (143).
   - **The three chunk datasets are the design, not redundancy (Architect, 2026-09-27).** Measured per dataset: `wikichunk` **152.444 GB**, `wikichunk2021` **185.602 GB**, `wikichunk2026` **225.151 GB** — three distinct sizes for three distinct cut dates (2017 / 2021 / 2026), the frozen-record axis Truthdrift compares a claim across (`MOTIVATION.md` §2). **Never deduplicate, prune, merge or collapse these against one another**, and never read a size difference between them as a fault or a stale copy. "Two copies" in this document means **drives**: the same three snapshots on `D:` and `I:`, with per-dataset byte totals identical to three decimals. `wikichunk2021` and `wikichunk2026` match file-for-file across the drives (497/497 and 411/411); `wikichunk` differs only by 19 `.wal` files (562 vs 543); the rest of the churn is Weaviate's internal `vector_index_*` dirs. `eve-audit/weaviate-datasets.py` reproduces this table, so the claim stays scoped to drives and cannot drift into "the snapshots are duplicates".
   - **Consequence for the plan:** a live-database copy can never be byte-identical, so "verify the copy" has to mean *compare the durable index files*, and the 2627 copy should be taken **after a clean Weaviate shutdown** (WALs checkpointed into the index) — see step 4.
7. ~~**`D:\AI_Factory\qdrant_storage`** — may hold reusable embeddings.~~ **RESOLVED 2026-09-27 — nothing to reuse.** Measured **2 files / ~0 GB** (created 2025-12-04, last written 2025-12-09). The "embeddings already paid for" hope in §3 does not survive contact with the directory, so nothing in the AI Factory tree needs special handling for that reason.
8. **Google Drive quota** — unreadable via the mount.
9. **The tooling for the remaining checks is not installed (measured 2026-09-27).** `smartctl`, `7z`, `rclone`, `bzip2`, `zimdump` and `zimcheck` are all **missing**; `docker`, `tar` and `python` are present. Per item: **ZIM integrity (#4)** still needs `kiwix-tools`/`libzim` (the `.bz2` dumps are fine — `tar` handles bzip2); **HDD health (#5)** needs **smartmontools**, and `winget install smartmontools.smartmontools` (7.5) is available — note SMART reads need elevation; **Google Drive quota (#8)** needs `rclone` or the Drive UI; **`media-weaviate` (#3)** is now **resolved** (compose project `cursor_hol`, 994.5 kB — §6 item 3), and it turned up ~12 GB of unique data inside `docker_data.vhdx` that the tiers did not account for.

## 7. Ordered next actions

**Copy-first (2026-09-27).** Every step below is a **copy or a read**; the delete halves are optional, last, and only
after that copy is verified. Identify the destination drive **by serial** before writing anything to it, and never
assume the free letter is the right disk — this document exists partly because a drive letter moved.

1. **Land `I:\HDD_MOVE_TEMP` (423 GB) onto the verified external drive** — still the highest urgency anywhere in this
   document. **Keeping the original is the point**; freeing 423 GB on I: is a side effect, not a goal.
2. **Health-check that drive before it holds anything irreplaceable** — SMART via `smartmontools -d sat`, plus a timed
   write test (both WD portables are likely SMR; identify by serial, e.g. the blank one is `WX32D10DE684`).
3. ~~**Size and compare `C:\wiki_*`** → take the C: win if they are stale.~~ **DONE 2026-09-27 — no C: win exists.** All three directories are empty (0 files); the step is void. What it *does* free is attention: the C: recovery story is now `docker_data.vhdx` (step 8) and nothing else.
4. **Copy `D:\weaviate_v2_archive` → the external drive**, verify — **then, optionally and later,** consider deleting from D: (§5 note: optional and last; the archive is irreplaceable and its three snapshots are the design).
   **Verification caveat (2026-09-27, corrected):** stop Weaviate and let it shut down **cleanly** before copying (so the write-ahead logs checkpoint into the index), and verify by comparing **durable index files** — 1,128 of them today — never by raw file count. A copy taken while the database is open will always differ in `*.wal` and `hnsw.commitlog` files, which is what made the `I:` copy look "short" when it was only unclean (§6 item 6).
5. **Pack + copy T1 markdown** (`D:\wiki_md`, 18.76M files) → external drive **and** `G:` — **the top priority after step 1**, because T1 is **single-copy** (§4). Pack it; do not copy 18.76M loose files.
6. **Extend restic**: add `C:\EMPIRE`, `%LOCALAPPDATA%\EMPIRE`, a `pg_dump`; replicate the repo off `I:`.
7. **Re-home the cloned repos** to `D:\repos\` (P9 source trees).
8. **Relocate `docker_data.vhdx`** to D: once D: is free → ~368 GB on C:.
9. **Archive the T6 legacy tree** to the 2627, after identifying items 1 and 3 above.
10. **Then, and only then**, the `V:\Cognee` cleanup — **optional and last** (it holds nothing but the three wiki datasets), and never before a verified backup exists. Nothing in this list requires deleting a snapshot, a source, or a copy.

## 8. What to glean before moving anything

The move is not urgent; the *reading* is. Extraction first, relocation second — because moving changes the paths that
docs and scripts reference, and because some of this is only readable while a given drive is alive.

### 8.1 The earliest material is older than the notes suggest

`E:\AI_PROJECTS` contains **`learning_hub_20241114_172407.log`** — a log **dated 2024-11-14 by its own filename**,
with siblings from mid-November and a `learning_hub.log`. So project activity predates the vault (whose oldest note
is 2025-01-12) by roughly two months, matching your memory of work starting in **October 2024**. Where to dig:

- **the `learning_hub*.log` series** in `E:\AI_PROJECTS` — likely the raw narrative of the first attempt
- `E:\transfer_112724` and `E:\workpc backup` (Nov–Dec 2024 migration snapshots)
- **OneDrive version history** on the vault folders — the only place a *pre-2025* note text could still exist
- (Note: `…\Desktop\FROM EXHDD` holds `.md` from **2020-09-29**, but its files are audio — that is music archive, not project history.)

### 8.2 The repo already contains a measurement layer — and it encodes your research thesis

`data/eval/` is small, structured, and far more valuable than its size suggests:

| Artifact | What it holds | Why it matters |
|---|---|---|
| **`wiki_driftbench_seed.jsonl`** | hand-written cases with `must_contain`, `expect_title_any`, **`must_not_contain`**, and **tags** like `parametric_distractor`, `revival`, `vague`, `bio`, `entity` | **The poisoned-well test already exists in miniature.** Case `hand_03` says it outright: *"Must not hallucinate Kate Bush single 'Wow' from parametric memory."* That is a drift probe: does she answer from the frozen archive, or from training? |
| `wiki_calibrate.jsonl` | the same cases plus calibration notes | the seed/calibrate pair — a starting ontology for drift questions |
| **`acceptance/retrieval_rerank_*.yaml`** | a **dated series** (Sep 7 → Sep 26) with `case_count`, `hit_count`, per-case backend, `production_embed: nomic-embed-text` | a real quality **trajectory**. The latest: **7 cases, 6 hits**, the single miss named `paraphrase_unpromoted_fact`. This is the baseline P5 (rerank) should be judged against — and it is about `cross_encoder`, exactly P5's open question |
| `research_bench.jsonl` | web cases with `expect_tool_any` and `must_not_mention` (e.g. *"as an AI language model"*) | anti-hallucination assertions for the research path |
| `wiki_workbench*.jsonl`, `wiki_extract.jsonl`, `architect_smoke_scorecard.json` | retrieval + extract + smoke scorecards | more measurement already sitting there |

**The strategic reading:** the drift benchmark is the bridge between the corpus and the research you described. It is
currently ~7 handwritten cases asking "does the model answer from the archive instead of its priors?" — and the
2017/2021/2026 corpus plus the **meta-history revision dump** can scale that from 7 cases to thousands, with the
*edits themselves* as ground truth about how a claim changed. Nothing needs to be built from scratch to start; the
vocabulary (`parametric_distractor`, `revival`) and the harness already exist.

### 8.3 Cheap reads with high yield, in order

1. **`data/eval/*` + the acceptance series** — minutes; establishes the baseline and the drift vocabulary.
2. **The five design notes** — `08-15-2025 - Raine blueprint.md`, `raine roadblocks - clear paths`,
   `08_16_25_rAIne non n8n_MVP_v1 setup.md`, `MASTER- Gemini Zet God script.md`, `3A - ZED2RSS.md`. Recovers
   designed-but-unbuilt work (Zet, and the reason n8n was dropped).
3. **`learning_hub*.log`** — the 2024 origin narrative, and where the October material likely hides.
4. **`AI_FACTORY_STATUS_REPORT.md` + `architecture_scan_results.md`** (Dec 2025) — prior self-assessment; the same
   questions asked a year earlier.
5. **`MASTER_RAINE_TO_EMBED`** — what was staged for embedding, i.e. the corpus strategy of that era.
6. **`H:\AI_ARCHIVE\AI_Archive_Legion\github_repos\`** — a third repo collection (open-webui, SillyTavern,
   text-generation-webui etc., cloned Nov–Dec 2025) = prior-art code, distinct from your own repos.
7. **`D:\AI_Factory\qdrant_storage`** — possibly embeddings already paid for.
8. **`%LOCALAPPDATA%\EMPIRE\chat-history`** + `eve-trace.jsonl` — what Eve was actually asked and answered.

### 8.4 What cannot be gleaned, and should not be claimed

Google Drive quota, ZIM integrity, and both HDDs' health are all still **unknown** (the `media-weaviate` volume was
resolved 2026-09-27 — §6 item 3). They
stay listed as unknown in §6 rather than estimated. Two former entries on this list are now closed rather than
unknown: **`RAINE_ABACUS_PROJ_FOLDER` was found** (digest §I.2), and the `I:` copies are no longer merely unknown —
`I:\weaviate_v2_archive` is *measurably short* (§6 item 6), which is a finding, not a gap in the record.


## 9. Method note

Every number here was measured on this machine on 2026-09-27 — drive serials, file counts, sizes, chunk counts from
a live Weaviate aggregate query, and a timed read benchmark. Where something is *not* known it is listed as unknown
above rather than estimated. Two earlier errors are recorded deliberately, because both would have destroyed value:
the dormant Cognee store was nearly discarded as "re-derivable public data" before its contents were read, and the
`E:` letter was assumed to name the same disk across a hardware swap.

## 10. Deep verification, 2026-09-28 — what IS and IS NOT present

The Architect's instruction: *"go deep into any structures that werent looked at before and verify what is and is not
there."* Method: `eve-audit/deep-probe.py` (read-only, 41 s) plus targeted follow-ups. Everything below was opened,
not inferred.

### 10.1 Verified present, and what each actually is

| Tree | Measured | What it is |
|---|---|---|
| **`I:\User_Files`** | **781,163 files / 1.67 GB** | **Identified at last: a music archive.** 777,941 `.mid`, 2,171 `.mp3`, 263 `.bfd2pal` (BFD palettes), plus `.g24`/`.dfh`/`.kt3` (Drumagog, Kontakt). Dirs: `800000_Drum_Percussion_MIDI_Archive[6_19_15]`, `Presets`, `PresetsEZX`, `User_Midi`, `User_Presets`. **Not project data — drum/MIDI material**, and a *tiny-file* tier, so it needs `tar` (the bsdtar crash on it is now explained by shape, not corruption) |
| **`H:\AI_stuff_backup`** | 259,754 files / 26.77 GB | A Python environment/dist backup — 67,830 `.py`, 62,832 `.pyc`, 58,061 `.xml`, 26,262 `.h` (a `site-packages` shape) — **plus the unique part: `setup_environment-Aporia.py`, `full_stack_setup-Aporia.py`, and a `.env`**. The `-Aporia` names tie it to the Aporia lineage; **`.env` is a secrets file** and must never be ingested |
| **`H:\gutenberg_books_txt`** | **67,588 `.txt` + index** / 26.21 GB | A clean **Project Gutenberg corpus**, `NNNNN-Title.txt`, with `.gutenberg_index.json`. Public domain; likely a second copy of the corpus in `E:\gutenberg_books_txt` |
| **`H:\colibri`** 252 files / 0.01 GB · **`H:\llama.cpp`** 1,141 / 0.14 GB · **`H:\User_Files`** **0 files** | — | trivial / empty |
| **`C:\Users\m69nr\.ollama\models\blobs`** | **61 files / 118.63 GB** | the ollama model store — **118.6 GB, not the ~38 GB implied by the large-file list** (that list only caught its biggest blobs). Regenerable (T5) |
| **`Desktop\PROJECT HUB\RAINE_ABACUS_PROJ_FOLDER`** | **70,861 files / 3.48 GB** | the Abacus project, present as the digest §I.2 said |
| **`C:\Empire_Workbench`** | 14,653 / 2.82 GB | the live vault (T4 copy made) |
| **`D:\Empire_Workbench`** | **11,313 / 1.27 GB** | **not a stub** — holds **`_github_staging\`** (the P9 repo source trees) + `04_Infrastructure`. **Not backed up** |
| **`I:\EMPIRE_BACKUP\restic`** | 74 files / 1.18 GB | the only restic repository; its `restore-test\` (14,653 files / 2.82 GB) is a restored copy of `C:\Empire_Workbench` — so **that backup covers the Workbench only** |
| **`C:\ProgramData`** | — | DockerDesktop data, Toontrack, and the music-gear vendors (Akai, Roland Cloud, inMusic, Drum Workshop), NVIDIA, Oculus |
| **`V:\Cognee`** | just `databases\` | the Cognee store, as expected |
| **`C:\EMPIRE\backend\pocketbase\pb_data`** | 3 files / 2 MB | the PocketBase database is tiny |

### 10.2 The Legion's never-opened subdirectories (measured)

`AI_Archive_Legion` = 1,131 GB. Its 1,054 GB headline hides this split:

| Subdir | Files | Size | Verdict |
|---|---|---|---|
| `knowledge_bases` | 6,328 | **771.6 GB** | 49 ZIMs (595 GB) + StackExchange/devdocs/other — **being copied now** |
| `models` | 384 | 237.2 GB | T5, regenerable |
| `embeddings_models` | 818 | 54.8 GB | T5 |
| `datasets` | 191 | 23.8 GB | **HumanEval, OpenOrca** — HF datasets, re-downloadable |
| `github_repos` | **215,019** | 18.9 GB | 38 repo clones (anything-llm, ComfyUI, applio, alltalk-tts, amical…) — re-clonable |
| `python_packages` | 904 | 17.1 GB | T5 |
| `binaries` | 8 | 4.9 GB | T5 |
| **`rag_tools`** | **42,484** | **2.4 GB** | chroma, docling, faiss, graphrag, haystack, lancedb, langchain, llama_index, meilisearch, milvus — a RAG tooling collection. **Excluded from the T6 copy** |
| `drivers` · `runtimes` · `docker_images` | 3 · 5 · 1 | 0.8 · 0.2 · 0 GB | T5 |
| **`search_engines`** | 4 | 0.16 GB | **meilisearch.exe (132 MB), qdrant, typesense, zincsearch** — a local search kit. **Excluded from T6** |
| **`prompts`** · **`documentation`** · `scripts` | 5 · 4 · 62 | ~0 | `phase1_architect.md`, `phase2_engineer.md`, `PROMPT_LIBRARY.md`, `prompts.json`; `AI_DEVELOPER_TOOLKIT.md`, `SPECIALIST_MODELS.md`. **These WERE copied** (T6 included root + these dirs) |
| `500-AI-Agents-Projects` | 35 | ~0 | list only |

So the T6 exclusion was **right about the 1,050 GB** and **deliberately left two small-but-real collections behind**:
`rag_tools` (2.4 GB) and `search_engines` (0.16 GB) — both re-installable, but now named rather than assumed.

### 10.3 What is still in NO backup tier (the honest gap list)

| Item | Size | Why it matters |
|---|---|---|
| **`D:\Empire_Workbench`** (`_github_staging` — the P9 repo trees) | 1.27 GB | unique working trees; T4 copied only `C:` |
| **the two later Heptabase exports** (`Downloads`, 1,009 + 1,290 cards) | ~1.5 GB | discovered 2026-09-28; newer than the April export |
| **`I:\User_Files`** (MIDI/drum archive) | 1.67 GB | music material, single copy, tiny-file shape |
| **`rag_tools` + `search_engines`** (Legion) | 2.6 GB | excluded on purpose; re-installable |
| **`H:\AI_stuff_backup`** unique parts (`*-Aporia.py`, `.env`) | ~MBs | the rest of that 26.8 GB is a venv |
| `H:\gutenberg_books_txt` | 26.2 GB | public domain, re-downloadable |
| **T1 `2021` + `2026` archives** | — | the resume job is queued |
| **T2 Weaviate**, **T0 (25E1 ZIMs + XML)** | 563 GB + 558 GB | T2 already on two drives; T0 needs the drive attached |

**Unit caution for future readings:** `robocopy` reports **GiB**, my Python probes report **decimal GB** — the ratio is
1.0737. That difference (718.587 vs 771.58 for the same 6,328 files) is not a discrepancy and not missing files; it
was checked.

## 11. Google Drive (`G:`) — the tier that was never opened

Added 2026-09-28, on the Architect's prompt: *"dont forget about my google drive on G: drive / the folder
'G:\My Drive\0.0_new_incoming_including_knit_perform' doesnt say AI or coding but has alot in there."* Correct on both
counts: `G:` had never been inventoried, and that folder is far more than its name suggests. Census:
`eve-audit/g-drive-census.py`.

### 11.1 Quota — §6 item 8 is resolved

| | |
|---|---|
| Total | **~1,021.8 GB** |
| Used | **749.3 GB (73.3%)** |
| **Free** | **272.5 GB** |

§1 said the Drive FS "reports the same size as `C:` — not your Drive quota" and §6 item 8 listed the quota as
unreadable via the mount. **It is readable now** (`shutil.disk_usage` on `G:\My Drive`), and the numbers are not
`C:`'s (951.6 total / 267.4 free). **Consequence: `G:` is a usable cloud destination with ~272 GB free** — enough for
the packed 2017 markdown plus a manifest, which is what §4's placement table proposed for it.

### 11.2 Top level of `G:\My Drive`

| Folder / item | What it is |
|---|---|
| **`_Project Master`** | **a Drive copy of the repo's `docs/expansion_docs/`** — `EVE_OLLAMA_EXPANSION_MANIFEST.md` (68.9 KB), `EMPIRE_LOCAL_UPGRADE_RESEARCH.md` (61.2 KB), the research snapshot, idea queue, `LOCAL_NO_ACCOUNT_MCP_CATALOG.md`, `local-no-account-tools.yaml`, `CURSOR_HANDOFF.md`, `last_communication.md`, and a `.github/agents/empire-upgrade-researcher.agent.md` Copilot agent definition — **plus** `PROMPTS AND RESULTS\` (NLM-extraction prompts for Eve with their outputs: `aiunited`, `SimplyAI`, `48 LAWS OF POWER`), `3 prong processing engine` (270 KB), and the **`P_Raine to Empire_pt1…pt5_final.md`** series with `P_Truth Drift.md`, `P_Universal Primitives.md`, `P_Universal Synthesis Framework.md`, `P_ProctorWIZ.md` |
| **`0.0_new_incoming_including_knit_perform`** | 20 entries: the **Alliance** band material (`ALLIANCE - WRITING ON THE WALL`, `GIG_FILES COMBINED`, `WOW2`, `Alliance Knitting Factory Photos`), `ELECTRIC CALLBOY BLISS`, `BRIDGE`, `KEEPER_7_7_26`, `THE KEEPER AND LOOM CONSTRUCT IN FULL`, `TOOLBOX_GUMLOOP_PROJECT`, `gumloop_multi_agent skill audit`, `notebooklm to gumloop for skills creation`, `master guides`, `NEXTUS`, `kimi experimenr`, `openai_workaround`, `inspiration_images_shotdesk`, a 1.8 GB `RMC_CHOIR_PROMO.VOB` (the same file as in `I:\HDD_MOVE_TEMP`), two drumming PDFs — **and `comparing_models_for_eve_and_weaviate.txt`** |
| **`1. AI related in any way`** | 12 entries: `1. SCRIPT AND TOOL LIBRARY`, `2. App_Projects`, `BEE HUB`, `CREATED PROMPT LIBRARY`, `DAZE`, `DAZE-docs`, `DIFY KNOWLEDGE BASE FILES`, **`hatchprojects_app_closed_down`**, **`Perplexity Reports`**, `proctor_WIZ`, `UNSORTED`, `WEB TUTORIALS` |
| **`nov26_lcc_laptop_docs`** | 14 recent project folders: **`BEE HUB`, `chatter`, `chord sheet container`, `DAZE`, `dbs`, `HIGH LEVEL RESEARCH HUB`, `NEXTUS`, `proctor_WIZ`, `Project_polymath`, `ragbuild`, `Repo_ripper Agent`, `student degree tracker`** — several of these names appear in no repo document |
| **`DAZE-docs`** | 8 files: `DAZE_Case_Study`, `DAZE_Full_Summary`, `DAZE_New_Developer_Checklist`, `DAZE_Prompt_Library`, `DAZE_Slide_Outline`, `DAZE_Smoke_Test_Script`, `DAZE_Teaching_Packet`, `DAZE_Workshop_Handout` — **a full product-and-teaching packet for a shipped EMPIRE product** |
| `_NLM PROCESSING` · `0.1_postLCC_AI` · `..shadowplanner_sync` · `3_16_26_wiki_research` · `lcc laptop dump` · `AI model dump` · `Flowchart AI` (×2) · `Gemini Gems` | NotebookLM processing (the Workbench vault's recorded source), post-LCC AI material, wiki research, laptop dumps, an AI model dump |
| `2. DRUM_MIDI_STEM_CENTRAL` · `3.MUSIC RELATED` · `5.BAND_MEDIA` · `6. AI MUSIC AND VOICE CREATIONS` · `MY MUSIC HUB` · `Jennifer's music` | the music estate, in the cloud |
| `4_1_26_work_pc_backup_new_pc_coming` · `4. personal` | a work-PC backup and personal material |
| **`DAZE-prevscode`** | a previous VS Code state: `src`, `index.html`, `package.json`, `tailwind.config.js`, `vite.config.js`, **and a `.env`** (secrets — never ingest) |
| **110 loose `.gdoc` files** | an architecture-doc library by title: *100x Synoptic System Research Expansion*, *Advanced Agentic AI Design Patterns and Execution Skills*, *Advanced Agentic Workflow and LLM Skill Registry*, *Advanced Knowledge Graph Embeddings and Semantic Entity Resolution Framework (SERF) Implementation Blueprint*, *Advanced MCP Skill Sets for Agentic Workflows*, *Architectural Blueprint: Semantic Routing Gateways and Agentic Governance*, *Agentic PRD Generation*, *AI AND MENTAL HEALTH*, *AI Toolbase Research: LangSmith/Langfuse*, *Architecture Guide: VLM Ingestion & Claim Check Pattern*, … **+50 loose `.eml` files** (5.4 MB of AI newsletters, `🦾`-prefixed TAAFT items) |

### 11.3 The three things here that matter most

1. **`EVE_OLLAMA_EXPANSION_MANIFEST.md` is the source contract for the system as built** — *"Status: research complete;
   implementation plan ready for Cursor. **Verified: 2026-09-06**"*, written against *"RTX 5080-class GPU with 16 GB
   VRAM, 64 GB system RAM"*, stating the governance in plain terms: **"PostgreSQL is authoritative for jobs,
   approvals, audit records, artifacts, and provenance"** · **"PocketBase is the human-facing task/realtime UI layer,
   not a second source of truth"** · **"Never give the model an arbitrary shell, filesystem path, SQL, Docker, or
   browser-JavaScript tool"** · **"Every destructive, external, desktop-input, Docker-lifecycle, or source-file
   mutation action requires an explicit approval token"** · Cognee *"holds curated durable memories… not a
   raw-document dumping ground."* **This is the design that `OPERATING_CONTRACT.md`, the Toolbelt and `admit_for_goal`
   implement.** It also makes model availability *"a health check, not an assumption."*
2. **`comparing_models_for_eve_and_weaviate.txt` (created 2026-09-05)** — a model-selection conversation **about Eve
   itself**, sitting in the folder that "doesn't say AI": *"I have 16gb vram and 64gb ram. i am using if for versel
   eve."* It weighs **Spark-X2.5-4B** (1 M-token context, ~2.5 GB, leaving VRAM for the KV cache — recommended
   precisely because *"Eve agents parse directories of code and text"*) against **Qwen3.8-27B-GSQ-RCO IQ3_S** (~11.8 GB,
   native reasoning traces, multimodal, 262 K context, MTP for speculative decoding). **A dated, reasoned model decision
   for the Eve runtime that exists nowhere in the repo.**
3. **`P_Raine to Empire_pt5_final.md`** — a structured self-review of the migration in seven sections, closing with
   **"Semantic analysis of overall feelings on the project"**: *"Overall mood: Pragmatically ambitious yet financially
   and structurally constrained."* It records an intent not yet carried out — **"Plans to reuse behavioral data and
   conversation logs (focused on frustration management) from previous Gemini Gems to shape the personality of the
   agent Eve"** — and names the lineage: *"Rain: serves as the direct successor/evolution of the Rain project,
   retaining PocketBase as the local task manager"*, plus the **Universal Synthesis Architecture** as its origin. The
   `pt1…pt5` series with `P_Truth Drift.md` is the Raine→EMPIRE transition write-up, in the Architect's own words.

### 11.4 Correction to `DOC_MAP.md`

`DOC_MAP` §3 files `docs/expansion_docs/` (9 files) under **"History — kept, not read"**, described as work logs with
"no code references". That is wrong in substance: three of those files are **contracts** —
`EVE_OLLAMA_EXPANSION_MANIFEST.md`, `EMPIRE_LOCAL_UPGRADE_RESEARCH.md`, `LOCAL_NO_ACCOUNT_MCP_CATALOG.md` — and the
manifest is the *source* of the operating rules the repo now enforces. The mislabel is explained by size: DOC_MAP
recorded the folder as 0.2 MB, but it holds a 68.9 KB manifest and a 61.2 KB research report. **Corrected in
`DOC_MAP.md` on 2026-09-28** — the folder is read-when-relevant, not history.

### 11.5 What is unique here, what is duplicated, and the honest boundary

- **Duplicated (safe):** `project_manifesto_9_7_26` **is** the repo's `docs/expansion_docs/`, and
  `2. EMPIRE_MANIFESTO.md` is the repo's root `EMPIRE_MANIFESTO.md`. **Both exist in two places, one of them cloud.**
- **Unique to `G:` (not found in the repo in this pass):** the `P_*` prompt series (`P_Raine to Empire_pt1–5`,
  `P_Truth Drift`, `P_Universal Primitives`, `P_Universal Synthesis Framework`, `P_ProctorWIZ`), `3 prong processing
  engine` (270 KB), the `PROMPTS AND RESULTS` prompt/output pairs, the **`DAZE-docs` product-and-teaching packet**,
  `hatchprojects_app_closed_down`, the **`Perplexity Reports`**, the `nov26_lcc_laptop_docs` project set
  (`chatter`, `Project_polymath`, `NEXTUS`, `HIGH LEVEL RESEARCH HUB`, `chord sheet container`, `student degree
  tracker`, `ragbuild`…), the `KEEPER`/`LOOM`/`GUMLOOP` material, the Eve model-comparison chat, and the
  **110 `.gdoc` titles + 50 `.eml` newsletters**.
- **Boundary that matters:** **`.gdoc` files on a Drive mount are *shortcuts*, not documents.** A filesystem walk sees
  the title and the id; the content is not there. Reading those 110 documents needs a Drive export (web UI or API), so
  **they are inventoried but unread, and nothing should be claimed about them beyond their titles.**
- **Also unresolved:** `Gemini Gems` and `lcc laptop dump` report **0 children** through the mount — either empty or
  online-only and unmaterialised. Not guessed at.
- **Nothing unique in 11.5 is backed up.** It exists **only in the cloud**, and `G:` is a *sync* target, not a backup
  (deletions and account problems propagate — the same rule §2 applies to OneDrive). `G:` is therefore a candidate for
  **both** roles, and the two are not the same thing: the 272 GB of free space makes it a destination, while being the
  sole home of the `P_*` series and the DAZE packet makes it a *source* to copy outward.


