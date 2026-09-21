"""topology_audit: dependency-graph outage propagation and cycle detection.

Original generated implementation. License: MIT.
Edge source depends_on target. Outage of a node reaches transitive dependents.
"""
from __future__ import annotations

SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "topology_audit_input",
    "type": "object",
    "additionalProperties": False,
    "required": ["nodes", "edges", "outage"],
    "properties": {
        "nodes": {
            "type": "array",
            "minItems": 1,
            "maxItems": 64,
            "items": {"type": "string", "minLength": 1, "maxLength": 64},
        },
        "edges": {
            "type": "array",
            "minItems": 0,
            "maxItems": 256,
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["source", "target"],
                "properties": {
                    "source": {"type": "string", "minLength": 1, "maxLength": 64},
                    "target": {"type": "string", "minLength": 1, "maxLength": 64},
                },
            },
        },
        "outage": {"type": "string", "minLength": 1, "maxLength": 64},
    },
}

MAX_NODES = 64
MAX_EDGES = 256
MAX_NAME = 64

SAMPLE = {
    "nodes": ["app", "api", "db"],
    "edges": [
        {"source": "app", "target": "api"},
        {"source": "api", "target": "db"},
    ],
    "outage": "db",
}

EXPECTED = {
    "n_nodes": 3,
    "n_edges": 2,
    "outage": "db",
    "affected": ["api", "app", "db"],
    "n_affected": 3,
    "unaffected": [],
    "has_cycle": False,
    "cyclic_components": [],
    "strongly_connected_components": [["api"], ["app"], ["db"]],
    "n_scc": 3,
}


def _err(msg: str) -> None:
    raise ValueError(msg)


def _require_dict(data: object, label: str) -> dict:
    if type(data) is not dict:
        _err("%s must be an object" % label)
    return data


def _require_str(value: object, label: str) -> str:
    if type(value) is not str:
        _err("%s must be a string" % label)
    if not value or len(value) > MAX_NAME or value != value.strip():
        _err("%s must be a non-empty trimmed string of length 1..%d" % (label, MAX_NAME))
    return value


def _validate(data: object) -> tuple:
    obj = _require_dict(data, "input")
    extra = set(obj) - {"nodes", "edges", "outage"}
    if extra:
        _err("unknown keys: %s" % ", ".join(sorted(extra)))
    for key in ("nodes", "edges", "outage"):
        if key not in obj:
            _err("%s is required" % key)
    nodes_raw = obj["nodes"]
    edges_raw = obj["edges"]
    if type(nodes_raw) is not list:
        _err("nodes must be an array")
    if type(edges_raw) is not list:
        _err("edges must be an array")
    if not nodes_raw:
        _err("nodes must be non-empty")
    if len(nodes_raw) > MAX_NODES:
        _err("at most %d nodes" % MAX_NODES)
    if len(edges_raw) > MAX_EDGES:
        _err("at most %d edges" % MAX_EDGES)
    nodes = []
    seen = set()
    for i, item in enumerate(nodes_raw):
        name = _require_str(item, "nodes[%d]" % i)
        if name in seen:
            _err("duplicate node %s" % name)
        seen.add(name)
        nodes.append(name)
    node_set = set(nodes)
    outage = _require_str(obj["outage"], "outage")
    if outage not in node_set:
        _err("outage must be a declared node")
    edges = []
    pair_seen = set()
    for i, item in enumerate(edges_raw):
        edge = _require_dict(item, "edges[%d]" % i)
        extra_e = set(edge) - {"source", "target"}
        if extra_e:
            _err("unknown keys in edges[%d]: %s" % (i, ", ".join(sorted(extra_e))))
        if "source" not in edge or "target" not in edge:
            _err("edges[%d] requires source, target" % i)
        src = _require_str(edge["source"], "edges[%d].source" % i)
        tgt = _require_str(edge["target"], "edges[%d].target" % i)
        if src not in node_set or tgt not in node_set:
            _err("edges[%d] references unknown node" % i)
        pair = (src, tgt)
        if pair in pair_seen:
            _err("duplicate edge %s -> %s" % (src, tgt))
        pair_seen.add(pair)
        edges.append((src, tgt))
    return nodes, edges, outage


def _scc(nodes: list, edges: list) -> list:
    adj = {n: [] for n in nodes}
    radj = {n: [] for n in nodes}
    for src, tgt in edges:
        adj[src].append(tgt)
        radj[tgt].append(src)
    visited = set()
    order = []

    def dfs1(u: str) -> None:
        visited.add(u)
        for v in adj[u]:
            if v not in visited:
                dfs1(v)
        order.append(u)

    for n in nodes:
        if n not in visited:
            dfs1(n)
    visited.clear()
    components = []

    def dfs2(u: str, bucket: list) -> None:
        visited.add(u)
        bucket.append(u)
        for v in radj[u]:
            if v not in visited:
                dfs2(v, bucket)

    for u in reversed(order):
        if u not in visited:
            bucket = []
            dfs2(u, bucket)
            bucket.sort()
            components.append(bucket)
    components.sort(key=lambda c: (c[0], len(c), c))
    return components


def _affected(nodes: list, edges: list, outage: str) -> list:
    dependents = {n: [] for n in nodes}
    for src, tgt in edges:
        dependents[tgt].append(src)
    seen = set()
    stack = [outage]
    while stack:
        u = stack.pop()
        if u in seen:
            continue
        seen.add(u)
        for v in dependents[u]:
            if v not in seen:
                stack.append(v)
    return sorted(seen)


def run(data):
    nodes, edges, outage = _validate(data)
    components = _scc(nodes, edges)
    self_loop_nodes = {src for src, tgt in edges if src == tgt}
    cyclic = [c for c in components if len(c) > 1 or (len(c) == 1 and c[0] in self_loop_nodes)]
    affected = _affected(nodes, edges, outage)
    affected_set = set(affected)
    unaffected = [n for n in nodes if n not in affected_set]
    return {
        "n_nodes": len(nodes),
        "n_edges": len(edges),
        "outage": outage,
        "affected": affected,
        "n_affected": len(affected),
        "unaffected": unaffected,
        "has_cycle": bool(cyclic),
        "cyclic_components": cyclic,
        "strongly_connected_components": components,
        "n_scc": len(components),
    }
