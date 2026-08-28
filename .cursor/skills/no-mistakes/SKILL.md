---
name: no-mistakes
description: Sets up and drives no-mistakes, a local git proxy remote that intercepts `git push`, spins up a disposable worktree, and runs an AI-driven review/test/docs/lint pipeline — only forwarding the branch and opening a PR once every check passes. Use for an automated pre-push quality gate on a repo, or to gate agent-driven coding tasks before they reach review. Infra-agnostic dev-tooling; when configuring its AI review step for Build1 development, point it at Local Ollama instead of a cloud LLM to keep the whole gate offline.
icon: git-pull-request
color: Green
---

# no-mistakes: AI-gated git push pipeline

no-mistakes (kunchenguid/no-mistakes, Go) adds a second git remote (`no-mistakes`) that gates pushes in front of the real remote (`origin`). Pushing to it creates a disposable worktree, runs a review → test → docs → lint pipeline, applies safe "auto-fix" findings automatically, and escalates "ask-user" findings for human/agent approval. Only once every check is green does it forward the branch and open the PR.

## Setup

1. Install the `no-mistakes` binary (per the repo's release page / build instructions for the target OS).
2. Add it as a second remote pointing at the local proxy, alongside the existing `origin`:
   ```bash
   git remote add no-mistakes <local-proxy-url>
   ```
3. Configure the pipeline's review/test/docs/lint stages (per the repo's config file) for the project's language/toolchain.

## Usage

```bash
# push to the gate instead of directly to origin
git push no-mistakes <branch>
```

The proxy: clones a disposable worktree → runs review, tests, docs generation/check, and lint → auto-applies safe fixes → surfaces "ask-user" findings for approval → on all-green, forwards the branch to `origin` and opens the PR.

## Escalation model

| Finding type | Behavior |
|---|---|
| Auto-fix | Applied automatically in the disposable worktree, then re-checked |
| Ask-user | Blocks and surfaces to the human/agent for approve / fix / skip |
| Failing test/lint | Blocks the push entirely until resolved |

## Build1 Integration

- Configure no-mistakes' AI review stage to call **local Ollama** (`http://localhost:11434`) instead of a cloud LLM provider — this keeps the pre-push code-review gate fully local/offline, consistent with Build1's zero-cloud policy.
- If gating the Build1 project's own repo, the pipeline's disposable worktree can spin up the FastMCP server and a scratch PocketBase instance to run real integration tests against the local stack before approving the push, rather than mocking those services.
- This skill is otherwise infra-agnostic — it works the same regardless of which language/toolchain the gated repo uses.
