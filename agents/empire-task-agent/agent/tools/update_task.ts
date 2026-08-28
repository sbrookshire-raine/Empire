import { defineTool } from "eve/tools";
import { z } from "zod";
import { updateTask } from "#lib/pocketbase";

export default defineTool({
  description: "Update an existing PocketBase task by id.",
  inputSchema: z.object({
    id: z.string().min(1),
    title: z.string().min(1).max(255).optional(),
    description: z.string().max(5000).optional(),
    status: z.enum(["todo", "in_progress", "done"]).optional(),
    priority: z.number().int().min(0).max(999).optional(),
  }),
  async execute({ id, ...patch }) {
    const task = await updateTask(id, patch);
    return {
      id: task.id,
      title: task.title,
      description: task.description,
      status: task.status,
      priority: task.priority,
      updated: task.updated,
    };
  },
});
