"""Build Eve production output only when authored inputs are newer."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AGENT_ROOT = ROOT / "agents" / "empire-task-agent"
OUTPUT = AGENT_ROOT / ".output" / "server" / "index.mjs"
BUILD_TIMEOUT_SECONDS = 300
PACKAGE_INPUTS = ("package.json", "package-lock.json", "tsconfig.json")


def collect_inputs(agent_root: Path) -> list[Path]:
    inputs = [
        path
        for path in (agent_root / "agent").rglob("*")
        if path.is_file()
    ]
    inputs.extend(
        path
        for name in PACKAGE_INPUTS
        if (path := agent_root / name).is_file()
    )
    return sorted(inputs)


def build_required(output: Path, inputs: list[Path]) -> bool:
    if not output.is_file():
        return True
    output_mtime = output.stat().st_mtime
    return any(path.stat().st_mtime > output_mtime for path in inputs)


def main() -> int:
    inputs = collect_inputs(AGENT_ROOT)
    if not inputs:
        print("Eve build inputs are missing.", file=sys.stderr)
        return 1
    if not build_required(OUTPUT, inputs):
        print(f"Eve production build is current: {OUTPUT}")
        return 0
    npm = shutil.which("npm.cmd") or shutil.which("npm")
    if npm is None:
        print("npm is unavailable.", file=sys.stderr)
        return 1
    try:
        result = subprocess.run(
            [npm, "run", "build"],
            cwd=AGENT_ROOT,
            timeout=BUILD_TIMEOUT_SECONDS,
            check=False,
        )
    except subprocess.TimeoutExpired:
        print(
            f"Eve production build timed out after {BUILD_TIMEOUT_SECONDS}s.",
            file=sys.stderr,
        )
        return 1
    if result.returncode != 0:
        return result.returncode
    if not OUTPUT.is_file():
        print(f"Eve build completed without expected output: {OUTPUT}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
