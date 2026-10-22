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

const DEFAULT_GHIDRA_INSTALL_DIR = path.join(
  EMPIRE_ROOT,
  "tools",
  "ghidra",
  "ghidra_12.1.4_PUBLIC",
);

const DEFAULT_JAVA_HOME =
  process.platform === "win32"
    ? "C:/Program Files/Microsoft/jdk-21.0.12.101-hotspot"
    : "";

function reaChildEnv(): Record<string, string> {
  const env: Record<string, string> = {
    REA_EVIDENCE_ROOT,
  };
  const ghidra =
    process.env.GHIDRA_INSTALL_DIR?.trim() || DEFAULT_GHIDRA_INSTALL_DIR;
  env.GHIDRA_INSTALL_DIR = ghidra.replace(/\//g, path.sep);
  const javaHome = process.env.JAVA_HOME?.trim() || DEFAULT_JAVA_HOME;
  if (javaHome) {
    env.JAVA_HOME = javaHome.replace(/\//g, path.sep);
  }
  return env;
}

const mcp = createEmpireMcpClient({
  label: "rea",
  clientName: "eve-rea",
  command: process.execPath,
  args: [REA_SCRIPT, "mcp"],
  cwd: REA_PACKAGE_ROOT,
  env: reaChildEnv,
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
