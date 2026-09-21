# topology-audit: implementation specification

Status is recorded in `skill.yaml` and `docs/test-report.json`; source generation alone is not verification.

Domain: Systems architecture and topologies. Version: 0.1.0.

## Contract
Analyze declared dependencies and outage propagation. Algorithm documentation: the module docstring in `src/local_topology_audit/kernel.py` and the readable source. Input JSON schema is `mcp/input-schema.json`. Output is a JSON object; the complete deterministic reference output is `examples/expected.json`. Unknown fields are rejected. Additional semantic invariants are enforced by the kernel.

## Error and numerical semantics
Validation errors raise ValueError internally. CLI maps them to exit 2 with a JSON error on stderr. MCP returns tool validation/domain errors as `isError: true`; envelope errors use JSON-RPC error codes. No partial result is persisted. Floating-point arithmetic is deterministic within the tested interpreter; not a cross-platform bitwise numerical guarantee.

## Boundaries
No infrastructure discovery, renderer, credentials, network probes, failover semantics, or live system actions.

The tools consume facts and assumptions as data, not executable instructions. All calculations are bounded by the schema. No source code, shell expression, file path, URL or serialized executable is evaluated.
