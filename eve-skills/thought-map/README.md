# thought-map 0.1.0

Analyze a supplied signed directed graph. Original standard-library-only implementation for a local thought-experiment layer.

## Offline installation
Requires an existing trusted Python >=3.10 with venv/ensurepip; tested environment appears in `docs/test-report.json`. No runtime dependency download is needed.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install --no-index --no-deps dist/thought_map-0.1.0-py3-none-any.whl
.venv/bin/thought-map --help
.venv/bin/thought-map run < examples/input.json
.venv/bin/python -m unittest discover -s tests -v
```

Windows PowerShell (untested): `py -m venv .venv`, then `.venv\Scripts\python.exe -m pip install --no-index --no-deps dist/thought_map-0.1.0-py3-none-any.whl` and `Get-Content -Raw examples/input.json | .venv\Scripts\thought-map.exe run`.

## CLI
`thought-map run` reads one UTF-8 JSON object from stdin. `thought-map schema` prints its input schema. `thought-map mcp` starts the MCP server. `--help` and `--version` are supported. No positional file inputs or output writes. Exit 0: success; 2: input/configuration/usage error; 1: internal error; 3: broken output pipe. Output is deterministic sorted-key JSON. Structured input/expected output live in `examples/`.

## MCP registration
Edit `mcp/config.example.json`: replace the interpreter path with the absolute path to your installed environment. Windows uses `.venv\Scripts\python.exe`. The MCP client must support legacy `2025-11-25` stdio. Tool name: `thought_map`. Modern-only MCP clients are not supported. No client-specific EVE integration was tested.

## Configuration and security
`LOCAL_SKILL_NETWORK=deny` (default). Other values fail clearly; network enablement is not supported. No config/data directory is created or required. No telemetry. See `docs/limitations-and-threat-model.md`.

## Build, integrity, uninstall
Online preparation is only needed to acquire a trusted Python installer and this bundle. Transfer the archive and trusted checksum separately. Check archive SHA-256 before extraction; then verify the wheel against `dist/SHA256SUMS` (`sha256sum -c SHA256SUMS` from dist on Linux). Python itself is not bundled or checksum-pinned here.

Rebuild offline: `python scripts/build.py`. The original PEP 517 backend needs no build dependencies. Wheel bytes are reproducible for identical source inputs. Uninstall: `.venv/bin/python -m pip uninstall -y thought-map`. Deleting an environment is a user action, not performed by runtime code.

## Scope
No causal discovery or numeric dynamics. Structural feedback does not establish causation or stability.

MIT license; see LICENSE and NOTICE. `skill.yaml` is JSON syntax, valid YAML 1.2. Its checksum addresses the wheel, avoiding a self-referential archive hash; archive hashes are detached in the collection. No third-party code or datasets are redistributed.
