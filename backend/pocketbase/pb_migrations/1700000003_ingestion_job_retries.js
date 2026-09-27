/// <reference path="../pb_data/types.d.ts" />

// EMPIRE P3 — retry scheduling and quarantine for ingestion_jobs.
//
// Measured 2026-09-27: 14 of 544 job rows were stuck in "running" with no way to say "try again at 10:04". The
// status vocabulary had exactly one terminal failure state, "failed", so an interrupted process and a genuine
// error were indistinguishable, and the stale-job cleanup could only close both.
//
//   retry_count      attempts already made (survives process death, unlike an in-process sleep)
//   max_retries      per-row ceiling so one pathological file cannot retry forever
//   next_run_at      when the row becomes eligible again; null means "no schedule"
//   failure_reason   interrupted | transient | permanent (see pipeline/job_schedule.py)
//   status           + dead_letter: quarantined, needs a human — distinct from an ordinary failure
//
// The existing `error` field holds the last error text and is NOT duplicated.
migrate((app) => {
    const collection = app.findCollectionByNameOrId("ingestion_jobs");

    collection.fields.add(new NumberField({ name: "retry_count", required: false }));
    collection.fields.add(new NumberField({ name: "max_retries", required: false }));
    collection.fields.add(new DateField({ name: "next_run_at", required: false }));
    collection.fields.add(new SelectField({
        name: "failure_reason",
        required: false,
        maxSelect: 1,
        values: ["interrupted", "transient", "permanent"],
    }));

    const status = collection.fields.getByName("status");
    status.values = ["pending", "running", "success", "failed", "dead_letter"];

    app.save(collection);
}, (app) => {
    const collection = app.findCollectionByNameOrId("ingestion_jobs");

    for (const name of ["retry_count", "max_retries", "next_run_at", "failure_reason"]) {
        const field = collection.fields.getByName(name);
        if (field) {
            collection.fields.removeById(field.id);
        }
    }

    const status = collection.fields.getByName("status");
    status.values = ["pending", "running", "success", "failed"];

    app.save(collection);
});
