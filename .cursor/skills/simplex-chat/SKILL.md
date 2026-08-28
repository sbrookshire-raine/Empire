---
name: simplex-chat
description: Guides installing and using SimpleX Chat, a decentralized, identifier-free private messaging platform available as a terminal (console) CLI and as mobile/desktop apps, which can be scripted into chat bots. Use when a user wants to install/run the SimpleX terminal CLI, connect via a one-time invitation link, build a chat bot on SimpleX, or understand its privacy model. Infra-agnostic — does not depend on Ollama, PocketBase, Cognee, or FastMCP, though a SimpleX bot's reply logic can be wired to Build1's local stack.
icon: message-circle
color: Purple
---

# SimpleX Chat (simplex-chat/simplex-chat)

Privacy-focused messaging platform with no phone numbers, usernames, or persistent random IDs identifying users. Connections are established only via one-time invitation links or optional temporary SimpleX addresses. Data lives client-side; message relay servers see no identifying metadata.

## Installing the terminal (CLI) app

1. Get the pre-built terminal binary for the target OS from the latest GitHub release: `https://github.com/simplex-chat/simplex-chat/releases/latest`. Confirm the current asset name/version from that page — do not assume a specific filename, release naming changes.
2. If no pre-built binary exists for the target platform, build from source with Haskell Stack per the "For developers" section of the repo docs.
3. Run the binary (commonly `simplex-chat`) to enter its interactive REPL. First run creates a local user profile stored only in a local SQLite database on the device — nothing is uploaded to any server except transient message relay.

## Core usage patterns

- The REPL accepts slash-style chat commands. Run `simplex-chat -h` or use the in-app help command to get the exact, version-current command list — don't assume specific slash-command syntax, it changes between releases.
- **Connecting:** get a one-time invitation link or SimpleX address from the other party (shared out-of-band, e.g. QR code or URL), then use the connect command with that link.
- **Groups:** create/join groups; discover public groups via the SimpleX Directory (`https://simplex.chat/directory/`).
- **Building a bot:** the terminal app exposes a WebSocket/JSON API designed for bots/integrations — consult the "Develop a chat bot" section of the repo docs (`docs/`) for the client/bot API pattern rather than parsing REPL text output.
- Can run against the operator's default federated relay servers, or fully self-hosted SMP relay/XFTP servers for complete infrastructure control (aligns with a local-first posture if that matters to the user).

## GUI apps

- iOS: App Store / TestFlight beta. Android: Google Play / F-Droid. Desktop: GitHub releases page.
Same underlying protocol as the CLI — only reach for this skill's CLI instructions when the user specifically wants the terminal app or programmatic/bot usage.

## Notes for the agent

- Don't fabricate slash-command syntax not confirmed live — defer to `--help`/in-app help or current docs.
- The repo is a large multi-platform (Haskell/Kotlin/Swift) codebase — never `git clone` the whole thing for this skill; fetch only the specific README/docs page needed via `raw.githubusercontent.com/simplex-chat/simplex-chat/stable/<path>`.
- SimpleX has had a third-party security audit (Trail of Bits) — mention this if asked about security posture.

## Build1 Integration

SimpleX itself is orthogonal to Ollama/PocketBase/Cognee/FastMCP — it's a messaging transport, not part of the local AI stack. If the user wants an AI-driven bot on SimpleX (e.g. an assistant reachable over SimpleX), wire the bot's message-handling logic through a FastMCP tool that calls **local Ollama** for response generation, and optionally logs conversation history to PocketBase or feeds it into Cognee for memory — this keeps the entire bot pipeline local/offline except for the SimpleX relay hop itself. Do not route bot replies through a cloud LLM API.
