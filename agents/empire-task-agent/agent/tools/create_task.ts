import { defineTool } from "eve/tools";
import { z } from "zod";
import { createTask } from "#lib/pocketbase";

export default defineTool({
  description:
    "Create a new PocketBase task. Never use for questions about projects in Cognee memory or workbench knowledge.",
  inputSchema: z.object({
    title: z.string().min(1).max(255),
    description: z.string().max(5000).optional(),
    status: z.enum(["todo", "in_progress", "done"]).optional(),
    priority: z.number().int().min(0).max(999).optional(),
  }),
  async execute(input) {
    const task = await createTask(input);
    return {
      id: task.id,
      title: task.title,
      status: task.status,
      priority: task.priority,
      created: task.created,
    };
  },
});
