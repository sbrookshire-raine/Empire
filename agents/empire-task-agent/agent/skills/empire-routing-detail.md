# Empire routing detail (full intent -> tool map)

Load this when the compact routing index in your system prompt is not enough —
it carries the full annotated map of user intent to local tool, with per-row notes
on what to call, what to load, and what never to do.

## Routing (automatic — never ask, never announce)

| User asks about… | Do this silently in the same turn |
|------------------|-----------------------------------|
| Interests, themes, research, notes, "memory graph", "what you know about me", "projects in memory", workbench memory | `cognee_recall` with `dataset=eve_memory` or `eve_core` — **never** `create_task` |
| Something worth keeping after a successful turn (extract crumb, lesson, marker) | **`propose_remember`** into `eve_staging` — then **ask** the Architect to keep or drop. **`list_staging`** to show open proposals. **`confirm_remember`** / **`drop_staging`** only when they explicitly say keep/drop that id. Never auto-confirm. Never bulk Wikipedia |
| What tools/skills you have, headroom, GPU busy, “can you turn X on?”, what’s free on the machine | Load **skill-resource-pulse**; call **`resource_pulse`** first (silently). Answer from its `summary` / inventory — **not** Wikipedia. Admit light scouts with **`admit_for_goal`** when needed. If `need_architect` / GPU heavy → ask once. Prefer managing the space yourself |
| Companion / CURRENT status (or `[[EMPIRE_NOW]]`) | Load **skill-companion**; trust injected **ARCHITECT_NOW** — do not quiz or ask them to re-remind; `architect_now_update` only if they explicitly ask to save a change |
| Curated primitives, Pattern Weaver, Universal Primitives | `cognee_recall` with `dataset=primitives_test` |
| Tasks, todos, task list | `list_tasks` / `search_tasks` / `create_task` / `update_task` |
| Run Triage, Resource Queue, evaluate intake, USEFUL NOW / COOL IDEA / JUNK | Load **skill-triage-officer**; `workbench_list_dir` with relative `00_Resource_Queue`; for USEFUL NOW forge needs call **`draft_work_order`** |
| Workbench health, disk space, Active Tools count, “is the workbench online?” | Load **skill-workbench-health**; call **`check_workbench_health`** |
| Local Wikipedia facts / multi-hop wiki work (who is X, cast, briefs, sections) | Prefer server-injected `[[EMPIRE_WIKI_LOOKUP]]` or `[[EMPIRE_WIKI_EXTRACT]]` (Title DNS + structured extract). Use **`wiki_extract`** for dates/tables/lists/numbers. Use **`wiki_scratch_upsert`/`wiki_scratch_read`** for multi-hop. **`wiki_read_section`** when a named H2 is needed and no LOOKUP lock. **Do not** call `wiki_scout_search` when LOOKUP/EXTRACT is present. **Do not** invent when EXTRACT state is empty. **Do not** mention Weaviate/Docker/8091. Misses go to Error Book — do not invent |
| Remember / save structured Wikipedia extract | **`wiki_remember`** (preferred) or **`remember_wiki_lead`** — only when asked; rejects non-ok extracts; never bulk corpus |
| Multi-source research (wiki + GitHub + Product Hunt), MCP/CLI repo discovery | Load **skill-research-orchestrator**; call **`research_orchestrate`** when Research Partner ON; else **`capability_status`** and tell user to enable Research Partner (More tab) or Toolbelt limbs |
| GitHub repo search / README for forge triage | **`github_scout_search`** / **`github_scout_readme`** — always callable; auto-admits GitHub Scout when headroom OK. **Never** say you lack internet/GitHub. Never clone or install |
| Promote a wiki_cache `.md` into memory | **`promote_wiki_cache`** only when the Architect explicitly asks — path under wiki_cache |
| Remember / save / keep this Wikipedia lookup | **`remember_wiki_lead`** with the title just answered — lead only, dataset `eve_memory`. Never auto-remember. Never ingest the full article or corpus |
| Public web page → Thought Experiments cache | Load **skill-web-scout**; **`web_scout`** with a **full URL** (requires **Web Scout**) — fetch only, not search; never invent page text; if blocked say so and stop — **never** claim you will browse manually; never auto-memory; **never** use as silent fallback for failed Wiki Local |
| Docker Hub images / container discovery / which empire-* containers are up | Load **skill-container-scout**; **`container_scout_search`** / **`container_scout_detail`** / **`container_scout_docker_status`** (requires **Container Scout** Toolbelt) — never auto-pull, never auto-memory, not Kubernetes |
| Structured document metadata (title/author/tags/summary JSON) | Load **skill-structured-extract**; **`structured_extract`** (requires **Structured Extract** Toolbelt; llama.cpp worker on :8092) — scratch only, never auto-memory |
| Rerank retrieval candidates / retrieval A/B | Load **skill-retrieval-rerank**; **`retrieval_rerank`** (requires **Retrieval Rerank**) — eval only; nomic production embeds unchanged |
| Local Workbench/PocketBase page inspect | Load **skill-browser-local**; **`browser_local_fetch`** (requires **Browser Local**) — allowlist only; no public web; no form submit |
| Screenshot UI regions (observe only) | **`vision_ui_observe`** (requires **Vision Local**) — no actuators |
| Thought experiment / YouTube idea capture | **`thought_experiment_capture`** (requires **Thought Experiments** Toolbelt) |
| PDF/Office → markdown staging | **`docling_convert`** then remember/upload when asked |
| Day schedule, free time, overbooking, exercise/meditation slots, DAZE, planned vs actual | Prefer directing them to **DAZE** (`daze.html` / chat dock). If they want Eve to act on the schedule: load **skill-daze-time**; **`daze_list_day`** / **`daze_free_windows`** / **`daze_compare_phases`** / **`daze_upsert_block`** (requires **Time Reclaim** Product limb) — PocketBase day_blocks, not Tasks |
| Stems, stem inbox, Demucs, practice tracks, Stem Factory / Shard of the Division | Prefer: enable **Stem Factory** product limb + drop files in `C:/Empire_Workbench/stem_factory/input`. Then load **skill-stem-factory**; **`stem_list_inbox`** then **`stem_run`**. Do not treat stems as chat personality |
| Truth Drift / compare Wikipedia across 2017–2026 | Load **skill-wiki-scout**; **`wiki_scout_compare_years`** only when they explicitly ask — product home is Wiki Ops (`wiki.html`). Not for simple artist/album questions |
| Voice / mic / speak | **`voice_transcribe`** / **`voice_speak`** (requires **Voice Presence**; speech API on :8000) |
| Screenshot / image describe | **`vision_describe`** (requires **Vision Local**; `qwen3-vl:8b`; GPU lease) |
| Who has the GPU | **`gpu_lease_status`** |
| Start/stop local services for a task, service health, or GPU tenant serialization | Load **skill-switchboard**; **`switchboard_status`** then **`switchboard_plan`** then **`switchboard_ensure`**/`switchboard_release`/`switchboard_tenant` (dry-run first; only mutate on headroom green; never start/stop Ollama or Eve) |
| Find text/files locally, keyword search across notes and docs | **`workspace_search`** — read-only; no network |
| Pull answers from a local CSV/JSON/Parquet/SQLite file | **`query_data`** — read-only SQL (SELECT only); pass `data_file` + query against `data` |
| Read a local PDF/DOCX/XLSX/HTML/markdown file | **`read_document`** — MarkItDown → Docling fallback; read-only |
| Turn a table/list into an actual spreadsheet file | **`create_spreadsheet`** — writes `.xlsx` to `eve-output`; formula injection blocked |
| Write or change code (build with me) | Load **skill-author-code**; **`author_code`** (disposable worktree) then **`python_verify`**; show the diff, never merge |
| Verify Python changes are safe | **`python_verify`** — syntax + lint + tests in the worktree |
| Any file inside `03_Active_Tools/` — flattened codebases, `*_flattened.txt`, harvested tool scripts | **`read_active_tool`** (requires Tool Forge in Toolbelt) — **mandatory**, see rule below |
| Scrape official docs site → Markdown guide (llms.txt / sitemap) | Load **skill-tool-forge**; **`docs_guide_scrape`** with full docs root URL (requires **Tool Forge**) — writes `harvest_cache/*_Complete_Guide.md`; never auto-Cognee |
| Skill zip/dump 3-Bin triage for Build1 | **`skill_triage_manifest`** (requires **Tool Forge**) — heuristic triage of `.cursor/skills` ± uploaded paths; writes `harvest_cache/SKILL_TRIAGE_MANIFEST.md` |
| Parallel multi-site doc harvest or Gumloop artifact CDN | **Gumloop Cloud** (Toolbelt, default off) — use when local scrape is insufficient; do not pretend Eve ran Gumloop |
| Shell Packet CSV / raw PKM dump → primitive ledger | Load **skill-loom-intake**; **`loom_process_shell_csv`** then **`loom_status`** (requires **Loom Intake**) — max 7 promoted/cycle; never auto-Cognee |
| Primitive ledger / gap report / Seeker prompt paths | **`loom_status`** (requires **Loom Intake**) — ledger at `04_Thought_Experiments/loom/workspace_data/` |
| Workbench folder map, Resource Queue, Memory Bank, Skills and Prompts, Thought Experiments, Work Orders listing, or listing any workbench directory | `workbench_list_dir` / `workbench_read_file` with **relative** paths only (e.g. `01_Memory_Bank`) — never `/home/vercel-sandbox` or absolute `C:\` |
