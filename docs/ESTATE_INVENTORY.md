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
| **E** | WD My Passport **25E1** `WX41AA69RHTD` | **HDD** USB | 1863.0 | 1017.4 | 845.6 | NTFS |
| **H** | Samsung T7 Shield `E843119X0SNFS6S` (T7 #2) | SSD USB | 3725.9 | 1291.7 | 2434.2 | exFAT |
| **I** | Samsung T7 Shield `M471025W0JNFS6S` (T7 #1) | SSD USB | 3725.7 | 1860.1 | 1865.6 | exFAT |
| **V** | VHDX file *inside* `I:\EMPIRE_VHDX\empire_cognee.vhdx` | — | 2048 | 2044.4 | 3.6 | NTFS |
| **G** | Google Drive FS (client running) | cloud | quota **unreadable this way** | — | — | — |
| *(detached)* | WD My Passport **2627** `WX32D10DE684` | **HDD** USB | 3726 | **3726 — wiped blank** | 0 | NTFS |

Notes that matter:

- **`V:` is not a disk.** It is an NTFS volume inside a VHDX *file* that lives on `I:`. Clearing it frees nothing on
  C: or D:, and frees nothing on I: unless the VHDX is compacted. Mount/detach: `scripts/mount-cognee-vhdx.ps1`
  (and `-Detach`, which needs elevation).
- **`G:` reports the same size as `C:` (951.7 GB)** — that is the Drive FS mirroring the system volume, **not** your
  Drive quota. Ask the Drive UI, or `rclone about`.
- **No SMART from either HDD's USB bridge.** Windows "Healthy" is a shallow status. `smartmontools -d sat` before
  trusting either with irreplaceable data.
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
  exists. There is a Desktop folder `R_UNIVERSAL SYNTHESIS ARCH` (2026-08-30) — **hypothesis only, unverified**.
- **`media-weaviate`** used docker volume `cursor_hol_weaviate_data` — contents unidentified.
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
| **T7 notes** | **three documentation eras, all located:** OneNote (`ONENOTE BACKUP PREOBSIDIAN.md`, 383,846 B / 8,339 lines, **Dec 2024 → 2025**) · Obsidian (497 + 474 notes) · Heptabase (`All-Data.json` 25.3 MB + `Card Library` + `Journal` + `Whiteboard`) — plus Desktop note folders (`DAZE`, `PROJECT HUB`, `HIDDEN`, `TOOL_FACTORY_GUMLOOP*`) | ~1.5 GB | OneNote + Obsidian live **in OneDrive** (sync ≠ backup); the Heptabase export sits on `H:`. See digest §H |

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
| Reconcile `C:\Empire_Workbench` vs `D:\Empire_Workbench` | small | **RESOLVED 2026-09-27:** `C:` is live (13 top-level entries, written 2026-09-26); `D:\Empire_Workbench` is a **2-entry stub** from 2026-09-01. The stub can go later **if you choose** — optional, and not needed for any backup |

Keep on internal D:: `wiki_md` (81 GB) — it is the runtime corpus and wants SSD latency.

## 6. Open items — verify before touching

1. ~~**`RAINE_ABACUS_PROJ_FOLDER`**~~ **RESOLVED 2026-09-27** — never missing: it lives at `…\Desktop\PROJECT HUB\RAINE_ABACUS_PROJ_FOLDER\` (May 2026), containing a dockerised agent system with `agent_resource_pipeline/`, its own Weaviate `runtime/`, cloned resource repos and a `MANUAL.md`. Read `MANUAL.md` + `agent_resource_pipeline/` first. See digest §I.2.
2. ~~**`C:\wiki_*`** — sizes unknown; must be compared against D: before any deletion.~~ **RESOLVED 2026-09-27 — they are empty.** `C:\wiki_md`, `C:\wiki_runs` and `C:\wiki_dumps` each hold **0 files / 0 GB** (verified to depth 2 with `-Force`). No comparison was needed because there is nothing there. **The §5 space-recovery row is corrected accordingly** — a reminder that the 2026-04-07 creation dates were evidence of a *plan*, not of content.
3. **`media-weaviate` volume** `cursor_hol_weaviate_data` — unidentified.
4. **ZIM integrity** — 16 archives, 461 GB; verify checksums before treating as a source of record.
5. **HDD health** — no SMART from either WD; read real counters before entrusting T3/T0/T2.
6. **`I:\wiki_md` + `I:\weaviate_v2_archive`** (dated 2026-04-16) — complete or stale? Answered **2026-09-27, by file-level comparison** (`eve-audit/compare-trees.py`, `eve-audit/weaviate-diff-classify.py`) — and it corrected this document's own first attempt at the answer:
   - **`weaviate_v2_archive`: the durable data is the same on both copies.** 1,430 paths are shared and **1,128 durable index files match with 0 differing**. Every difference is *write-ahead traffic*: 456 `.wal` + 42 LSM only on `D:`, 403 `.wal` + 24 LSM only on `I:`, 2 `hnsw.commitlog` files that differ in size — **~37 MB vs ~2 MB out of 563 GB**. **Correction:** an earlier edit here called the `I:` copy *"71 files / ~30 MB short — verifiably incomplete."* That was wrong twice over: the 71 was a net coincidence between 498 and 427 differing paths, and *every one of those paths is an ephemeral log*, not archive content. The right conclusion: the copy is **not short, it is non-quiescent** — its WALs were mid-rotation when the copy was taken.
   - **`I:\wiki_md` is an empty tree: 0 files, 0 GB** (only an empty `2017` folder exists). **There is no `I:` copy of the wiki corpus at all.** `D:\wiki_md` holds the corpus: `2017` (535 entries), `2021` (126), `2026` (143).
   - **The three chunk datasets are the design, not redundancy (Architect, 2026-09-27).** Measured per dataset: `wikichunk` **152.444 GB**, `wikichunk2021` **185.602 GB**, `wikichunk2026` **225.151 GB** — three distinct sizes for three distinct cut dates (2017 / 2021 / 2026), the frozen-record axis Truthdrift compares a claim across (`MOTIVATION.md` §2). **Never deduplicate, prune, merge or collapse these against one another**, and never read a size difference between them as a fault or a stale copy. "Two copies" in this document means **drives**: the same three snapshots on `D:` and `I:`, with per-dataset byte totals identical to three decimals. `wikichunk2021` and `wikichunk2026` match file-for-file across the drives (497/497 and 411/411); `wikichunk` differs only by 19 `.wal` files (562 vs 543); the rest of the churn is Weaviate's internal `vector_index_*` dirs. `eve-audit/weaviate-datasets.py` reproduces this table, so the claim stays scoped to drives and cannot drift into "the snapshots are duplicates".
   - **Consequence for the plan:** a live-database copy can never be byte-identical, so "verify the copy" has to mean *compare the durable index files*, and the 2627 copy should be taken **after a clean Weaviate shutdown** (WALs checkpointed into the index) — see step 4.
7. ~~**`D:\AI_Factory\qdrant_storage`** — may hold reusable embeddings.~~ **RESOLVED 2026-09-27 — nothing to reuse.** Measured **2 files / ~0 GB** (created 2025-12-04, last written 2025-12-09). The "embeddings already paid for" hope in §3 does not survive contact with the directory, so nothing in the AI Factory tree needs special handling for that reason.
8. **Google Drive quota** — unreadable via the mount.
9. **The tooling for the remaining checks is not installed (measured 2026-09-27).** `smartctl`, `7z`, `rclone`, `bzip2`, `zimdump` and `zimcheck` are all **missing**; `docker`, `tar` and `python` are present. Per item: **ZIM integrity (#4)** still needs `kiwix-tools`/`libzim` (the `.bz2` dumps are fine — `tar` handles bzip2); **HDD health (#5)** needs **smartmontools**, and `winget install smartmontools.smartmontools` (7.5) is available — note SMART reads need elevation; **Google Drive quota (#8)** needs `rclone` or the Drive UI; **`media-weaviate` (#3)** needs only Docker, which *is* present — so that one is runnable right now, and is the cheapest remaining unknown.

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

`media-weaviate` volume contents, Google Drive quota, ZIM integrity, and both HDDs' health are all still **unknown**. They
stay listed as unknown in §6 rather than estimated. Two former entries on this list are now closed rather than
unknown: **`RAINE_ABACUS_PROJ_FOLDER` was found** (digest §I.2), and the `I:` copies are no longer merely unknown —
`I:\weaviate_v2_archive` is *measurably short* (§6 item 6), which is a finding, not a gap in the record.


## 9. Method note

Every number here was measured on this machine on 2026-09-27 — drive serials, file counts, sizes, chunk counts from
a live Weaviate aggregate query, and a timed read benchmark. Where something is *not* known it is listed as unknown
above rather than estimated. Two earlier errors are recorded deliberately, because both would have destroyed value:
the dormant Cognee store was nearly discarded as "re-derivable public data" before its contents were read, and the
`E:` letter was assumed to name the same disk across a hardware swap.


