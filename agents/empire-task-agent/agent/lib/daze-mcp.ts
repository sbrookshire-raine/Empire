import path from "node:path";
import { EMPIRE_ROOT, PYTHON_BIN } from "#lib/empire";

const DAZE_MCP_SCRIPT = path.join(EMPIRE_ROOT, "mcp", "daze_mcp.py");
const POCKETBASE_URL = process.env.POCKETBASE_URL ?? "http://127.0.0.1:8090";

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

function dazeMcpEnv(): Record<string, string> {
  const env: Record<string, string> = {};
  for (const [key, value] of Object.entries(process.env)) {
    if (typeof value === "string") {
      env[key] = value;
    }
  }
  env.PYTHONPATH = EMPIRE_ROOT;
  env.POCKETBASE_URL = POCKETBASE_URL;
  return env;
}

function parseMcpToolJson(result: unknown): unknown {
  if (!result || typeof result !== "object") {
    return { ok: false, error: "Invalid empire-daze MCP response." };
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
      error: message || "empire-daze MCP tool returned an error.",
    };
  }
  const raw = (payload.content ?? [])
    .map((part) => (part.text ?? ""))
    .join("\n")
    .trim();
  if (!raw) {
    return { ok: false, error: "Empty response from empire-daze MCP." };
  }
  try {
    return JSON.parse(raw) as unknown;
  } catch {
    return { ok: false, error: "Invalid JSON from empire-daze MCP.", raw };
  }
}

export async function connectEmpireDazeMcp(): Promise<void> {
  sessionRefs += 1;
  if (client) return;
  if (!connectPromise) {
    connectPromise = (async () => {
      const { Client, StdioClientTransport } = await loadSdk();
      transport = new StdioClientTransport({
        command: PYTHON_BIN,
        args: [DAZE_MCP_SCRIPT],
        env: dazeMcpEnv(),
        cwd: EMPIRE_ROOT,
        stderr: "pipe",
      });
      client = new Client({ name: "eve-empire-daze", version: "1.0.0" });
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

export async function disconnectEmpireDazeMcp(): Promise<void> {
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

async function callDazeTool(
  name: string,
  args: Record<string, unknown>,
): Promise<unknown> {
  try {
    await connectEmpireDazeMcp();
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    return { ok: false, error: `Could not start empire-daze MCP: ${message}` };
  }
  if (!client) {
    return { ok: false, error: "empire-daze MCP client is not connected." };
  }
  try {
    const result = await client.callTool({ name, arguments: args });
    return parseMcpToolJson(result);
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    return { ok: false, error: `${name} failed: ${message}` };
  }
}

export async function dazeListDayViaMcp(input: {
  date?: string;
  phase?: string;
}): Promise<unknown> {
  return callDazeTool("daze_list_day", {
    date: input.date ?? "",
    phase: input.phase ?? "",
  });
}

export async function dazeUpsertBlockViaMcp(input: {
  title: string;
  start_minute: number;
  end_minute: number;
  date?: string;
  kind?: string;
  phase?: string;
  notes?: string;
  color?: string;
  record_id?: string;
}): Promise<unknown> {
  return callDazeTool("daze_upsert_block", {
    title: input.title,
    start_minute: input.start_minute,
    end_minute: input.end_minute,
    date: input.date ?? "",
    kind: input.kind ?? "focus",
    phase: input.phase ?? "planned",
    notes: input.notes ?? "",
    color: input.color ?? "",
    record_id: input.record_id ?? "",
  });
}

export async function dazeFreeWindowsViaMcp(input: {
  date?: string;
  phase?: string;
  min_minutes?: number;
}): Promise<unknown> {
  return callDazeTool("daze_free_windows", {
    date: input.date ?? "",
    phase: input.phase ?? "planned",
    min_minutes: input.min_minutes ?? 30,
  });
}
