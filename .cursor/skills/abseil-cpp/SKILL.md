---
name: abseil-cpp
description: Reference/integration skill for abseil/abseil-cpp, Google's C++17 library augmenting the standard library (containers, strings, Status/StatusOr error handling, hashing, synchronization, time, flags, logging). Use when a user is writing or extending C++ code (e.g. a native FastMCP tool binding or a performance-critical local component) and wants to add Abseil via Bazel/CMake, pick the right absl component, or look up what an absl module provides. Infra-agnostic — a C++ library reference with no dependency on Ollama/PocketBase/Cognee/FastMCP/HTMX-Alpine.
icon: box
color: Grey
---

# Abseil C++ (abseil/abseil-cpp)

Reference lookup + build-integration skill for Google's Abseil C++ common libraries. Treat this as a
"reference lookup" skill, not something to build/run directly in a lightweight sandbox — Bazel/CMake C++
builds are out of scope here.

## 1. Adding Abseil to a project
- **Bazel:** add Abseil as a dependency (e.g. `bazel_dep(name = "abseil-cpp", ...)` in `MODULE.bazel`/Bzlmod,
  or a WORKSPACE entry), then depend on specific `@abseil-cpp//absl/<module>` targets in `deps`.
- **CMake:** use `FetchContent`/`add_subdirectory(abseil-cpp)`, then
  `target_link_libraries(mytarget PRIVATE absl::<component>)`.
- Always resolve the exact target/library for the component needed (e.g. `absl::flat_hash_map`,
  `absl::status`) rather than linking the whole library blindly.

## 2. Component lookup
| User need | Abseil library | Path |
|---|---|---|
| Foundational init/base types | base | absl/base/ |
| STL-style algorithms | algorithm | absl/algorithm/ |
| Scope-exit / cleanup callback | cleanup (`absl::Cleanup`) | absl/cleanup/ |
| Fast hash-based containers ("Swiss tables") | container | absl/container/ |
| CRC / cyclic redundancy checks | crc | absl/crc/ |
| Leak checking, stack traces | debugging | absl/debugging/ |
| Command-line flags | flags | absl/flags/ |
| Hashing framework | hash | absl/hash/ |
| LOG/CHECK macros, structured logging | log | absl/log/ |
| Memory helpers | memory | absl/memory/ |
| Type traits | meta | absl/meta/ |
| 128-bit ints, bit-math backports | numeric | absl/numeric/ |
| Pseudorandom generation | random | absl/random/ |
| Error handling (`absl::Status`, `absl::StatusOr`) | status | absl/status/ |
| String utilities | strings | absl/strings/ |
| `absl::Mutex` and concurrency primitives | synchronization | absl/synchronization/ |
| Time points, durations, time zones | time | absl/time/ |
| Non-container utility types | types | absl/types/ |

## 3. Notes
- Abseil recommends "live at head" (track latest master); LTS releases exist for pinned versions.
- Apache-2.0 licensed.
- For a specific header/function question, fetch just that file from the repo's raw source rather than
  cloning the full repo — it is large and not meant to be built in a lightweight sandbox.
- Check the compatibility guidance before advising on API stability guarantees.

## Build1 Integration
Infra-agnostic. Only relevant if Build1 gains a native C++ component (e.g. a perf-critical extension called
from the FastMCP Python layer via bindings). It has no bearing on Ollama, PocketBase, Cognee, or the
HTMX/Alpine frontend.
