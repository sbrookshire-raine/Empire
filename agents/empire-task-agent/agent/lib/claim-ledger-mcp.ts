/**
 * claim-ledger limb adapter.
 *
 * Thin by contract: this file declares the client config and one function per
 * tool. It does NOT import the MCP SDK, manage process lifetime, or parse MCP
 * JSON - the shared client does all of that.
 *
 * The server lives at `mcp/claim_ledger_mcp.py` (vendored from the Gumloop
 * handoff, MIT). Roots are declared explicitly and never defaulted to cwd:
 * a check runs inside one of these directories, and a check naming a path
 * outside them is refused.
 */
import path from "node:path";
import { EMPIRE_ROOT } from "#lib/empire";
import { createEmpireMcpClient } from "./mcp-client";

/** Where the ledger's SQLite file lives. */
export const CLAIM_LEDGER_DB =
  process.env.CLAIM_LEDGER_DB ??
  path.join(EMPIRE_ROOT, "eve-output", "claim-ledger", "claims.db");

/** Directories a check may run inside. Declared, never inferred. */
export const CLAIM_LEDGER_ROOTS =
  process.env.CLAIM_LEDGER_ROOTS ??
  path.join(EMPIRE_ROOT, "eve-output", "claim-ledger");

const client = createEmpireMcpClient({
  label: "claim-ledger",
  clientName: "claim-ledger",
  script: "claim_ledger_mcp.py",
  env: () => ({
    // Declared roots. A check runs with cwd inside one of these; a check that
    // names a path outside them is refused. Do not default these to cwd.
    CLAIM_LEDGER_DB,
    CLAIM_LEDGER_ROOTS,
    CLAIM_LEDGER_TIMEOUT: process.env.CLAIM_LEDGER_TIMEOUT ?? "120",
  }),
});

/** Record a claim, optionally with the command that would prove it wrong. */
export async function claimAdd(
  claim: string,
  checkCmd?: string,
  grade?: string,
  source?: string,
) {
  return client.callTool("claim_add", {
    claim,
    check_cmd: checkCmd ?? "",
    grade: grade ?? "community-reported",
    source: source ?? "",
  });
}

/** Run the checks and record what happened. Empty slug checks everything. */
export async function claimVerify(slug?: string) {
  return client.callTool("claim_verify", { slug: slug ?? "" });
}

/** How much of what is claimed can actually be proven. */
export async function claimHealth() {
  return client.callTool("claim_health", {});
}

/** List claims; optionally only documents (no check) or only failing ones. */
export async function claimList(opts?: { unchecked?: boolean; failing?: boolean }) {
  return client.callTool("claim_list", {
    unchecked: opts?.unchecked ?? false,
    failing: opts?.failing ?? false,
  });
}
