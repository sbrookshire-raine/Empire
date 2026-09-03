import path from "node:path";
import { EMPIRE_ROOT, PYTHON_BIN } from "#lib/empire";

const WORKBENCH_MCP_SCRIPT = path.join(EMPIRE_ROOT, "mcp", "workbench_mcp.py");
const ACTIVE_TOOLS_DIR =
  process.env.EMPIRE_ACTIVE_TOOLS_DIR ?? "C:/Empire_Workbench/03_Active_Tools";

// Dynamic imports to avoid bundler resolving @modelcontextprotocol/sdk as a
// Windows path at build time.  The package is listed in externalDependencies so
// it stays as a runtime require, but the bundler still trips on the deep
// subpath.  Lazy-loading sidesteps it entirely.
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

function workbenchMcpEnv(): Record<string, string> {
  const env: Record<string, string> = {
    PYTHONPATH: EMPIRE_ROOT,
    EMPIRE_ACTIVE_TOOLS_DIR: ACTIVE_TOOLS_DIR,
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
    return { ok: false, error: "Invalid empire-workbench MCP response." };
  }

  const payload = result as { isError?: boolean; content?: Array<{ text?: string }> };
  if (payload.isError) {
    const message = (payload.content ?? [])
      .map((part) => (part.text ?? ""))
      .join("\n")
      .trim();
    return {
      ok: false,
      error: message || "empire-workbench MCP tool returned an error.",
    };
  }

  const raw = (payload.content ?? [])
    .map((part) => (part.text ?? ""))
    .join("\n")
    .trim();
  if (!raw) {
    return { ok: false, error: "Empty response from empire-workbench MCP." };
  }
  try {
    return JSON.parse(raw) as unknown;
  } catch {
    return { ok: false, error: "Invalid JSON from empire-workbench MCP.", raw };
  }
}

export async function connectEmpireWorkbenchMcp(): Promise<void> {
  sessionRefs += 1;
  if (client) {
    return;
  }
  if (!connectPromise) {
    connectPromise = (async () => {
      const { Client, StdioClientTransport } = await loadSdk();
      transport = new StdioClientTransport({
        command: PYTHON_BIN,
        args: [WORKBENCH_MCP_SCRIPT],
        env: workbenchMcpEnv(),
        cwd: EMPIRE_ROOT,
        stderr: "pipe",
      });
      client = new Client({ name: "eve-empire-workbench", version: "1.0.0" });
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

export async function disconnectEmpireWorkbenchMcp(): Promise<void> {
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

export async function readActiveToolViaMcp(filename: string): Promise<unknown> {
  try {
    await connectEmpireWorkbenchMcp();
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    return {
      ok: false,
      error: `Could not start empire-workbench MCP: ${message}`,
      filename,
    };
  }

  if (!client) {
    return {
      ok: false,
      error: "empire-workbench MCP client is not connected.",
      filename,
    };
  }

  try {
    const result = await client.callTool({
      name: "read_active_tool",
      arguments: { filename },
    });
    return parseMcpToolJson(result);
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    return {
      ok: false,
      error: `read_active_tool failed: ${message}`,
      filename,
    };
  }
}
