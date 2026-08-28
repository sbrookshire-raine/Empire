---
name: skillguard-offline
description: Runs yangyixxxx/skillguard offline static scans on Cursor SKILL.md files and skill scripts for prompt injection, exfiltration, and destructive-ops patterns with zero LLM cost. Use before enabling new community skills under .cursor/skills, or when auditing scripts/ in EMPIRE skills. Prefer over NVIDIA SkillSpector for Build1.
---

# SkillGuard Offline (Build1)

Zero-LLM static auditor for agent skills. Scan new or updated `.cursor/skills/**/SKILL.md` (and bundled scripts) **before** registering them for agent use.

## Why this wins

| Tool | Verdict |
|---|---|
| **yangyixxxx/skillguard** | Bin 1 winner — offline, cheap, skill-focused |
| NVIDIA/SkillSpector (`--no-llm`) | Bin 3 for EMPIRE — same job, heavier; keep out of active skill set |
| `no-mistakes` | Different job (git push gate with optional Ollama review) — complementary |

## Install

```bash
pip install skillguard
# or: follow https://github.com/yangyixxxx/skillguard README / Munir port if primary package moves
```

## Workflow

1. Identify target: a skill directory or a single `SKILL.md`.
2. Run SkillGuard (or `scripts/main.py`) with **no** cloud LLM flags.
3. Triage findings: block enablement on high-severity exfil / destructive / injection hits.
4. Only then add MCP/skill wiring or tell the agent the skill is approved.

## Agent commands

```bash
python .cursor/skills/skillguard-offline/scripts/main.py .cursor/skills/some-new-skill
python .cursor/skills/skillguard-offline/scripts/main.py --check-install
```

If the upstream CLI differs, `scripts/main.py` prints install hints and attempts common entrypoints.

## EMPIRE policy

- No OpenAI/Anthropic for this audit path
- Prefer scanning any community skill that ships `scripts/`
- Do not replace `destructive-command-guard` for shell ops — SkillGuard is skill-content focused

## Scripts / references

- `scripts/main.py` — install check + invoke skillguard CLI if present
- [references/docs.md](references/docs.md)
