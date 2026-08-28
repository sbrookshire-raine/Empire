/// <reference path="../pb_data/types.d.ts" />

// Adds "wikipedia" to the source_type / type select options so the Wikipedia
// ingestion pipeline can log batch jobs in ingestion_jobs.
migrate((app) => {
    const withWikipedia = ["slack", "github", "email", "mock", "wikipedia"];

    const ingestionJobs = app.findCollectionByNameOrId("ingestion_jobs");
    const jobField = ingestionJobs.fields.getByName("source_type");
    jobField.values = withWikipedia;
    app.save(ingestionJobs);

    const sources = app.findCollectionByNameOrId("sources");
    const typeField = sources.fields.getByName("type");
    typeField.values = withWikipedia;
    app.save(sources);
}, (app) => {
    const original = ["slack", "github", "email", "mock"];

    try {
        const ingestionJobs = app.findCollectionByNameOrId("ingestion_jobs");
        const jobField = ingestionJobs.fields.getByName("source_type");
        jobField.values = original;
        app.save(ingestionJobs);
    } catch (_) {}

    try {
        const sources = app.findCollectionByNameOrId("sources");
        const typeField = sources.fields.getByName("type");
        typeField.values = original;
        app.save(sources);
    } catch (_) {}
});
