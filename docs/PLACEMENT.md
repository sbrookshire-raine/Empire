# Placement — what belongs in VRAM, measured

**One breath:** on this machine the GPU is ~4× faster at *writing* and, on a long prompt, only ~1.4×
faster at *prefilling* when half the model is offloaded — so the number that decides placement is
**"how long before she says the first word"**, and half the chat model can live in system RAM without
costing conversation.

**Machine:** Intel Core Ultra 9 275HX (24 threads), 63.4 GB RAM, RTX 5080 Laptop 16,303 MiB.
**Measured:** 2026-09-24 with `scripts/measure-placement.py` (evidence in `eve-audit/placement*.json`).
Numbers are hardware-specific — re-run the probe rather than trusting this table elsewhere.

## Placement table — `empire-fast:14b`, 48 layers, 1,080-token prompt

| Placement | VRAM | Resident | Prefill | Generation | Eve's 4,382-token floor |
|---|---|---|---|---|---|
| 100% GPU | 11.9 GB | 11.9 GB | 1,304 tok/s | 29.3 tok/s | **3.4 s** |
| ~50% GPU (`num_gpu 24`) | **6.2 GB** | 12.4 GB (6.2 VRAM + 6.2 RAM) | 901 tok/s | 12.6 tok/s | **4.9 s** |
| 100% CPU (`num_gpu 0`) | 0 | 12.5 GB RAM | 50 tok/s | 6.8 tok/s | **87 s** |

`num_gpu` is only settable on Ollama's **native** endpoint — the OpenAI-compat one ignores
per-request `options` (E-02). That is why the probe posts to `/api/chat`.

## KV-cache quantization (E-39) — more room for less VRAM

`q8_0` KV + flash attention, same prompts (`eve-audit/placement-q8.json`):

| Context | KV | VRAM | Prefill | Generation | Floor |
|---|---|---|---|---|---|
| 16,384 (today's default) | f16 stock | 11.9 GB | 1,304 tok/s | 29.3 tok/s | 3.4 s |
| 16,384 | **q8_0 + FA** | **10.4 GB** | 1,193 tok/s | 28.2 tok/s | 3.7 s |
| **24,576** | **q8_0 + FA** | **11.3 GB** | 1,237 tok/s | 27.8 tok/s | 3.5 s |

Read that last row twice: **a 1.5× larger context now costs 0.6 GB *less* VRAM than the current 16k
window with stock KV**, at the same speed. Applied via
`.\\scripts\\ensure-ollama-parallel.ps1 -NumParallel 1 -ContextLength 16384 -KvCacheType q8_0 -FlashAttention`
(one slot keeps the full context per request). **Revert is the same script without the two flags.**

Quality gate: `scripts/ab-fast-toolcalling.py --models empire-fast:14b` passes **before and after**
(tool calls still emitted through the compat proxy; 10,022-token prompt uncut) — evidence
`eve-audit/ab-toolcalling-f16-before.json` vs `ab-toolcalling-q8-after.json`. **Caveat:** the probe is
not deterministic (temp 0.2), so it cannot prove answers are identical — DriftBench
(`run-wiki-calibrate.py`) is the arbiter and needs the Workbench running.

## The policy

1. **If a human is waiting → GPU.** If a clock is waiting → CPU. That single rule resolves nearly
   every placement question.
2. **VRAM holds exactly one interactive chat model.** That is what the GPU lease
   (`pipeline/gpu_lease.py`, `admit_for_goal`) exists to enforce; the measured failure was a stale
   `llama-server` squatting on 14.7 GB.
3. **Half offload is the second-tenant mode:** 5.4 GB VRAM (q8_0) frees ~10 GB for a resident
   `qwen3-vl:8b` (6.1 GB) — chat *and* vision at once, impossible at full offload. Cost: generation
   halves to ~12 tok/s, which is still faster than reading speed.
4. **All specialists live in RAM, never VRAM:** GLiNER, FlashRank, MiniCheck, Speaches (whisper /
   Piper), Docling, extraction, SearXNG, Cognee, Postgres, PocketBase. 63 GB holds the lot.
5. **Batch/desk jobs may run CPU-only on purpose** (`num_gpu: 0`) so they can never evict her — that
   is the worker model for overnight/deep work, at ~7 tok/s.
6. **RAM adds capacity, not speed.** Keeping models in memory lets you *hold* more; bandwidth decides
   pace. CPU-only chat stays ruled out: 87 s before the first word.

## How to re-measure

```powershell
.\\venv\\Scripts\\python.exe scripts\\measure-placement.py                    # cpu / half / full
.\\venv\\Scripts\\python.exe scripts\\measure-placement.py --num-ctx 24576    # a bigger window
.\\venv\\Scripts\\python.exe scripts\\measure-placement.py --prompt short
```

Writes `eve-audit/placement.json` (machine, layers, floor, per-placement latency, rates and the real
`/api/ps` VRAM split via `size_vram`).

## Related

- [`EMPIRE_IDEA_QUEUE.md`](EMPIRE_IDEA_QUEUE.md) — E-38 (this probe), E-39 (KV tuning), E-41 (24k promotion)
- [`VOICE_PRESENCE.md`](VOICE_PRESENCE.md) — the model A/B procedure this extends
- [`RESEARCH_BENCH.md`](RESEARCH_BENCH.md) — the desk jobs that rule 5 is for
