"""graph_map: structural analysis of an explicitly supplied signed directed graph.

Original generated implementation. License: MIT.
No causal discovery, no dynamics, no cycle enumeration, no network I/O.
"""
from __future__ import annotations

SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "graph_map_input",
    "type": "object",
    "additionalProperties": False,
    "required": ["nodes", "edges"],
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
                "required": ["source", "target", "sign"],
                "properties": {
                    "source": {"type": "string", "minLength": 1, "maxLength": 64},
                    "target": {"type": "string", "minLength": 1, "maxLength": 64},
                    "sign": {"type": "integer", "enum": [-1, 1]},
                },
            },
        },
    },
}

MAX_NODES = 64
MAX_EDGES = 256
MAX_NAME = 64

SAMPLE = {
    "nodes": ["A", "B", "C"],
    "edges": [
        {"source": "A", "target": "B", "sign": 1},
        {"source": "B", "target": "C", "sign": 1},
        {"source": "C", "target": "A", "sign": -1},
        {"source": "A", "target": "A", "sign": 1},
    ],
}

EXPECTED = {
    "n_nodes": 3,
    "n_edges": 4,
    "degrees": [
        {"node": "A", "in_degree": 2, "out_degree": 2},
        {"node": "B", "in_degree": 1, "out_degree": 1},
        {"node": "C", "in_degree": 1, "out_degree": 1},
    ],
    "self_loops": [{"node": "A", "sign": 1, "polarity": "reinforcing"}],
    "strongly_connected_components": [["A", "B", "C"]],
    "n_scc": 1,
    "has_cycle": True,
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


def _require_sign(value: object, label: str) -> int:
    if type(value) is not int:
        _err("%s must be integer -1 or 1" % label)
    if value not in (-1, 1):
        _err("%s must be integer -1 or 1" % label)
    return value


def _validate(data: object) -> tuple:
    obj = _require_dict(data, "input")
    extra = set(obj) - {"nodes", "edges"}
    if extra:
        _err("unknown keys: %s" % ", ".join(sorted(extra)))
    if "nodes" not in obj or "edges" not in obj:
        _err("nodes and edges are required")
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
    edges = []
    pair_seen = set()
    for i, item in enumerate(edges_raw):
        edge = _require_dict(item, "edges[%d]" % i)
        extra_e = set(edge) - {"source", "target", "sign"}
        if extra_e:
            _err("unknown keys in edges[%d]: %s" % (i, ", ".join(sorted(extra_e))))
        if "source" not in edge or "target" not in edge or "sign" not in edge:
            _err("edges[%d] requires source, target, sign" % i)
        src = _require_str(edge["source"], "edges[%d].source" % i)
        tgt = _require_str(edge["target"], "edges[%d].target" % i)
        sign = _require_sign(edge["sign"], "edges[%d].sign" % i)
        if src not in node_set or tgt not in node_set:
            _err("edges[%d] references unknown node" % i)
        pair = (src, tgt)
        if pair in pair_seen:
            _err("duplicate edge %s -> %s" % (src, tgt))
        pair_seen.add(pair)
        edges.append((src, tgt, sign))
    return nodes, edges


def _scc(nodes: list, edges: list) -> list:
    adj = {n: [] for n in nodes}
    radj = {n: [] for n in nodes}
    for src, tgt, _sign in edges:
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


def run(data):
    nodes, edges = _validate(data)
    in_deg = {n: 0 for n in nodes}
    out_deg = {n: 0 for n in nodes}
    self_loops = []
    for src, tgt, sign in edges:
        out_deg[src] += 1
        in_deg[tgt] += 1
        if src == tgt:
            polarity = "reinforcing" if sign == 1 else "balancing"
            self_loops.append({"node": src, "sign": sign, "polarity": polarity})
    self_loops.sort(key=lambda x: x["node"])
    components = _scc(nodes, edges)
    has_cycle = any(len(c) > 1 for c in components) or bool(self_loops)
    return {
        "n_nodes": len(nodes),
        "n_edges": len(edges),
        "degrees": [
            {"node": n, "in_degree": in_deg[n], "out_degree": out_deg[n]}
            for n in nodes
        ],
        "self_loops": self_loops,
        "strongly_connected_components": components,
        "n_scc": len(components),
        "has_cycle": has_cycle,
    }
