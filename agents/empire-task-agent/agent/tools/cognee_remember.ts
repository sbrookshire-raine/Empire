import { defineTool } from "eve/tools";
import { z } from "zod";
import { cogneeRemember } from "#lib/cognee";

export default defineTool({
  description:
    "Store a short note in local Cognee graph memory for later recall.",
  inputSchema: z.object({
    content: z.string().min(1).max(8000),
    dataset: z.string().optional().default("eve_memory"),
  }),
  async execute({ content, dataset }) {
    const result = await cogneeRemember(content, dataset);
    return { stored: true, dataset, chars: content.length, result };
  },
});
