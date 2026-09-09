"""LEGO whiteboard API — brick catalog, board JSON, Toolbelt apply."""

from __future__ import annotations

import json
import os
import uuid
from pathlib import Path
from typing import Any

try:
    from frontend import eve_toolbelt
except ModuleNotFoundError:
    import eve_toolbelt  # type: ignore[no-redef]

ROOT = Path(__file__).resolve().parents[1]
BRICKS_PATH = ROOT / "config" / "lego-bricks.json"
RECIPES_PATH = ROOT / "config" / "lego-recipes.json"
WORKBENCH = Path(
    os.environ.get("EMPIRE_WORKBENCH", r"C:\Empire_Workbench")
).resolve()
BOARD_DIR = WORKBENCH / "03_Active_Tools" / "lego_boards"
DEFAULT_BOARD = BOARD_DIR / "default.json"

EMPTY_BOARD: dict[str, Any] = {
    "schema_version": 1,
    "nodes": [],
    "edges": [],
    "viewport": {"x": 0, "y": 0, "zoom": 1},
}


def _empire_root() -> Path:
    return ROOT


def load_bricks() -> dict[str, Any]:
    try:
        raw = BRICKS_PATH.read_text(encoding="utf-8")
        data = json.loads(raw)
    except (OSError, json.JSONDecodeError) as exc:
        return {"ok": False, "error": f"Cannot read brick catalog: {exc}", "bricks": []}
    bricks = data.get("bricks") if isinstance(data, dict) else None
    if not isinstance(bricks, list):
        return {"ok": False, "error": "Brick catalog missing bricks[]", "bricks": []}
    return {
        "ok": True,
        "schema_version": data.get("schema_version", 1),
        "bricks": bricks,
        "path": str(BRICKS_PATH),
    }


def load_recipes() -> dict[str, Any]:
    try:
        raw = RECIPES_PATH.read_text(encoding="utf-8")
        data = json.loads(raw)
    except (OSError, json.JSONDecodeError) as exc:
        return {"ok": False, "error": f"Cannot read recipes: {exc}", "recipes": []}
    recipes = data.get("recipes") if isinstance(data, dict) else None
    if not isinstance(recipes, list):
        return {"ok": False, "error": "Recipes file missing recipes[]", "recipes": []}
    public = []
    for recipe in recipes:
        if not isinstance(recipe, dict):
            continue
        rid = str(recipe.get("id") or "").strip()
        if not rid:
            continue
        public.append(
            {
                "id": rid,
                "label": str(recipe.get("label") or rid),
                "description": str(recipe.get("description") or ""),
            }
        )
    return {
        "ok": True,
        "schema_version": data.get("schema_version", 1),
        "recipes": public,
        "path": str(RECIPES_PATH),
    }


def _brick_by_id(bricks: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for brick in bricks:
        if isinstance(brick, dict) and isinstance(brick.get("id"), str):
            out[brick["id"]] = brick
    return out


def _ports(brick: dict[str, Any], side: str) -> list[str]:
    ports = brick.get("ports")
    if not isinstance(ports, dict):
        return []
    raw = ports.get(side)
    if not isinstance(raw, list):
        return []
    return [str(item).strip() for item in raw if str(item).strip()]


def _new_node_id() -> str:
    return "n_" + uuid.uuid4().hex[:10]


def _new_edge_id() -> str:
    return "e_" + uuid.uuid4().hex[:10]


def instantiate_recipe(recipe_id: str) -> dict[str, Any]:
    catalog = load_bricks()
    if not catalog.get("ok"):
        return catalog
    by_id = _brick_by_id(catalog["bricks"])

    try:
        raw = json.loads(RECIPES_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {"ok": False, "error": f"Cannot read recipes: {exc}"}

    recipes = raw.get("recipes") if isinstance(raw, dict) else None
    if not isinstance(recipes, list):
        return {"ok": False, "error": "Recipes file missing recipes[]"}

    recipe = next(
        (item for item in recipes if isinstance(item, dict) and item.get("id") == recipe_id),
        None,
    )
    if recipe is None:
        return {"ok": False, "error": f"Unknown recipe: {recipe_id}"}

    template_nodes = recipe.get("nodes")
    template_edges = recipe.get("edges")
    if not isinstance(template_nodes, list):
        return {"ok": False, "error": "Recipe nodes must be a list"}

    nodes: list[dict[str, Any]] = []
    id_map: list[str] = []
    for template in template_nodes:
        if not isinstance(template, dict):
            return {"ok": False, "error": "Recipe node must be an object"}
        brick = str(template.get("brick") or "").strip()
        if brick not in by_id:
            return {"ok": False, "error": f"Recipe references unknown brick: {brick}"}
        node_id = _new_node_id()
        id_map.append(node_id)
        nodes.append(
            {
                "id": node_id,
                "brick": brick,
                "x": int(template.get("x") or 0),
                "y": int(template.get("y") or 0),
                "enabled": bool(template.get("enabled", True)),
            }
        )

    edges: list[dict[str, Any]] = []
    if isinstance(template_edges, list):
        for template in template_edges:
            if not isinstance(template, dict):
                continue
            try:
                from_index = int(template.get("from_index"))
                to_index = int(template.get("to_index"))
            except (TypeError, ValueError):
                continue
            if not (0 <= from_index < len(id_map) and 0 <= to_index < len(id_map)):
                continue
            kind = str(template.get("kind") or "scratch").strip() or "scratch"
            edges.append(
                {
                    "id": _new_edge_id(),
                    "from": id_map[from_index],
                    "to": id_map[to_index],
                    "kind": kind,
                }
            )

    board = {
        "schema_version": 1,
        "nodes": nodes,
        "edges": edges,
        "viewport": {"x": 40, "y": 40, "zoom": 1},
        "recipe_id": recipe_id,
        "recipe_label": str(recipe.get("label") or recipe_id),
    }
    return {
        "ok": True,
        "recipe_id": recipe_id,
        "board": board,
        "note": "Recipe loaded — Save then Apply to Toolbelt when ready.",
    }


def validate_board(payload: dict[str, Any] | None = None) -> dict[str, Any]:
    catalog = load_bricks()
    if not catalog.get("ok"):
        return catalog
    by_id = _brick_by_id(catalog["bricks"])

    if payload and isinstance(payload.get("nodes"), list):
        nodes = payload["nodes"]
        edges = payload.get("edges") if isinstance(payload.get("edges"), list) else []
    else:
        loaded = load_board()
        if not loaded.get("ok"):
            return loaded
        nodes = loaded["board"]["nodes"]
        edges = loaded["board"]["edges"]

    issues: list[dict[str, str]] = []
    node_ids = set()
    for node in nodes:
        if not isinstance(node, dict):
            issues.append({"level": "error", "message": "Node is not an object"})
            continue
        node_id = str(node.get("id") or "").strip()
        brick_id = str(node.get("brick") or "").strip()
        if node_id:
            node_ids.add(node_id)
        if not brick_id:
            issues.append({"level": "error", "message": f"Node {node_id or '?'} missing brick id"})
            continue
        if brick_id not in by_id:
            issues.append(
                {
                    "level": "error",
                    "message": f"Unknown brick '{brick_id}' on node {node_id or '?'}",
                }
            )

    for edge in edges:
        if not isinstance(edge, dict):
            issues.append({"level": "error", "message": "Edge is not an object"})
            continue
        edge_id = str(edge.get("id") or "?")
        from_id = str(edge.get("from") or "").strip()
        to_id = str(edge.get("to") or "").strip()
        kind = str(edge.get("kind") or "scratch").strip() or "scratch"
        if from_id not in node_ids or to_id not in node_ids:
            issues.append(
                {
                    "level": "error",
                    "message": f"Edge {edge_id} references missing node(s)",
                }
            )
            continue
        from_node = next((n for n in nodes if isinstance(n, dict) and n.get("id") == from_id), None)
        to_node = next((n for n in nodes if isinstance(n, dict) and n.get("id") == to_id), None)
        if not from_node or not to_node:
            continue
        from_brick = by_id.get(str(from_node.get("brick") or ""))
        to_brick = by_id.get(str(to_node.get("brick") or ""))
        if not from_brick or not to_brick:
            continue
        out_ports = _ports(from_brick, "out")
        in_ports = _ports(to_brick, "in")
        if kind not in out_ports:
            issues.append(
                {
                    "level": "warn",
                    "message": (
                        f"Edge {edge_id}: {from_brick.get('label')} out ports "
                        f"{out_ports} may not include '{kind}'"
                    ),
                }
            )
        if kind not in in_ports:
            issues.append(
                {
                    "level": "warn",
                    "message": (
                        f"Edge {edge_id}: {to_brick.get('label')} in ports "
                        f"{in_ports} may not include '{kind}'"
                    ),
                }
            )

    enabled_optional = 0
    for node in nodes:
        if not isinstance(node, dict) or not bool(node.get("enabled", True)):
            continue
        meta = by_id.get(str(node.get("brick") or ""))
        if meta and meta.get("toolbelt"):
            enabled_optional += 1

    ok = not any(item["level"] == "error" for item in issues)
    return {
        "ok": ok,
        "issues": issues,
        "node_count": len(nodes),
        "edge_count": len(edges),
        "enabled_optional_limbs": enabled_optional,
        "note": "Warnings are port hints; edges still save. Errors block Apply.",
    }


def load_board() -> dict[str, Any]:
    try:
        if not DEFAULT_BOARD.exists():
            return {
                "ok": True,
                "board": dict(EMPTY_BOARD),
                "path": str(DEFAULT_BOARD),
                "exists": False,
            }
        data = json.loads(DEFAULT_BOARD.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            return {"ok": False, "error": "Board file is not an object"}
        board = {
            "schema_version": int(data.get("schema_version") or 1),
            "nodes": data.get("nodes") if isinstance(data.get("nodes"), list) else [],
            "edges": data.get("edges") if isinstance(data.get("edges"), list) else [],
            "viewport": data.get("viewport")
            if isinstance(data.get("viewport"), dict)
            else {"x": 0, "y": 0, "zoom": 1},
        }
        if isinstance(data.get("recipe_id"), str):
            board["recipe_id"] = data["recipe_id"]
        if isinstance(data.get("recipe_label"), str):
            board["recipe_label"] = data["recipe_label"]
        return {
            "ok": True,
            "board": board,
            "path": str(DEFAULT_BOARD),
            "exists": True,
        }
    except (OSError, json.JSONDecodeError) as exc:
        return {"ok": False, "error": f"Cannot read board: {exc}"}


def save_board(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict):
        return {"ok": False, "error": "Expected JSON object"}
    board = {
        "schema_version": 1,
        "nodes": payload.get("nodes") if isinstance(payload.get("nodes"), list) else [],
        "edges": payload.get("edges") if isinstance(payload.get("edges"), list) else [],
        "viewport": payload.get("viewport")
        if isinstance(payload.get("viewport"), dict)
        else {"x": 0, "y": 0, "zoom": 1},
    }
    for key in ("recipe_id", "recipe_label"):
        if isinstance(payload.get(key), str) and payload.get(key):
            board[key] = payload[key]
    try:
        BOARD_DIR.mkdir(parents=True, exist_ok=True)
        DEFAULT_BOARD.write_text(
            json.dumps(board, indent=2) + "\n", encoding="utf-8"
        )
    except OSError as exc:
        return {"ok": False, "error": f"Cannot write board: {exc}"}
    return {"ok": True, "board": board, "path": str(DEFAULT_BOARD)}


def apply_toolbelt_from_board(payload: dict[str, Any] | None = None) -> dict[str, Any]:
    """Enable Toolbelt categories for enabled optional bricks on the board."""
    catalog = load_bricks()
    if not catalog.get("ok"):
        return catalog
    by_id = _brick_by_id(catalog["bricks"])

    merge = bool((payload or {}).get("merge"))

    if payload and isinstance(payload.get("nodes"), list):
        nodes = payload["nodes"]
    else:
        loaded = load_board()
        if not loaded.get("ok"):
            return loaded
        nodes = loaded["board"]["nodes"]

    validation = validate_board({"nodes": nodes, "edges": (payload or {}).get("edges") or []})
    if not validation.get("ok"):
        return {
            "ok": False,
            "error": "Board validation failed — fix errors before Apply.",
            "issues": validation.get("issues") or [],
        }

    selected: list[str] = []
    enabled_bricks: list[str] = []
    for node in nodes:
        if not isinstance(node, dict):
            continue
        brick_id = str(node.get("brick") or "").strip()
        enabled = bool(node.get("enabled", True))
        if not enabled or not brick_id:
            continue
        meta = by_id.get(brick_id)
        if not meta:
            continue
        enabled_bricks.append(brick_id)
        toolbelt = meta.get("toolbelt")
        if isinstance(toolbelt, str) and toolbelt.strip():
            cat = toolbelt.strip()
            if cat in eve_toolbelt.ALLOWED_CATEGORIES and cat not in selected:
                selected.append(cat)

    if merge:
        existing = eve_toolbelt.load_active_tools()
        for cat in existing:
            if cat not in selected:
                selected.append(cat)

    path = eve_toolbelt.write_active_tools(selected)
    return {
        "ok": True,
        "active_tools": selected,
        "enabled_bricks": enabled_bricks,
        "toolbelt_path": str(path),
        "merge": merge,
        "note": "Core bricks (memory/tasks/docling/gpu) stay available without Toolbelt.",
    }
