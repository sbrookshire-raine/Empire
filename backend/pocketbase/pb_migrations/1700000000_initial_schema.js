/// <reference path="../pb_data/types.d.ts" />

migrate((app) => {
    const tasks = new Collection({
        name: "tasks",
        type: "base",
        listRule: "",
        viewRule: "",
        createRule: "",
        updateRule: "",
        deleteRule: "",
        fields: [
            { name: "title", type: "text", required: true, min: 1, max: 255 },
            { name: "description", type: "text", required: false, max: 5000 },
            {
                name: "status",
                type: "select",
                required: true,
                maxSelect: 1,
                values: ["todo", "in_progress", "done"],
            },
            { name: "priority", type: "number", required: false },
            { name: "created", type: "autodate", onCreate: true, onUpdate: false },
            { name: "updated", type: "autodate", onCreate: true, onUpdate: true },
        ],
    });

    const ingestionJobs = new Collection({
        name: "ingestion_jobs",
        type: "base",
        listRule: "",
        viewRule: "",
        createRule: "",
        updateRule: "",
        deleteRule: "",
        fields: [
            {
                name: "source_type",
                type: "select",
                required: true,
                maxSelect: 1,
                values: ["slack", "github", "email", "mock"],
            },
            { name: "source_file", type: "text", required: false, max: 500 },
            {
                name: "status",
                type: "select",
                required: true,
                maxSelect: 1,
                values: ["pending", "running", "success", "failed"],
            },
            { name: "records_ingested", type: "number", required: false },
            { name: "error", type: "text", required: false, max: 5000 },
            { name: "started_at", type: "date", required: false },
            { name: "finished_at", type: "date", required: false },
            { name: "created", type: "autodate", onCreate: true, onUpdate: false },
            { name: "updated", type: "autodate", onCreate: true, onUpdate: true },
        ],
    });

    const sources = new Collection({
        name: "sources",
        type: "base",
        listRule: "",
        viewRule: "",
        createRule: "",
        updateRule: "",
        deleteRule: "",
        fields: [
            {
                name: "type",
                type: "select",
                required: true,
                maxSelect: 1,
                values: ["slack", "github", "email", "mock"],
            },
            { name: "name", type: "text", required: true, min: 1, max: 255 },
            { name: "enabled", type: "bool", required: false },
            { name: "last_sync_at", type: "date", required: false },
            { name: "created", type: "autodate", onCreate: true, onUpdate: false },
            { name: "updated", type: "autodate", onCreate: true, onUpdate: true },
        ],
    });

    app.save(tasks);
    app.save(ingestionJobs);
    app.save(sources);
}, (app) => {
    const names = ["tasks", "ingestion_jobs", "sources"];
    for (const name of names) {
        try {
            const collection = app.findCollectionByNameOrId(name);
            app.delete(collection);
        } catch (_) {}
    }
});
