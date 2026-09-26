import { createEmpireMcpClient } from "#lib/mcp-client";

const WIKI_CACHE_DIR =
  process.env.EMPIRE_WIKI_CACHE_DIR ??
  "C:/Empire_Workbench/04_Thought_Experiments/wiki_cache";
const WEAVIATE_URL = process.env.WEAVIATE_URL ?? "http://127.0.0.1:8091";
const WEAVIATE_API_KEY =
  process.env.WEAVIATE_API_KEY ?? "WVF5YThaHlkYwhGUSmCRgsX3tD5ngdN8pkih";

const mcp = createEmpireMcpClient({
  label: "empire-wiki-scout",
  clientName: "eve-empire-wiki-scout",
  script: "wiki_scout_mcp.py",
  env: () => ({
    EMPIRE_WIKI_CACHE_DIR: WIKI_CACHE_DIR,
    WEAVIATE_URL,
    WEAVIATE_API_KEY,
    // Host OLLAMA_HOST is often "0.0.0.0" (a bind address) - pin client endpoints.
    EMPIRE_OLLAMA_URL: "http://127.0.0.1:11434",
    OLLAMA_HOST: "http://127.0.0.1:11434",
    // Chat turns need sub-second wiki tools - heuristics only (no BGE cold load).
    EMPIRE_WIKI_RERANK: "0",
    EMPIRE_WIKI_CANDIDATE_POOL: "12",
  }),
});

export const connectEmpireWikiScoutMcp = (): Promise<void> => mcp.connect();
export const disconnectEmpireWikiScoutMcp = (): Promise<void> =>
  mcp.disconnect();

export async function wikiScoutSearchViaMcp(input: {
  query: string;
  year?: string;
  limit?: number;
}): Promise<unknown> {
  return mcp.callTool("wiki_scout_search", {
    query: input.query,
    year: input.year ?? "2026",
    limit: input.limit ?? 2,
  });
}

export async function wikiScoutCompareYearsViaMcp(input: {
  query: string;
  years?: string;
  limit_per_year?: number;
}): Promise<unknown> {
  return mcp.callTool("wiki_scout_compare_years", {
    query: input.query,
    years: input.years ?? "2017,2021,2026",
    limit_per_year: input.limit_per_year ?? 2,
  });
}
