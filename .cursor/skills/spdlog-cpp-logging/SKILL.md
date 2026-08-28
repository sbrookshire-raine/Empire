---
name: spdlog-cpp-logging
description: Explains how to integrate and use spdlog, a fast C++ logging library, including header-only vs compiled setup, sinks (console, rotating file, daily file, syslog), log level/pattern configuration, and fmt-style formatting. Use when a user is writing or debugging C++ code that needs logging or wants a spdlog snippet. Infra-agnostic — C++ tooling unrelated to Build1's Python/Ollama/PocketBase/Cognee/FastMCP/HTMX stack; relevant only if the user builds a native C++ component alongside Build1.
icon: file-text
color: Bronze
---

# spdlog C++ Logging Integration

spdlog (gabime/spdlog) is a fast, header-only-or-compiled C++ logging library using `fmt`-style formatting. This is a library the user compiles into their own C++ project — an agent cannot compile/run C++ directly, so this skill only produces setup and usage snippets for the user's own build.

## Setup options

1. **Header-only** (simplest, slower to compile across many translation units): copy the `include/spdlog` folder into the project's include path, C++11+. No linking step.
2. **Compiled** (faster rebuilds in larger projects):
   ```bash
   git clone https://github.com/gabime/spdlog.git
   cd spdlog && mkdir build && cd build
   cmake .. && cmake --build .
   ```
   Link against the built library and `#define SPDLOG_COMPILED_LIB` before including headers.
3. **Package managers**:
   - `apt install libspdlog-dev` (Debian/Ubuntu)
   - `brew install spdlog` (macOS)
   - `vcpkg install spdlog`
   - `conan install --requires=spdlog/[*]`
   - `conda install -c conda-forge spdlog`
   - `pacman -S spdlog` (Arch) / `dnf install spdlog` (Fedora)

## Core usage snippets

**Basic global logger:**
```cpp
#include "spdlog/spdlog.h"

int main() {
    spdlog::info("Welcome to spdlog!");
    spdlog::warn("Easy padding in numbers like {:08d}", 12);
    spdlog::error("Some error with arg: {}", 1);
    spdlog::set_level(spdlog::level::debug);
    spdlog::debug("This message should be displayed..");
}
```

**Rotating file sink:**
```cpp
#include "spdlog/sinks/rotating_file_sink.h"

auto logger = spdlog::rotating_logger_mt("file_logger", "logs/app.log",
                                          1048576 * 5, 3); // 5MB x 3 files
logger->info("log message #{}", 1);
```

**Daily file sink:**
```cpp
#include "spdlog/sinks/daily_file_sink.h"
auto logger = spdlog::daily_logger_mt("daily_logger", "logs/daily.txt", 2, 30);
```

**Custom pattern:**
```cpp
spdlog::set_pattern("[%H:%M:%S %z] [%n] [%^%l%$] %v");
```

**Multi-sink logger:**
```cpp
#include "spdlog/sinks/stdout_color_sinks.h"
#include "spdlog/sinks/basic_file_sink.h"

auto console_sink = std::make_shared<spdlog::sinks::stdout_color_sink_mt>();
auto file_sink = std::make_shared<spdlog::sinks::basic_file_sink_mt>("logs/multi.log");
spdlog::logger logger("multi_sink", {console_sink, file_sink});
logger.info("message to both console and file");
```

## Build1 Integration

No direct dependency on Ollama/PocketBase/Cognee/FastMCP/HTMX — spdlog is pure C++ tooling. If a native C++ helper process is built alongside Build1 (e.g. a custom transport bridge or a performance-critical extension), configure its spdlog sinks to write to local files rather than any cloud log aggregation service, consistent with Build1's zero-cloud policy. Rotate logs locally (rotating/daily sinks above) rather than shipping them off-box.
