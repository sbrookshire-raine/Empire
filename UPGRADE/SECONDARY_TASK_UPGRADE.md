# EMPIRE Technical Specification: The Autonomous Research Scavenger (AMS-02)

### Architecture Overview

The Autonomous Research Scavenger is a background daemon designed to eliminate manual input friction. It turns Eve from a passive responder into an active research partner by silently observing your active conversation stream, extracting technical intent via a lightweight local model, programmatically harvesting structured metadata from open-access repositories (arXiv), and indexing them into a local SQLite table (`catalog.db`) for instant retrieval.

---

### Complete Step-by-Step Implementation Workflow

#### Step 1: Initialize the Database Table

The scavenger requires a dedicated, lightweight relational table inside your local SQLite catalog (`catalog.db`) to store research abstracts and direct access vectors without bloating the main repository index.

Run this SQL block to initialize the table:

```sql
CREATE TABLE IF NOT EXISTS research_abstracts (
    id TEXT PRIMARY KEY,
    title TEXT,
    authors TEXT,
    published_date TEXT,
    abstract_summary TEXT,
    keywords TEXT,
    local_file_path TEXT
);

```

#### Step 2: Deploy the Scavenger Daemon Script

Save the complete, standalone Python script below as **`C:\EMPIRE\config\eve-capabilities\research_scavenger.py`**.

This script handles ambient log-tailing, intent filtering, local model topic extraction, API querying, and safe SQLite upserts completely offline.

```python
"""
EMPIRE Autonomous Research Scavenger (AMS-02)
Silently listens to active chat logs, detects when research-heavy topics 
are discussed, automatically generates extraction queries, and populates 
the SQLite research index in the background without user intervention.
"""

import time
import os
import json
import urllib.request
import urllib.parse
import sqlite3
import xml.etree.ElementTree as ET
from pathlib import Path

# --- Configuration ---
EMPIRE_ROOT = Path(os.environ.get("EMPIRE_ROOT", "C:/EMPIRE"))
CHAT_LOG_PATH = EMPIRE_ROOT / "eve-audit" / "active_chat.log"
DB_PATH = EMPIRE_ROOT / "config" / "eve-capabilities" / "catalog.db"
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3:8b" # Lightweight local model for background classification

def tail_chat_log(filepath):
    """Generator that tails the active chat log line-by-line in real-time."""
    file = open(filepath, 'r', encoding='utf-8')
    file.seek(0, os.SEEK_END)
    while True:
        line = file.readline()
        if not line:
            time.sleep(1.0)
            continue
        yield line

def should_trigger_research(message_text: str) -> bool:
    """Filters user input for technical, research, or simulation intent triggers."""
    research_triggers = [
        "what about", "how does", "look into", "research", "find papers", 
        "model", "simulation", "causal", "forecast", "algorithm", "theory", "architecture"
    ]
    text = message_text.lower()
    return any(trigger in text for trigger in research_triggers) and len(text) > 15

def extract_search_topic(recent_history: list) -> str:
    """Passes recent dialogue context to the local model to distill a precise API query string."""
    context_text = "\n".join(recent_history[-5:]) # Look at last 5 conversational turns
    
    prompt = f"""
    Analyze the following conversation snippet and extract a precise academic or technical search query (max 4 words) suitable for querying arXiv or open research repositories. 
    Return ONLY the raw search query text. No quotes, no preamble.
    
    CONVERSATION:
    {context_text}
    
    SEARCH QUERY:
    """
    try:
        req_data = json.dumps({
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": 0.1}
        }).encode('utf-8')
        
        req = urllib.request.Request(OLLAMA_URL, data=req_data, headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            return result.get("response", "").strip()
    except Exception as e:
        print(f"[Scavenger Error] Topic extraction failed: {e}")
        return ""

def harvest_and_index(query: str):
    """Queries arXiv API with the generated topic and upserts clean metadata into SQLite."""
    if not query or len(query) < 2:
        return
        
    print(f"\n[Scavenger] Autonomous trigger detected! Harvesting papers for: '{query}'")
    encoded_query = urllib.parse.quote(query)
    url = f"http://export.arxiv.org/api/query?search_query=all:{encoded_query}&start=0&max_results=5"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'EMPIRE-Autonomous-Scavenger/1.0'})
        with urllib.request.urlopen(req) as response:
            xml_data = response.read()
            
        root = ET.fromstring(xml_data)
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        count = 0
        for entry in root.findall('atom:entry', ns):
            paper_id = entry.find('atom:id', ns).text.split('/')[-1]
            title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
            summary = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')
            published = entry.find('atom:published', ns).text
            pdf_link = f"https://arxiv.org/pdf/{paper_id}.pdf"
            
            # Safe upsert protecting against duplicates
            cursor.execute("""
                INSERT OR REPLACE INTO research_abstracts (id, title, published_date, abstract_summary, keywords, local_file_path)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (paper_id, title, published, summary, query, pdf_link))
            count += 1
            
        conn.commit()
        conn.close()
        print(f"[Scavenger] Successfully indexed {count} new research payloads into catalog.db.")
        
    except Exception as e:
        print(f"[Scavenger Error] Harvesting failed: {e}")

def main():
    if not CHAT_LOG_PATH.parent.exists():
        CHAT_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not CHAT_LOG_PATH.exists():
        CHAT_LOG_PATH.touch()

    print(f"Starting Autonomous Research Scavenger watching {CHAT_LOG_PATH}...")
    recent_history = []
    
    for line in tail_chat_log(CHAT_LOG_PATH):
        line = line.strip()
        if not line:
            continue
            
        recent_history.append(line)
        if len(recent_history) > 10:
            recent_history.pop(0)
            
        if line.startswith("USER:") and should_trigger_research(line):
            topic = extract_search_topic(recent_history)
            if topic:
                harvest_and_index(topic)

if __name__ == "__main__":
    main()

```

#### Step 3: Integrate with Eve's Discovery Router

To ensure Eve can actually query the papers gathered by the background scavenger, update your `discovery-router.py` (or add a companion tool) so Eve can search her own abstract index on demand:

```python
@mcp.tool
def search_research_library(keyword: str, limit: int = 5) -> str:
    """
    Search the local background-harvested research abstract index.
    Use this to find preprints, theoretical papers, and methodologies gathered during past discussions.
    
    Args:
        keyword: Topic or keyword to search for in titles and abstracts.
        limit: Max results to return (default 5).
    """
    conn = get_db_connection() # Uses existing read-only SQLite connection pattern
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, title, published_date, abstract_summary, local_file_path 
            FROM research_abstracts 
            WHERE title LIKE ? OR keywords LIKE ? OR abstract_summary LIKE ?
            LIMIT ?
        """, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%", limit))
        
        rows = cursor.fetchall()
        if not rows:
            return f"No harvested research found matching '{keyword}'."
        return json.dumps([dict(row) for row in rows], indent=2)
    finally:
        conn.close()

```

#### Step 4: Run as a Background Service

To keep the scavenger active during your working sessions without occupying your terminal, launch it as a background process in Windows PowerShell:

```powershell
Start-Process python -ArgumentList "C:\EMPIRE\config\eve-capabilities\research_scavenger.py" -NoNewWindow

```