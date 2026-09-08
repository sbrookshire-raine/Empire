# skill-voice-presence

1. Toolbelt **Voice Presence** on; speech API at `EMPIRE_VOICE_BASE_URL` (default :8000).
2. Workbench auto-speaks finished Eve chat replies when Voice Presence is on — you usually do **not** need `voice_speak` for normal chat.
3. `voice_transcribe` for local audio paths; `voice_speak` only when the user asks for a one-off TTS file or a spoken line outside auto-play.
4. If health fails, say the speech server is down and point to `docs/VOICE_PRESENCE.md` — do not fake transcripts.
