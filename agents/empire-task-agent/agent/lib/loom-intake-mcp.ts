import { createEmpireMcpClient } from "#lib/mcp-client";

const LOOM_ROOT =
  process.env.EMPIRE_LOOM_ROOT ??
  "C:/Empire_Workbench/04_Thought_Experiments/loom";
const RESOURCE_QUEUE =
  process.env.EMPIRE_RESOURCE_QUEUE_DIR ??
  "C:/Empire_Workbench/00_Resource_Queue";

const mcp = createEmpireMcpClient({
  label: "empire-loom-intake",
  clientName: "eve-empire-loom-intake",
  script: "loom_intake_mcp.py",
  env: () => ({
    EMPIRE_LOOM_ROOT: LOOM_ROOT,
    EMPIRE_RESOURCE_QUEUE_DIR: RESOURCE_QUEUE,
  }),
});

export const connectEmpireLoomIntakeMcp = (): Promise<void> => mcp.connect();
export const disconnectEmpireLoomIntakeMcp = (): Promise<void> =>
  mcp.disconnect();

export async function loomStatusViaMcp(): Promise<unknown> {
  return mcp.callTool("loom_status", {});
}

export async function loomProcessShellCsvViaMcp(input: {
  csv_path: string;
  domain_bucket?: string;
  max_per_cycle?: number;
}): Promise<unknown> {
  return mcp.callTool("loom_process_shell_csv", {
    csv_path: input.csv_path,
    domain_bucket: input.domain_bucket ?? "general",
    max_per_cycle: input.max_per_cycle ?? 7,
  });
}
