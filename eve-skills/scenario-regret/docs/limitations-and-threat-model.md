# Limitations and threat model

Payoffs and scenario completeness are user assumptions. Not probabilities or predictions. No horizon scanning or autonomous wargaming.

## Trust boundary
Caller supplies untrusted bounded JSON. Runtime reads stdin and writes stdout/stderr only; Python imports installed code from disk. No user-controlled file APIs, deserialization beyond JSON, shell, dynamic code, subprocess, network, models, datasets, certificates or persistent state. Synthetic fixture data only. Python audit hooks reject socket-family events; this is defense-in-depth, not a malicious-code sandbox. External runtime, host OS, MCP client and installed Python package integrity remain trusted.

## Resource and transport limits
256 KiB input frames and output budget; JSON nesting 32. See input schema for algorithm-specific limits. Single-threaded synchronous calls. Tool calls are limited to 10 per second with a burst of 20. Request IDs are strings of at most 128 characters or integers with absolute value <= 9007199254740991. Oversized MCP frames end the process with exit 2 rather than draining unbounded input. No hard wall-clock or memory enforcement inside the process; deploy with client timeout (15 seconds recommended) and OS process limits. Stalled partial input can wait indefinitely until client shutdown; close stdin or terminate the process. No TCP/HTTP listener, cancellation preemption, progress, resources, prompts, sampling or tasks.

## Compatibility
MCP 2025-11-25 legacy initialization only. The 2026-07-28 modern metadata/discovery protocol is not implemented. `server/discover` returns Method not found. Configure a client with legacy fallback. No EVE-specific integration was possible without EVE settings. Linux CPython 3.12 is tested; other versions/platforms need validation. Generic MCP config is an example, not a verified EVE config.

## Privacy
No telemetry, log files or caches are intentionally created by the runtime. Successful output contains caller-supplied labels and analytical results; the caller and MCP host may log them. Error messages are bounded validation diagnostics. Install-time Python may create bytecode caches. Do not send secrets as analytical input.

## Review limits
Generated code received static and executable negative testing, not independent penetration testing, formal proof, legal opinion or domain-model validation. No dependency advisory database clearance or interpreter CVE clearance is claimed.
