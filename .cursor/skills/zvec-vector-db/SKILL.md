---
name: zvec-vector-db
description: Installs and drives Zvec, an open-source in-process embedded vector database with dense/sparse vector search, full-text search, and hybrid retrieval — no server process required. Use when a user wants a lightweight local vector index for embeddings/similarity search that sits outside or alongside Build1's Cognee graph memory (e.g. a narrow embedding-only lookup that doesn't need Cognee's full graph). Touches Build1's Memory/RAG layer (Cognee 1.0) as a secondary, in-process option; runs 100% locally with no cloud dependency.
icon: database
color: Teal
---

# Zvec Vector Database

Zvec is an in-process embedded vector database — it runs as a library inside your application (no separate
server process, no client/server protocol to configure). It supports dense vectors, sparse vectors,
full-text search (FTS), and hybrid retrieval combining all three with scalar filtering. Because it is
embedded and local by design, it fits a zero-cloud stack without modification.

Do NOT attempt to build Zvec from source (large C++ project with many thirdparty submodules) — always use
the published language packages.

## Installation
| Language | Install command | Requirements |
|---|---|---|
| Python | `pip install zvec` | 64-bit Python 3.10–3.14 |
| Node.js | `npm install @zvec/zvec` | — |
| Dart/Flutter | `flutter pub add zvec` | — |
| Go / Rust | see the respective `zvec-go` / `zvec-rust` repos | — |

Supported platforms: Linux (x86_64, ARM64), macOS (ARM64), Windows (x86_64). On an unsupported platform,
building from source is the only option — do not attempt it in a sandboxed/CI context.

A GUI, **Zvec Studio**, is available for browsing data and debugging queries without code.

## Core workflow
1. Define a schema for the collection (vector dimension, dense/sparse/FTS fields, any scalar metadata columns).
2. Create or open a collection on local disk.
3. Insert documents (id, vector(s), metadata, text for FTS).
4. Query: vector similarity, keyword FTS, or hybrid (vector + keyword + scalar filter) in one call.

## Build1 Integration
- **Cognee 1.0 (Graph)** is Build1's primary Memory/RAG layer and should stay the default for
  conversational/document memory — it captures relationships, not just nearest-neighbor similarity.
- Reach for Zvec only when a component needs a narrow, fast, embedded vector index that doesn't warrant
  Cognee's graph overhead (e.g. a local cache of embeddings for a single tool). It runs in-process, so it can
  live inside a FastMCP tool without adding a new network service.
- Generate embeddings locally via **Ollama's** embedding models (do not call a cloud embedding API) before
  inserting into Zvec.
- If a workflow ends up needing both graph relationships and raw vector search, prefer extending Cognee's
  schema over standing up Zvec as a second, disconnected store.
