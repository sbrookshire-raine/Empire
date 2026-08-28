import { defineTool } from "eve/tools";
import { z } from "zod";
import { once } from "eve/tools/approval";
import { cogneeForget } from "#lib/cognee";

export default defineTool({
  description:
    "Remove a Cognee dataset from local graph memory. Destructive — requires approval.",
  inputSchema: z.object({
    dataset: z
      .string()
      .min(1)
      .describe("Dataset to forget, e.g. eve_memory or primitives_test"),
  }),
  approval: once(),
  async execute({ dataset }) {
    const result = await cogneeForget(dataset);
    return { dataset, result };
  },
});
