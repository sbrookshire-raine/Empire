---
name: hiring-agent-resume-scorer
description: Runs a Python CLI pipeline that parses a resume PDF, extracts structured JSON via a local Ollama model (hosted LLM only as an explicit opt-in fallback), enriches it with GitHub profile/repo signals, and produces an explainable, scored candidate evaluation. Use this skill when a user gives you a resume PDF and asks for a candidate score, resume-to-JSON extraction, or a GitHub-augmented hiring evaluation. Touches Build1's Inference layer (Local Ollama), and integrates with Backend (PocketBase) and Memory/RAG (Cognee) for storage and retrieval.
icon: user-check
color: Purple
---

# Hiring Agent — Resume-to-Score Pipeline

A CLI pipeline: resume PDF → structured JSON → GitHub-signal enrichment → explainable candidate score.

## Setup
```bash
pip install -r requirements.txt

# Configure the extraction LLM: default to local Ollama
export HIRING_AGENT_LLM_PROVIDER=ollama
export HIRING_AGENT_LLM_MODEL=llama3
export OLLAMA_HOST=http://localhost:11434

# Optional: GitHub enrichment needs a personal access token
export GITHUB_TOKEN=<token>
```
Only set `HIRING_AGENT_LLM_PROVIDER=gemini` (or another hosted provider) if the user explicitly wants to use a hosted model instead of local Ollama — call this out when you do, since it breaks the zero-cloud default.

## Run
```bash
python hiring_agent.py --resume path/to/resume.pdf --github-username <candidate-gh-handle>
```
This:
1. Parses the resume PDF into raw text.
2. Extracts structured JSON (name, skills, experience, education) via the configured local model.
3. Fetches the candidate's public GitHub profile and repo signals (languages, contribution activity, notable repos) if a username/URL is provided.
4. Produces a scored, explainable evaluation report (per-criterion rationale, not just a bare number).

## Build1 Integration
- **Inference**: extraction defaults to local Ollama; never silently fall back to a hosted LLM for PII-bearing resume content.
- **Backend**: persist parsed candidate JSON and the final score/report in a PocketBase collection (e.g. `candidates`) for querying and audit history.
- **Memory/RAG**: feed extracted skills/experience into Cognee's graph memory to enable cross-candidate retrieval queries later (e.g. "which candidates have production Kubernetes experience").
- **Nervous System**: expose `score_resume(pdf_path, github_username)` as a FastMCP tool so other Build1 agents (e.g. a hiring-pipeline orchestrator) can call it directly.
