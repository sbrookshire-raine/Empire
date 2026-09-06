Use when the user asks to split songs into stems, create practice tracks, run Stem Factory / Shard of the Division, or process the stem inbox — and **Stem Factory** is enabled in the Toolbelt.

## Mission

Orchestrate the isolated music stem splitter. Do not invent audio files or pretend separation finished without tool results.

## Folders

- **Inbox:** `C:/Empire_Workbench/stem_factory/input` — user drops songs here
- **Outbox:** `C:/Empire_Workbench/stem_factory/output` — stems + focus mixes

## Tools

1. `stem_status` — project/venv/inbox ready?
2. `stem_list_inbox` — what songs are waiting?
3. `stem_run` — run separation (`limit` default 1; takes minutes)

## How to answer

1. If inbox is empty, tell the user to drop audio into the inbox folder first.
2. Call `stem_list_inbox`, then `stem_run` when they ask to process.
3. Report output paths (`1_stems`, `3_focus`) in plain language.
4. Warn that a run can take a few minutes per song.
5. If Stem Factory Toolbelt is off, ask them to enable it — do not invent stems.

## Hard rules

- Never rewrite or “inline” Demucs logic — only call the tools.
- Stay local; no cloud stem APIs.
- Default to `limit=1` unless the user asks for a batch.
