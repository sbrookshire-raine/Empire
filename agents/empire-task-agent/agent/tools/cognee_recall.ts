import { defineTool } from "eve/tools";
import { z } from "zod";
import { cogneeRecall } from "#lib/cognee";

export default defineTool({
  description:
    "Query Cognee graph memory. Use dataset eve_memory for Workbench uploads, primitives_test for curated primitives.",
  inputSchema: z.object({
    query: z.string().min(1),
    dataset: z
      .string()
      .optional()
      .describe("eve_memory (Workbench), primitives_test (curated), or omit for default search"),
  }),
  async execute({ query, dataset }) {
    const result = await cogneeRecall(query, dataset);
    return { query, dataset: dataset ?? null, result };
  },
});
