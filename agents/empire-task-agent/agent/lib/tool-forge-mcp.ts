import { createEmpireMcpClient } from "#lib/mcp-client";

const HARVEST_CACHE_DIR =
  process.env.EMPIRE_HARVEST_CACHE_DIR ??
  "C:/Empire_Workbench/04_Thought_Experiments/harvest_cache";
const ACTIVE_TOOLS_DIR =
  process.env.EMPIRE_ACTIVE_TOOLS_DIR ?? "C:/Empire_Workbench/03_Active_Tools";

const mcp = createEmpireMcpClient({
  label: "empire-tool-forge",
  clientName: "eve-empire-tool-forge",
  script: "tool_forge_mcp.py",
  env: () => ({
    EMPIRE_HARVEST_CACHE_DIR: HARVEST_CACHE_DIR,
    EMPIRE_ACTIVE_TOOLS_DIR: ACTIVE_TOOLS_DIR,
  }),
});

export const connectEmpireToolForgeMcp = (): Promise<void> => mcp.connect();
export const disconnectEmpireToolForgeMcp = (): Promise<void> =>
  mcp.disconnect();

export async function docsGuideScrapeViaMcp(input: {
  root_url: string;
  max_pages?: number;
  note?: string;
}): Promise<unknown> {
  return mcp.callTool("docs_guide_scrape", {
    root_url: input.root_url,
    max_pages: input.max_pages ?? 80,
    note: input.note ?? "",
  });
}

export async function skillTriageManifestViaMcp(input: {
  paths?: string;
  include_installed?: boolean;
}): Promise<unknown> {
  return mcp.callTool("skill_triage_manifest", {
    paths: input.paths ?? "",
    include_installed: input.include_installed ?? true,
  });
}

export async function listHarvestOutputsViaMcp(): Promise<unknown> {
  return mcp.callTool("list_harvest_outputs", {});
}
