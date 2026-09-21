from pathlib import Path
import sys
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root))
from build_backend import build_wheel
print(build_wheel(str(root/'dist')))
