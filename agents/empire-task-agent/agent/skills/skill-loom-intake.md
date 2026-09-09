# Skill: Loom Intake (Knowledge Shell)

Load when **Loom Intake** is enabled in the Workbench Toolbelt.

## Purpose

Intake membrane for THE_KEEPER — turn raw PKM dumps (NotebookLM/Obsidian CSV exports) into gated rows in `primitive_ledger.csv` without flooding Domain Agents.

## Tools

| Tool | When |
|------|------|
| `loom_status` | Check ledger counts, paths, seeker prompt location |
| `loom_process_shell_csv` | Run full Shell pipeline on a 12-column CSV |

## Protocol (do not skip)

1. **Single articulated problem** → skip Shell; use primitive names + synthesis directly (no CSV).
2. **Raw dump / CSV** → run `loom_process_shell_csv` **before** any domain deep-dive.
3. CSV must have 12 columns: `packet_id, source_tool, capture_timestamp, raw_excerpt, condensed_claim, candidate_primitive_s, candidate_domain_agent, confidence_score, link_back_id, recurrence_count, mechanism, sibling`
4. Seeker prompt for extraction: `04_Thought_Experiments/loom/intake/seeker_extraction_prompt_v5.md`
5. Max **7 packets promoted per cycle** — overflow stays in buffer (by design).
6. **Never delete ledger rows** (Mechanical Ratchet).
7. **Never auto-Cognee** ledger — offer curated ingest only if Architect asks.

## Keeper persona boundary

Eve is **not** The Keeper at runtime. Use Loom tools and plain synthesis — do not boot with ceremonial Keeper greeting or inject Gumloop AGENT.md persona.

## Paths

- Loom root: `C:/Empire_Workbench/04_Thought_Experiments/loom/`
- Ledger: `loom/workspace_data/primitive_ledger.csv`
- Domain agents (reference): `loom/subagents/*/AGENT.md` — deep work via Cursor Task, not Eve chat by default

## Gumloop fallback

Parallel Loom weaving with live A1–A6 Gumloop gummies remains on **Gumloop Cloud** (Toolbelt off) when local intake is insufficient.
