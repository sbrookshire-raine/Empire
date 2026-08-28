# SkillGuard offline — EMPIRE reference pointers

## Upstream

- Repo: https://github.com/yangyixxxx/skillguard
- Job: static scan of `SKILL.md` + skill scripts (injection, exfil, destructive ops)
- Cost: **zero LLM** (fully offline)

## EMPIRE policy

- Run against `.cursor/skills/<new-skill>/` before enabling community skills
- Especially required when a skill ships `scripts/`
- Do not also install NVIDIA SkillSpector as a second active skill (declared Bin 3)

## Complementary tools (different jobs)

- `no-mistakes` — git push gate (optional local Ollama review)
- `destructive-command-guard` — shell/CLI destructive command interception
- `safe-llm` — Ollama-default LLM routing (not a skill scanner)

## Related matrix

- `docs/reference/MASTER_INTEGRATION_MATRIX.md`
- `docs/reference/bin-routing-batch.json`
