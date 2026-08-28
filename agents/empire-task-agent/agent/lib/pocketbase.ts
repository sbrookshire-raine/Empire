import { POCKETBASE_URL } from "#lib/empire";

export type TaskStatus = "todo" | "in_progress" | "done";

export interface TaskRecord {
  id: string;
  collectionId: string;
  collectionName: string;
  title: string;
  description?: string;
  status: TaskStatus;
  priority?: number;
  created: string;
  updated: string;
}

interface ListResponse {
  page: number;
  perPage: number;
  totalItems: number;
  totalPages: number;
  items: TaskRecord[];
}

async function pbFetch<T>(urlPath: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${POCKETBASE_URL}${urlPath}`, init);
  if (!response.ok) {
    const body = await response.text();
    throw new Error(`PocketBase ${response.status}: ${body}`);
  }
  if (response.status === 204) {
    return undefined as T;
  }
  return (await response.json()) as T;
}

export async function checkPocketBaseHealth(): Promise<{ message: string }> {
  return pbFetch("/api/health");
}

export async function listTasks(options?: {
  sort?: string;
  perPage?: number;
  filter?: string;
}): Promise<ListResponse> {
  const params = new URLSearchParams({
    sort: options?.sort ?? "-created",
    perPage: String(options?.perPage ?? 50),
  });
  if (options?.filter) {
    params.set("filter", options.filter);
  }
  return pbFetch(`/api/collections/tasks/records?${params}`);
}

export async function searchTasks(
  query: string,
  perPage = 50,
): Promise<ListResponse> {
  const safe = query.replace(/"/g, '\\"');
  const filter = `title ~ "${safe}" || description ~ "${safe}"`;
  return listTasks({ filter, perPage });
}

export async function createTask(input: {
  title: string;
  description?: string;
  status?: TaskStatus;
  priority?: number;
}): Promise<TaskRecord> {
  return pbFetch("/api/collections/tasks/records", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      title: input.title,
      description: input.description ?? "",
      status: input.status ?? "todo",
      priority: input.priority ?? 1,
    }),
  });
}

export async function updateTask(
  id: string,
  patch: Partial<{
    title: string;
    description: string;
    status: TaskStatus;
    priority: number;
  }>,
): Promise<TaskRecord> {
  return pbFetch(`/api/collections/tasks/records/${id}`, {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(patch),
  });
}

export async function deleteTask(
  id: string,
): Promise<{ deleted: true; id: string }> {
  await pbFetch(`/api/collections/tasks/records/${id}`, { method: "DELETE" });
  return { deleted: true, id };
}
