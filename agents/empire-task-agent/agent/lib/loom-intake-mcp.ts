import path from "node:path";
import { EMPIRE_ROOT, PYTHON_BIN } from "#lib/empire";

const LOOM_MCP_SCRIPT = path.join(EMPIRE_ROOT, "mcp", "loom_intake_mcp.py");
const LOOM_ROOT =
  process.env.EMPIRE_LOOM_ROOT ??
  "C:/Empire_Workbench/04_Thought_Experiments/loom";
const RESOURCE_QUEUE =
  process.env.EMPIRE_RESOURCE_QUEUE_DIR ??
  "C:/Empire_Workbench/00_Resource_Queue";

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

function loomMcpEnv(): Record<string, string> {
  const env: Record<string, string> = {};
  for (const [key, value] of Object.entries(process.env)) {
    if (typeof value === "string") {
      env[key] = value;
    }
  }
  env.PYTHONPATH = EMPIRE_ROOT;
  env.EMPIRE_LOOM_ROOT = LOOM_ROOT;
  env.EMPIRE_RESOURCE_QUEUE_DIR = RESOURCE_QUEUE;
  return env;
}

function parseMcpToolJson(result: unknown): unknown {
  if (!result || typeof result !== "object") {
    return { ok: false, error: "Invalid empire-loom-intake MCP response." };
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
      error: message || "empire-loom-intake MCP tool returned an error.",
    };
  }
  const raw = (payload.content ?? [])
    .map((part) => (part.text ?? ""))
    .join("\n")
    .trim();
  if (!raw) {
    return { ok: false, error: "Empty response from empire-loom-intake MCP." };
  }
  try {
    return JSON.parse(raw) as unknown;
  } catch {
    return {
      ok: false,
      error: "Invalid JSON from empire-loom-intake MCP.",
      raw,
    };
  }
}

export async function connectEmpireLoomIntakeMcp(): Promise<void> {
  sessionRefs += 1;
  if (client) return;
  if (!connectPromise) {
    connectPromise = (async () => {
      const { Client, StdioClientTransport } = await loadSdk();
      transport = new StdioClientTransport({
        command: PYTHON_BIN,
        args: [LOOM_MCP_SCRIPT],
        env: loomMcpEnv(),
        cwd: EMPIRE_ROOT,
        stderr: "pipe",
      });
      client = new Client({
        name: "eve-empire-loom-intake",
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

export async function disconnectEmpireLoomIntakeMcp(): Promise<void> {
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

async function callLoomTool(
  name: string,
  args: Record<string, unknown> = {},
): Promise<unknown> {
  try {
    await connectEmpireLoomIntakeMcp();
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    return {
      ok: false,
      error: `Could not start empire-loom-intake MCP: ${message}`,
    };
  }
  if (!client) {
    return {
      ok: false,
      error: "empire-loom-intake MCP client is not connected.",
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

export async function loomStatusViaMcp(): Promise<unknown> {
  return callLoomTool("loom_status");
}

export async function loomProcessShellCsvViaMcp(input: {
  csv_path: string;
  domain_bucket?: string;
  max_per_cycle?: number;
}): Promise<unknown> {
  return callLoomTool("loom_process_shell_csv", {
    csv_path: input.csv_path,
    domain_bucket: input.domain_bucket ?? "general",
    max_per_cycle: input.max_per_cycle ?? 7,
  });
}
