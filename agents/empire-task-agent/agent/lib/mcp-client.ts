import path from "node:path";
import { EMPIRE_ROOT, PYTHON_BIN } from "#lib/empire";

/**
 * Shared stdio MCP client for the empire-* Python servers.
 *
 * Every `agent/lib/*-mcp.ts` wrapper used to carry its own copy of this plumbing
 * (lazy SDK import, client/transport lifetime, ref-counted sessions, env merge,
 * JSON error parsing) - ~190 lines each, 1,328 lines across seven files, with the
 * same 34 boilerplate lines repeated. Wrappers now declare a config and expose
 * thin tool functions; the lifetime and error shapes live here once, so a fix
 * lands everywhere instead of in the copy someone remembered.
 *
 * Error strings keep the `label` in every message ("empire-work-orders MCP ..."),
 * so diagnostics still name the server that failed.
 */

async function loadSdk() {
  const { Client } = await import("@modelcontextprotocol/sdk/client/index.js");
  const { StdioClientTransport } = await import(
    "@modelcontextprotocol/sdk/client/stdio.js"
  );
  return { Client, StdioClientTransport };
}

type Sdk = Awaited<ReturnType<typeof loadSdk>>;

export type McpClientConfig = {
  /** Server label used in error messages, e.g. "empire-work-orders". */
  label: string;
  /** Name this client reports to the server, e.g. "eve-empire-work-orders". */
  clientName: string;
  /** Server script under `<EMPIRE_ROOT>/mcp/`, e.g. "work_order_mcp.py". */
  script: string;
  /** Extra environment for the server process; PYTHONPATH is added for you. */
  env?: () => Record<string, string>;
};

export type EmpireMcpClient = {
  connect: () => Promise<void>;
  disconnect: () => Promise<void>;
  /** Connect if needed, call the tool, and normalise errors to `{ ok: false }`. */
  callTool: (name: string, args: Record<string, unknown>) => Promise<unknown>;
};

export function createEmpireMcpClient(config: McpClientConfig): EmpireMcpClient {
  const scriptPath = path.join(EMPIRE_ROOT, "mcp", config.script);
  let client: InstanceType<Sdk["Client"]> | null = null;
  let transport: InstanceType<Sdk["StdioClientTransport"]> | null = null;
  let connectPromise: Promise<void> | null = null;
  let sessionRefs = 0;

  function buildEnv(): Record<string, string> {
    const env: Record<string, string> = {
      PYTHONPATH: EMPIRE_ROOT,
      ...(config.env?.() ?? {}),
    };
    for (const [key, value] of Object.entries(process.env)) {
      if (typeof value === "string") {
        env[key] = value;
      }
    }
    return env;
  }

  function parseToolJson(result: unknown): unknown {
    if (!result || typeof result !== "object") {
      return { ok: false, error: `Invalid ${config.label} MCP response.` };
    }

    const payload = result as {
      isError?: boolean;
      content?: Array<{ text?: string }>;
    };
    const raw = (payload.content ?? [])
      .map((part) => part.text ?? "")
      .join("\n")
      .trim();

    if (payload.isError) {
      return {
        ok: false,
        error: raw || `${config.label} MCP tool returned an error.`,
      };
    }
    if (!raw) {
      return { ok: false, error: `Empty response from ${config.label} MCP.` };
    }
    try {
      return JSON.parse(raw) as unknown;
    } catch {
      return {
        ok: false,
        error: `Invalid JSON from ${config.label} MCP.`,
        raw,
      };
    }
  }

  async function connect(): Promise<void> {
    sessionRefs += 1;
    if (client) {
      return;
    }
    if (!connectPromise) {
      connectPromise = (async () => {
        const { Client, StdioClientTransport } = await loadSdk();
        transport = new StdioClientTransport({
          command: PYTHON_BIN,
          args: [scriptPath],
          env: buildEnv(),
          cwd: EMPIRE_ROOT,
          stderr: "pipe",
        });
        client = new Client({ name: config.clientName, version: "1.0.0" });
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

  async function disconnect(): Promise<void> {
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

  async function callTool(
    name: string,
    args: Record<string, unknown>
  ): Promise<unknown> {
    try {
      await connect();
    } catch (error) {
      const message = error instanceof Error ? error.message : String(error);
      return {
        ok: false,
        error: `Could not start ${config.label} MCP: ${message}`,
      };
    }

    if (!client) {
      return {
        ok: false,
        error: `${config.label} MCP client is not connected.`,
      };
    }

    try {
      const result = await client.callTool({ name, arguments: args });
      return parseToolJson(result);
    } catch (error) {
      const message = error instanceof Error ? error.message : String(error);
      return { ok: false, error: `${name} failed: ${message}` };
    }
  }

  return { connect, disconnect, callTool };
}
