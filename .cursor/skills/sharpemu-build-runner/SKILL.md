---
name: sharpemu-build-runner
description: Builds SharpEmu, an experimental C# PlayStation 5 emulator, from source with the .NET SDK and runs it against a user-owned game dump. Use when a user wants to compile SharpEmu, launch a legally-dumped eboot.bin/.elf file, or check its per-game/feature compatibility status; also use to flag piracy-adjacent requests (ROMs/firmware) that the project explicitly disallows. Infra-agnostic — unrelated to any Build1 component (no LLM, backend, memory, or frontend dependency).
icon: cpu
color: Red
---

# SharpEmu — Build & Run (PS5 Emulator, Early-Stage)

SharpEmu is a from-scratch, research/educational C# PS5 emulator. Development currently targets **Windows**; Linux/macOS support is planned but not primary yet.

## 1. Prerequisites
- .NET SDK matching the version pinned in `global.json`.
- (Optional but recommended) VS Code for opening the solution.

## 2. Build
```bash
dotnet restore
dotnet build -c Release
```

## 3. Run
```bash
dotnet run --project SharpEmu -- --game "<path-to-legally-dumped-eboot.bin-or-.elf>"
```
Only use dumps the user legally owns and extracted themselves; do not source or suggest ROM/firmware download sites — this is explicitly disallowed by the project.

## 4. Compatibility status
Check the repo's compatibility tracker/issues for the current per-game and per-feature support matrix before promising a specific title will run; this is an early-stage, research-grade emulator with partial hardware support.

## Build1 Integration
None — this is a standalone build/run tool with no dependency on Ollama, PocketBase, Cognee, FastMCP, or the HTMX/Alpine frontend. Infra-agnostic.
