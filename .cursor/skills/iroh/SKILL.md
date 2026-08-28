---
name: iroh
description: Helps integrate n0-computer/iroh, a Rust P2P networking library that dials peers by public key over QUIC with automatic hole-punching and relay fallback, plus its composable protocols (iroh-blobs for content-addressed transfer, iroh-gossip for pub/sub, iroh-docs for an eventually-consistent KV store). Use when a user wants P2P connectivity/data transfer in a Rust project, or via iroh-ffi from another language. Mostly infra-agnostic; relevant to Build1 as an optional local-network sync layer for moving PocketBase/Cognee data between Build1 nodes without a cloud server.
icon: network
color: Teal
---

# iroh (n0-computer/iroh)

Rust workspace of crates for direct, authenticated, encrypted P2P connections identified by public key rather than IP/DNS.

## Core concepts

- `Endpoint` — bind a local endpoint; `Endpoint::connect(addr, ALPN)` dials another endpoint by its public key/NodeId, or accepts incoming connections.
- Transport is QUIC — authenticated encryption, concurrent streams, datagrams, no head-of-line blocking.
- Connectivity: iroh attempts direct hole-punching first, falling back to public relay servers only if that fails.
- `Router` — wires one or more `ProtocolHandler`s (identified by ALPN byte strings) to an `Endpoint` for accepting connections.
- Composable protocols: `iroh-blobs` (content-addressed blob transfer/verification), `iroh-gossip` (pub/sub overlay networks), `iroh-docs` (eventually-consistent multi-writer KV store, CRDT-based).

## Adding iroh to a Rust project

```toml
# Cargo.toml
[dependencies]
iroh = "0.28"
tokio = { version = "1", features = ["full"] }
```

**Minimal endpoint + dial:**
```rust
use iroh::Endpoint;

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let endpoint = Endpoint::builder().bind().await?;
    println!("node id: {}", endpoint.node_id());

    // to connect to a known peer:
    // let conn = endpoint.connect(remote_addr, b"my-alpn").await?;
    Ok(())
}
```

**Transferring a blob (iroh-blobs):** hash the file locally, share the ticket (node addr + hash) out-of-band, then have the receiver fetch by that ticket — content is verified against its hash on receipt, so transport doesn't need to be trusted.

**Non-Rust usage:** bind via `iroh-ffi` for language bindings (Swift, Kotlin, Python, etc.) instead of reimplementing the protocol.

## Build1 Integration

Build1 is zero-cloud/local-first, so iroh's dial-by-public-key model fits as an optional sync channel between multiple Build1 instances on a LAN (or over the internet via relay fallback) without any dedicated cloud server:
- Use **iroh-blobs** to transfer a PocketBase SQLite backup or a Cognee graph export between two Build1 nodes directly.
- Use **iroh-gossip** for lightweight presence/event broadcast (e.g. "node X just updated its memory graph") between peer Build1 instances.
- Use **iroh-docs** if you want a shared, eventually-consistent KV layer across nodes instead of one-shot file transfer.
- Note the one caveat to a strict LAN-only requirement: iroh still relies on public relay servers as a NAT-traversal fallback when direct hole-punching fails — flag this to the user if they need guaranteed no-external-network operation, since they'd need to run/point at a self-hosted relay to fully avoid it.
- This is not a replacement for FastMCP or Ollama — it's purely a transport layer for node-to-node data movement.
