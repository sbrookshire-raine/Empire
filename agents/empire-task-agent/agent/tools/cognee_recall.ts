import { defineTool } from "eve/tools";
import { z } from "zod";
import { cogneeRecall } from "#lib/cognee";

export default defineTool({
  description:
    "Query Cognee graph memory. Prefer dataset eve_core for fast chat recall; eve_memory for uploads/archive; primitives_test for curated primitives.",
  inputSchema: z.object({
    query: z.string().min(1),
    dataset: z
      .string()
      .optional()
      .describe("eve_core (fast recall), eve_memory (archive), primitives_test (curated)"),
  }),
  async execute({ query, dataset }) {
    const result = await cogneeRecall(query, dataset);
    return { query, dataset: dataset ?? null, result };
  },
});
