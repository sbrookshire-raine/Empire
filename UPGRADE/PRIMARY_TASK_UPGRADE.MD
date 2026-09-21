Here is the clean, streamlined instruction block you can paste directly to your coding AI. It hands off the heavy lifting, directs the code creation, and tells it exactly how to wire up EMPIRE using your Postgres database.

---

**Copy and paste this message to your coding AI:**

```markdown
We are building the EMPIRE architecture for Eve. Please execute the following setup plan across our local workspace and remote Postgres database.

### Phase 1: Directory Structure & Micro-Skills Placement
1. Create the following local directory layout under `C:\EMPIRE\`:
   - `C:\EMPIRE\config\eve-capabilities\`
   - `C:\EMPIRE\eve-skills\thought-map\`
   - `C:\EMPIRE\eve-skills\scenario-regret\`
   - `C:\EMPIRE\eve-skills\forecast-baseline\`
   - `C:\EMPIRE\eve-skills\topology-audit\`
   - `C:\EMPIRE\eve-skills\bayes-update\`
   - `C:\EMPIRE\eve-audit\`

2. Unpack the provided micro-skill `.zip` archives directly into their respective folders under `C:\EMPIRE\eve-skills\`. Ensure each folder contains its corresponding `SKILL.md` instruction manual.

3. Create the central governance file at `C:\EMPIRE\config\eve-capabilities\capability-registry.yaml` and populate it with a strict deny-network, read/write-bounded policy for all five micro-skills.

### Phase 2: Postgres Database Registration
1. Connect to our primary Postgres database using environment credentials (or Supabase connection strings).
2. Ensure the main `repositories` table exists (mirroring the schema from our OSINT JSON export).
3. Execute the following SQL query to manually register our 5 private micro-skills into the Postgres `repositories` table so the discovery router can index them:

```sql
INSERT INTO repositories 
  (id, description, category, eve_capability, trust_domain, primary_language, score_local, score_cli, score_mcp, score_functional, has_cli, deployment_modes) 
VALUES 
  ('local/thought-map', 'Analyze a supplied signed directed graph for reinforcing and balancing feedback loops', 'AI Tool', 'read.document', 'Local Evidence', 'Python', 5, 5, 0, 5, true, '["local_binary"]'),
  ('local/scenario-regret', 'Rank strategic decisions under severe uncertainty using minimax regret', 'AI Tool', 'read.document', 'Local Evidence', 'Python', 5, 5, 0, 5, true, '["local_binary"]'),
  ('local/forecast-baseline', 'Produce transparent univariate forecast baselines without hallucinations', 'AI Tool', 'query.data', 'Local Evidence', 'Python', 5, 5, 0, 5, true, '["local_binary"]'),
  ('local/topology-audit', 'Analyze declared dependencies and predict outage propagation paths', 'AI Tool', 'read.document', 'Local Evidence', 'Python', 5, 5, 0, 5, true, '["local_binary"]'),
  ('local/bayes-update', 'Formally update finite hypothesis probabilities using Bayes theorem from explicit likelihoods', 'AI Tool', 'query.data', 'Local Evidence', 'Python', 5, 5, 0, 5, true, '["local_binary"]');

```

### Phase 3: The Discovery-as-MCP Router (Postgres-Backed)

1. Write the `discovery-router.py` script to `C:\EMPIRE\config\eve-capabilities\discovery-router.py`.
2. **Crucial:** Configure `discovery-router.py` to use a **PostgreSQL connection** (using `psycopg2` or `asyncpg` with a read-only role or query restrictions) instead of SQLite, allowing Eve to search the Postgres `repositories` table dynamically via FastMCP.
3. Register the MCP server in `.cursor\mcp.json` (or our active MCP client config) using `stdio` transport:

```json
{
  "mcpServers": {
    "eve-discovery-router": {
      "command": "uv",
      "args": [
        "run",
        "fastmcp",
        "run",
        "C:/EMPIRE/config/eve-capabilities/discovery-router.py"
      ],
      "env": {
        "EMPIRE_ROOT": "C:/EMPIRE"
      }
    }
  }
}

```

### Phase 4: Tone Constriction & Ambient Memory Watchdog

1. Append the "Tone Constriction" rules (direct, concise, subtle gallows humor on failure, zero celebration on success) to Eve's system prompt.
2. Save the **Ambient Memory Watchdog** script as `C:\EMPIRE\config\eve-capabilities\ambient_memory_watchdog.py`. It should tail `C:\EMPIRE\eve-audit\active_chat.log`, intercept success phrases, use local Ollama (`qwen2.5:14b`) to extract durable facts, and commit them asynchronously to Cognee (`http://localhost:8000/api/v1/memory/add`).

```

```