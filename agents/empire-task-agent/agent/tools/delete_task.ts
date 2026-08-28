import { defineTool } from "eve/tools";
import { once } from "eve/tools/approval";
import { z } from "zod";
import { deleteTask } from "#lib/pocketbase";

export default defineTool({
  description: "Delete a PocketBase task by id. Requires approval once per session.",
  inputSchema: z.object({
    id: z.string().min(1),
  }),
  approval: once(),
  async execute({ id }) {
    return deleteTask(id);
  },
});
