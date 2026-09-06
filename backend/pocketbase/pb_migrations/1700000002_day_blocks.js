/// <reference path="../pb_data/types.d.ts" />

// EMPIRE Phase 5 — DAZE day blocks (local time reclaim; no Firebase).
migrate((app) => {
    const dayBlocks = new Collection({
        name: "day_blocks",
        type: "base",
        listRule: "",
        viewRule: "",
        createRule: "",
        updateRule: "",
        deleteRule: "",
        fields: [
            {
                name: "date",
                type: "text",
                required: true,
                min: 10,
                max: 10,
            },
            { name: "title", type: "text", required: true, min: 1, max: 255 },
            { name: "start_minute", type: "number", required: true },
            { name: "end_minute", type: "number", required: true },
            {
                name: "kind",
                type: "select",
                required: true,
                maxSelect: 1,
                values: ["focus", "body", "admin", "creative", "rest", "other"],
            },
            {
                name: "phase",
                type: "select",
                required: true,
                maxSelect: 1,
                values: ["planned", "actual"],
            },
            { name: "notes", type: "text", required: false, max: 5000 },
            { name: "color", type: "text", required: false, max: 32 },
            { name: "created", type: "autodate", onCreate: true, onUpdate: false },
            { name: "updated", type: "autodate", onCreate: true, onUpdate: true },
        ],
    });
    app.save(dayBlocks);
}, (app) => {
    try {
        const collection = app.findCollectionByNameOrId("day_blocks");
        app.delete(collection);
    } catch (_) {}
});
