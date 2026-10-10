# EMPIRE document map

One page to find any document in this workspace. Measured 2026-09-26: **754 `.md` files,
169,062 lines** — the project is not short of documents, it is short of an index, so this is
the index. Nothing here replaces content; it says where things live and what is dead weight.

## 1. Read these, in this order

| Order | Document | What it is for |
|---|---|---|
| 1 | [../AGENTS.md](../AGENTS.md) | Daily loop, commands, ports, gates. The operational page. |
| 2 | [EMPIRE_GUIDE.md](../EMPIRE_GUIDE.md) | Fresh-chat context brief. Start here in a new session. |
| 3 | [EMPIRE_CLARITY.md](EMPIRE_CLARITY.md) | Core vs LEGO vs staging; light hands (`resource_pulse` / `admit_for_goal`). |
| 4 | [EMPIRE_USAGE_GUIDE.md](EMPIRE_USAGE_GUIDE.md) | Architect how-to: pages, Toolbelt, recipes. |
| 5 | [EMPIRE_MANIFESTO.md](../EMPIRE_MANIFESTO.md) | Why the thing exists (vision phases). |

## 2. By job

| Job | Document |
|---|---|
| Disassembly catalog + GitHub resource farm (pick up here) | [RESOURCE_FARM_AND_CATALOG.md](RESOURCE_FARM_AND_CATALOG.md), [DISASSEMBLY_CATALOG.md](DISASSEMBLY_CATALOG.md), [prompts/external-resource-farm-agent.md](prompts/external-resource-farm-agent.md) |
| **Capability verification (all tools + MCP — before UX smoke)** | [CAPABILITY_VERIFICATION.md](CAPABILITY_VERIFICATION.md), `scripts/verify-capabilities.ps1`, `data/curated_primitives/raw_materials/EVE_VERIFIED_CAPABILITIES.md` |
| Capability contract Eve reads | [PLAYBOOK.md](PLAYBOOK.md) |
| Tool/limb keyword index (route before overload) | [CAPABILITY_ROUTE.md](CAPABILITY_ROUTE.md) |
| Everyday verb → intent codex (scrape, research, lookup, …) | [INTENT_CODEX.md](INTENT_CODEX.md) |
| What runs in VRAM vs RAM (measured) | [PLACEMENT.md](PLACEMENT.md) |
| Web/wiki research behaviour + bench | [RESEARCH_BENCH.md](RESEARCH_BENCH.md), [RESEARCH_CLOSURE.md](RESEARCH_CLOSURE.md) |
| Voice (Speaches, push-to-talk) | [VOICE_PRESENCE.md](VOICE_PRESENCE.md) |
| Wiki / scout reasoning + prompt budget | [WIKI_SCOUT.md](WIKI_SCOUT.md) |
| Wiki layer audit: 20 GB corpus, one-shot converter, Eve read path, retired Weaviate | [WIKI_LAYER_AUDIT.md](WIKI_LAYER_AUDIT.md) |
| Switching to the operational (local) phase | [OPERATIONAL_HANDOFF.md](OPERATIONAL_HANDOFF.md) |
| Cognee storage on the T7 VHDX | [COGNEE_VHDX.md](COGNEE_VHDX.md) |
| Architecture, APIs, Eve tools, backup | [manifest/README.md](manifest/README.md) |
| Structural plan / evaluation | [REFACTOR_PLAN.md](REFACTOR_PLAN.md), [REFACTOR_EVAL.md](REFACTOR_EVAL.md) |
| Audit record (dated, measured running state) | [audits/2026-09-26.md](audits/2026-09-26.md) |
| **Vault + dialogue digest** (what the Obsidian entries and Gemini chats add: development, feelings, depth) | [audits/2026-09-28-vault-and-dialogue-digest.md](audits/2026-09-28-vault-and-dialogue-digest.md) |
| **Operating contract** (single source of truth; measured by `scripts/audit-empire.py`) | [OPERATING_CONTRACT.md](OPERATING_CONTRACT.md) |
| **Memory governance** (what Eve may remember, and where — her tier rules, wired into the `memory-and-ideas` limb) | [MEMORY_GOVERNANCE.md](MEMORY_GOVERNANCE.md) |
| **LEGO contract** (what fits: brick footprint, invariants, reject list, acceptance checklist) | [LEGO_CONTRACT.md](LEGO_CONTRACT.md) |
| **LEGO prompt** (hand this to an outside model: rules, output format, self-check, rejections) | [LEGO_PROMPT.md](LEGO_PROMPT.md) |
| **Attribution** (credits by origin, not a licence gate) | [ATTRIBUTION.md](ATTRIBUTION.md) |
| **Library access points** (reference material Eve reaches by name; registry `config/library.json`) | [OPERATING_CONTRACT.md](OPERATING_CONTRACT.md) §7 |
| **Local-upgrade contracts** — `EVE_OLLAMA_EXPANSION_MANIFEST.md` (the source of the operating rules), `EMPIRE_LOCAL_UPGRADE_RESEARCH.md`, `LOCAL_NO_ACCOUNT_MCP_CATALOG.md` | [expansion_docs/](expansion_docs/) |
| Idea queue / deferred ideas | [EMPIRE_IDEA_QUEUE.md](EMPIRE_IDEA_QUEUE.md), [ideas/README.md](ideas/README.md) |
| **Backup: what exists, how to copy it, how much space** | [ESTATE_INVENTORY.md](ESTATE_INVENTORY.md), [BACKUP_RUNBOOK.md](BACKUP_RUNBOOK.md), [ODYSSEY.md](ODYSSEY.md) |
| **Portfolio demonstration hub** (Empire/Eve story for web; sync from ODYSSEY — not EMPIRE runtime) | [PORTFOLIO.md](PORTFOLIO.md), [PORTFOLIO_MAINTENANCE.md](PORTFOLIO_MAINTENANCE.md), [PORTFOLIO_FRAMER.md](PORTFOLIO_FRAMER.md), [data/framer-portfolio/](../data/framer-portfolio/), [scripts/export-framer-portfolio.ps1](../scripts/export-framer-portfolio.ps1) |
| **Consolidation phase (E: hub → cloud → disc → GitHub)** | [BACKUP_CONSOLIDATION.md](BACKUP_CONSOLIDATION.md), [config/hub-upload.json](../config/hub-upload.json), [scripts/hub-rclone-sync.ps1](../scripts/hub-rclone-sync.ps1) |
| OneDrive performance tuning (optional) | [ONEDRIVE.md](ONEDRIVE.md) |
| **Cursor / Cline session reset** (agent Memory Bank — not Eve Cognee; local untracked) | [../memory-bank/activeContext.md](../memory-bank/activeContext.md) (+ five sibling files under `memory-bank/`) |

If a fact appears in more than one of these, **AGENTS.md wins for commands**, this map wins
for "where is it", and the specialist doc wins for its own subject.

## 3. History — kept, not read

These are work logs. They have no code references; read one only when reconstructing why a
decision was made.

| Cluster | Size | What it is |
|---|---|---|
| `tools/archify/docs/` | 52 files, 0.7 MB | `research-visual-evolution-round-N.md` — per-round design logs |
| `docs/superpowers/` | 9 files, 0.1 MB | dated specs and plans (`2026-…`) |
| `docs/expansion_docs/` | 9 files, 0.2 MB | **RECLASSIFIED 2026-09-28 — not history.** Three of these are **contracts**: the Eve/Ollama expansion manifest (68.9 KB, *the source of the operating rules the repo now enforces*), the local-upgrade research (61.2 KB) and the no-account MCP catalog. Read when relevant; see ESTATE_INVENTORY §11.3–§11.4 |
| `docs/research/` | 2 files, 0.1 MB | earlier structure/strategy notes |

`eve-skills/*/docs/**` (40 files, <0.1 MB) is per-skill reference that ships with each skill —
keep it next to the skill.

## 4. Vendor reference — look up, never ingest

`docs/reference/` — **44 files, 10.2 MB** of third-party guides (Gumloop ×3, Dify ×4,
AnythingLLM, Cursor ×3, FlutterFlow, Ollama, Magic Patterns). Not EMPIRE documentation and
not fuel: do not feed these to Cognee. Search them when you need an upstream fact.

## 5. Generated — never read, never edit, never index

Already git-ignored (439 of the 754 `.md` files are tracked; the rest are these):

| Path | Why it exists |
|---|---|
| `agents/empire-task-agent/.eve/dev-runtime/snapshots/**` | dev-runtime snapshots, one full copy of agent skills each |
| `agents/empire-task-agent/.output/.eve/compile/**` | compiled workspace resources (skills copied from `agent/skills/*.md`) |
| `data/eve_memory/uploads/<hash>/**` | workbench upload staging |
| `backend/pocketbase/pb_public/dashboard/` | dashboard snapshot written by `refresh-dashboard.ps1` |

Rule of thumb: if the file exists because something ran, it belongs on this list — keep it out
of searches and out of the memory pipeline.

## 6. The vault outside the repo: `C:\Empire_Workbench`

Not documentation — this is the **data**: 14,651 files / 2.68 GB / 13,444 markdown, and the primary
root for `read_document`, so a *relative* path in a tool call resolves here (not in the repo).

| Folder | Files | Size | Role |
|---|---|---|---|
| `01_Memory_Bank` | 12,620 | 1.04 GB | ingest source (default) |
| `02_Skills_and_Prompts` | 715 | 1.06 GB | ingest source (default) |
| `03_Active_Tools` | 118 | 560 MB | tool material |
| `04_Thought_Experiments` | 1,174 | 8.2 MB | experiments |
| `00_Core_Profile`, `00_Resource_Queue`, `05_Work_Orders`, `stem_factory` | 21 | 7.9 MB | profile, queue, orders |

**State files at its root** (read them before trusting ingest numbers):

| File | Meaning |
|---|---|
| `harvest_summary.json` | where the vault came from (`G:\My Drive\_NLM PROCESSING`, `D:\Empire_Workbench\_github_staging\…`) |
| `ingest_progress.json` | last run: 612 batches, 11,644 ingested, 594 skipped, 0 pending |
| `ingest_skipped_files.txt` | append-only skip log — **1,683 lines for 870 unique paths**, so count unique paths, not lines |
| `_encoding_probe/` | scratch copies from the 2026-09-26 encoding fix; delete freely |

**How to read a skip line.** Reason is the field after the tab: `whitespace-only` / `NUL/binary` are
junk files carrying a `.md` extension (correctly refused, ~796 of them, and the source of the
"1.9 GB skipped" scare — that was file *size*, not readable text); `csv_not_supported_by_cognee` is a
Cognee limit (62); encoding-shaped skips are fixed by the UTF-8 → cp1252 → latin-1 ladder in
`pipeline/ingest_files.py` (`read_text_any`).

**Duplicates:** 1,387 identical groups / 2,282 redundant copies / 25.7 MB. Left in place on purpose —
ingest keys on content hash (`dataset:sha256`), so duplicates were already collapsed in memory, and
moving 2,282 files out of a personal vault buys 25.7 MB and risks reorganising material you filed by hand.

## 7. When you add a document

1. If it changes how to **run** things → edit `AGENTS.md`.
2. If it is a **contract/measurement** for one limb → `docs/` next to its peers and add a row above.
3. If it is a **dated log or plan** → the matching history cluster, no index entry.
4. If it came from **someone else** → `docs/reference/`.
5. Never a sixth place.
