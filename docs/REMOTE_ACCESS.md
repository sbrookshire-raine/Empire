# Secure remote access (Phase 6)

EMPIRE binds services to **localhost**. Do not open LAN inbound ports.

## Recommended

1. Install [Tailscale](https://tailscale.com/) on this Windows host.
2. Use Tailscale Serve / Funnel only if you accept the exposure model — prefer
   **Tailscale SSH** or MagicDNS to reach `127.0.0.1:8080` from your phone/laptop
   on the same tailnet (subnet router or local proxy as needed).
3. Alternative: Cloudflare Tunnel pointed at `http://127.0.0.1:8080` with access
   policies — never expose PocketBase admin or Ollama publicly without auth.

## Hard rules

- Keep Ollama, Eve, PocketBase, Cognee, Weaviate on loopback.
- No cloud BaaS, no public inbound as a shortcut.
- After tunnel works, smoke: open Workbench over the tunnel, send one chat turn.

## Status

Scaffold documented for Capability Atlas Wave 4. Architect enables tunnel when ready.
