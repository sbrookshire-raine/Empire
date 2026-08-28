"""CLI for Eve agent subprocess calls (inventory + active model)."""

from __future__ import annotations

import argparse
import json
import sys

from frontend.ollama_api import (
    OllamaConnectionError,
    OllamaRequestError,
    fetch_tags,
    models_status,
    set_active_model,
)
from frontend.ollama_inventory import build_inventory


def _print_json(payload: dict) -> int:
    sys.stdout.write(json.dumps(payload, indent=2, default=str) + "\n")
    return 0


def cmd_inventory() -> int:
    try:
        tags = fetch_tags()
    except OllamaConnectionError as exc:
        return _print_json({"ok": False, "connected": False, "error": str(exc)})
    return _print_json(build_inventory(tags))


def cmd_models() -> int:
    try:
        tags = fetch_tags()
    except OllamaConnectionError as exc:
        return _print_json({"ok": False, "connected": False, "error": str(exc)})
    return _print_json(models_status(tags, connected=True))


def cmd_set_active(model: str) -> int:
    try:
        tags = fetch_tags()
        payload = set_active_model(model, tags)
    except OllamaConnectionError as exc:
        return _print_json({"ok": False, "connected": False, "error": str(exc)})
    except OllamaRequestError as exc:
        return _print_json({"ok": False, "error": str(exc), "status": exc.status})
    return _print_json({"ok": True, **payload})


def main() -> int:
    parser = argparse.ArgumentParser(description="Ollama inventory CLI for Eve tools")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("inventory", help="Full model suite analysis JSON")
    sub.add_parser("models", help="Chat model list + active model")

    active = sub.add_parser("set-active", help="Set Eve chat model")
    active.add_argument("model", help="Ollama model id")

    args = parser.parse_args()
    if args.command == "inventory":
        return cmd_inventory()
    if args.command == "models":
        return cmd_models()
    if args.command == "set-active":
        return cmd_set_active(args.model)
    raise ValueError(f"Unknown command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
