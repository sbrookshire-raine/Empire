#!/usr/bin/env python3
"""Build small source-derived fixtures for the target-free REA readers.

Creates a SQLite database, a WASM module, an EVM bytecode carrier, and a Go
and Rust source tree, so each reader can be exercised against content whose
expected shape is known.

Usage:
  python3 build_fixtures.py --out /tmp/rea-fixtures
  python3 build_fixtures.py --out /tmp/rea-fixtures --json

Exit codes: 0 built, 2 usage error.
"""
import argparse
import json
import os
import sqlite3
import sys

WAT = """(module
  (func $add (param i32 i32) (result i32)
    local.get 0
    local.get 1
    i32.add)
  (export "add" (func $add))
  (memory (export "mem") 1)
)
"""

# Minimal EVM runtime with two dispatch selectors.
EVM_HEX = ("6080604052348015600f57600080fd5b506004361060285760003560e01c8063"
           "2e64cec114602d5780636057361d146033575b600080fd5b60336047565b005b"
           "6039604d565b005b60005481565b600080fd")

GO_SRC = '''package main

import (
\t"fmt"
\t"strings"
)

func Greet(n string) string { return "Hello, " + strings.ToUpper(n) }

func main() { fmt.Println(Greet("world")) }
'''

RUST_SRC = '''fn greet(n: &str) -> String { format!("Hello, {}", n) }

fn main() { println!("{}", greet("world")); }
'''


def build(out):
    os.makedirs(out, exist_ok=True)
    made = {}

    # SQLite
    db = os.path.join(out, "test.db")
    if os.path.exists(db):
        os.remove(db)
    con = sqlite3.connect(db)
    con.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, "
                "name TEXT NOT NULL, email TEXT)")
    con.execute("CREATE INDEX idx_name ON users(name)")
    con.execute("INSERT INTO users (name,email) VALUES "
                "('alice','a@x.com'),('bob','b@x.com')")
    con.commit()
    con.close()
    made["sqlite"] = {"path": db, "tables": ["users"], "indexes": ["idx_name"],
                      "rows": 2}

    # WASM source (compile with wat2wasm)
    wat = os.path.join(out, "module.wat")
    with open(wat, "w") as f:
        f.write(WAT)
    made["wasm"] = {"wat": wat, "exports": ["add", "mem"],
                    "compile": f"wat2wasm {wat} -o {out}/module.wasm"}

    # EVM bytecode carrier
    evm = os.path.join(out, "bytecode.hex")
    with open(evm, "w") as f:
        f.write(EVM_HEX)
    made["evm"] = {"path": evm, "encoding": "hex",
                   "expected_selectors": ["0x2e64cec1", "0x6057361d"]}

    # Go source tree
    godir = os.path.join(out, "gotest")
    os.makedirs(godir, exist_ok=True)
    with open(os.path.join(godir, "main.go"), "w") as f:
        f.write(GO_SRC)
    made["go"] = {"dir": godir,
                  "build": f"cd {godir} && go mod init gotest && "
                           f"go build -o {godir}/gotest ."}

    # Rust source tree
    rustdir = os.path.join(out, "rusttest")
    os.makedirs(os.path.join(rustdir, "src"), exist_ok=True)
    with open(os.path.join(rustdir, "Cargo.toml"), "w") as f:
        f.write('[package]\nname = "rusttest"\nversion = "0.1.0"\n'
                'edition = "2021"\n')
    with open(os.path.join(rustdir, "src", "main.rs"), "w") as f:
        f.write(RUST_SRC)
    made["rust"] = {"dir": rustdir,
                    "build": f"cd {rustdir} && cargo build --release"}

    return made


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    made = build(args.out)
    if args.json:
        print(json.dumps(made, indent=2))
    else:
        print(f"fixtures written to {args.out}")
        for kind, info in made.items():
            print(f"\n{kind}:")
            for k, v in info.items():
                print(f"  {k}: {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
