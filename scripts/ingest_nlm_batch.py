from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from optimize_eve_memory import DATASET, ingest_paths

paths = []
for path in sorted(Path(r"C:\Empire_Workbench\01_Memory_Bank").glob("nlm*.md")):
    try:
        if path.stat().st_size == 0:
            print(f"SKIP empty: {path.name}")
            continue
        if not path.read_text(encoding="utf-8").strip():
            print(f"SKIP whitespace-only: {path.name}")
            continue
    except OSError as exc:
        print(f"SKIP unreadable {path.name}: {exc}")
        continue
    paths.append(path)

print(f"Ingesting {len(paths)} NLM files into {DATASET}...")
for index in range(0, len(paths), 10):
    batch = paths[index : index + 10]
    try:
        result = ingest_paths(batch, DATASET)
        print(f"  batch {index // 10 + 1}: {result.get('documents', 0)} new docs")
    except RuntimeError as exc:
        print(f"  batch {index // 10 + 1} failed ({exc}); trying files individually ...")
        for path in batch:
            try:
                result = ingest_paths([path], DATASET)
                print(f"    {path.name}: {result.get('documents', 0)} new docs")
            except RuntimeError as file_exc:
                print(f"    SKIP {path.name}: {file_exc}")
print("Done.")
