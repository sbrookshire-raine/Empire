# EMPIRE Refactor Plan (2026-09-24)

**One breath:** EMPIRE works, but it works *for the wrong reason* in places — the model has been
acting as the integration layer between parts that never agreed on a contract. This plan makes the
answer path explicit and testable, triages the tool surface down to a spine, and sets the gates that
let "throw a better brain at it" be safe instead of hopeful.

**How this relates to the other documents**

| Document | Role |
|----------|------|
| [`EMPIRE_CLARITY.md`](EMPIRE_CLARITY.md) | The bounding box: Eve Core / LEGO shelf / Session reach, staging memory, Mechanic-before-Architect |
| [`EMPIRE_IDEA_QUEUE.md`](EMPIRE_IDEA_QUEUE.md) | Where the phase items live (`R-*` rows) and how they get promoted to Work Orders |
| [`manifest/README.md`](manifest/README.md) | Architecture, APIs, tool inventory (the "what exists" reference) |
| **This document** | The "what is structurally wrong and in what order we fix it" plan. **Not** a rewrite plan |

---

## 1. Diagnosis (measured 2026-09-23/24)

### 1.1 The numbers

| Area | Files | Lines |
|------|-------|-------|
| `pipeline/` | 78 | 20,764 |
| `frontend/` | 26 | 12,478 (`eve-workbench.js` 2,874 · `serve.py` 1,982 · `wiki_drift_api.py` 1,237) |
| `mcp/` | 24 | 1,452 (84 `@mcp.tool` definitions — thin wrappers over `pipeline/`) |
| `scripts/` | 89 | 8,785 |
| `tests/` | 66 | 7,700 |
| `docs/` | 113 | **145,490** |

| Surfaces | Count |
|----------|-------|
| Agent tool files | **86** — 57 gated by Toolbelt, **29 always registered** |
| Toolbelt categories | 25 (`DEFAULT_ACTIVE = voice_presence, wiki_local`) |
| MCP hook servers | 7 (wiki-scout, daze, loom-intake, stem-factory, tool-forge, work-orders, workbench) |
| Skills (`.md`) | 33 |

| Always-on prompt component | Source | ~Tokens |
|----------------------------|--------|---------|
| `eve_instructions.md` + `empire-routing.md` | `agent/instructions.ts` (`loadSystemPrompt`) | ~5,800 (measured; raw text ~3.9k by chars ÷ 3.8 — rest is template overhead) |
| Tool schemas (enabled set, ~32 tools) | AGENTS.md measurement | ~5,300 |
| **Floor before the user speaks** | measured | **~11,100 of 16,384** |
| Loaded *on demand*, not always | `agent/skills/*.md` (33 files) | `empire-routing-detail.md` ~3.3k · `skill-wiki-scout.md` ~1.5k |

That last row is both the good news and the warning: the floor holds at ~11k **only because**
selectable content (skills, category docs) is not always resident. It leaves ~5k of window for the
conversation plus tool results — which is exactly why a 7-search loop or a long evidence card blows
the budget, and why the 2026-09-23 fixes worked (refusal, `available_sections`, capped generation).

Two ratios frame everything else:

- **Docs are ~4× the runtime code.** The design conversation outgrew the construction.
- **~170 tool surfaces** (86 agent + 84 MCP) are competing for ~5k of remaining conversation budget.

### 1.2 The four lessons

**L1 — The model is being used as the integration layer.** Every fix in the 2026-09-23 session
replaced "hope the model behaves" with a deterministic contract: repeat-search refusal at strike 3,
tool-call-as-text stripping, question-form normalization, baked generation limits, stream/speech
sanitizers. The tell is simple: *when you find yourself writing a rule to nudge a model, you have
found a missing contract in the system* — not a model deficiency.

**L2 — A bigger brain buys masking, not correctness.** The Fast A/B is a clean experiment: the 7B was
**3× faster** (25.2 s vs 76.9 s over three questions) but answered *"How do magnets work?"* from
**"The Magnets"** — an a cappella group — in 4.9 s with one search, because title resolution is
exact-match with no notion of ambiguity (E-13). The 14B got it right *by searching more*. Scale did
not fix the semantics; it paid to route around them.

**L3 — Tool count is a tax on every turn, not a feature list.** 29 tools are always registered, 57 are
gated by 25 categories, and the enabled schemas alone are ~5.3k tokens against a measured floor of
**~11.1k of a 16,384 window** — leaving ~5k for the conversation and tool results. Prompt pressure is
what produced the truncation, the loops and the latency this session chased. Every tool added taxes
*every* existing tool's reliability.

**L4 — Docs written around code become wish lists.** Three contradictions surfaced in one session:
`SHARED_NUM_CTX` "must match" (Python 8192 vs TS/baked 16384), a progress report asserting no native
`tool_calls` (verified working), and UI fixes invisible because nothing cache-busted
`eve-workbench.js`. Prose and implementation evolved separately; the prose lost.

### 1.3 The structural statement

EMPIRE has been a **research sandbox dressed as a product**. A sandbox may hold 170 tools and four
experiments at once; a product needs ~10 surfaces and one spine. Both are legitimate — the failure
mode is not choosing **per subsystem**. That choice is what makes the rest of this plan finite.

---

## 2. The spine: one contract for the answer path

Everything ambitious converges on one path. Today it is implicit and distributed across `serve.py`,
`eve_proxy.py`, the agent runtime, `wiki_title_dns`, `wiki_scout`, `wiki_read_lead`,
`wiki_interpreter` and the instruction files. The refactor is not to rewrite it — it is to *name it*
and give every stage an invariant plus a way to prove it.

```
intent ──▶ resolution ──▶ evidence ──▶ answer
(what is asked)   (which page)   (grounded cards)   (text + speech)
```

| Stage | Invariant | Verified today by | Gap |
|-------|-----------|-------------------|-----|
| **Intent** | A question needing the wiki says so; a how-to about the user's own task does not | `tests/pipeline/test_wiki_interpreter.py` (pronoun guard) | No routing battery asserting tool choice per intent (E-03) |
| **Resolution** | Deterministic, fast, and **ambiguous is a legal outcome** with candidates | `tests/pipeline/test_wiki_title_dns.py`; 0.03–0.62 s exact hits | `magnets` → "The Magnets" with `usable: true` and no signal (**E-13**) |
| **Evidence** | A card set with a termination rule; refusal is a valid result | `available_sections`, `HARD_STOP_REPEAT_HINT`, `tests/pipeline/test_wiki_scout.py` | No explicit "enough evidence" contract the model can check |
| **Answer** | Text satisfies the sanitizer contract and cites the evidence | `scripts/test-eve-browser-playwright.py`, `tests/frontend/test_eve_proxy.py` | Sanitizers are the *floor*; nothing asserts the answer is grounded |

**Rules that follow, and hold for every future change:**

1. **The model is a guest, never the glue.** Any behaviour we care about gets a deterministic owner:
   the tool refuses, the resolver flags ambiguity, the proxy strips scaffolding. Prompt rules are for
   *tone*, not for correctness.
2. **Every stage has a probe script** (`scripts/ab-fast-toolcalling.py`,
   `scripts/trace-eve-browser.py`, `scripts/test-eve-browser-playwright.py`). A stage without a probe
   is a stage nobody can refactor safely.
3. **Failures are loud.** `EMPTY_AFTER_CLEAN_REPLY` replaced an empty bubble rather than hiding a
   broken turn. Extend that principle: a stage that cannot satisfy its contract says so.

---

## 3. Tool surface triage

Target shape, expressed in the buckets already in [`EMPIRE_CLARITY.md`](EMPIRE_CLARITY.md) — no new
taxonomy:

| Bucket | Budget | Today | Target |
|--------|--------|-------|--------|
| **Always (Eve Core)** | ≤ 15 tools | 29 always-registered | Tasks, memory, wiki lookup, voice, resource pulse, workbench health — nothing else |
| **Session (intent groups)** | ≤ 3 groups active | 25 categories, free multi-select | Group by intent (`research`, `author`, `ops`, `media`); enabling a group enables its tools |
| **LEGO (products)** | opened by page/intent | DAZE, Stem Factory, Truth Drift | unchanged — this part of CLARITY already works |
| **Archive** | 0 prompt cost | — | Tools nobody called in 90 days leave the registry (files stay on disk) |

**The ceiling becomes a test.** A unit test asserts the measured prompt floor (always-on instructions
+ enabled schemas) stays under a fixed budget, so growth fails the build instead of becoming a mystery
slowdown. The measurement already exists — `scripts/ab-fast-toolcalling.py` reports `prompt_tokens` on
a calibrated prompt; reuse it rather than inventing a second tool.

**Exit criteria:** always-on ≤ 15; schemas ≤ ~3k tokens; floor ≤ ~9k of 16,384; a category is
enabled/disabled in one place (`toolbelt.ts`) and tests prove a disabled group's tools are not
registered.

---

## 4. Model contract (make "a better brain" safe)

Owned models stay (`empire-fast:14b`, `empire-fast:7b`; `config/ollama/Modelfile.*`, built by
`scripts/build-empire-ollama-models.ps1`). What changes is that **promotion is a test, not a
judgement call**:

| Gate | Command | Must show |
|------|---------|-----------|
| Tool calling through the compat proxy | `scripts/ab-fast-toolcalling.py` | native `tool_calls` using the real tool names |
| Context window | same script | the ~10k-token prompt ingested uncut (`prompt_tokens ≈ 10,022`) |
| End-to-end behaviour | `scripts/test-eve-browser-playwright.py` | one bubble per question, no scratch in bubble *or* speech |
| Grounding | browser A/B (section 2, evidence stage) | the answer comes from the resolved page, not an adjacent entity |

A new model that fails any gate is not promoted — however good it feels in chat. That is what turns
L2 from a warning into a procedure.

---

## 5. Docs policy

- **One page per subsystem**, stating *what it guarantees* and *the command that verifies it*, with
  numbers where numbers exist. `docs/WIKI_SCOUT.md` (post-2026-09-23 sections) is the model: question
  shapes, repeat refusal, known limitation — each naming its test file.
- **Narrative / design / vision prose** moves to a dated archive or the idea queue. It is allowed to
  be wrong; it is not allowed to sit next to code pretending to describe it.
- **Rule of thumb:** if a doc line cannot be checked in under a minute, it belongs in the queue as an
  item with a status, not in a subsystem page as a claim.

---

## 6. Non-goals (explicit)

- ❌ No big-bang rewrite, no "v2", no new abstraction layer over the existing one.
- ❌ No mega-FastMCP rewrite (already a hard reject in CLARITY) — the 84 thin MCP wrappers are fine.
- ❌ No paid cloud LLM in app code; no silent full-wiki ingest; no regex middleware for model *behaviour*.
- ❌ No deleting working capability to hit a tool budget — archive, don't amputate.
- ❌ No new planning documents beyond this one. Phases live in the queue as `R-*` rows.

---

## 7. Phased order

Every phase ends with `.\scripts\mechanic-green.ps1` green **and** recorded evidence (a queue-row note
plus the numbers in the relevant subsystem page). A phase is not done because code merged; it is done
when its exit criteria are measured.

**Phase 0 — Freeze and measure (cheap, immediate).**
Publish this plan; add the `R-*` rows; write the prompt-floor ceiling test from existing measurements;
record the spine invariants in the relevant subsystem pages.
*Exit:* the ceiling test exists and reports the real number, so the per-turn budget is visible to
anyone.

**Phase 1 — Resolution semantics (the load-bearing slice).**
Make ambiguity a first-class result: a resolver that can say "two candidates, here they are" instead
of silently returning the article-prefixed entity (**E-13**).
*Exit:* `How do magnets work?` / `magnets` either resolve to the physics page or return `ambiguous`
with candidates, and the browser A/B shows a **small model answering the disambiguation case
correctly** — the first real test of whether the spine removes the need for the bigger brain.

**Phase 2 — Tool surface triage and intent groups.**
Triage the 86 agent tools and 84 MCP tools into Core / session groups / archive using section 3's
buckets, then implement group-level gating.
*Exit:* always-on ≤ 15, schemas ≤ ~3k tokens, floor ≤ ~9k, and a test proving a disabled group is not
registered.

**Phase 3 — Docs consolidation.**
Reduce subsystem pages to guarantee + verification; archive the rest; extend
[`EMPIRE_CLARITY.md`](EMPIRE_CLARITY.md) with the per-subsystem sandbox-vs-product boundary.
*Exit:* the three drifts from L4 cannot recur undetected (each now has a test or a single-source
constant).

**Phase 4 — Gates in CI.**
Wire the model-promotion gates (section 4) and the prompt ceiling into `mechanic-green.ps1`, so a new
model, tool or instruction file cannot raise the floor unnoticed.
*Exit:* `mechanic-green` fails when the floor is exceeded.

---

## 8. What to keep (the assets this session proved)

- **Trace-first debugging** — `EMPIRE_TRACE=1` + `eve-audit/eve-trace.jsonl` (now carrying
  `model`/`mode` per turn) + `scripts/trace-eve-browser.py`. Wrong hypotheses die in minutes here.
- **The Mechanic-green gate** — units + wiki battery + verify-stack before any Architect smoke.
- **Probe scripts as promotion gates** — `scripts/ab-fast-toolcalling.py` is why the 7B decision took
  minutes instead of a day of vibes.
- **Determinism rules that already paid:** repeat refusal (7 searches / 66 s → 2 / 14–26 s), the
  stream/speech sanitizers (0 leaks measured), owned/baked model parameters, the cache-buster.
- **The CLARITY vocabulary** — Core / LEGO / Session reach needs no replacement; it needs enforcement.

---

## Related

- [`EMPIRE_CLARITY.md`](EMPIRE_CLARITY.md) — bounding box (Core / LEGO / Session reach)
- [`EMPIRE_IDEA_QUEUE.md`](EMPIRE_IDEA_QUEUE.md) — `R-*` phase rows, `E-*` items (E-13 = Phase 1)
- [`VOICE_PRESENCE.md`](VOICE_PRESENCE.md) — measured latency budget + Fast model A/B procedure
- [`WIKI_SCOUT.md`](WIKI_SCOUT.md) — retrieval contract, question shapes, repeat refusal
- [`manifest/README.md`](manifest/README.md) — full architecture and tool inventory
