import sqlite3
import json
import os
from pathlib import Path
from fastmcp import FastMCP

# 1. EMPIRE Environment Configuration
# Adheres to the exact Windows directory layout required by the architecture
EMPIRE_ROOT = Path(os.environ.get("EMPIRE_ROOT", "C:/EMPIRE"))
CATALOG_DB_PATH = EMPIRE_ROOT / "config" / "eve-capabilities" / "catalog.db"
SKILLS_DIR = EMPIRE_ROOT / "eve-skills"

# 2. Initialize the MCP Server
# FastMCP handles JSON-RPC, stdio transport, and schema generation automatically.
mcp = FastMCP(name="Eve Discovery Router")

def get_db_connection():
    """Establish a read-only connection to the catalog SQLite database."""
    if not CATALOG_DB_PATH.exists():
        raise FileNotFoundError(f"EMPIRE catalog database not found at {CATALOG_DB_PATH}")
    
    # URI=True and mode=ro ensures the agent cannot mutate the registry via this connection
    conn = sqlite3.connect(f"file:{CATALOG_DB_PATH}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn

@mcp.tool
def search_catalog(query: str = "", eve_capability: str = None, limit: int = 15) -> str:
    """
    Search the EMPIRE catalog for approved tools, CLI binaries, and MCP servers.
    Use this to discover tools when you lack a capability to fulfill a user request.
    
    Args:
        query: Optional keyword search in tool description or name (e.g., 'pdf', 'search').
        eve_capability: Optional taxonomy code (e.g., 'edit.code', 'read.document', 'query.data').
        limit: Maximum number of results to return (default 15).
    """
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        
        # Return a deliberately sparse schema to avoid token flooding
        sql = """
            SELECT id, description, eve_capability, trust_domain, score_local, score_mcp, score_cli 
            FROM repositories 
            WHERE 1=1
        """
        params = []
        
        if query:
            sql += " AND (id LIKE ? OR description LIKE ?)"
            params.extend([f"%{query}%", f"%{query}%"])
            
        if eve_capability:
            sql += " AND eve_capability = ?"
            params.append(eve_capability)
            
        # Prioritize tools that are functionally stable and local-first
        sql += " ORDER BY score_functional DESC, score_local DESC LIMIT ?"
        params.append(limit)
        
        cursor.execute(sql, params)
        rows = cursor.fetchall()
        
        if not rows:
            return f"No tools found matching query '{query}' and capability '{eve_capability}'."
            
        return json.dumps([dict(row) for row in rows], indent=2)
    finally:
        conn.close()

@mcp.tool
def inspect_tool_metadata(repo_id: str) -> str:
    """
    Retrieve full inspection details for a specific repository tool from the catalog,
    including its scores, license, deployment modes, and security constraints.
    
    Args:
        repo_id: The exact ID of the repository returned from search_catalog (e.g., 'astral-sh/ruff').
    """
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM repositories WHERE id = ?", (repo_id,))
        row = cursor.fetchone()
        
        if not row:
            return f"Tool with ID '{repo_id}' not found in the catalog."
            
        tool_data = dict(row)
        
        # Hydrate the capability tags
        cursor.execute("SELECT capability_name FROM capabilities WHERE repo_id = ?", (repo_id,))
        tool_data["tags"] = [r["capability_name"] for r in cursor.fetchall()]
        
        return json.dumps(tool_data, indent=2)
    finally:
        conn.close()

@mcp.tool
def load_skill_manifest(skill_name: str) -> str:
    """
    Read the SKILL.md instruction manifest for a specifically installed CLI tool.
    Call this BEFORE attempting to execute an unfamiliar CLI tool to understand its rules, 
    path constraints, and exact argument schema.
    
    Args:
        skill_name: The local directory name of the skill (e.g., 'ripgrep', 'markitdown').
    """
    skill_path = SKILLS_DIR / skill_name / "SKILL.md"
    
    if not skill_path.exists():
        return (f"SKILL.md not found for '{skill_name}'. "
                f"Ensure the skill is installed in {SKILLS_DIR} or check the exact name.")
        
    with open(skill_path, "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    # Execute via standard input/output (stdio), which is the secure transport layer
    # required by EMPIRE to prevent unauthorized local network exposure.
    mcp.run()