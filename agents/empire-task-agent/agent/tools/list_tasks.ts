import { defineTool } from "eve/tools";
import { z } from "zod";
import { listTasks } from "#lib/pocketbase";

export default defineTool({
  description: "List tasks from PocketBase, newest first.",
  inputSchema: z.object({
    perPage: z.number().int().min(1).max(100).optional(),
    status: z.enum(["todo", "in_progress", "done"]).optional(),
  }),
  async execute({ perPage, status }) {
    const filter = status ? `status = "${status}"` : undefined;
    const data = await listTasks({ perPage, filter });
    return {
      totalItems: data.totalItems,
      items: data.items.map((task) => ({
        id: task.id,
        title: task.title,
        description: task.description,
        status: task.status,
        priority: task.priority,
        updated: task.updated,
      })),
    };
  },
});
