---
area: machine-and-services
one_line: Headroom, capability admission, service switchboard, GPU lease, model inventory.
tools: resource_pulse, admit_for_goal, capability_status, request_capability, release_capabilities, switchboard_status, switchboard_ensure, switchboard_release, switchboard_tenant, gpu_lease_status, ollama_health, list_models, get_model_suite, pb_health, check_workbench_health
skills: route-local-models, skill-resource-pulse, skill-switchboard
---

# This machine and its services — worked pathways

One 16 GB GPU, one stack. **Check headroom before heavy work**, mutate services only when headroom is
green, and never start/stop Ollama or Eve from inside a turn. The Architect flips switches; tools that
admit light skills exist for a reason — `resource_pulse` then `admit_for_goal`.

## Headroom and admission
Use when: "can you run X?", "is the GPU busy?", "what's free?", or before any heavy limb.

- **Ask:** "can we run a 27B model right now?" → **Do:** `resource_pulse()` → **Get:** RAM/disk/GPU, loaded models, `headroom_ok`, and what is safe to admit.
- **Ask:** "is anything heavy running?" → **Do:** `resource_pulse()` → **Get:** resident models with context sizes (the GPU tenant picture).
- **Ask:** "try the stems limb on this track" → **Do:** `resource_pulse()` → `admit_for_goal("stem_run")` → **Get:** an admitted session or a refusal with reasons — never a blind start.
- **Ask:** "what light skills are safe right now?" → **Do:** `resource_pulse()` → **Get:** the short list it reports.
- **Ask:** "why did that job crawl?" → **Do:** `resource_pulse()` + `ollama_health()` → **Get:** the tenant/queue explanation instead of a guess.

## Capabilities (governed switches)
Use when: a limb is off and the work genuinely needs it.

- **Ask:** "can you use the vision limb?" → **Do:** `capability_status("vision_local")` → **Get:** on/off plus why.
- **Ask:** "turn on Wiki Local" → **Do:** the Architect flips it in the Workbench; you may `request_capability(...)` → **Get:** a request he can approve (you never flip switches yourself).
- **Ask:** "what capabilities are on?" → **Do:** `capability_status()` with no argument → **Get:** the full switchboard state.
- **Ask:** "we're done with the rerank pass — free it" → **Do:** `release_capabilities("retrieval_rerank")` → **Get:** the resource handed back.
- **Ask:** "why is X refused?" → **Do:** `capability_status("X")` → **Get:** fail-closed reason (missing snapshot, drifted schema, or off).

## Services (start, stop, verify)
Use when: something is down, or a task needs a service that is off.

- **Ask:** "is everything up?" → **Do:** `switchboard_status()` → **Get:** every service with its state.
- **Ask:** "start Postgres and PocketBase" → **Do:** `switchboard_status()` → `switchboard_ensure([...])` (dry-run first) → **Get:** the services up, with a log of what changed.
- **Ask:** "stop the voice service while we work" → **Do:** `switchboard_release(...)` → **Get:** it stopped, with the reason recorded.
- **Ask:** "who has Postgres right now?" → **Do:** `switchboard_tenant("postgres")` → **Get:** the current tenant/lease.
- **Ask:** "is Eve herself healthy?" → **Do:** `pb_health()` + `check_workbench_health()` → **Get:** service answers (never restart her mid-turn).

## GPU lease
Use when: two limbs want the GPU, or a model is resident that shouldn't be.

- **Ask:** "who has the GPU?" → **Do:** `gpu_lease_status()` → **Get:** the lease holder and expiry.
- **Ask:** "can I load a 14B beside the current one?" → **Do:** `gpu_lease_status()` + `resource_pulse()` → **Get:** a yes/no with the VRAM arithmetic.
- **Ask:** "why is my answer slow?" → **Do:** `gpu_lease_status()` + `ollama_health()` → **Get:** the model-swap explanation.
- **Ask:** "release the GPU after this" → **Do:** `switchboard_release("gpu")` (or let the lease expire) → **Get:** the GPU free for the next task.

## Models and profiles
Use when: choosing Fast vs Deep vs Librarian, or checking what is installed.

- **Ask:** "which models do I have?" → **Do:** `list_models()` → **Get:** installed tags with sizes.
- **Ask:** "what's the Fast profile using?" → **Do:** `get_model_suite()` → **Get:** the active profile and its model (empire-fast:14b on this machine).
- **Ask:** "should this run on Deep instead?" → **Do:** `get_model_suite()` + `resource_pulse()` → **Get:** a recommendation with the VRAM cost.
- **Ask:** "is Ollama awake?" → **Do:** `ollama_health()` → **Get:** reachability and loaded models.
- **Ask:** "is the context long enough for this prompt?" → **Do:** `get_model_suite()` → **Get:** the profile's context (the shared 8192 invariant) so truncation is ruled out.
