import path from "node:path";
import { EMPIRE_ROOT, PYTHON_BIN } from "#lib/empire";

const STEM_MCP_SCRIPT = path.join(EMPIRE_ROOT, "mcp", "stem_factory_mcp.py");
const STEM_DIR =
  process.env.EMPIRE_STEM_FACTORY_DIR ??
  "C:/Users/m69nr/OneDrive/Desktop/HIDDEN/Shard_of_the_Division";
const STEM_INBOX =
  process.env.EMPIRE_STEM_INBOX ?? "C:/Empire_Workbench/stem_factory/input";
const STEM_OUTBOX =
  process.env.EMPIRE_STEM_OUTBOX ?? "C:/Empire_Workbench/stem_factory/output";

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

function stemMcpEnv(): Record<string, string> {
  const env: Record<string, string> = {};
  for (const [key, value] of Object.entries(process.env)) {
    if (typeof value === "string") {
      env[key] = value;
    }
  }
  env.PYTHONPATH = EMPIRE_ROOT;
  env.EMPIRE_STEM_FACTORY_DIR = STEM_DIR;
  env.EMPIRE_STEM_INBOX = STEM_INBOX;
  env.EMPIRE_STEM_OUTBOX = STEM_OUTBOX;
  return env;
}

function parseMcpToolJson(result: unknown): unknown {
  if (!result || typeof result !== "object") {
    return { ok: false, error: "Invalid empire-stem-factory MCP response." };
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
      error: message || "empire-stem-factory MCP tool returned an error.",
    };
  }
  const raw = (payload.content ?? [])
    .map((part) => (part.text ?? ""))
    .join("\n")
    .trim();
  if (!raw) {
    return { ok: false, error: "Empty response from empire-stem-factory MCP." };
  }
  try {
    return JSON.parse(raw) as unknown;
  } catch {
    return {
      ok: false,
      error: "Invalid JSON from empire-stem-factory MCP.",
      raw,
    };
  }
}

export async function connectEmpireStemFactoryMcp(): Promise<void> {
  sessionRefs += 1;
  if (client) return;
  if (!connectPromise) {
    connectPromise = (async () => {
      const { Client, StdioClientTransport } = await loadSdk();
      transport = new StdioClientTransport({
        command: PYTHON_BIN,
        args: [STEM_MCP_SCRIPT],
        env: stemMcpEnv(),
        cwd: EMPIRE_ROOT,
        stderr: "pipe",
      });
      client = new Client({
        name: "eve-empire-stem-factory",
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

export async function disconnectEmpireStemFactoryMcp(): Promise<void> {
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

async function callStemTool(
  name: string,
  args: Record<string, unknown> = {},
): Promise<unknown> {
  try {
    await connectEmpireStemFactoryMcp();
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    return {
      ok: false,
      error: `Could not start empire-stem-factory MCP: ${message}`,
    };
  }
  if (!client) {
    return {
      ok: false,
      error: "empire-stem-factory MCP client is not connected.",
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

export async function stemStatusViaMcp(): Promise<unknown> {
  return callStemTool("stem_status");
}

export async function stemListInboxViaMcp(): Promise<unknown> {
  return callStemTool("stem_list_inbox");
}

export async function stemRunViaMcp(input: {
  limit?: number;
  device?: string;
  overwrite?: boolean;
  input_dir?: string;
  output_dir?: string;
}): Promise<unknown> {
  return callStemTool("stem_run", {
    limit: input.limit ?? 1,
    device: input.device ?? "cuda",
    overwrite: input.overwrite ?? false,
    input_dir: input.input_dir ?? "",
    output_dir: input.output_dir ?? "",
  });
}
