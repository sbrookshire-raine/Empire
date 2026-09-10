# EMPIRE Research Closure

**Date:** 2026-09-10  
**Status:** Discovery phase **closed**. Build phase **open**.

This document is the capstone for five research packs (Product Hunt, CLI, missed OSS, Hugging Face specialty, local capability gap analysis). Upload it last when briefing a fresh research AI — it overrides “go find more tools.”

**North star architecture (final):**

> One hot generalist (**Qwen 2.5 14B**, ~10 GB with 8k ctx) + a fleet of tiny **CPU specialists** that never touch VRAM.

---

## What research answered

| Question | Answer |
|----------|--------|
| Do we need a new Wikipedia index? | **No.** Weaviate + `D:\wiki_md` retrieve; grounding was the gap. |
| Do we need Kiwix / AnythingLLM / second vector DB? | **No.** Steal contracts only (kiwix 3-rung ladder → server-side). |
| Do we need Product Hunt / broad GitHub trawls? | **No.** ~2% hit rate; **monthly 30 min** on r/LocalLLaMA + Ollama library only. |
| Do we need a second chat model? | **No** on 16 GB. Optional **qwen2.5-coder:7b** for offline coding fallback. |
| What actually failed? | Parametric override (“Wow”), fat injection, Truth Drift hijack — **not retrieval**. |
| What fixes it? | `wiki_read_lead` + allowlist guard (+ GLiNER later) + DriftBench calibrate. |
| What has an expiry date? | **Offline mirror** — models/wheels/ZIM must be captured while online. |

---

## Capability matrix (gap doc → as-built)

| Capability | Gap doc | EMPIRE today | Queue | Next build step |
|------------|---------|--------------|-------|-----------------|
| Chat / synthesis | Qwen 2.5 14B | ✅ Fast mode | — | Solidify, not swap |
| Wikipedia retrieval | Weaviate + md | ✅ | T-01, T-21 | Architect smoke |
| Wiki grounding | lead + guard | ✅ Phase A shipped | T-21–T-23 | GLiNER upgrade F-36 |
| Memory | Cognee | ✅ | — | — |
| Persistence | PocketBase | ✅ | — | — |
| UI | HTMX + Alpine | ✅ | — | — |
| Embeddings | audit | ✅ **nomic-embed-text** | T-24 | Run `audit-embedding-stack.ps1` |
| Rerank | FlashRank CPU | ⏸ eval only | F-32 | Only if calibrate fails ordering |
| Grounding verify | MiniCheck CPU | ⏸ parked | F-34 | After GLiNER metrics |
| Entity extraction | GLiNER CPU | 🔧 scaffold | F-36 | `pip install gliner` + enable |
| Speech in | faster-whisper | ✅ via Speaches | T-08 | Architect smoke |
| Speech out | Piper / Speaches | ✅ Speaches CPU | T-08 | Piper optional compare F-37 |
| Vision | Qwen VL swap | ✅ qwen3-vl:8b | T-09 | GPU lease + swap mode |
| Document ingest | Docling | ✅ MCP forged | T-06 | Architect smoke |
| Constrained output | Ollama `format` | 🔧 not wired | F-38 | JSON schema for title pick |
| Personal file search | FTS5 + Weaviate | ⏸ | I-06 | After Docling personal corpus |
| **Offline mirror** | **critical gap** | 🔧 script | **F-35, T-25** | **`build-offline-mirror.ps1`** |
| Image gen | deprioritize | ❌ rejected | — | — |
| Product Hunt discovery | wind down | ❌ closed | I-05 | No new PH scraping |

Legend: ✅ done · 🔧 in progress / scaffold · ⏸ measured-failure only · ❌ rejected

---

## Build sequence (not discovery)

| When | Work | Why |
|------|------|-----|
| **Now (online)** | Offline mirror + MANIFEST | Expires; cannot rebuild offline later |
| **Week 1** | Architect smokes T-01–T-23, T-08 | Prove forged limbs in daily use |
| **Week 1–2** | GLiNER grounding gate (F-36) | Generalizes beyond Kate Bush regex |
| **Week 2** | Ollama JSON-schema title selection (F-38) | Deterministic pick before prose |
| **Week 2–3** | Docling → personal Weaviate corpus | Your docs, same lead contract |
| **On failure only** | FlashRank (F-32), MiniCheck eval (F-34), HF import (F-33) | DriftBench must prove need |

---

## Research sources — final cadence

**Closed (do not re-open unless DriftBench proves a hole):**

- Product Hunt bulk lists (129 items → 0 adoptable products)
- Generic “local RAG” GitHub trawls
- Live Wikipedia MCP servers
- Second vector database proposals
- LangChain / LangGraph orchestration rewrites

**Allowed (≤30 min / month):**

- r/LocalLLaMA — 16 GB local patterns
- [Ollama library](https://ollama.com/library) — filter by size
- [Kiwix library](https://library.kiwix.org/) — new ZIM archives for offline mirror
- llama.cpp release notes — structured output / grammar
- **EMPIRE DriftBench failures** — primary signal (`data/eval/wiki_calibrate.jsonl`)

---

## Offline mirror checklist

Run while internet is available:

```powershell
.\scripts\build-offline-mirror.ps1              # inventory + optional pulls
.\scripts\build-offline-mirror.ps1 -PullOllama  # ollama pull manifest models
.\scripts\build-offline-mirror.ps1 -Wheelhouse  # pip wheels to D:\wheels
.\scripts\audit-embedding-stack.ps1             # confirm nomic + Weaviate
```

Manifest lands at `D:\empire\MANIFEST.md` (override: `-MirrorRoot`).

Minimum Ollama pulls (from gap analysis + current stack):

- `qwen2.5:14b-instruct` — Eve Fast
- `nomic-embed-text` — Weaviate + Cognee embed
- `qwen2.5-coder:7b` — offline coding fallback
- `qwen2.5vl:7b` or `qwen3-vl:8b` — vision swap (one family)

---

## Calibration — how we know we’re done researching

| Harness | Command | Pass criteria |
|---------|---------|---------------|
| Wiki smoke | `scripts/test-wiki-chat-smoke.py` | 4/4 injection + live |
| Wiki calibrate | `scripts/run-wiki-calibrate.py --tier smoke` | 8/8 smoke tier |
| Playwright UI | `scripts/test-wiki-eve-playwright.py` | Stranger Things Q in browser |
| Full calibrate | `run-wiki-calibrate.py` (no tier filter) | Track routing_gap count ↓ over time |

Future architecture changes require a **measured DriftBench regression**, not a new README.

---

## Related docs

| Doc | Role |
|-----|------|
| [EMPIRE_IDEA_QUEUE.md](EMPIRE_IDEA_QUEUE.md) | Living backlog + smoke IDs |
| [EMPIRE_RESEARCH_SNAPSHOT.md](EMPIRE_RESEARCH_SNAPSHOT.md) | As-built system truth |
| [WIKI_SCOUT.md](WIKI_SCOUT.md) | Wiki Local ops |
| [VOICE_PRESENCE.md](VOICE_PRESENCE.md) | Speaches STT/TTS |
| [OPERATIONAL_HANDOFF.md](OPERATIONAL_HANDOFF.md) | Ollama operational phase |

*When this file and the idea queue disagree, update the queue — then stop searching.*
