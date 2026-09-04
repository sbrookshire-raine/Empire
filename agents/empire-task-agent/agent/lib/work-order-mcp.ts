import path from "node:path";
import { EMPIRE_ROOT, PYTHON_BIN } from "#lib/empire";

const WORK_ORDER_MCP_SCRIPT = path.join(EMPIRE_ROOT, "mcp", "work_order_mcp.py");
const WORK_ORDERS_DIR =
  process.env.EMPIRE_WORK_ORDERS_DIR ?? "C:/Empire_Workbench/05_Work_Orders";
const RESOURCE_QUEUE_DIR =
  process.env.EMPIRE_RESOURCE_QUEUE_DIR ?? "C:/Empire_Workbench/00_Resource_Queue";

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

function workOrderMcpEnv(): Record<string, string> {
  const env: Record<string, string> = {
    PYTHONPATH: EMPIRE_ROOT,
    EMPIRE_WORK_ORDERS_DIR: WORK_ORDERS_DIR,
    EMPIRE_RESOURCE_QUEUE_DIR: RESOURCE_QUEUE_DIR,
  };
  for (const [key, value] of Object.entries(process.env)) {
    if (typeof value === "string") {
      env[key] = value;
    }
  }
  return env;
}

function parseMcpToolJson(result: unknown): unknown {
  if (!result || typeof result !== "object") {
    return { ok: false, error: "Invalid empire-work-orders MCP response." };
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
      error: message || "empire-work-orders MCP tool returned an error.",
    };
  }

  const raw = (payload.content ?? [])
    .map((part) => (part.text ?? ""))
    .join("\n")
    .trim();
  if (!raw) {
    return { ok: false, error: "Empty response from empire-work-orders MCP." };
  }
  try {
    return JSON.parse(raw) as unknown;
  } catch {
    return {
      ok: false,
      error: "Invalid JSON from empire-work-orders MCP.",
      raw,
    };
  }
}

export async function connectEmpireWorkOrdersMcp(): Promise<void> {
  sessionRefs += 1;
  if (client) {
    return;
  }
  if (!connectPromise) {
    connectPromise = (async () => {
      const { Client, StdioClientTransport } = await loadSdk();
      transport = new StdioClientTransport({
        command: PYTHON_BIN,
        args: [WORK_ORDER_MCP_SCRIPT],
        env: workOrderMcpEnv(),
        cwd: EMPIRE_ROOT,
        stderr: "pipe",
      });
      client = new Client({ name: "eve-empire-work-orders", version: "1.0.0" });
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

export async function disconnectEmpireWorkOrdersMcp(): Promise<void> {
  sessionRefs = Math.max(0, sessionRefs - 1);
  if (sessionRefs > 0 || !client) {
    return;
  }

  const activeClient = client;
  const activeTransport = transport;
  client = null;
  transport = null;
  connectPromise = null;

  try {
    await activeClient.close();
  } catch {
    /* ignore close errors */
  }
  if (activeTransport) {
    try {
      await activeTransport.close();
    } catch {
      /* ignore close errors */
    }
  }
}

export async function draftWorkOrderViaMcp(input: {
  capability_needed: string;
  justification: string;
  source_file?: string;
}): Promise<unknown> {
  try {
    await connectEmpireWorkOrdersMcp();
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    return {
      ok: false,
      error: `Could not start empire-work-orders MCP: ${message}`,
    };
  }

  if (!client) {
    return {
      ok: false,
      error: "empire-work-orders MCP client is not connected.",
    };
  }

  try {
    const result = await client.callTool({
      name: "draft_work_order",
      arguments: {
        capability_needed: input.capability_needed,
        justification: input.justification,
        source_file: input.source_file ?? "",
      },
    });
    return parseMcpToolJson(result);
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    return {
      ok: false,
      error: `draft_work_order failed: ${message}`,
    };
  }
}
