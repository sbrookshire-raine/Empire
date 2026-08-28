import path from "node:path";
import { fileURLToPath } from "node:url";

const agentLibDir = path.dirname(fileURLToPath(import.meta.url));

/** Monorepo root (EMPIRE/). Override with EMPIRE_ROOT when deployed elsewhere. */
export const EMPIRE_ROOT =
  process.env.EMPIRE_ROOT ?? path.resolve(agentLibDir, "../../../..");

export const POCKETBASE_URL = (
  process.env.POCKETBASE_URL ?? "http://127.0.0.1:8090"
).replace(/\/$/, "");

export const PYTHON_BIN =
  process.env.EMPIRE_PYTHON ??
  path.join(EMPIRE_ROOT, "venv", "Scripts", "python.exe");
