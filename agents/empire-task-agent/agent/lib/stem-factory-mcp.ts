import { createEmpireMcpClient } from "#lib/mcp-client";

const STEM_DIR =
  process.env.EMPIRE_STEM_FACTORY_DIR ??
  "C:/Users/m69nr/OneDrive/Desktop/HIDDEN/Shard_of_the_Division";
const STEM_INBOX =
  process.env.EMPIRE_STEM_INBOX ?? "C:/Empire_Workbench/stem_factory/input";
const STEM_OUTBOX =
  process.env.EMPIRE_STEM_OUTBOX ?? "C:/Empire_Workbench/stem_factory/output";

const mcp = createEmpireMcpClient({
  label: "empire-stem-factory",
  clientName: "eve-empire-stem-factory",
  script: "stem_factory_mcp.py",
  env: () => ({
    EMPIRE_STEM_FACTORY_DIR: STEM_DIR,
    EMPIRE_STEM_INBOX: STEM_INBOX,
    EMPIRE_STEM_OUTBOX: STEM_OUTBOX,
  }),
});

export const connectEmpireStemFactoryMcp = (): Promise<void> => mcp.connect();
export const disconnectEmpireStemFactoryMcp = (): Promise<void> =>
  mcp.disconnect();

export async function stemStatusViaMcp(): Promise<unknown> {
  return mcp.callTool("stem_status", {});
}

export async function stemListInboxViaMcp(): Promise<unknown> {
  return mcp.callTool("stem_list_inbox", {});
}

export async function stemRunViaMcp(input: {
  limit?: number;
  device?: string;
  overwrite?: boolean;
  input_dir?: string;
  output_dir?: string;
}): Promise<unknown> {
  return mcp.callTool("stem_run", {
    limit: input.limit ?? 1,
    device: input.device ?? "cuda",
    overwrite: input.overwrite ?? false,
    input_dir: input.input_dir ?? "",
    output_dir: input.output_dir ?? "",
  });
}
