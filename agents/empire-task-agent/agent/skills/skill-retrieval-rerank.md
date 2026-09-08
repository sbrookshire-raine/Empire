# skill-retrieval-rerank

When the Architect wants to rerank retrieval candidates or run retrieval A/B eval:

1. Toolbelt **Retrieval Rerank** must be ON.
2. Call `retrieval_rerank` with query + JSON candidates `{id,text}`.
3. Never claim production Cognee embeddings changed — nomic stays production.
4. Never auto-`cognee_remember`.
