# Skill: Intake → Disassembly Card → Heptabase → memory (web + GitHub)

Use when the Architect wants Eve to **analyze, learn from, and catalog** outside material — **without** the Architect running separate commands. One tool drives the pipeline.

## Triggers

- "Analyze this URL", "learn from this page", "intake this site"
- "Analyze this repo", "study this GitHub project", "farm and put on the board"
- "Turn that into a disassembly card / Heptabase / memory lego"
- Voice-friendly: after speech aliases, "GitHub" routes here — not Docker Hub

## One action (always)

Call **`intake_to_lego_run`** once per intake request. Do **not** manually chain `web_scout` → `disassembly_card_write` → `disassembly_publish_heptabase` unless this tool failed.

### Web page

```text
intake_to_lego_run({
  kind: "web",
  url: "https://…",
  architect_confirm: true,   // only if Architect said yes to board this turn
  promote_memory: true,      // optional: stage summary to eve_staging
  promote_confirm: true      // only with architect_confirm: confirm → eve_memory + green mature
})
```

### GitHub — search (scout catalog)

```text
intake_to_lego_run({
  kind: "github",
  query: "local mcp server",
  max_new_cards: 5,
  architect_confirm: true
})
```

### GitHub — one repo (scout or study)

```text
intake_to_lego_run({
  kind: "github",
  repo: "owner/name",   // or full github.com URL
  depth: "study",       // shallow clone → Resource Queue + study card
  architect_confirm: true
})
```

### Catalog status only

```text
intake_to_lego_run({ kind: "github" })   // no query/repo
```

## Depth rules

| depth | GitHub meaning | REA |
|-------|----------------|-----|
| **scout** | README + metadata ticket (`farm_kind: scout`) | Not run — hypotheses only |
| **study** | Shallow `git clone` under `00_Resource_Queue` + study card | **Next:** `rea_doctor` → analyze local path (skill-reverse-engineering) |

Scout/search results are **not** "top repos on all of GitHub" — say that plainly if the Architect asked for global trending.

## Infrastructure (automatic)

- **Git:** stack start adds Git to PATH; study depth shallow-clones with `git` when installed (`scripts/ensure-git-path.ps1 -PersistUser` once if needed).
- **Heptabase:** publish calls **`ensure_app_running`** — starts desktop if CLI is down, then runs CLI (fast publish skips extra layout read). Warm early: `scripts/ensure-heptabase-app.ps1`.
- **Cognee:** `promote_memory` is capped (chars + proposes/hour + skips when Cognee lock busy) so intake does not overload ingest.

## Confirm semantics (Architect voice)

- **Heptabase orange card:** `architect_confirm: true` only when the Architect said **yes / put it on the board / publish** in **this** turn.
- **Memory:** default `promote_memory: false`. Use `promote_memory: true` to **propose** staging. Use `promote_confirm: true` **with** `architect_confirm` when they said **remember this / keep in memory**.
- Never skip propose → confirm for durable memory unless they explicitly said remember.

## After the tool returns

Reply with: **card_id**, cache/clone paths, publish/memory sub-results, and **one** next step (REA for study, or "confirm staging in Memory tab").

## References

- Playbook: `playbook("intake-and-legos")`
- Scout farm detail: **skill-resource-farm**
- REA depth: **skill-reverse-engineering**
- [docs/RESOURCE_FARM_AND_CATALOG.md](../../../../docs/RESOURCE_FARM_AND_CATALOG.md)
