import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { runPythonModule } from "#lib/python-pipeline";
import { isCapabilityActive } from "#lib/toolbelt";

/**
 * REA skills runner (the six approved Bin-1 skills).
 *
 * One tool, six verbs. The upstream bundle ships 22 skills; only the six that
 * need nothing beyond a local Python were approved. This tool cannot reach the
 * other sixteen — they are not vendored, and the runner refuses any skill id
 * outside the approved set.
 *
 * Gated behind the `rea_skills` Toolbelt limb. It is a separate category from
 * `rea` because these skills need no analysis engine — a session that only
 * audits evidence should not have to open Ghidra's lane.
 */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("rea_skills")
        ? defineTool({
  description:
    "Run one of six local reverse-engineering skills: verify_evidence, audit_reconstruction, parity_check, build_fixtures, forkdive, discover. All run locally and offline except forkdive/discover (network).",
  inputSchema: z.object({
    action: z
      .enum([
        "verify_evidence",
        "audit_reconstruction",
        "parity_check",
        "build_fixtures",
        "forkdive",
        "discover",
        "list",
      ])
      .describe("Which skill step to run."),
    files: z
      .array(z.string())
      .optional()
      .describe("Evidence JSON files (verify_evidence)."),
    claims: z.string().optional().describe("claims.json to cross-check."),
    config_dir: z.string().optional().describe("Config dir (audit_reconstruction)."),
    reference: z.string().optional().describe("Reference command (parity_check)."),
    candidate: z.string().optional().describe("Candidate command (parity_check)."),
    scenarios: z.string().optional().describe("Scenario corpus JSON (parity_check)."),
    out: z.string().optional().describe("Output dir (build_fixtures)."),
    repo: z.string().optional().describe("OWNER/REPO (forkdive)."),
    topics: z.array(z.string()).optional().describe("Topics (discover)."),
    min_stars: z.number().int().optional().describe("Min stars (discover)."),
    work_dir: z.string().optional().describe("Working dir inside the EMPIRE scratch root."),
  }),
  async execute(input) {
    const args: string[] = [];
    switch (input.action) {
      case "list":
        args.push("list");
        break;
      case "verify_evidence":
        if (!input.files?.length) {
          return { ok: false, error: "verify_evidence needs at least one evidence file" };
        }
        args.push("verify-evidence", ...input.files);
        if (input.claims) {
          args.push("--claims", input.claims);
        }
        break;
      case "audit_reconstruction":
        if (!input.config_dir) {
          return { ok: false, error: "audit_reconstruction needs config_dir" };
        }
        args.push("audit-reconstruction", "--config-dir", input.config_dir);
        break;
      case "parity_check":
        if (!input.reference || !input.candidate || !input.scenarios) {
          return {
            ok: false,
            error: "parity_check needs reference, candidate and scenarios",
          };
        }
        args.push(
          "parity",
          "--reference",
          input.reference,
          "--candidate",
          input.candidate,
          "--scenarios",
          input.scenarios,
        );
        break;
      case "build_fixtures":
        args.push("build-fixtures");
        if (input.out) {
          args.push("--out", input.out);
        }
        break;
      case "forkdive":
        if (!input.repo) {
          return { ok: false, error: "forkdive needs repo as OWNER/REPO" };
        }
        args.push("forkdive", input.repo);
        break;
      case "discover":
        args.push("discover");
        if (input.topics?.length) {
          args.push("--topics", ...input.topics);
        }
        if (input.min_stars != null) {
          args.push("--min-stars", String(input.min_stars));
        }
        break;
    }
    if (input.work_dir) {
      args.push("--work-dir", input.work_dir);
    }
    return runPythonModule("pipeline.rea_skills", args);
  },
})
        : null,
  },
});
