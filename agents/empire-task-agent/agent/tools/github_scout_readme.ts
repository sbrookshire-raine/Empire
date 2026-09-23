import { defineDynamic, defineTool } from "eve/tools";
import { z } from "zod";
import { ensureLightCapability } from "#lib/ensure-capability";
import { runPythonModule } from "#lib/python-pipeline";
import { isCapabilityActive } from "#lib/toolbelt";

export default defineDynamic({
  events: {
    "turn.started": () =>
      isCapabilityActive("github_scout")
        ? defineTool({
  description:
    "Fetch README excerpt for a GitHub repo (owner/name). Scratch cache only. " +
    "Auto-admits GitHub Scout when headroom allows. Never claim you lack GitHub access — call this tool.",
  inputSchema: z.object({
    repo: z.string().min(1).describe("Repository slug owner/name (e.g. modelcontextprotocol/servers)."),
    note: z.string().optional().describe("Optional Architect note."),
  }),
  async execute({ repo, note }) {
    const gate = await ensureLightCapability("github_scout", `github readme: ${repo}`);
    if (!gate.ok) {
      return gate;
    }
    const args = ["readme", repo];
    if (note) {
      args.push("--note", note);
    }
    return runPythonModule("pipeline.github_scout", args);
  },
})
        : null,
  },
});
