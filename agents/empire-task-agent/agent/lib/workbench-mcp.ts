import { createEmpireMcpClient } from "#lib/mcp-client";

const WORKBENCH_DIR =
  process.env.EMPIRE_WORKBENCH_DIR ?? "C:/Empire_Workbench";
const ACTIVE_TOOLS_DIR =
  process.env.EMPIRE_ACTIVE_TOOLS_DIR ?? "C:/Empire_Workbench/03_Active_Tools";

const mcp = createEmpireMcpClient({
  label: "empire-workbench",
  clientName: "eve-empire-workbench",
  script: "workbench_mcp.py",
  env: () => ({
    EMPIRE_WORKBENCH_DIR: WORKBENCH_DIR,
    EMPIRE_ACTIVE_TOOLS_DIR: ACTIVE_TOOLS_DIR,
  }),
});

export const connectEmpireWorkbenchMcp = (): Promise<void> => mcp.connect();
export const disconnectEmpireWorkbenchMcp = (): Promise<void> =>
  mcp.disconnect();

export async function checkWorkbenchHealthViaMcp(): Promise<unknown> {
  return mcp.callTool("check_workbench_health", {});
}

export async function readActiveToolViaMcp(filename: string): Promise<unknown> {
  const result = await mcp.callTool("read_active_tool", { filename });
  // Keep naming the file on failure: this tool's errors used to carry it.
  const failed = (result as { ok?: boolean } | null)?.ok === false;
  if (failed) {
    return { ...(result as Record<string, unknown>), filename };
  }
  return result;
}
