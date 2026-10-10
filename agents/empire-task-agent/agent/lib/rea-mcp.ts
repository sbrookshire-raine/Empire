import path from "node:path";
import { EMPIRE_ROOT } from "#lib/empire";
import { createEmpireMcpClient } from "#lib/mcp-client";

const REA_PACKAGE_ROOT = path.join(EMPIRE_ROOT, "tools", "rea");
const REA_SCRIPT = path.join(
  REA_PACKAGE_ROOT,
  "node_modules",
  "rea-agents",
  "scripts",
  "rea.mjs",
);

const REA_EVIDENCE_ROOT =
  process.env.REA_EVIDENCE_ROOT ??
  "C:/Empire_Workbench/04_Thought_Experiments/rea_cache";

const mcp = createEmpireMcpClient({
  label: "rea",
  clientName: "eve-rea",
  command: process.execPath,
  args: [REA_SCRIPT, "mcp"],
  cwd: REA_PACKAGE_ROOT,
  env: () => ({
    REA_EVIDENCE_ROOT,
  }),
});

export async function reaDoctorViaMcp(): Promise<unknown> {
  return mcp.callTool("doctor", {});
}

export async function reaBinarySessionViaMcp(): Promise<unknown> {
  return mcp.callTool("binary_session", {});
}

export async function reaAnalyzeJavascriptViaMcp(input: {
  path: string;
}): Promise<unknown> {
  return mcp.callTool("analyze_javascript_application", {
    path: input.path,
  });
}

export async function reaInvokeViaMcp(input: {
  tool: string;
  arguments: Record<string, unknown>;
}): Promise<unknown> {
  return mcp.callTool(input.tool, input.arguments);
}
