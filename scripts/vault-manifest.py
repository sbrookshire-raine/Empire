import hashlib, json
from datetime import datetime
from pathlib import Path

ROOT = Path(r"C:\Empire_Workbench")
OUT_DIR = ROOT / "_manifests"
OUT = OUT_DIR / "vault-manifest-2026-09-26.json"

entries = []
errors = []
for path in sorted(ROOT.rglob("*")):
    if not path.is_file() or "_manifests" in path.parts:
        continue
    try:
        digest = hashlib.sha256()
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
        entries.append({
            "path": str(path.relative_to(ROOT)),
            "bytes": path.stat().st_size,
            "sha256": digest.hexdigest(),
        })
    except OSError as exc:
        errors.append({"path": str(path), "error": str(exc)})

payload = {
    "created": datetime.now().isoformat(timespec="seconds"),
    "root": str(ROOT),
    "purpose": "Proof-of-completeness for any future vault move: verify counts + hashes before and after.",
    "files": len(entries),
    "total_bytes": sum(item["bytes"] for item in entries),
    "errors": errors,
    "entries": entries,
}
OUT_DIR.mkdir(exist_ok=True)
OUT.write_text(json.dumps(payload, indent=1) + "\n", encoding="utf-8")
print(f"files hashed : {len(entries)}")
print(f"total bytes  : {payload['total_bytes']}  ({payload['total_bytes']/1e6:.1f} MB)")
print(f"errors       : {len(errors)}")
print(f"manifest     : {OUT}")
print(f"sha256       : {hashlib.sha256(OUT.read_bytes()).hexdigest()}")
