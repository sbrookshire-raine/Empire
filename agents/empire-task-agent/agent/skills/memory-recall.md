Use automatically when the user asks about their interests, knowledge, notes, research themes, memory graph, what you know about them, workbench memory, or projects stored in memory.

## Do immediately (same turn, silent)

1. Call `cognee_recall` with dataset **`eve_core`** first for chat-style questions.
   - If results are thin, call again with `dataset=eve_memory`.
   - Broad interest questions: query like `EMPIRE FORGE projects user interests themes`
   - Narrow questions: use their exact topic as the query.
2. Read the recall results and answer in plain language — themes, projects, recurring topics.
3. If recall is empty or thin, say so honestly and suggest a more specific angle. Do not ask for access, skills, or embeddings.

## Never

- Mention skills, tools, datasets, vectors, or PocketBase tasks.
- Use `create_task`, `list_tasks`, or `search_tasks` when the user asks about **projects in memory** (Cognee ≠ PocketBase).
- Load `manage-tasks` for memory questions.
- Promise to search later — recall first, then speak.
