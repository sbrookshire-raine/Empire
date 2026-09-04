import fs from "node:fs/promises";
import path from "node:path";

/** Hardcoded local Windows workbench root — never a cloud/sandbox path. */
export const WORKBENCH_ROOT = "C:/Empire_Workbench";

/** Top-level folders allowed under WORKBENCH_ROOT. */
export const WORKBENCH_FOLDERS = [
  "00_Resource_Queue",
  "01_Memory_Bank",
  "02_Skills_and_Prompts",
  "03_Active_Tools",
  "04_Thought_Experiments",
  "05_Work_Orders",
] as const;

/** @deprecated Prefer WORKBENCH_ROOT + relative paths. Kept for callers that list roots. */
export const WORKBENCH_ROOTS = WORKBENCH_FOLDERS.map(
  (folder) => `${WORKBENCH_ROOT}/${folder}`,
);

const MAX_READ_BYTES = 512 * 1024;

const SANDBOX_PREFIXES = [
  "/home/vercel-sandbox/",
  "/home/vercel-sandbox",
  "home/vercel-sandbox/",
  "home/vercel-sandbox",
];

function toPosix(p: string): string {
  return p.replace(/\\/g, "/");
}

/**
 * Strip hallucinated cloud/sandbox prefixes and absolute drive roots so only a
 * relative path under WORKBENCH_ROOT remains (e.g. 00_Resource_Queue/file.md).
 */
export function sanitizeWorkbenchRelativePath(raw: string): string {
  let cleaned = toPosix(raw.trim());
  if (!cleaned) {
    throw new Error(
      "Path is required. Pass a relative workbench path such as 00_Resource_Queue.",
    );
  }

  for (const prefix of SANDBOX_PREFIXES) {
    const lower = cleaned.toLowerCase();
    const pref = prefix.toLowerCase();
    if (lower.startsWith(pref)) {
      cleaned = cleaned.slice(prefix.length);
      break;
    }
  }

  // Strip leading slashes after sandbox strip.
  cleaned = cleaned.replace(/^\/+/, "");

  // Strip Windows drive + optional Empire_Workbench prefix.
  cleaned = cleaned.replace(/^[A-Za-z]:\/*/, "");
  cleaned = cleaned.replace(/^\/+/, "");
  const rootName = "empire_workbench";
  const lower = cleaned.toLowerCase();
  if (lower === rootName || lower.startsWith(`${rootName}/`)) {
    cleaned = cleaned.slice(rootName.length).replace(/^\/+/, "");
  }

  cleaned = cleaned.replace(/^\/+/, "").replace(/\/+$/, "");
  if (!cleaned) {
    throw new Error(
      "Path resolved empty. Pass a relative folder such as 00_Resource_Queue.",
    );
  }

  const parts = cleaned.split("/").filter((part) => part.length > 0);
  if (parts.some((part) => part === "..")) {
    throw new Error("path traversal (..) is not allowed.");
  }
  if (parts.some((part) => part === ".")) {
    throw new Error("'.' path segments are not allowed.");
  }

  const top = parts[0];
  if (!(WORKBENCH_FOLDERS as readonly string[]).includes(top)) {
    throw new Error(
      `Path must start with one of: ${WORKBENCH_FOLDERS.join(", ")}. Got: ${top}`,
    );
  }

  return parts.join("/");
}

export function resolveWorkbenchPath(requested: string): string {
  const relative = sanitizeWorkbenchRelativePath(requested);
  const joined = path.resolve(
    path.join(WORKBENCH_ROOT, ...relative.split("/")),
  );
  const rootResolved = path.resolve(WORKBENCH_ROOT);
  if (joined !== rootResolved && !joined.startsWith(rootResolved + path.sep)) {
    throw new Error("Resolved path escaped WORKBENCH_ROOT.");
  }
  return joined;
}

export async function listWorkbenchDir(dirPath: string): Promise<{
  path: string;
  relativePath: string;
  entries: Array<{ name: string; type: "file" | "directory" }>;
}> {
  const relativePath = sanitizeWorkbenchRelativePath(dirPath);
  const resolved = resolveWorkbenchPath(relativePath);
  try {
    const entries = await fs.readdir(resolved, { withFileTypes: true });
    return {
      path: resolved,
      relativePath,
      entries: entries
        .filter((e) => !e.name.startsWith("."))
        .map((e) => ({
          name: e.name,
          type: (e.isDirectory() ? "directory" : "file") as
            | "file"
            | "directory",
        }))
        .sort((a, b) => a.name.localeCompare(b.name)),
    };
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    throw new Error(
      `Could not list ${relativePath} under ${WORKBENCH_ROOT}: ${message}`,
    );
  }
}

export async function readWorkbenchFile(
  filePath: string,
  maxBytes = MAX_READ_BYTES,
): Promise<{
  path: string;
  relativePath: string;
  sizeBytes: number;
  truncated: boolean;
  content: string;
}> {
  const relativePath = sanitizeWorkbenchRelativePath(filePath);
  const resolved = resolveWorkbenchPath(relativePath);
  try {
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
        relativePath,
        sizeBytes,
        truncated,
        content: buffer.toString("utf-8"),
      };
    } finally {
      await handle.close();
    }
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    throw new Error(
      `Could not read ${relativePath} under ${WORKBENCH_ROOT}: ${message}`,
    );
  }
}
