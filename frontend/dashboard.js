document.addEventListener("alpine:init", function () {
  Alpine.data("empireCockpit", function () {
    return {
      view: "guard",
      pulse: {},
      workers: { workers: [] },
      services: [],
      lease: { tenant: "idle" },
      catalog: { stats: {}, options: {}, rows: [] },
      filters: { category: "", capability: "", trust: "" },
      catalogQuery: "",
      drawerOpen: false,
      activeModel: "qwen2.5:14b",
      lastUpdated: "",
      ingest: { keyword: "", log: "Scanner console ready. Ingestion workers are not wired to this cockpit yet.\n" },
      async init() {
        await this.refreshAll();
        setInterval(() => this.refreshAll(), 15000);
      },
      async getJson(url, options) {
        const response = await fetch(url, Object.assign({ cache: "no-store" }, options || {}));
        const body = await response.json().catch(() => ({}));
        if (!response.ok) throw new Error(body.error || "HTTP " + response.status);
        return body;
      },
      async refreshAll() {
        await Promise.all([this.loadGuard(), this.loadCatalog(), this.loadServices()]);
        this.lastUpdated = new Date().toLocaleTimeString();
      },
      async loadGuard() {
        try {
          const [pulse, workers, lease] = await Promise.all([
            this.getJson("/api/resource-pulse"),
            this.getJson("/api/workers/status"),
            this.getJson("/api/gpu-lease")
          ]);
          this.pulse = pulse;
          this.workers = workers;
          this.lease = lease;
        } catch (error) {
          this.pulse = { ok: false, headroom_ok: false, headroom_reasons: [error.message] };
        }
      },
      async loadCatalog() {
        try {
          const params = new URLSearchParams({ query: this.catalogQuery, category: this.filters.category, capability: this.filters.capability, trust: this.filters.trust });
          this.catalog = await this.getJson("/api/catalog?" + params.toString());
        } catch (error) {
          this.catalog = { stats: {}, options: {}, rows: [] };
        }
      },
      async loadServices() {
        try {
          const data = await this.getJson("/api/services/status");
          this.services = data.services || [];
        } catch (error) {
          this.services = [];
        }
      },
      get statusClass() {
        if (!this.pulse.ok || !this.pulse.headroom_ok) return "blocked";
        if ((this.pulse.ask_architect_first || []).length) return "approval";
        if (!(this.pulse.services && Object.values(this.pulse.services).every(Boolean))) return "limited";
        return "safe";
      },
      get statusLabel() {
        return { safe: "SAFE", limited: "LIMITED", blocked: "BLOCKED", approval: "ARCHITECT APPROVAL REQUIRED" }[this.statusClass];
      },
      get statusReason() {
        if (!this.pulse.ok) return "Resource diagnostics unavailable. Automatic admission is disabled.";
        if (this.pulse.headroom_reasons?.length) return "Action blocked: " + this.pulse.headroom_reasons.join("; ");
        if (this.pulse.ask_architect_first?.length) return "Heavy capabilities remain behind an Architect approval boundary.";
        return this.pulse.summary || "All local safety checks are within limits.";
      },
      get activeTools() {
        return this.pulse.inventory?.effective_tools || [];
      },
      formatMetric(source, available, total, unit) {
        const a = Number(source?.[available]); const t = Number(source?.[total]);
        return Number.isFinite(a) && Number.isFinite(t) ? `${a.toFixed(1)} / ${t.toFixed(1)} ${unit}` : "Unavailable";
      },
      formatVram() { return `${(Number(this.pulse.nvidia?.vram_free_mb || 0) / 1024).toFixed(2)} / ${(Number(this.pulse.nvidia?.vram_total_mb || 0) / 1024).toFixed(2)} GB free`; },
      meterStyle(value, total) { const ratio = Number(total) > 0 ? Math.max(0, Math.min(100, Number(value) / Number(total) * 100)) : 0; return `width:${ratio}%`; },
      diskValue(letter) { return letter === "C" ? `${Number(this.pulse.resources?.disk_free_gb || 0).toFixed(1)} GB` : (letter === "V" ? "Cognee" : "T7 / data"); },
      scoreStyle(score) { return `width:${Math.max(0, Math.min(5, Number(score || 0))) * 20}%`; },
      async releaseLease() {
        try { await this.getJson("/api/gpu-lease", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ action: "release" }) }); await this.loadGuard(); }
        catch (error) { this.ingest.log += `\n[error] ${error.message}`; }
      },
      async runVerify() {
        try { await this.getJson("/api/verify/stack", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ skipCognee: false }) }); await this.refreshAll(); }
        catch (error) { this.ingest.log += `\n[verify] ${error.message}`; }
      },
      logIngest(mode) {
        const keyword = this.ingest.keyword ? ` (${this.ingest.keyword})` : "";
        this.ingest.log += `\n[${new Date().toLocaleTimeString()}] ${mode}${keyword}: no ingestion endpoint is registered yet; catalog remains read-only.`;
      }
    };
  });
});
