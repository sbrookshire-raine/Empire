# Structured Extract worker

Bounded **llama.cpp** specialist for schema-constrained JSON extraction. Ollama remains Eve's interactive chat brain.

**Toolbelt:** `structured_extract` (default OFF)  
**Listen:** `http://127.0.0.1:8092`  
**Schema:** `DocumentMetadata.v1`  
**GPU tenant:** `extract` (via `pipeline.gpu_lease`)  
**Scratch out:** `C:\Empire_Workbench\04_Thought_Experiments\extract_cache\`  
**Never** auto-promotes to Cognee.

## Install (done on this machine 2026-09-07)

Mechanic already installed:

1. GGUF: `%LOCALAPPDATA%\EMPIRE\models\gguf\Qwen3-14B-Q4_K_M.gguf` (sha256 pinned in release manifest)
2. `llama-server` b10840 CUDA 12.4: `%LOCALAPPDATA%\EMPIRE\bin\llama.cpp\win-cuda-12.4\llama-server.exe`

Prelim test: health on `:8092`, 5/5 golden fixtures extracted via `llama.cpp`, scratch under `extract_cache/`, then server stopped.

## Start / stop

```powershell
cd C:\EMPIRE
.\scripts\start-structured-extract.ps1
.\scripts\stop-structured-extract.ps1
```

If llama-server is missing, the pipeline can still run **eval/compare** against Ollama JSON prompting for Mechanic headless checks — that path is for measurement only, not a second chat brain.

## Eve usage

1. Start the worker (or accept Ollama fallback for dry runs).
2. Enable Toolbelt **Structured Extract**.
3. Ask Eve to extract document metadata from a text path or paste.
4. Confirm lineage JSON in the cached artifact.
5. Stop the worker when done.

## Rollback

1. Disable Toolbelt **Structured Extract**.
2. `.\scripts\stop-structured-extract.ps1`
3. Optionally set `workers.structured_extract.status` to `disabled` in the release manifest.
4. No Cognee cleanup needed (scratch only).

## Rejection

Park the worker if: Windows/CUDA path is unstable; interactive Eve latency becomes unacceptable; grammar/JSON parse rate is not better than Ollama JSON on the golden fixtures.
