import path from "node:path";
import { EMPIRE_ROOT, PYTHON_BIN } from "#lib/empire";

const WIKI_SCOUT_MCP_SCRIPT = path.join(EMPIRE_ROOT, "mcp", "wiki_scout_mcp.py");
const WIKI_CACHE_DIR =
  process.env.EMPIRE_WIKI_CACHE_DIR ??
  "C:/Empire_Workbench/04_Thought_Experiments/wiki_cache";
const WEAVIATE_URL = process.env.WEAVIATE_URL ?? "http://127.0.0.1:8091";
const WEAVIATE_API_KEY =
  process.env.WEAVIATE_API_KEY ?? "WVF5YThaHlkYwhGUSmCRgsX3tD5ngdN8pkih";

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

function wikiScoutMcpEnv(): Record<string, string> {
  const env: Record<string, string> = {};
  for (const [key, value] of Object.entries(process.env)) {
    if (typeof value === "string") {
      env[key] = value;
    }
  }
  // Force client endpoints after env copy — host OLLAMA_HOST is often "0.0.0.0" (bind).
  env.PYTHONPATH = EMPIRE_ROOT;
  env.EMPIRE_WIKI_CACHE_DIR = WIKI_CACHE_DIR;
  env.WEAVIATE_URL = WEAVIATE_URL;
  env.WEAVIATE_API_KEY = WEAVIATE_API_KEY;
  env.EMPIRE_OLLAMA_URL = "http://127.0.0.1:11434";
  env.OLLAMA_HOST = "http://127.0.0.1:11434";
  return env;
}

function parseMcpToolJson(result: unknown): unknown {
  if (!result || typeof result !== "object") {
    return { ok: false, error: "Invalid empire-wiki-scout MCP response." };
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
      error: message || "empire-wiki-scout MCP tool returned an error.",
    };
  }

  const raw = (payload.content ?? [])
    .map((part) => (part.text ?? ""))
    .join("\n")
    .trim();
  if (!raw) {
    return { ok: false, error: "Empty response from empire-wiki-scout MCP." };
  }
  try {
    return JSON.parse(raw) as unknown;
  } catch {
    return {
      ok: false,
      error: "Invalid JSON from empire-wiki-scout MCP.",
      raw,
    };
  }
}

export async function connectEmpireWikiScoutMcp(): Promise<void> {
  sessionRefs += 1;
  if (client) {
    return;
  }
  if (!connectPromise) {
    connectPromise = (async () => {
      const { Client, StdioClientTransport } = await loadSdk();
      transport = new StdioClientTransport({
        command: PYTHON_BIN,
        args: [WIKI_SCOUT_MCP_SCRIPT],
        env: wikiScoutMcpEnv(),
        cwd: EMPIRE_ROOT,
        stderr: "pipe",
      });
      client = new Client({ name: "eve-empire-wiki-scout", version: "1.0.0" });
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

export async function disconnectEmpireWikiScoutMcp(): Promise<void> {
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

export async function wikiScoutSearchViaMcp(input: {
  query: string;
  year?: string;
  limit?: number;
}): Promise<unknown> {
  try {
    await connectEmpireWikiScoutMcp();
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    return {
      ok: false,
      error: `Could not start empire-wiki-scout MCP: ${message}`,
    };
  }

  if (!client) {
    return {
      ok: false,
      error: "empire-wiki-scout MCP client is not connected.",
    };
  }

  try {
    const result = await client.callTool({
      name: "wiki_scout_search",
      arguments: {
        query: input.query,
        year: input.year ?? "2021",
        limit: input.limit ?? 3,
      },
    });
    return parseMcpToolJson(result);
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    return {
      ok: false,
      error: `wiki_scout_search failed: ${message}`,
    };
  }
}

export async function wikiScoutCompareYearsViaMcp(input: {
  query: string;
  years?: string;
  limit_per_year?: number;
}): Promise<unknown> {
  try {
    await connectEmpireWikiScoutMcp();
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    return {
      ok: false,
      error: `Could not start empire-wiki-scout MCP: ${message}`,
    };
  }

  if (!client) {
    return {
      ok: false,
      error: "empire-wiki-scout MCP client is not connected.",
    };
  }

  try {
    const result = await client.callTool({
      name: "wiki_scout_compare_years",
      arguments: {
        query: input.query,
        years: input.years ?? "2017,2021,2026",
        limit_per_year: input.limit_per_year ?? 2,
      },
    });
    return parseMcpToolJson(result);
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    return {
      ok: false,
      error: `wiki_scout_compare_years failed: ${message}`,
    };
  }
}
