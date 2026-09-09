import path from "node:path";
import { EMPIRE_ROOT, PYTHON_BIN } from "#lib/empire";

const TOOL_FORGE_MCP_SCRIPT = path.join(EMPIRE_ROOT, "mcp", "tool_forge_mcp.py");
const HARVEST_CACHE_DIR =
  process.env.EMPIRE_HARVEST_CACHE_DIR ??
  "C:/Empire_Workbench/04_Thought_Experiments/harvest_cache";
const ACTIVE_TOOLS_DIR =
  process.env.EMPIRE_ACTIVE_TOOLS_DIR ?? "C:/Empire_Workbench/03_Active_Tools";

async function loadSdk() {
  const { Client } = await import("@modelcontextprotocol/sdk/client/index.js");
  const { StdioClientTransport } = await import(
    "@modelcontextprotocol/sdk/client/stdio.js"
  );
  return { Client, StdioClientTransport };
}

let client: InstanceType<Awaited<ReturnType<typeof loadSdk>>["Client"]> | null =
  null;
let transport: InstanceType<
  Awaited<ReturnType<typeof loadSdk>>["StdioClientTransport"]
> | null = null;
let connectPromise: Promise<void> | null = null;
let sessionRefs = 0;

function toolForgeMcpEnv(): Record<string, string> {
  const env: Record<string, string> = {};
  for (const [key, value] of Object.entries(process.env)) {
    if (typeof value === "string") {
      env[key] = value;
    }
  }
  env.PYTHONPATH = EMPIRE_ROOT;
  env.EMPIRE_HARVEST_CACHE_DIR = HARVEST_CACHE_DIR;
  env.EMPIRE_ACTIVE_TOOLS_DIR = ACTIVE_TOOLS_DIR;
  return env;
}

function parseMcpToolJson(result: unknown): unknown {
  if (!result || typeof result !== "object") {
    return { ok: false, error: "Invalid empire-tool-forge MCP response." };
  }
  const payload = result as {
    isError?: boolean;
    content?: Array<{ text?: string }>;
  };
  if (payload.isError) {
    const message = (payload.content ?? [])
      .map((part) => (part.text ?? ""))
      .join("\n")
      .trim();
    return {
      ok: false,
      error: message || "empire-tool-forge MCP tool returned an error.",
    };
  }
  const raw = (payload.content ?? [])
    .map((part) => (part.text ?? ""))
    .join("\n")
    .trim();
  if (!raw) {
    return { ok: false, error: "Empty response from empire-tool-forge MCP." };
  }
  try {
    return JSON.parse(raw) as unknown;
  } catch {
    return {
      ok: false,
      error: "Invalid JSON from empire-tool-forge MCP.",
      raw,
    };
  }
}

export async function connectEmpireToolForgeMcp(): Promise<void> {
  sessionRefs += 1;
  if (client) return;
  if (!connectPromise) {
    connectPromise = (async () => {
      const { Client, StdioClientTransport } = await loadSdk();
      transport = new StdioClientTransport({
        command: PYTHON_BIN,
        args: [TOOL_FORGE_MCP_SCRIPT],
        env: toolForgeMcpEnv(),
        cwd: EMPIRE_ROOT,
        stderr: "pipe",
      });
      client = new Client({
        name: "eve-empire-tool-forge",
        version: "1.0.0",
      });
      await client.connect(transport);
    })().catch((error) => {
      client = null;
      transport = null;
      connectPromise = null;
      sessionRefs = Math.max(0, sessionRefs - 1);
      throw error;
    });
  }
  await connectPromise;
}

export async function disconnectEmpireToolForgeMcp(): Promise<void> {
  sessionRefs = Math.max(0, sessionRefs - 1);
  if (sessionRefs > 0 || !client) return;
  const activeClient = client;
  const activeTransport = transport;
  client = null;
  transport = null;
  connectPromise = null;
  try {
    await activeClient.close();
  } catch {
    /* ignore */
  }
  if (activeTransport) {
    try {
      await activeTransport.close();
    } catch {
      /* ignore */
    }
  }
}

async function callToolForgeTool(
  name: string,
  args: Record<string, unknown> = {},
): Promise<unknown> {
  try {
    await connectEmpireToolForgeMcp();
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    return {
      ok: false,
      error: `Could not start empire-tool-forge MCP: ${message}`,
    };
  }
  if (!client) {
    return {
      ok: false,
      error: "empire-tool-forge MCP client is not connected.",
    };
  }
  try {
    const result = await client.callTool({ name, arguments: args });
    return parseMcpToolJson(result);
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    return { ok: false, error: `${name} failed: ${message}` };
  }
}

export async function docsGuideScrapeViaMcp(input: {
  root_url: string;
  max_pages?: number;
  note?: string;
}): Promise<unknown> {
  return callToolForgeTool("docs_guide_scrape", {
    root_url: input.root_url,
    max_pages: input.max_pages ?? 80,
    note: input.note ?? "",
  });
}

export async function skillTriageManifestViaMcp(input: {
  paths?: string;
  include_installed?: boolean;
}): Promise<unknown> {
  return callToolForgeTool("skill_triage_manifest", {
    paths: input.paths ?? "",
    include_installed: input.include_installed ?? true,
  });
}

export async function listHarvestOutputsViaMcp(): Promise<unknown> {
  return callToolForgeTool("list_harvest_outputs");
}
