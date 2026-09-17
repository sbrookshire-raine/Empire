# skill-switchboard

Use when the Architect's task needs a specific local service (PocketBase, the frontend), a heavy GPU tenant (vision/stem/voice/extract), or when a task finishes and services should be released. You run services so the Architect never toggles them.

## Mission

Start exactly the services a task needs, never oversubscribe the 16 GB GPU, and release what you started when the task is done. Always plan first, mutate only on headroom green.

## Tools

1. `switchboard_status` — services up/down + headroom + GPU lease (read-only).
2. `switchboard_plan` — dry-run plan of what would start/stop (no mutation).
3. `switchboard_ensure` — start services (headroom-gated; dry-run default).
4. `switchboard_release` — stop managed services (never Ollama/Eve; dry-run default).
5. `switchboard_tenant` — GPU lease acquire/release/status.

## How to work a goal

1. Call `switchboard_status` (silently) to see what's already up and the headroom.
2. If a service is missing and needed, call `switchboard_plan` to see the start/stop plan, then `switchboard_ensure` with `dry_run=false` **only** when headroom is green.
3. GPU tenants serialize: before acquiring a heavy tenant, `switchboard_tenant release` the previous one. One heavy tenant at a time.
4. When the task is finished, `switchboard_release` the services you started so the machine stays tidy.

## Routing by task class

- Chat / Q&A → `ollama` + `pocketbase` + `eve` (all external/self — nothing for you to start; just answer).
- Tasks/memory → `pocketbase` (managed — ensure if down).
- Vision / stem / voice / extract → their **one** GPU tenant at a time via `switchboard_tenant`.
- Frontend / dashboard → `frontend` (managed — ensure if down).

## Hard rules

- **Never start or stop `ollama` or `eve`** — they are external/self. The switchboard filters them out; don't request them.
- Mutate only on headroom green. If headroom is blocked, report the reasons and stop — do not retry.
- Always `dry_run` first. Never silent Cognee remember.
- Release the heavy tenant before switching tasks so VRAM never thrashs.
