import { defineTool } from "eve/tools";
import { z } from "zod";
import { cogneeImprove } from "#lib/cognee";

export default defineTool({
  description:
    "Run a Cognee improve/enrichment pass on a dataset after remember or ingest.",
  inputSchema: z.object({
    dataset: z
      .string()
      .optional()
      .default("eve_memory")
      ,
  }),
  async execute({ dataset }) {
    const result = await cogneeImprove(dataset);
    return { dataset, result };
  },
});
