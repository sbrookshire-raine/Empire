import json
import urllib.request
import urllib.parse
import uuid
import time

BASE_URL = 'http://127.0.0.1:8080'

def post(path, payload):
    req = urllib.request.Request(
        BASE_URL + path, 
        data=json.dumps(payload).encode(), 
        headers={'Content-Type': 'application/json'}
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())

def stream_and_trace(session):
    start_time = time.time()
    req = urllib.request.Request(
        BASE_URL + '/api/eve/session/' + urllib.parse.quote(session, safe='') + '/stream?startIndex=0', 
        headers={'Accept': 'application/x-ndjson'}
    )
    
    assistant_text = ""
    trace_log = []
    
    with urllib.request.urlopen(req, timeout=300) as r:
        for line in r:
            try:
                event = json.loads(line)
            except:
                continue
            
            event_type = event.get('type')
            elapsed = round(time.time() - start_time, 2)
            
            if event_type == 'actions.requested':
                trace_log.append(f"[{elapsed}s] TOOL CALLED: {json.dumps(event.get('data', {}))}")
            elif event_type == 'action.result':
                trace_log.append(f"[{elapsed}s] TOOL RETURNED")
            elif event_type == 'error':
                trace_log.append(f"[{elapsed}s] ERROR: {json.dumps(event.get('data', {}))}")
                
            data = event.get('data')
            if isinstance(data, dict) and isinstance(data.get('messageSoFar') or data.get('message'), str):
                assistant_text = data.get('messageSoFar') or data.get('message')
                
            if event_type == 'session.waiting':
                trace_log.append(f"[{elapsed}s] SYNTHESIS COMPLETE")
                break
                
    return trace_log, assistant_text, round(time.time() - start_time, 2)

battery = [
    {
        "name": "1. Catalog Discovery Test",
        "prompt": "Eve, query your catalog for tools related to 'minimax' or 'decision making'. Return the exact tool name."
    },
    {
        "name": "2. Wikipedia RAG & Lock Test",
        "prompt": "Look up the Wikipedia article for 'Jevons paradox'. Summarize the lead paragraph and ensure the evidence block is cited."
    },
    {
        "name": "3. Local Evidence & Artifact Test",
        "prompt": "Check the health of the Workbench using your local tools, then tell me how much free disk space is available."
    }
]

if __name__ == "__main__":
    print("--- ENABLING RESEARCH PARTNER ---")
    try:
        post('/api/admission', {'action': 'set_research_partner', 'enabled': True})
    except Exception as e:
        print(f"Failed to enable research partner: {e}")

    for test in battery:
        print(f"\n========================================")
        print(f"RUNNING TEST: {test['name']}")
        print(f"PROMPT: {test['prompt']}")
        print(f"========================================")
        
        # NOTE: deliberately omits "active_tools". Posting that field makes
        # eve_toolbelt.apply_active_tools persist the posted list verbatim, which
        # would strip the "always" bucket (voice_presence / push-to-talk) from the
        # operator toolbelt as a side effect. The persisted toolbelt already
        # enables wiki_local, so the wiki tests still run.
        payload = {
            'message': test['prompt'],
            'mode': 'fast',
            'chat_id': 'diag-' + uuid.uuid4().hex[:8],
            'workbench_ui': {}
        }
        
        try:
            session_data = post('/api/eve/session', payload)
            session_id = session_data.get('sessionId')
            
            if not session_id:
                print("ERROR: Server responded, but no sessionId was returned.")
                continue
                
            trace_log, assistant_text, total_time = stream_and_trace(session_id)
            
            print("\n--- TRACE TIMELINE ---")
            for log in trace_log:
                print(log)
                
            print("\n--- EVE SYNTHESIS ---")
            print(assistant_text)
            print(f"\nTotal Turn Time: {total_time}s")
            
        except urllib.error.HTTPError as e:
            print(f"TEST FAILED: HTTP Error {e.code} - {e.reason}")
            print(f"Server response: {e.read().decode('utf-8', errors='ignore')}")
        except Exception as e:
            print(f"TEST FAILED: {str(e)}")

    print("\n--- DISABLING RESEARCH PARTNER ---")
    try:
        post('/api/admission', {'action': 'set_research_partner', 'enabled': False})
    except Exception as e:
        print(f"Failed to disable research partner: {e}")