import { createEmpireMcpClient } from "#lib/mcp-client";

const WORK_ORDERS_DIR =
  process.env.EMPIRE_WORK_ORDERS_DIR ?? "C:/Empire_Workbench/05_Work_Orders";
const RESOURCE_QUEUE_DIR =
  process.env.EMPIRE_RESOURCE_QUEUE_DIR ?? "C:/Empire_Workbench/00_Resource_Queue";

const mcp = createEmpireMcpClient({
  label: "empire-work-orders",
  clientName: "eve-empire-work-orders",
  script: "work_order_mcp.py",
  env: () => ({
    EMPIRE_WORK_ORDERS_DIR: WORK_ORDERS_DIR,
    EMPIRE_RESOURCE_QUEUE_DIR: RESOURCE_QUEUE_DIR,
  }),
});

export const connectEmpireWorkOrdersMcp = (): Promise<void> => mcp.connect();

export const disconnectEmpireWorkOrdersMcp = (): Promise<void> =>
  mcp.disconnect();

export async function draftWorkOrderViaMcp(input: {
  capability_needed: string;
  justification: string;
  source_file?: string;
}): Promise<unknown> {
  return mcp.callTool("draft_work_order", {
    capability_needed: input.capability_needed,
    justification: input.justification,
    source_file: input.source_file ?? "",
  });
}
