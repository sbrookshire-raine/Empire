# intake_to_lego_run

**One call:** web URL or GitHub query/repo → Disassembly Card → optional Heptabase publish → optional memory staging/confirm.

| Field | Use |
|-------|-----|
| `kind` | `web` or `github` |
| `url` | Required for web |
| `query` / `repo` | GitHub search or single slug |
| `depth` | `scout` (default) or `study` (shallow clone) |
| `architect_confirm` | true when Architect approved board/memory **this turn** |
| `promote_memory` | propose card summary to `eve_staging` |
| `promote_confirm` | with confirm: promote to `eve_memory` + mature card on board |

Skill: **skill-intake-to-lego**. Playbook: **intake-and-legos**.
