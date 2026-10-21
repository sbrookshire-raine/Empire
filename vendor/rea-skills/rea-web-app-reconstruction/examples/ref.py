#!/usr/bin/env python3
"""Reference app: a tiny JSON-over-stdio ledger. Persists to ./store.json."""
import json, os, sys
P = "store.json"
store = json.load(open(P)) if os.path.exists(P) else []
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        op = json.loads(line)
    except json.JSONDecodeError:
        print("bad json", file=sys.stderr); sys.exit(2)
    kind = op.get("op")
    if kind == "add":
        store.append({"id": len(store) + 1, "title": op["title"]})
        json.dump(store, open(P, "w"))
        print(json.dumps({"ok": True, "id": len(store)}))
    elif kind == "list":
        print(json.dumps({"items": store}))
    else:
        print("unknown op", file=sys.stderr); sys.exit(2)
