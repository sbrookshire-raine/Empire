import { defineTool } from "eve/tools";
import { z } from "zod";
import { ensureLightCapability } from "#lib/ensure-capability";
import { runPythonModule } from "#lib/python-pipeline";

export default defineTool({
  description:
    "Fetch one public http(s) page URL and cache markdown under 04_Thought_Experiments/web_cache. " +
    "Not a search engine — needs a full URL. Auto-admits Web Scout when headroom allows. Does NOT write Cognee.",
  inputSchema: z.object({
    url: z
      .string()
      .min(1)
      .describe("Full page URL to fetch (https://…). Bare domains ok; not a search query."),
    note: z.string().optional().describe("Optional Architect note."),
  }),
  async execute({ url, note }) {
    const gate = await ensureLightCapability("web_scout", `web scout: ${url}`);
    if (!gate.ok) {
      return gate;
    }
    const args = [url];
    if (note) {
      args.push("--note", note);
    }
    return runPythonModule("pipeline.web_scout", args);
  },
});
