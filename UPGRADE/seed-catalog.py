import sqlite3
import json
from pathlib import Path

# Paths
JSON_PATH = Path(r"C:\EMPIRE\config\eve-capabilities\osint-catalog.json")
DB_PATH = Path(r"C:\EMPIRE\config\eve-capabilities\catalog.db")

def build_database():
    if not JSON_PATH.exists():
        print(f"Error: Could not find {JSON_PATH}")
        return

    print("Reading JSON catalog...")
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    repos = data.get("repositories", [])
    
    # Connect to SQLite
    print("Building SQLite database...")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create normalized tables
    cursor.executescript("""
        DROP TABLE IF EXISTS capabilities;
        DROP TABLE IF EXISTS repositories;
        
        CREATE TABLE repositories (
            id TEXT PRIMARY KEY,
            url TEXT,
            description TEXT,
            category TEXT,
            eve_capability TEXT,
            trust_domain TEXT,
            primary_language TEXT,
            license_type TEXT,
            has_mcp BOOLEAN,
            has_cli BOOLEAN,
            score_mcp INTEGER,
            score_local INTEGER,
            score_cli INTEGER,
            score_functional INTEGER,
            stars INTEGER,
            deployment_modes TEXT,
            last_analyzed_at TEXT
        );

        CREATE TABLE capabilities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            repo_id TEXT,
            capability_name TEXT,
            FOREIGN KEY(repo_id) REFERENCES repositories(id)
        );
    """)
    
    # Insert Data
    for repo in repos:
        deployment_modes = json.dumps(repo.get("deployment_modes", []))
        
        cursor.execute("""
            INSERT INTO repositories (
                id, url, description, category, eve_capability, trust_domain, 
                primary_language, license_type, has_mcp, has_cli, 
                score_mcp, score_local, score_cli, score_functional, 
                stars, deployment_modes, last_analyzed_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            repo.get("id"), repo.get("url"), repo.get("description"), 
            repo.get("category"), repo.get("eve_capability"), repo.get("trust_domain"),
            repo.get("primary_language"), repo.get("license_type"), 
            repo.get("has_mcp"), repo.get("has_cli"), repo.get("score_mcp"), 
            repo.get("score_local"), repo.get("score_cli"), repo.get("score_functional"),
            repo.get("stars"), deployment_modes, repo.get("last_analyzed_at")
        ))
        
        # Insert tag array into relational table
        for cap in repo.get("capabilities", []):
            cursor.execute("INSERT INTO capabilities (repo_id, capability_name) VALUES (?, ?)", 
                           (repo.get("id"), cap))
                           
    conn.commit()
    conn.close()
    print(f"Success! Loaded {len(repos)} repositories into {DB_PATH}")

if __name__ == "__main__":
    build_database()
Step 3: Connect the Router to Your Agent
Once catalog.db exists, you must expose the router to Eve. If you are using Claude Desktop, Cursor, or a custom LangChain/AgentOS client, you register it in the standard MCP client configuration file (e.g., claude_desktop_config.json or .cursor/mcp.json).

Add this configuration block to launch the router securely via standard input/output (stdio):

JSON
{
  "mcpServers": {
    "eve-discovery": {
      "command": "uv",
      "args": [
        "run",
        "fastmcp",
        "run",
        "C:/EMPIRE/config/eve-capabilities/discovery-router.py"
      ]
    }
  }
}