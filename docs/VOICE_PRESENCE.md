# Voice Presence (Phase 7)

Local STT/TTS behind an OpenAI-compatible HTTP API so Eve and the Workbench composer
can hear and speak without cloud LLMs.

## Prefer

- **Speaches** (or Voicebox) on `http://127.0.0.1:8000`
- **Kokoro ONNX** TTS (`speaches-ai/Kokoro-82M-v1.0-ONNX`, voice `af_heart`)
- **faster-whisper base** STT (`Systran/faster-whisper-base`) so chat VRAM stays free

## Start

```powershell
.\scripts\start-voice.ps1
```

That script:

1. Creates/starts Docker container `empire-speaches` (`ghcr.io/speaches-ai/speaches:latest-cpu` by default)
2. Binds `127.0.0.1:8000` only (no LAN expose)
3. Ensures the default STT + TTS models are downloaded into volume `empire-speaches-hf`

Or run your chosen speech container/server and set:

```text
EMPIRE_VOICE_BASE_URL=http://127.0.0.1:8000
EMPIRE_VOICE_STT_MODEL=Systran/faster-whisper-base
EMPIRE_VOICE_TTS_MODEL=speaches-ai/Kokoro-82M-v1.0-ONNX
EMPIRE_VOICE_TTS_VOICE=af_heart
```

Optional: `EMPIRE_SPEACHES_IMAGE=ghcr.io/speaches-ai/speaches:latest-cuda` if you deliberately want GPU speech (will contend with Ollama).

## Workbench

1. Enable Toolbelt **Voice Presence**.
2. **Hold the mic** to talk, **release** to transcribe and auto-send (no arrow click).
3. Eve’s reply is spoken **sentence-by-sentence** as text streams in. **Stop** (or **Esc**) cuts speech anytime — even after text finished. Holding the mic also barges in (stops her voice).
4. Eve tools: `voice_transcribe`, `voice_speak` (optional; Workbench covers normal chat).

## Mechanic smoke

```powershell
$env:PYTHONPATH="C:\EMPIRE"
.\venv\Scripts\python.exe -m pipeline.voice_presence health
.\venv\Scripts\python.exe -m pipeline.voice_presence speak "Hello from Eve." -o tmp\voice-out.mp3
.\venv\Scripts\python.exe -m pipeline.voice_presence transcribe tmp\voice-out.mp3
```

API:

```powershell
# Requires Voice Presence limb on
Invoke-RestMethod http://127.0.0.1:8080/api/voice/health
# POST text → audio/mpeg
```

If unreachable, chat still works — voice is opt-in.

## Spoken text must never be scratch (2026-09-23)

Reported from the mic: *"it showed some gibberish, then called the tool, then started talking but
only got a few words out."* Two distinct faults — both fixed, both covered by a browser test:

| Fault | Cause | Fix |
|---|---|---|
| Spoke **"Ask: … Have: … Next: …"** and showed `<thought` in the bubble | Reasoning deltas carry no tag once the block is open, so per-event filtering leaked the body; a partial tag (`"<thought"`, no `>`) also slipped through | `eve_proxy.ReasoningStreamFilter` (stateful per step, holds split tags) + `strip_reasoning_blocks` drops trailing partial tags; `cleanSpeechText` strips blocks client-side |
| Speech started **mid-sentence** and stopped early | `voiceSpokenOffset` was a raw character offset into text that the next step replaces (thought step → tool step → answer), so the cursor landed mid-word | `streamSpeakFromAssistant` resets the cursor when the already-spoken prefix no longer matches the current text |

Also: internal markers (`[[EMPIRE_CHAT_SUMMARY]]` etc.) are stripped from assistant-visible text,
and a leading run of degenerate non-Latin tokens (seen: Thai, on a long prompt) is dropped.

```powershell
$env:PYTHONPATH="C:\EMPIRE"
.\venv\Scripts\python.exe scripts\test-eve-browser-playwright.py            # headless
.\venv\Scripts\python.exe scripts\test-eve-browser-playwright.py --headful  # watch it
```

It drives real Chromium against `eve.html`, watches every assistant bubble as it streams,
captures `/api/voice/speak` bodies, and fails if any scratch text, marker, or non-Latin prefix
reaches the bubble or the speaker, or if speech starts mid-sentence. It enables
`wiki_local` + `voice_presence` for the run and restores your Toolbelt afterwards.

## Latency budget (measured 2026-09-23, RTX 5080 16 GB)

Real browser turns, traced end to end (`scripts/trace-eve-browser.py`, multi-turn in one session):

| Measurement | Before | After |
|---|---|---|
| `wiki_scout_search` | 10,745 ms | **47–78 ms** |
| `wiki_read_section` | 12–22 s (rg timeout) | **210–260 ms** |
| Turn, first (cold model) | ~90–108 s | **16–19 s** |
| Turn, warm | ~20 s | **6–8 s** |
| Tool calls on a miss ("how do magnets work?") | **15** (`wiki_read_section` loop) | **2** |
| Assistant bubbles per question | 2–3 (looked like a loop) | **1** |

Raw model speed: **49 tok/s generate, 1,025 tok/s prefill**. What made it slow, and the fixes:

1. **Title DNS miss → filesystem scan.** `resolve("white stripes")` didn't try "The White Stripes",
   so it fell into a fuzzy `LIKE '%…%'` join over 7.1M rows (~9.5 s), then `wiki_read_lead` used a
   ripgrep scan that timed out after 12 s (21.9 s on that path). Fixed: article-prefix variants,
   two narrow scans ranked in Python, rg capped at 3 s / 4 batches.
2. **Nothing capped generation.** Ollama's compat endpoint ignores per-request `options` (measured:
   `num_predict=24` still generated 458 tokens; `num_ctx=8192` left the model at 4096), so one
   degenerate reply ran ~90 s. Fixed by baking the limits into an EMPIRE-owned model —
   `scripts/build-empire-ollama-models.ps1` creates **`empire-fast:14b`** (`num_ctx 16384`,
   `num_predict 512`, temp 0.2, top_p 0.9); Fast mode uses it.
3. **Missing-section loop.** When a named section didn't exist the tool said only "not available",
   so the model guessed 15 section names in a row. `wiki_read` now returns
   `available_sections` (the page's real H2 headings) plus a rule: use at most one of those, never
   repeat a call, and "the archive does not cover that detail" is a finished answer. The routing
   prompt also states a 3-call budget per turn.
4. **Voice router** ran `llama3.1` (a second model in 16 GB) on every completed message and
   returned `fallback: true`. Off by default now (`EMPIRE_VOICE_ROUTER=1` restores it).
5. **One bubble per step** (`message.completed` cleared the bubble id) — the "doubling" the
   Architect saw. The UI now ends the bubble on `session.waiting`/failure only.
6. **Stale UI.** `eve.html` loaded `eve-workbench.js` with no cache-buster, so fixed UI code kept
   looking broken in the browser. The server now injects `?v=<mtime>` for local `.js`/`.css` — a
   normal refresh is enough.

Trace everything with:

```powershell
$env:EMPIRE_TRACE='1'; .\venv\Scripts\python.exe -m frontend.serve      # turn on tracing
$env:PYTHONPATH='C:\EMPIRE'; .\venv\Scripts\python.exe scripts\trace-eve-browser.py --questions "q1|q2|q3"
```

Logs: `eve-audit/eve-trace.jsonl` (server: turn/step/tool/timing events — `turn.start` carries
`model`/`mode`, and **every record carries a per-turn `turn` id**, so with two sessions in flight the
tracer can still group one question's tool events; the id is minted on the POST and bridged to the
GET `/stream` through a bounded session→turn map, E-18) and `eve-audit/browser-trace.jsonl` (every HTTP
hop with ms). The tracer reports bubbles added per question, so a future regression shows up as
`bubbles_added=2`.

### Fast model A/B (measured 2026-09-23)

Before promoting a different Fast model, gate it on the two things a "looks fine in chat" check
cannot tell you — tool calling through the **compat** proxy, and the ~10k-token prompt fitting
`num_ctx` without truncation:

```powershell
.\scripts\build-empire-ollama-models.ps1                      # builds empire-fast:14b + empire-fast:7b
$env:PYTHONPATH='C:\EMPIRE'; .\venv\Scripts\python.exe scripts\ab-fast-toolcalling.py
```

`empire-fast:7b` (`config/ollama/Modelfile.empire-fast-7b`, built from `qwen2.5:7b-instruct`) passes
both gates: native `tool_calls=['wiki_scout_search']`, prompt **10,022 tokens** ingested uncut.

#### Ambiguity A/B (R-02, 2026-09-24) — the acceptance case

Question: **"How do magnets work?"** — the resolver reports three readings (`The Magnets` a cappella
group, `Magnet` the device, `Magnetism` the concept) and the tool rule says to name the page used or
ask which was meant.

| | `empire-fast:14b` (variant a) | `empire-fast:7b` (variant b) |
|---|---|---|
| Tool trace | `wiki_scout_search` 70.4 ms | `wiki_scout_search` 46.8 ms → `wiki_read_section` 232.0 ms |
| Reply | *"The term \"magnets\" is ambiguous in the local archive. It could refer to the musical group **The Magnets**, the concept of a **Magnet**, or the broader topic of **Magnetism**. Could you specify which…"* | `wiki_read_section("magnetism", section="magnetic_fields_and_theory")` then, on retry, a **301.6 s / 304.7 s** turn |
| Hygiene | **PASS** (1 bubble, speech calls 15 → 3 after the mid-turn-narration fix) | FAIL — the leak is now converted to an honest "that answer didn't come through" instead of gibberish in the speaker |
| Verdict | **grounded and safe** — no hallucinated answer, no invented tool call | small model still blocked by *text-step fluency*, not by context, tool calling or routing (**E-16**) |

The 14B asks rather than guesses; the 7B's failure is documented with its trace in
`eve-audit/r02-b-7b-graded.txt` and `eve-audit/r02-trace-summary.txt`. Grounding beats speed, so Fast
stays **`empire-fast:14b`**; the retrieval cause is fixed (**E-13** closed by R-02) and the remaining
small-model gap is tracked as **E-16** in [`EMPIRE_IDEA_QUEUE.md`](EMPIRE_IDEA_QUEUE.md).

## Architect smoke

1. `.\scripts\start-voice.ps1`
2. Hard-refresh http://127.0.0.1:8080/eve.html → Toolbelt **Voice Presence** on
3. **Hold mic → speak → release** — transcript should send itself; Eve answers in text + voice
4. Ask for a multi-sentence reply — first sentence should speak before streaming finishes

Later: hands-free continuous listen / barge-in (not built yet).
