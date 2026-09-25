---
area: media-and-time
one_line: Audio stems, vision, voice, documents to media, and the DAZE schedule.
tools: stem_list_inbox, stem_run, stem_status, vision_describe, vision_ui_observe, voice_speak, voice_transcribe, daze_list_day, daze_free_windows, daze_compare_phases, daze_upsert_block, docling_convert
---

# Media and time — worked pathways

These limbs touch real hardware (GPU for Demucs/vision, the mic and speaker for voice). Check headroom
first when the job is heavy; speech goes through Speaches on :8000.

## Audio stems (practice + production)
Use when: he drops a track and wants it split, or wants a practice version.

- **Ask:** "split this song into stems" → **Do:** `stem_list_inbox()` → `stem_run("<track>")` → `stem_status()` → **Get:** vocals/drums/bass/other files and their path.
- **Ask:** "what's waiting in the stem inbox?" → **Do:** `stem_list_inbox()` → **Get:** the queue with sizes.
- **Ask:** "make me a drums-only practice track" → **Do:** `stem_run` then point at the `drums` output → **Get:** the isolated track path.
- **Ask:** "how did the last batch go?" → **Do:** `stem_status()` → **Get:** progress/completion, and what failed.
- **Ask:** "can I run Demucs now?" → **Do:** `resource_pulse()` then `admit_for_goal("stem_run")` → **Get:** an admitted run instead of a stalled GPU.

## Vision (see a screenshot or a region)
Use when: he shares an image, or a UI region needs describing.

- **Ask:** "what's in this screenshot?" → **Do:** `vision_describe("<path>")` → **Get:** an itemized description (observe only).
- **Ask:** "why is my Workbench page blank?" → **Do:** `vision_ui_observe("<local url>")` → **Get:** what the rendered region actually shows.
- **Ask:** "read the error text on screen" → **Do:** `vision_describe(path)` → **Get:** the literal text plus context.
- **Ask:** "compare these two mockups" → **Do:** `vision_describe` on both → **Get:** a structured difference list.
- **Ask:** "note what you see for later" → **Do:** `vision_describe` then `thought_experiment_capture(notes=...)` → **Get:** the observation saved under `vision_notes`/thought experiments.

## Voice (speak and listen)
Use when: push-to-talk is on, or he asks for spoken output.

- **Ask:** "read that answer out loud" → **Do:** `voice_speak(answer)` → **Get:** audio through the local TTS (say nothing about the pipeline).
- **Ask:** "transcribe what I just said" → **Do:** `voice_transcribe("<audio path or live>")` → **Get:** the text as heard.
- **Ask:** "is the mic working?" → **Do:** `capability_status("voice_presence")` + the :8000 health → **Get:** an honest state, not a promise.
- **Ask:** "keep speech to the final answer only" → **Do:** nothing but the policy: speech fires once per turn from the final text → **Get:** no mid-turn recitals (`turnHadToolStep` guards this).

## DAZE (schedule, free time, phases)
Use when: day planning, free windows, planned vs actual.

- **Ask:** "what's my day look like?" → **Do:** `daze_list_day(date)` → **Get:** the blocks in order.
- **Ask:** "when am I free for a 90-minute build session?" → **Do:** `daze_free_windows(date, minutes=90)` → **Get:** the open windows.
- **Ask:** "how did planned vs actual go last week?" → **Do:** `daze_compare_phases(...)` → **Get:** the comparison table.
- **Ask:** "add a practice block Thursday 7pm" → **Do:** `daze_upsert_block(...)` **after confirming** → **Get:** the block written to PocketBase.
- **Ask:** "protect my mornings" → **Do:** `daze_free_windows` then `daze_upsert_block` for the guard → **Get:** the recurring block, with the change named.

## Documents into reusable media
Use when: a PDF/office file should become something searchable or presentable.

- **Ask:** "turn this manual into markdown I can search" → **Do:** `docling_convert("<path>")` → **Get:** staged markdown for `workspace_search`.
- **Ask:** "pull the track list out of this PDF and make a sheet" → **Do:** `docling_convert` → `structured_extract` → `create_spreadsheet` → **Get:** the `.xlsx`.
- **Ask:** "summarize this 40-page report in 5 bullets" → **Do:** `docling_convert` → read the markdown → **Get:** bullets that quote the document.
- **Ask:** "extract the references section" → **Do:** `docling_convert` then `grep` for the heading → **Get:** just that section.
