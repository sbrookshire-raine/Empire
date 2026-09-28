# Ideas and evidence digest — what the legacy estate actually contains

Written 2026-09-27, during the estate survey. Purpose: capture what is extractable from the legacy material while
it is still in place, and record two findings that **correct earlier statements in
[`ESTATE_INVENTORY.md`](../ESTATE_INVENTORY.md)**. Everything here was read from the machine; nothing has been moved
or modified.

## A. Truthdrift's true origin — a recon on page-change documents

You described the sequence: a small recon program looking at **historical page-change documents first**, which
carried enough weight to justify going after the full repositories. That matches what is on disk: the revision-history
slice (see §C) plus a DriftBench harness that already exists in the repository — not sketched, *built*.

## B. DriftBench is a built system, not an idea

| Component | Size | Role |
|---|---|---|
| `pipeline/wiki_driftbench_seed.py` | 11.7 KB | **the generator** — writes calibration rows from "known archive patterns (redirects, vague descriptions, parametric distractors)" |
| `pipeline/wiki_glasses_eval.py` | 20.4 KB | evaluation of the retrieval "glasses" (the BGE rerank layer) |
| `frontend/wiki_drift_api.py` | 54.6 KB | the drift API/classifier — the largest single piece of wiki machinery |
| `scripts/run-wiki-calibrate.py` | 17.5 KB | the calibration runner |
| `scripts/e2e_truth_drift.py` | 5.9 KB | end-to-end drift check |
| `data/eval/wiki_driftbench_seed.jsonl` | 7.1 KB | the generated seed (hand_01…hand_04+) |
| `data/eval/acceptance/retrieval_rerank_*.yaml` | 485–800 B × many | dated quality trajectory, Sep 7 → Sep 26 |

**The case schema** (`CalibrateCase`, from the generator's source) is the reusable asset — it encodes the whole method:

```
id, source, tier, query, year, mode: lookup|compare|retrieval,
must_contain[], must_not_contain[], expect_title_any[], forbid_title[],
injection, live_eve, retrieval, tags[], notes
```

`must_not_contain` + `forbid_title` + a `parametric_distractor` tag is precisely how "answered from the archive" is
separated from "answered from training priors". **Case `hand_03` states the intent outright:** *"Must not hallucinate
Kate Bush single 'Wow' from parametric memory."*

**And there is a scaling path already noted in the source:** public HuggingFace datasets are merged via
`scripts/import-wiki-calibrate-samples.py`. So the corpus→benchmark bridge has a designed route, not just a
possibility.

**Provenance honesty:** the generator comment says these are "cases that failed before Phase A `wiki_read_lead` +
grounding guard" — i.e. the seed cases are *regression tests earned from real failures*, which is why they are worth
more than synthetic ones.

## C. Correction: the revision-history dump is a **partial slice**, not "every revision"

Earlier I described `D:\wiki_dumps\2026_meta_history` as containing every revision of every page. The *format* does
allow that, but **what is actually on disk is incomplete**:

| File | Size | State |
|---|---|---|
| `enwiki-20260401-pages-meta-history1.xml-p9479p10061.bz2.part` | **1,076,887,552 B (1.08 GB)** | **`.part` — interrupted download** |
| `enwiki-20260401-pages-meta-history1.xml-p2955p3418\…-p2955p3418.bz2.part` | **590,245,888 B (590 MB)** | **`.part` — interrupted download** |
| `enwiki-20260401-pages-meta-history1.xml-p2955p3418` | 1 B | a 1-byte placeholder, not content |

Total: **~1.67 GB across two page-ID ranges** (p2955–3418 and p9479–10061) of a dump that ships as many parts.

So the honest position is: **the recon proved the method on a narrow, truncated slice.** That is not a weakness in the
theory — a partial slice is exactly what a recon is for — but it means any plan built on meta-history must account
for *re-acquiring the full multi-part set*, and must not assume the current files can be decompressed end to end.
Verify with `bzip2 -t` before relying on either file.

This also explains the order you described: the page-range recon came first, and the *full* corpus work followed.

## D. The "full repos" intent has prior art on disk

The Raine-era pipeline already ran a **repo trial harness**:

```
H:\AI_ARCHIVE\v2_markdown_pipeline\data\raine\repo_trial_pipeline\
  ├─ batches\
  ├─ runs\20260418T054818Z_JulienPalard_Pipe\
  ├─ runs\20260418T055559Z_JulienPalard_Pipe__batch_minimal\
  ├─ runs\20260418T055600Z_JulienPalard_Pipe__batch_django\
  ├─ runs\20260418T055600Z_JulienPalard_Pipe__batch_scientific\
  ├─ runs\20260418T055600Z_JulienPalard_Pipe__batch_web\
  ├─ runs\20260418T162304Z_cvat-ai_cvat__batch_scientific\repo_clone\…
  └─ hermes_toolset_rollup.json  (7.7 KB)
```

Repositories were **cloned into `repo_clone/` and processed in typed batches — minimal, django, scientific, web** —
with timestamped runs. So "we may need unflattened versions" is not a new thought: April 2026 already had a working
trial harness, and it is worth reading `hermes_toolset_rollup.json` and one batch's manifest before designing the
replacement. The same pipeline also carries `stack_exchange_to_md.py` (2026-05-24) — another intended corpus source.

## E. Project names recovered (the idea register, expanded)

Beyond Zet/Zed and Raine, the vault path structure exposes more:

```
RESYNC_2026\2. PAST LIVES\SBX\The time before Seth\3_Computer room\Projects\
    ├─ PREVaiL\ABACUS - prompt changes.md
    └─ Z_Future project hub\rAInE - Raine AI Expression (or exchange).md
```

| Name | First seen | Status |
|---|---|---|
| **Abacus** | 2025-01-18 | first named system; prompted and iterated |
| **rAInE / Raine** | 2025-01-19 | "AI Expression (or exchange)" — the concept behind the name |
| **Zet / Zettelkasten (Zed)** | 2025-03-22 | capture → summarize → zettel pipeline; designed, never shipped |
| **PREVaiL** | *(vault folder)* | previously unrecorded here — needs reading |
| **Z_Future project hub** | *(vault folder)* | the forward-looking idea hub |
| **IRENE** | 2024-11 files, 2025-11 notes | two lives: scripts then 2.0 |
| **AI Factory** | 2025-12-04 | agent + n8n + Qdrant stack |
| **DAZE** | Desktop 2026-05 | shipped into EMPIRE as `daze_mcp.py` |

## F. What to read next, highest yield first

1. `docs/research/EMPIRE_WIKI_ARCHITECTURE_STRATEGY.md` and `docs/research/EMPIRE_WIKI_STORAGE_RESEARCH_REPORT.md` — already **in the repo** (copies also sit on the Desktop); these are the design record for the corpus.
2. `docs/expansion_docs/1. EMPIRE_RESEARCH_SNAPSHOT.md` — a research snapshot already committed.
3. **The five design notes** (§8.3 of the inventory) — Raine blueprint, roadblocks, non-n8n MVP, Zet God script, ZED2RSS.
4. `learning_hub*.log` in `E:\AI_PROJECTS` — the **2024-11 origin**, and the October trail.
5. `hermes_toolset_rollup.json` + one `repo_trial_pipeline` batch manifest — how repos were previously chunked.
6. `PREVaiL` and `Z_Future project hub` notes — the two project names not yet read at all.

## G. Corrections to earlier statements

1. **Meta-history** — described as "every revision of every page". Reality: **two partial `.part` slices, ~1.67 GB, truncated.** The method is sound; the data on disk is a recon sample.
2. **Timeline start** — the vault (2025-01-12) is not the project start; `learning_hub_20241114_172407.log` puts files at **2024-11-14**, with your recollection of **October 2024** looking right and still to be confirmed from the logs.
3. **`docs/research/` already holds** the Desktop research reports — so the "Desktop research docs should be ingested" action is partly already done; the check is whether the repo copies are current.

## H. The documentation has three eras — all three are located

You said it went OneNote → Obsidian → Heptabase. All three survive on disk, and the **earliest one is the key to the
October–December 2024 gap**:

| Era | Where it lives | Scale | Dates |
|---|---|---|---|
| **OneNote** | `…\RESYNC_2026\2. PAST LIVES\ONENOTE BACKUP PREOBSIDIAN.md` (duplicate in `…\Desktop\SBX_Vault\2. PAST LIVES\`) + the live notebook `…\Documents\OneNote Notebooks\Seth @ FVCC\` | **383,846 B / 8,339 lines** | **Dec 2024 → 2025** |
| **Obsidian** | `…\Documents\RESYNC_2026` (497 notes, live) + `…\Desktop\SBX_Vault` (474 notes) | ~971 notes | 2025-01-12 → 2026-06-29 |
| **Heptabase** | `H:\Heptabase backup 4_7_26\Heptabase-Data-Backup-2026-04-08T03-50-14-422Z\` | `All-Data.json` **25.3 MB** + `Card Library`, `Highlight`, `Journal`, `Text Element`, `Whiteboard` | export 2026-04-08 |

**Obsidian and Heptabase overlapped** (Jan 2025 → Apr 2026), so they are two *views* of the same period rather than
sequential eras — the Heptabase cards hold whiteboard/card thinking, the vault holds dated notes.

### H.1 What the OneNote archive actually contains

It is a `Quick Notes` dump with timestamps preserved (`Monday, December 2, 2024`, `Wednesday, December 25, 2024`,
`Friday, January 3, 2025`), and it holds **three distinct threads** — not project logs:

1. **Prompt craft.** A complete Flask tool design dated **2024-12-25**: `prompt_rewriter_tool/` with `app.py`,
   `utils/rewriter.py`, templates, requirements — whose `rewrite_prompt()` implements an **8-point prompt protocol**
   (identify subject/objective · add context · ensure specificity · clear and concise language · open-ended questions
   · avoid leading questions · provide instructions · appropriate length). **This is the earliest design artifact
   found anywhere in the estate**, three weeks after the 2024-11 logs, and it is prior art for prompt quality that
   EMPIRE now handles implicitly through `eve_instructions` and routing.
2. **Music research.** A full curated analysis — *"Grooves Through the Decades"*, ~50 songs with per-track
   significance notes on drum grooves across genres. This is the thread that connects to the **music-theory ZIMs**
   (openmusictheory, mutopiaproject, tonedear) and to the `drum-train-visualizer` and `Area_56_Bandapp` repos.
3. **Education + AI.** Curriculum-reform thinking ("integrating AI, modernizing curricula, supporting teachers,
   ensuring equity") — matching the `academic_hub` repo and the `Seth @ FVCC` notebook.

So the OneNote era is where the **domain interests** live, while the Obsidian/Heptabase eras hold the **system
ideas**. Both matter, and they answer different questions.

### H.2 Heptabase is convertible, not locked

The export includes `README - How to export all data to markdown files.md`, and the `Card Library` is already `.md`
per card — hundreds of them, including clearly *conceptual* cards: *"Building It Right vs. Building The Right
Thing"*, *"Chasing High Scores Creates Fragile Learners"*, *"Bugs Are Actually Features"*, *"Trap sentinel
instructions for dify coin tracker with rules for buying"*, *"producer ai use gemini feedback"*, `TOOLS.md`.
**That means the third era is ingestible** — strip to markdown, curate, and it can flow into the same Cognee
`primitives`/reference path as everything else. It is the largest unread body of *recorded thinking* in the estate
after the OneNote dump.

### H.3 The staged repos are bigger than first reported

`D:\Empire_Workbench\_github_staging\sbx2020\` alone holds **29+ repositories**, and they split into three groups:

- **Knowledge/notes-adjacent** (the "repo for it" candidates): `notie`, `Aporia`, `PA_Aporia`, `lcc-mindmap-standalone`, `cursor_HOL`, `code2prompt`, `gpt-crawler`, `crawl4ai`, `mcpadapt`, `ottomator-agents`
- **Personal projects**: `Habit_Magnet`, `exam_manager`, `drum-train-visualizer`, `Area_56_Bandapp`, `Gelfing`, `Lillyan_reimagined`, `lmms-sbx`, `Hatch_LCC_tasker`, `flow-scaffold`, `goal_breakdown`
- **Reference/forks**: `kokoro-fastapi`, `google`, `google_homepage`, `git_test`, `cursor_playground`, `cursor-practice-01`

Note `cursor_HOL` — it matches the abandoned docker volume **`cursor_hol_weaviate_data`** (the `media-weaviate`
container), which links one of the §6 "unidentified" items to a known project.

### H.4 Priority reads, updated

1. **`ONENOTE BACKUP PREOBSIDIAN.md`** — the 2024 origin, the 8-point prompt protocol, and the Oct–Dec 2024 trail.
   Highest value per minute of reading anywhere in this estate.
2. **Heptabase `Card Library` + `All-Data.json`** — the recorded-thinking layer; convert to markdown and curate.
3. The five design notes, the `learning_hub` logs, `hermes_toolset_rollup.json` (previous repo chunking), and the
   still-unread `PREVaiL` / `Z_Future project hub` notes.


