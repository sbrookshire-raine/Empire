from pathlib import Path

root = Path(r"C:\Empire_Workbench\03_Active_Tools")
for item in sorted(root.iterdir()):
    print(f"{'[dir]' if item.is_dir() else '[file]'} {item.name}")
