import fs from "node:fs/promises";
import path from "node:path";

/** Allowed read roots for Empire Workbench (Gemini Step 1 scope). */
export const WORKBENCH_ROOTS = [
  "C:/Empire_Workbench/01_Memory_Bank",
  "C:/Empire_Workbench/02_Skills_and_Prompts",
  "C:/Empire_Workbench/03_Active_Tools",
] as const;

const MAX_READ_BYTES = 512 * 1024;

function normalize(p: string): string {
  return path.resolve(p.replace(/\//g, path.sep));
}

export function resolveWorkbenchPath(requested: string): string {
  const resolved = normalize(requested);
  const allowed = WORKBENCH_ROOTS.some((root) => {
    const rootResolved = normalize(root);
    return resolved === rootResolved || resolved.startsWith(rootResolved + path.sep);
  });
  if (!allowed) {
    throw new Error(
      "Path must be under 01_Memory_Bank, 02_Skills_and_Prompts, or 03_Active_Tools.",
    );
  }
  return resolved;
}

export async function listWorkbenchDir(dirPath: string): Promise<{
  path: string;
  entries: Array<{ name: string; type: "file" | "directory" }>;
}> {
  const resolved = resolveWorkbenchPath(dirPath);
  const entries = await fs.readdir(resolved, { withFileTypes: true });
  return {
    path: resolved,
    entries: entries
      .filter((e) => !e.name.startsWith("."))
      .map((e) => ({
        name: e.name,
        type: (e.isDirectory() ? "directory" : "file") as "directory" | "file",
      }))
      .sort((a, b) => a.name.localeCompare(b.name)),
  };
}

export async function readWorkbenchFile(
  filePath: string,
  maxBytes = MAX_READ_BYTES,
): Promise<{
  path: string;
  sizeBytes: number;
  truncated: boolean;
  content: string;
}> {
  const resolved = resolveWorkbenchPath(filePath);
  const stat = await fs.stat(resolved);
  if (!stat.isFile()) {
    throw new Error("Path is not a file.");
  }

  const sizeBytes = stat.size;
  const truncated = sizeBytes > maxBytes;
  const handle = await fs.open(resolved, "r");
  try {
    const buffer = Buffer.alloc(Math.min(sizeBytes, maxBytes));
    await handle.read(buffer, 0, buffer.length, 0);
    return {
      path: resolved,
      sizeBytes,
      truncated,
      content: buffer.toString("utf-8"),
    };
  } finally {
    await handle.close();
  }
}
