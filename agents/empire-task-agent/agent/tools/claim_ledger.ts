import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import {
  claimAdd,
  claimHealth,
  claimList,
  claimVerify,
} from "#lib/claim-ledger-mcp";
import { isCapabilityActive } from "#lib/toolbelt";

/**
 * Claim ledger — knowledge that is done, not read.
 *
 * A claim without a check is a document. A claim with a passing check is a
 * capability. A claim with a failing check is a known-false. This limb holds
 * claims for *execution*: Eve does not recall "binwalk extracts squashfs", it
 * runs the check and learns whether that is still true today.
 *
 * It is deliberately not a second memory store — it stores no prose for
 * retrieval and embeds nothing. Cognee keeps text for recall; this keeps
 * (claim, check, last_result).
 */
export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("claim_ledger")
        ? defineTool({
  description:
    "Record and re-check claims that carry the command that would prove them wrong. Add a claim with its check, verify the ledger, read its health, or list unchecked/failing claims. Offline, local SQLite.",
  inputSchema: z.object({
    action: z
      .enum(["add", "verify", "health", "list"])
      .describe("add a claim, run the checks, read health, or list claims."),
    claim: z.string().optional().describe("The claim text (action=add)."),
    check_cmd: z
      .string()
      .optional()
      .describe("Command that would prove the claim wrong (action=add)."),
    grade: z
      .enum([
        "promotional",
        "community-reported",
        "first-party-documented",
        "independently-corroborated",
        "reproduced",
      ])
      .optional()
      .describe("How well supported the claim is (action=add)."),
    slug: z.string().optional().describe("One claim to check (action=verify)."),
    unchecked: z.boolean().optional().describe("Only claims with no check."),
    failing: z.boolean().optional().describe("Only claims whose check failed."),
  }),
  async execute(input) {
    switch (input.action) {
      case "add": {
        if (!input.claim) {
          return { ok: false, error: "claim text is required" };
        }
        return claimAdd(input.claim, input.check_cmd, input.grade, "");
      }
      case "verify":
        return claimVerify(input.slug);
      case "health":
        return claimHealth();
      default:
        return claimList({ unchecked: input.unchecked, failing: input.failing });
    }
  },
})
        : null,
  },
});
