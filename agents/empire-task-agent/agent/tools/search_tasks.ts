import { defineTool } from "eve/tools";
import { z } from "zod";
import { searchTasks } from "#lib/pocketbase";

export default defineTool({
  description: "Search tasks by title or description substring.",
  inputSchema: z.object({
    query: z.string().min(1),
    perPage: z.number().int().min(1).max(100).optional(),
  }),
  async execute({ query, perPage }) {
    const data = await searchTasks(query, perPage);
    return {
      query,
      totalItems: data.totalItems,
      items: data.items.map((task) => ({
        id: task.id,
        title: task.title,
        status: task.status,
        priority: task.priority,
      })),
    };
  },
});
