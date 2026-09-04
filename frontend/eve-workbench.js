(function () {
  "use strict";

  var MAX_FILE_BYTES = 50 * 1024 * 1024;
  var MAX_FILES = 20;
  var ALLOWED_EXTENSIONS = [".md", ".txt", ".pdf"];
  var DIRECTIVE_FILENAME = "SYSTEM.md";
  var TOOL_LABELS = {
    cognee_recall: "Searching memory…",
    cognee_remember: "Saving memory…",
    cognee_improve: "Improving memory graph…",
    cognee_forget: "Preparing to clear memory…",
    list_tasks: "Reading PocketBase tasks…",
    search_tasks: "Searching PocketBase tasks…",
    create_task: "Creating a PocketBase task…",
    update_task: "Updating a PocketBase task…",
    delete_task: "Preparing to delete a PocketBase task…",
    get_model_suite: "Reading model suite plan…",
    list_models: "Listing Ollama models…",
    switch_chat_model: "Switching chat model…",
    ollama_health: "Checking Ollama…",
    pb_health: "Checking PocketBase…",
    workbench_list_dir: "Scanning workbench folders…",
    workbench_read_file: "Reading workbench file…",
    read_active_tool: "Reading Active Tools file…",
    draft_work_order: "Filing a Work Order for the Mechanic…",
    check_workbench_health: "Checking Workbench health…",
  };
  var DEFAULT_CHAT_MODES = [
    {
      id: "fast",
      label: "Fast Mode (14b)",
      description:
        "Daily driver — brainstorming, quick file reads, standard scripts, and tool calls.",
      model: "richardyoung/qwen2.5-14b-instruct-abliterated:latest",
      numCtx: 8192,
      temperature: 0.2,
    },
    {
      id: "deep",
      label: "Deep Mode (32b)",
      description: "Architect — deep planning, complex MCP work, and highest-tier reasoning.",
      model: "qwen2.5:32b",
      numCtx: 8192,
      temperature: 0.7,
    },
    {
      id: "librarian",
      label: "Librarian (Command-R 35b)",
      description:
        "Mass synthesis — cross-reference many flattened files and long memory snippets.",
      model: "command-r:35b",
      numCtx: 8192,
      temperature: 0.4,
    },
  ];
  var SERVICE_LABELS = {
    eve: "Eve",
    memory: "Memory",
    pocketbase: "PocketBase",
    ollama: "Ollama",
  };

  function plainText(value) {
    var node = document.createElement("span");
    node.textContent = typeof value === "string" ? value : "";
    return node.textContent;
  }

  function errorMessage(payload, fallback) {
    return plainText(payload && (payload.error || payload.message)) || fallback;
  }

  var REPLY_FLASH_MS = 900;

  function triggerReplyFlash() {
    if (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      return;
    }
    var body = document.body;
    if (!body) return;
    body.classList.remove("storm-reply-flash");
    void body.offsetWidth;
    body.classList.add("storm-reply-flash");
    window.setTimeout(function () {
      body.classList.remove("storm-reply-flash");
    }, REPLY_FLASH_MS);
  }

  function fileExtension(name) {
    var normalized = String(name || "").toLowerCase();
    var dot = normalized.lastIndexOf(".");
    return dot >= 0 ? normalized.slice(dot) : "";
  }

  function formatBytes(bytes) {
    if (bytes < 1024) return bytes + " B";
    if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + " KiB";
    return (bytes / (1024 * 1024)).toFixed(1) + " MiB";
  }

  function validateFiles(files) {
    if (!files.length) return "Choose at least one Markdown, text, or PDF file.";
    if (files.length > MAX_FILES) return "Choose 20 files or fewer, then try again.";
    for (var index = 0; index < files.length; index += 1) {
      var file = files[index];
      var normalizedPath = String(file.webkitRelativePath || file.name).replace(/\\/g, "/");
      var basename = String(file.name || "");
      var upperName = basename.toUpperCase();
      if (
        upperName === DIRECTIVE_FILENAME.toUpperCase() ||
        upperName.indexOf("LENS_") === 0 ||
        normalizedPath.toLowerCase().split("/").indexOf("directives") >= 0
      ) {
        return basename + " is a directive file and cannot be added to memory.";
      }
      if (ALLOWED_EXTENSIONS.indexOf(fileExtension(basename)) < 0) {
        return basename + " must be a .md, .txt, or .pdf file.";
      }
      if (file.size <= 0) return basename + " is empty. Choose a file with content.";
      if (file.size > MAX_FILE_BYTES) {
        return basename + " is larger than 50 MiB. Choose a smaller file.";
      }
    }
    return "";
  }

  function displayToolName(name) {
    return String(name || "local tool")
      .replace(/[_-]+/g, " ")
      .replace(/\b\w/g, function (letter) {
        return letter.toUpperCase();
      });
  }

  function isPrivateEventType(type) {
    var normalized = String(type || "")
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, ".")
      .replace(/^\.+|\.+$/g, "");
    var tokens = normalized.split(".");
    return tokens.indexOf("reasoning") >= 0 || tokens.indexOf("thinking") >= 0;
  }

  function actionToolName(action) {
    if (!action || typeof action !== "object") return "";
    return plainText(
      action.toolName ||
        action.actionName ||
        action.name ||
        (action.tool && action.tool.name) ||
        ""
    );
  }

  function normalizeOptions(request) {
    var options = Array.isArray(request && request.options) ? request.options : [];
    if (!options.length && request && request.type === "approval") {
      options = [
        { id: "approve", label: "Approve" },
        { id: "deny", label: "Deny" },
      ];
    }
    return options.map(function (option, index) {
      if (typeof option === "string") {
        return { id: option, label: option };
      }
      return {
        id: plainText(option && (option.optionId || option.id || option.value)) || String(index + 1),
        label:
          plainText(option && (option.label || option.title || option.value || option.id)) ||
          "Option " + String(index + 1),
      };
    });
  }

  function initialHealth() {
    return Object.keys(SERVICE_LABELS).map(function (id) {
      return {
        id: id,
        label: SERVICE_LABELS[id],
        state: "checking",
        status: "Checking",
        symbol: "·",
      };
    });
  }

  var POCKETBASE_URL = "http://127.0.0.1:8090";
  var TASK_STATUSES = ["todo", "in_progress", "done"];

  function emptyTaskDraft() {
    return { title: "", description: "", status: "todo", priority: 1 };
  }

  window.eveWorkbench = function () {
    return {
      selectedFiles: [],
      rawFiles: [],
      dragActive: false,
      dataset: "eve_memory",
      fullGraph: false,
      uploading: false,
      activeJob: null,
      uploadedContext: null,
      recentJobs: [],
      memoryError: "",
      pollTimer: null,
      pollInFlight: false,
      pollGeneration: 0,
      draft: "",
      sessionId: null,
      continuationToken: null,
      streamIndex: 0,
      messages: [],
      activities: [],
      pendingInputs: [],
      sending: false,
      chatError: "",
      chatStatus: "Ready for a local conversation.",
      streamController: null,
      requestController: null,
      cancelController: null,
      chatGeneration: 0,
      streamReader: null,
      currentAssistantId: null,
      nextId: 1,
      historyOpen: false,
      historyLoading: false,
      chatHistory: [],
      historyChatId: null,
      historyChatCreatedAt: null,
      persistTimer: null,
      ollamaModels: [],
      chatModes: [],
      selectedMode: "fast",
      toolbeltOpen: true,
      toolbeltCategories: [
        {
          id: "gumloop_cloud",
          label: "Gumloop Cloud",
          description: "Heavy remote workflows via Gumloop (external).",
        },
        {
          id: "web_research",
          label: "Web Research",
          description: "Firecrawl / Exa scraping and external web research.",
        },
        {
          id: "tool_forge",
          label: "Tool Forge",
          description: "Execute / read harvested 03_Active_Tools flattened scripts.",
        },
      ],
      activeTools: {
        gumloop_cloud: false,
        web_research: false,
        tool_forge: false,
      },
      activeMode: "fast",
      activeModeLabel: "Fast Mode (14b)",
      activeModeDescription: "",
      selectedModel: "",
      activeOllamaModel: "",
      ollamaConnected: false,
      ollamaStatus: "Checking Ollama…",
      switchingModel: false,
      tasks: [],
      taskFilter: "all",
      tasksLoading: false,
      taskError: "",
      taskDraft: emptyTaskDraft(),
      editingId: "",
      editDraft: emptyTaskDraft(),
      pendingDeleteId: "",
      activeTab: "chat",
      taskSummary: "",
      taskSummaryLoading: false,
      taskSummaryError: "",
      taskSummaryModel: "",
      taskOverviewOpen: false,
      taskSummaryStamp: "",
      memoryConfig: {
        embeddingModel: "nomic-embed-text:latest",
        embeddingProvider: "ollama",
        defaultDataset: "eve_memory",
        chatRecallDatasets: "eve_core, eve_memory",
      },
      eveCoreStatus: { ready: false, fileCount: 0 },
      memoryOptimizing: false,
      memoryOptimizeMessage: "",
      projects: [],
      projectsLoading: false,
      projectsError: "",
      projectsMeta: { projectCount: 0, inEveCoreCount: 0, flattenedCount: 0 },
      modelInventory: [],
      modelRecommendations: {
        summary: "",
        suite: [],
        skills: [],
        pullGaps: [],
        removeSuggestions: [],
        recommendedKeep: [],
        eveBriefing: "",
        optionalCleanup: [],
        eveGuidance: {},
      },
      modelInventoryLoading: false,
      modelInventoryError: "",
      health: {
        services: initialHealth(),
        summary: "Checking local services…",
        repairing: false,
      },

      get canUpload() {
        return this.rawFiles.length > 0 && !this.memoryError && !this.memoryLocked;
      },

      get memoryLocked() {
        return this.uploading || this.pollTimer !== null || this.pollInFlight;
      },

      get pendingInput() {
        return this.pendingInputs.length ? this.pendingInputs[0] : null;
      },

      get visibleTasks() {
        var filter = this.taskFilter;
        if (filter === "all") return this.tasks;
        return this.tasks.filter(function (task) {
          return task.status === filter;
        });
      },

      get modeHintText() {
        var modeId = plainText(this.selectedMode) || plainText(this.activeMode);
        var mode = (this.chatModes || []).find(function (item) {
          return item.id === modeId;
        });
        return plainText(mode && mode.description) || plainText(this.activeModeDescription);
      },

      get activeModeShortLabel() {
        var labels = { fast: "Fast", deep: "Deep", librarian: "Librarian" };
        return labels[this.activeMode] || labels[this.selectedMode] || "Mode";
      },

      get toolbeltToggleLabel() {
        var count = this.activeToolIds().length;
        if (!count) return "No tools selected";
        if (count === 1) return "1 tool category active";
        return count + " tool categories active";
      },

      activeToolIds: function () {
        var ids = [];
        var categories = this.toolbeltCategories || [];
        for (var i = 0; i < categories.length; i += 1) {
          var id = categories[i].id;
          if (this.activeTools[id]) ids.push(id);
        }
        return ids;
      },

      get compactChatStatus() {
        if (this.switchingModel) return "Switching mode…";
        if (!this.ollamaConnected) return this.ollamaStatus || "Ollama offline";
        return this.activeModeShortLabel + " · " + (this.activeOllamaModel || "ready");
      },

      get chatActivityLabel() {
        if (!this.sending) return "";
        var status = plainText(this.chatStatus);
        if (!status || /^ready/i.test(status)) return "Eve is thinking…";
        return status;
      },

      get thinkingLabel() {
        return this.chatActivityLabel || "Eve is thinking…";
      },

      get visibleMessages() {
        return (this.messages || []).filter(function (message) {
          return message.role === "user" || message.role === "assistant";
        });
      },

      get chatLineStatus() {
        var modeLabel = plainText(this.activeModeLabel) || "Eve chat";
        var model = this.activeOllamaModel || this.selectedModel;
        var modelPart = this.ollamaConnected
          ? model
            ? modeLabel + " · " + model
            : modeLabel + " · Ollama connected"
          : this.ollamaStatus || "Ollama unavailable";
        if (this.sending) {
          return modelPart + " · " + (plainText(this.chatStatus) || "Eve is working…");
        }
        var chatPart = plainText(this.chatStatus);
        if (!chatPart || chatPart === modelPart) return modelPart;
        if (/^ready\.?$/i.test(chatPart) || /^ready for a (new )?local conversation\.?$/i.test(chatPart)) {
          return modelPart;
        }
        return modelPart + " · " + chatPart;
      },

      get hasWorkingActivity() {
        return (this.activities || []).some(function (item) {
          return item.state === "working";
        });
      },

      get showThinkingIndicator() {
        return this.sending && !this.hasWorkingActivity && !this.currentAssistantText();
      },

      currentAssistantText: function () {
        if (!this.currentAssistantId) return "";
        var message = this.messages.find(
          function (item) {
            return item.id === this.currentAssistantId;
          }.bind(this)
        );
        return message ? plainText(message.text) : "";
      },

      init: function () {
        try {
          var saved = localStorage.getItem("eve-workbench-tab");
          if (saved && ["chat", "tasks", "memory", "projects", "models", "more"].indexOf(saved) >= 0) {
            this.activeTab = saved;
          }
        } catch (_error) {
          /* ignore storage errors */
        }
        this.refreshMemoryStatus();
        this.refreshHealth();
        this.refreshTasks();
        this.restoreChatHistoryOnBoot();
      },

      setTab: function (tab) {
        var allowed = ["chat", "tasks", "memory", "projects", "models", "more"];
        if (allowed.indexOf(tab) < 0) tab = "chat";
        this.activeTab = tab;
        try {
          localStorage.setItem("eve-workbench-tab", tab);
        } catch (_error) {
          /* ignore storage errors */
        }
        if (tab === "chat") this.scrollTranscript();
        if (tab === "models") this.refreshModelInventory(false);
        if (tab === "projects") this.refreshProjectsCatalog(false);
      },

      refreshProjectsCatalog: async function (rebuild) {
        this.projectsLoading = true;
        this.projectsError = "";
        try {
          var url = "/api/projects/catalog" + (rebuild ? "?rebuild=1" : "");
          var response = await fetch(url, { cache: "no-store" });
          var raw = await response.text();
          var payload;
          try {
            payload = JSON.parse(raw);
          } catch (_parseError) {
            throw new Error(
              response.ok
                ? "Projects API returned invalid JSON."
                : "Projects API unavailable — restart the frontend (port 8080) to load the latest server."
            );
          }
          if (!response.ok || !payload.ok) {
            throw new Error(errorMessage(payload, "Could not load project catalog."));
          }
          this.projects = Array.isArray(payload.projects) ? payload.projects : [];
          this.projectsMeta = {
            projectCount: payload.projectCount || this.projects.length,
            inEveCoreCount: payload.inEveCoreCount || 0,
            flattenedCount: payload.flattenedCount || 0,
          };
        } catch (error) {
          this.projectsError = plainText(error.message) || "Could not load project catalog.";
        } finally {
          this.projectsLoading = false;
        }
      },

      askAboutProject: function (displayName) {
        this.setTab("chat");
        this.draft =
          "Tell me about my " +
          plainText(displayName) +
          " project — purpose, evolution, and what you know from memory.";
      },

      applyModelInventory: function (payload) {
        if (!payload || typeof payload !== "object") return;
        this.modelInventory = Array.isArray(payload.models) ? payload.models : [];
        if (payload.recommendations && typeof payload.recommendations === "object") {
          this.modelRecommendations = payload.recommendations;
        }
        this.modelInventoryError = "";
      },

      fitLabel: function (fit) {
        var labels = {
          excellent: "Excellent fit",
          good: "Good fit",
          tight: "Tight fit",
          heavy: "Heavy (RAM offload)",
          embed: "Embed only",
        };
        return labels[fit] || "Unknown fit";
      },

      isActiveChatModel: function (modelId) {
        var active = plainText(this.activeOllamaModel || this.selectedModel);
        return Boolean(modelId) && active === plainText(modelId);
      },

      formatModelSkills: function (model) {
        var labels = {
          dailyChat: "Daily chat",
          coding: "Coding",
          reasoning: "Reasoning",
          deepQuality: "Deep quality",
          embedding: "Embed",
        };
        return (model && Array.isArray(model.skills) ? model.skills : [])
          .map(function (skill) {
            return labels[skill] || skill;
          })
          .join(", ");
      },

      suiteStatusLabel: function (status) {
        var labels = {
          covered: "Covered",
          weak: "Workable",
          gap: "Gap",
        };
        return labels[status] || status;
      },

      copyEveBriefing: async function () {
        var text = plainText(this.modelRecommendations.eveBriefing);
        if (!text) return;
        try {
          if (navigator.clipboard && navigator.clipboard.writeText) {
            await navigator.clipboard.writeText(text);
            this.modelInventoryError = "";
            this.chatStatus = "Eve briefing copied.";
            return;
          }
        } catch (_error) {
          /* fall through */
        }
        this.modelInventoryError = "Could not copy — select the briefing text manually.";
      },

      refreshModelInventory: async function (force) {
        if (
          !force &&
          this.modelInventory.length &&
          plainText(this.modelRecommendations.summary)
        ) {
          return;
        }
        this.modelInventoryLoading = true;
        this.modelInventoryError = "";
        try {
          var response = await fetch("/api/ollama/inventory", { cache: "no-store" });
          if (response.status === 404) {
            response = await fetch("/api/ollama/models", { cache: "no-store" });
          }
          var payload = await response.json().catch(function () {
            return {};
          });
          if (!response.ok || payload.ok === false) {
            throw new Error(errorMessage(payload, "Model roster is unavailable."));
          }
          if (payload.inventory) {
            this.applyModelInventory(payload.inventory);
          } else {
            this.applyModelInventory(payload);
          }
        } catch (error) {
          this.modelInventoryError =
            plainText(error.message) || "Model roster is unavailable.";
        } finally {
          this.modelInventoryLoading = false;
        }
      },

      selectChatModel: async function (modelId) {
        var model = plainText(modelId);
        var mode = (this.chatModes || []).find(function (item) {
          return item.model === model;
        });
        if (mode) {
          this.selectedMode = mode.id;
          this.setTab("chat");
          return this.applyChatMode();
        }
        if (!model || !this.ollamaModels.some(function (item) { return item.id === model; })) {
          this.modelInventoryError = "That model is not available for Eve chat.";
          return;
        }
        this.selectedModel = model;
        this.setTab("chat");
        await this.applyOllamaModel();
      },

      taskSummaryKey: function () {
        return this.tasks
          .map(function (task) {
            return [
              plainText(task.id),
              plainText(task.status),
              plainText(task.title),
              String(task.priority),
              plainText(task.description),
            ].join("|");
          })
          .join(";");
      },

      onTaskOverviewToggle: function (event) {
        var open = Boolean(event.target && event.target.open);
        this.taskOverviewOpen = open;
        if (open) this.refreshTaskSummary(false);
      },

      refreshTaskSummary: async function (force) {
        if (!this.taskOverviewOpen && !force) return;
        var stamp = this.taskSummaryKey();
        if (!force && stamp === this.taskSummaryStamp && this.taskSummary) return;
        this.taskSummaryLoading = true;
        this.taskSummaryError = "";
        try {
          if (!this.tasks.length && !this.tasksLoading) await this.refreshTasks();
          var response = await fetch("/api/ollama/summarize-tasks", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              tasks: this.tasks,
              model: this.activeOllamaModel || this.selectedModel || undefined,
            }),
          });
          var payload = await response.json().catch(function () {
            return {};
          });
          if (!response.ok || payload.ok === false) {
            throw new Error(errorMessage(payload, "Task summary is unavailable."));
          }
          this.taskSummary = plainText(payload.summary);
          this.taskSummaryModel = plainText(payload.model);
          this.taskSummaryStamp = stamp;
        } catch (error) {
          this.taskSummaryError =
            plainText(error.message) || "Task summary is unavailable.";
        } finally {
          this.taskSummaryLoading = false;
        }
      },

      setDrag: function (active) {
        if (this.memoryLocked) return;
        this.dragActive = active;
      },

      handleFileInput: function (event) {
        if (this.memoryLocked) {
          event.target.value = "";
          this.memoryError = "Wait for the active memory job before changing files.";
          return;
        }
        this.selectFiles(Array.from(event.target.files || []));
      },

      handleDrop: function (event) {
        this.dragActive = false;
        if (this.memoryLocked) {
          this.memoryError = "Wait for the active memory job before changing files.";
          return;
        }
        this.selectFiles(Array.from(event.dataTransfer.files || []));
      },

      selectFiles: function (files) {
        if (this.memoryLocked) {
          this.memoryError = "Wait for the active memory job before changing files.";
          return;
        }
        this.activeJob = null;
        this.uploadedContext = null;
        this.memoryError = validateFiles(files);
        this.rawFiles = this.memoryError ? [] : files;
        this.selectedFiles = files.map(function (file, index) {
          return {
            key: file.name + ":" + file.size + ":" + index,
            name: plainText(file.name),
            sizeLabel: formatBytes(file.size),
            status: "Selected",
            state: "selected",
            symbol: "○",
          };
        });
      },

      uploadFiles: async function () {
        if (this.memoryLocked) return;
        this.memoryError = validateFiles(this.rawFiles);
        if (this.memoryError) return;
        if (!/^[A-Za-z0-9_-]{1,64}$/.test(this.dataset)) {
          this.memoryError =
            "The dataset name must use 1–64 letters, numbers, underscores, or hyphens.";
          return;
        }

        this.uploading = true;
        this.updateSelectedStatus("Uploading", "working", "↻");
        var uploadDataset = this.dataset;
        var form = new FormData();
        this.rawFiles.forEach(function (file) {
          form.append("files", file, file.name);
        });
        form.append("dataset", this.dataset);
        form.append("full_graph", this.fullGraph ? "true" : "false");

        try {
          var response = await fetch("/api/memory/upload", {
            method: "POST",
            body: form,
          });
          var payload = await response.json();
          if (!response.ok || !payload.ok || !payload.job) {
            throw new Error(errorMessage(payload, "The files could not be added to memory."));
          }
          this.activeJob = payload.job;
          this.uploadedContext = {
            jobId: plainText(payload.job.id),
            dataset: plainText(payload.job.dataset) || uploadDataset,
            files: Array.isArray(payload.job.files)
              ? payload.job.files.map(function (file) {
                  return plainText(file && file.name);
                })
              : [],
          };
          this.upsertRecentJob(payload.job);
          this.applyJobToFiles(payload.job);
          this.startPolling(payload.job.id);
        } catch (error) {
          this.memoryError = plainText(error.message) || "The files could not be added to memory.";
          this.updateSelectedStatus("Failed", "failed", "×");
        } finally {
          this.uploading = false;
        }
      },

      updateSelectedStatus: function (status, state, symbol) {
        this.selectedFiles.forEach(function (file) {
          file.status = status;
          file.state = state;
          file.symbol = symbol;
        });
      },

      applyJobToFiles: function (job) {
        var label = plainText(job.label) || "Learning";
        var state = job.status === "ready" ? "ready" : job.status === "failed" ? "failed" : "working";
        var symbol = job.status === "ready" ? "✓" : job.status === "failed" ? "×" : "↻";
        this.updateSelectedStatus(label, state, symbol);
      },

      startPolling: function (jobId) {
        this.stopPolling();
        this.schedulePoll(jobId, this.pollGeneration, 0);
      },

      schedulePoll: function (jobId, generation, delay) {
        if (generation !== this.pollGeneration) return;
        var workbench = this;
        this.pollTimer = setTimeout(function () {
          workbench.pollTimer = null;
          workbench.pollJob(jobId, generation);
        }, delay);
      },

      stopPolling: function () {
        this.pollGeneration += 1;
        if (this.pollTimer !== null) {
          clearTimeout(this.pollTimer);
          this.pollTimer = null;
        }
      },

      pollJob: async function (jobId, generation) {
        if (generation !== this.pollGeneration) return;
        if (this.pollInFlight) {
          this.schedulePoll(jobId, generation, 100);
          return;
        }
        this.pollInFlight = true;
        var keepPolling = false;
        try {
          var response = await fetch("/api/memory/jobs/" + encodeURIComponent(jobId), {
            cache: "no-store",
          });
          var payload = await response.json();
          if (generation !== this.pollGeneration) return;
          if (!response.ok || !payload.ok || !payload.job) {
            throw new Error(errorMessage(payload, "Memory progress is unavailable."));
          }
          this.activeJob = payload.job;
          this.upsertRecentJob(payload.job);
          this.applyJobToFiles(payload.job);
          if (payload.job.status === "ready" || payload.job.status === "failed") {
            this.stopPolling();
          } else {
            keepPolling = true;
          }
        } catch (error) {
          if (generation !== this.pollGeneration) return;
          this.memoryError = plainText(error.message) || "Memory progress is unavailable.";
          this.stopPolling();
        } finally {
          this.pollInFlight = false;
          if (keepPolling && generation === this.pollGeneration) {
            this.schedulePoll(jobId, generation, 1000);
          }
        }
      },

      retryJob: async function (jobId) {
        this.memoryError = "";
        try {
          var response = await fetch(
            "/api/memory/jobs/" + encodeURIComponent(jobId) + "/retry",
            { method: "POST" }
          );
          var payload = await response.json();
          if (!response.ok || !payload.ok || !payload.job) {
            throw new Error(errorMessage(payload, "The memory job could not be retried."));
          }
          this.activeJob = payload.job;
          this.upsertRecentJob(payload.job);
          this.applyJobToFiles(payload.job);
          this.startPolling(jobId);
        } catch (error) {
          this.memoryError = plainText(error.message) || "The memory job could not be retried.";
        }
      },

      refreshMemoryStatus: async function () {
        try {
          var response = await fetch("/api/memory/status", { cache: "no-store" });
          var payload = await response.json();
          if (!response.ok || !payload.ok) return;
          if (payload.config && typeof payload.config === "object") {
            this.memoryConfig = Object.assign({}, this.memoryConfig, payload.config);
          }
          if (payload.eveCore && typeof payload.eveCore === "object") {
            this.eveCoreStatus = Object.assign({}, this.eveCoreStatus, payload.eveCore);
          }
          this.recentJobs = Array.isArray(payload.jobs)
            ? payload.jobs
                .slice()
                .sort(function (left, right) {
                  return String(right.updated_at || "").localeCompare(String(left.updated_at || ""));
                })
                .slice(0, 8)
            : [];
        } catch (_error) {
          return;
        }
      },

      optimizeMemory: async function (fresh) {
        this.memoryOptimizeMessage = "";
        this.memoryOptimizing = true;
        try {
          var response = await fetch("/api/memory/optimize", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ fresh: !!fresh, maxFiles: 75 }),
          });
          var payload = await response.json();
          if (!response.ok || !payload.ok) {
            throw new Error(errorMessage(payload, "Memory optimize failed."));
          }
          this.memoryOptimizeMessage =
            plainText(payload.message) ||
            "eve_core updated (" + String(payload.fileCount || 0) + " files).";
          await this.refreshMemoryStatus();
        } catch (error) {
          this.memoryOptimizeMessage = plainText(error.message) || "Memory optimize failed.";
        } finally {
          this.memoryOptimizing = false;
        }
      },

      upsertRecentJob: function (job) {
        this.recentJobs = [job]
          .concat(
            this.recentJobs.filter(function (recent) {
              return recent.id !== job.id;
            })
          )
          .slice(0, 8);
      },

      jobSymbol: function (job) {
        if (!job) return "·";
        if (job.status === "ready") return "✓";
        if (job.status === "failed") return "×";
        return "↻";
      },

      jobFileSummary: function (job) {
        var files = Array.isArray(job && job.files) ? job.files : [];
        return files.length
          ? files
              .map(function (file) {
                return plainText(file.name);
              })
              .join(", ")
          : "Memory job";
      },

      askAboutFiles: function () {
        if (!this.uploadedContext || !this.activeJob || this.activeJob.status !== "ready") return;
        var names = this.uploadedContext.files;
        this.draft =
          "Summarize the files I just added" +
          (names.length ? " (" + names.join(", ") + ")" : "") +
          " from dataset " +
          this.uploadedContext.dataset +
          ".";
        this.sendMessage();
      },

      askAboutFilesInChat: function () {
        this.setTab("chat");
        this.askAboutFiles();
      },

      beginChatOperation: function () {
        if (this.requestController) this.requestController.abort();
        this.chatGeneration += 1;
        this.requestController = new AbortController();
        return this.chatGeneration;
      },

      isCurrentChatOperation: function (generation) {
        return generation === this.chatGeneration;
      },

      invalidateChatOperation: async function () {
        this.chatGeneration += 1;
        if (this.requestController) this.requestController.abort();
        this.requestController = null;
        if (this.streamController) this.streamController.abort();
        this.streamController = null;
        if (this.streamReader) {
          await this.streamReader.cancel().catch(function () {});
        }
        this.streamReader = null;
      },

      scrollTranscript: function () {
        if (typeof this.$nextTick !== "function") return;
        this.$nextTick(
          function () {
            var transcript = this.$refs && this.$refs.transcript;
            if (!transcript) return;
            window.requestAnimationFrame(function () {
              transcript.scrollTop = transcript.scrollHeight;
            });
          }.bind(this)
        );
      },

      isMemoryQuery: function (text) {
        return /\b(?:memory|memories|interests?|interested|graph|recall|recalled|what do you know|what can you (?:tell|see)|what am i|my projects?|projects?|research|themes?|workbench|knowledge|from what|notes?|uploaded)\b/i.test(
          text
        );
      },

      answerFromMemory: async function (text, generation) {
        this.chatStatus = "Searching memory…";
        this.scrollTranscript();
        try {
          var response = await fetch("/api/memory/answer", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              query: text,
              fast: this.activeMode === "fast",
            }),
            signal: this.requestController.signal,
          });
          if (!this.isCurrentChatOperation(generation)) return;
          var payload = await response.json();
          if (!response.ok || !payload.ok) {
            throw new Error(errorMessage(payload, "Memory answer failed."));
          }
          triggerReplyFlash();
          this.messages.push({
            id: this.makeId("message"),
            role: "assistant",
            text: plainText(payload.answer) || "I could not form an answer from memory yet.",
            sources: Array.isArray(payload.sources) ? payload.sources : [],
            createdAt: new Date().toISOString(),
          });
          this.chatStatus = "Ready.";
          this.persistCurrentChat(true);
        } catch (error) {
          if (this.isCurrentChatOperation(generation) && error.name !== "AbortError") {
            this.chatError = plainText(error.message) || "Memory answer failed.";
            this.chatStatus = "Eve needs attention.";
          }
        } finally {
          if (this.isCurrentChatOperation(generation)) {
            this.sending = false;
            this.scrollTranscript();
          }
        }
      },

      onComposerKeydown: function (event) {
        if (event.key !== "Enter" || event.shiftKey || event.altKey || event.ctrlKey || event.metaKey) {
          return;
        }
        if (event.isComposing || event.keyCode === 229) return;
        event.preventDefault();
        this.sendMessage();
      },

      sendMessage: async function () {
        var text = plainText(this.draft).trim();
        if (!text || this.sending) return;
        var generation = this.beginChatOperation();
        this.chatError = "";
        this.messages.push({ id: this.makeId("message"), role: "user", text: text, createdAt: new Date().toISOString() });
        this.scrollTranscript();
        this.draft = "";
        this.sending = true;
        this.chatStatus = "Eve is working…";
        this.schedulePersistChat();

        try {
          if (this.isMemoryQuery(text)) {
            await this.answerFromMemory(text, generation);
            return;
          }
          var path = this.sessionId
            ? "/api/eve/session/" + encodeURIComponent(this.sessionId)
            : "/api/eve/session";
          var body = this.sessionId
            ? {
                continuationToken: this.continuationToken,
                message: text,
                mode: this.selectedMode || this.activeMode || "fast",
                active_tools: this.activeToolIds(),
              }
            : {
                message: text,
                mode: this.selectedMode || this.activeMode || "fast",
                active_tools: this.activeToolIds(),
              };
          var response = await fetch(path, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(body),
            signal: this.requestController.signal,
          });
          if (!this.isCurrentChatOperation(generation)) return;
          var payload = await response.json();
          if (!this.isCurrentChatOperation(generation)) return;
          if (!response.ok) {
            throw new Error(errorMessage(payload, "Eve could not start this message."));
          }
          this.sessionId =
            plainText(payload.sessionId) ||
            plainText(response.headers.get("X-Eve-Session-Id")) ||
            this.sessionId;
          this.continuationToken =
            plainText(payload.continuationToken) || this.continuationToken;
          if (!this.sessionId) throw new Error("Eve did not return a conversation ID.");
          await this.readStream(generation);
        } catch (error) {
          if (this.isCurrentChatOperation(generation) && error.name !== "AbortError") {
            this.chatError = plainText(error.message) || "Eve could not answer this message.";
            this.chatStatus = "Eve needs attention.";
          }
          if (this.isCurrentChatOperation(generation)) {
            this.sending = false;
          }
        } finally {
          if (this.isCurrentChatOperation(generation)) {
            this.streamReader = null;
            this.streamController = null;
            this.requestController = null;
          }
        }
      },

      readStream: async function (generation) {
        if (!this.isCurrentChatOperation(generation) || !this.requestController) return;
        this.streamController = this.requestController;
        var response = await fetch(
          "/api/eve/session/" +
            encodeURIComponent(this.sessionId) +
            "/stream?startIndex=" +
            encodeURIComponent(this.streamIndex),
          { cache: "no-store", signal: this.streamController.signal }
        );
        if (!this.isCurrentChatOperation(generation)) return;
        if (!response.ok || !response.body) {
          var payload = await response.json().catch(function () {
            return {};
          });
          throw new Error(errorMessage(payload, "Eve’s response stream is unavailable."));
        }

        var reader = response.body.getReader();
        this.streamReader = reader;
        var decoder = new TextDecoder();
        var buffer = "";
        while (true) {
          var result = await reader.read();
          if (!this.isCurrentChatOperation(generation)) return;
          buffer += decoder.decode(result.value || new Uint8Array(), { stream: !result.done });
          var newline = buffer.indexOf("\n");
          while (newline >= 0) {
            var line = buffer.slice(0, newline).trim();
            buffer = buffer.slice(newline + 1);
            if (line && this.consumeEventLine(line)) return;
            newline = buffer.indexOf("\n");
          }
          if (result.done) break;
        }
        if (buffer.trim()) this.consumeEventLine(buffer.trim());
      },

      consumeEventLine: function (line) {
        var event;
        try {
          event = JSON.parse(line);
        } catch (_error) {
          return false;
        }
        if (!event || typeof event !== "object" || typeof event.type !== "string") return false;
        var upstreamNextIndex =
          event._proxy && Number.isInteger(event._proxy.upstreamNextIndex)
            ? event._proxy.upstreamNextIndex
            : null;
        this.streamIndex =
          upstreamNextIndex !== null ? upstreamNextIndex : this.streamIndex + 1;
        this.projectEvent(event.type, event.data && typeof event.data === "object" ? event.data : {});
        if (event.type === "session.waiting") {
          this.sending = false;
          if (this.streamReader) this.streamReader.cancel().catch(function () {});
          return true;
        }
        return false;
      },

      projectEvent: function (type, data) {
        if (isPrivateEventType(type) || type === "message.received") return;
        if (type === "step.started" || type === "turn.started") {
          this.chatStatus = "Eve is working…";
          return;
        }
        if (type === "message.appended") {
          this.updateAssistantMessage(data);
          this.chatStatus = "Eve is responding…";
          return;
        }
        if (type === "message.completed") {
          this.updateAssistantMessage(data);
          this.currentAssistantId = null;
          this.schedulePersistChat();
          return;
        }
        if (type === "actions.requested") {
          this.addActions(data.actions || data.requests || []);
          return;
        }
        if (type === "action.result") {
          this.completeAction(data);
          return;
        }
        if (type === "input.requested") {
          this.setPendingInput(data.requests || []);
          return;
        }
        if (type === "session.waiting") {
          this.continuationToken =
            plainText(data.continuationToken) || this.continuationToken;
          this.sending = false;
          this.chatStatus = this.pendingInputs.length
            ? "Eve is waiting for your choice."
            : "Ready.";
          this.refreshTasks();
          this.persistCurrentChat(true);
          return;
        }
        if (type === "turn.cancelled") {
          this.chatStatus = "Stopped. You can send another message.";
          return;
        }
        if (type === "turn.failed" ||
          type === "session.failed" ||
          type === "step.failed" ||
          type === "proxy.error"
        ) {
          this.sending = false;
          this.chatError = plainText(data.message) || "Eve could not complete this turn.";
          this.chatStatus = "Eve needs attention.";
        }
      },

      updateAssistantMessage: function (data) {
        if (plainText(data.role).toLowerCase() === "user") return;
        var cumulative = plainText(data.messageSoFar || data.message);
        var delta = plainText(data.messageDelta || data.delta);
        if (!cumulative && !delta) return;
        var message = null;
        if (this.currentAssistantId) {
          message = this.messages.find(
            function (item) {
              return item.id === this.currentAssistantId;
            }.bind(this)
          );
        }
        if (!message) {
          message = {
            id: this.makeId("message"),
            role: "assistant",
            text: "",
            createdAt: new Date().toISOString(),
          };
          this.messages.push(message);
          this.currentAssistantId = message.id;
          triggerReplyFlash();
        }
        message.text = cumulative || message.text + delta;
        this.scrollTranscript();
      },

      addActions: function (actions) {
        var list = Array.isArray(actions) ? actions : [];
        var workbench = this;
        list.forEach(function (action) {
          var name = actionToolName(action);
          var activity = {
            id: plainText(action.callId || action.id) || workbench.makeId("activity"),
            role: "activity",
            label: TOOL_LABELS[name] || "Using " + displayToolName(name) + "…",
            state: "working",
            symbol: "↻",
          };
          workbench.messages.push(activity);
          workbench.activities.push(activity);
        });
        if (list.length) {
          this.chatStatus = "Running local tools…";
        }
        this.scrollTranscript();
      },

      completeAction: function (data) {
        var result = data.result && typeof data.result === "object" ? data.result : {};
        var id = plainText(result.callId);
        var activity = this.activities.find(function (item) {
          return item.id === id;
        }) || this.messages.find(function (item) {
          return item.role === "activity" && item.id === id;
        });
        if (!activity) {
          var name = actionToolName(result);
          activity = {
            id: id || this.makeId("activity"),
            role: "activity",
            label: TOOL_LABELS[name] || "Used " + displayToolName(name) + ".",
            state: data.status === "completed" ? "ready" : "failed",
            symbol: data.status === "completed" ? "✓" : "×",
          };
          this.messages.push(activity);
          this.activities.push(activity);
          this.scrollTranscript();
          return;
        }
        activity.state = data.status === "completed" ? "ready" : "failed";
        activity.symbol = data.status === "completed" ? "✓" : "×";
        activity.label = activity.label.replace(
          /…$/,
          data.status === "completed" ? " complete." : " did not run."
        );
        this.scrollTranscript();
      },

      setPendingInput: function (requests) {
        var list = Array.isArray(requests) ? requests : [];
        var workbench = this;
        list.forEach(function (request) {
          if (!request || typeof request !== "object") return;
          var requestId = plainText(request.requestId || request.id);
          if (
            !requestId ||
            workbench.pendingInputs.some(function (pending) {
              return pending.requestId === requestId;
            })
          ) {
            return;
          }
          workbench.pendingInputs.push({
            requestId: requestId,
            prompt: plainText(request.prompt || request.message) || "Eve needs your approval.",
            options: normalizeOptions(request),
          });
        });
        if (!this.pendingInputs.length) return;
        this.chatStatus = "Eve is waiting for your choice.";
        this.scrollTranscript();
      },

      answerInput: async function (requestId, optionId, label) {
        var pending = this.pendingInputs.find(function (request) {
          return request.requestId === requestId;
        });
        if (!pending || this.sending) return;
        var generation = this.beginChatOperation();
        this.sending = true;
        this.chatError = "";
        this.chatStatus = "Sending your choice…";
        try {
          var response = await fetch(
            "/api/eve/session/" + encodeURIComponent(this.sessionId),
            {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({
                continuationToken: this.continuationToken,
                inputResponses: [{ requestId: requestId, optionId: optionId }],
                mode: this.selectedMode || this.activeMode || "fast",
                active_tools: this.activeToolIds(),
              }),
              signal: this.requestController.signal,
            }
          );
          if (!this.isCurrentChatOperation(generation)) return;
          var payload = await response.json();
          if (!this.isCurrentChatOperation(generation)) return;
          if (!response.ok) {
            throw new Error(errorMessage(payload, "Eve could not accept that choice."));
          }
          this.pendingInputs = this.pendingInputs.filter(function (request) {
            return request.requestId !== requestId;
          });
          this.messages.push({ id: this.makeId("message"), role: "user", text: plainText(label) });
          this.scrollTranscript();
          this.continuationToken =
            plainText(payload.continuationToken) || this.continuationToken;
          await this.readStream(generation);
        } catch (error) {
          if (this.isCurrentChatOperation(generation) && error.name !== "AbortError") {
            this.chatError = plainText(error.message) || "Eve could not accept that choice.";
            this.chatStatus = "Eve needs attention.";
          }
        } finally {
          if (this.isCurrentChatOperation(generation)) {
            this.sending = false;
            this.streamReader = null;
            this.streamController = null;
            this.requestController = null;
          }
        }
      },

      stopChat: async function () {
        if (!this.sending) return;
        var sessionId = this.sessionId;
        await this.invalidateChatOperation();
        this.sending = false;
        this.chatStatus = sessionId ? "Stopping Eve…" : "Stopped before Eve started.";
        if (!sessionId) return;
        var cancelController = new AbortController();
        this.cancelController = cancelController;
        var generation = this.chatGeneration;
        try {
          var response = await fetch(
            "/api/eve/session/" + encodeURIComponent(sessionId) + "/cancel",
            {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: "{}",
              signal: cancelController.signal,
            }
          );
          if (!this.isCurrentChatOperation(generation)) return;
          if (!response.ok) {
            var payload = await response.json().catch(function () {
              return {};
            });
            throw new Error(errorMessage(payload, "Eve could not be stopped."));
          }
          if (this.isCurrentChatOperation(generation)) {
            this.chatStatus = "Stopped. You can send another message.";
          }
        } catch (error) {
          if (
            this.isCurrentChatOperation(generation) &&
            !cancelController.signal.aborted
          ) {
            this.chatError =
              plainText(error.message) ||
              "Eve could not be stopped. The local service may be unavailable.";
            this.chatStatus = "Eve needs attention.";
          }
        } finally {
          if (this.isCurrentChatOperation(generation)) this.cancelController = null;
        }
      },

      newChat: async function () {
        if (this.cancelController) this.cancelController.abort();
        this.cancelController = null;
        await this.invalidateChatOperation();
        await this.archiveCurrentChat();
        this.sessionId = null;
        this.continuationToken = null;
        this.streamIndex = 0;
        this.messages = [];
        this.activities = [];
        this.pendingInputs = [];
        this.sending = false;
        this.chatError = "";
        this.chatStatus = "Ready for a new local conversation.";
        this.currentAssistantId = null;
        this.historyChatId = null;
        this.historyChatCreatedAt = null;
        try {
          await fetch("/api/chat-history/active", { method: "DELETE", cache: "no-store" });
        } catch (_error) {
          /* ignore */
        }
        await this.refreshChatHistory();
      },

      toggleHistory: async function () {
        this.historyOpen = !this.historyOpen;
        if (this.historyOpen) {
          await this.refreshChatHistory();
        }
      },

      formatHistoryTime: function (value) {
        var raw = plainText(value);
        if (!raw) return "";
        var date = new Date(raw);
        if (Number.isNaN(date.getTime())) return raw;
        try {
          return date.toLocaleString(undefined, {
            month: "short",
            day: "numeric",
            hour: "numeric",
            minute: "2-digit",
          });
        } catch (_error) {
          return raw;
        }
      },

      persistableMessages: function () {
        return (this.messages || [])
          .filter(function (message) {
            return (
              (message.role === "user" || message.role === "assistant") &&
              plainText(message.text).trim()
            );
          })
          .map(function (message) {
            return {
              id: plainText(message.id) || undefined,
              role: message.role,
              text: plainText(message.text),
              createdAt: plainText(message.createdAt) || undefined,
            };
          });
      },

      ensureHistoryChatId: function () {
        if (this.historyChatId) return this.historyChatId;
        var id =
          "chat-" +
          String(Date.now()) +
          "-" +
          Math.random().toString(36).slice(2, 8);
        this.historyChatId = id;
        this.historyChatCreatedAt = new Date().toISOString();
        return id;
      },

      schedulePersistChat: function () {
        var workbench = this;
        if (this.persistTimer) {
          clearTimeout(this.persistTimer);
        }
        this.persistTimer = setTimeout(function () {
          workbench.persistTimer = null;
          workbench.persistCurrentChat(false);
        }, 400);
      },

      persistCurrentChat: async function (_immediate) {
        var messages = this.persistableMessages();
        if (!messages.length) return null;
        var chatId = this.ensureHistoryChatId();
        var payload = {
          id: chatId,
          title: "",
          mode: this.selectedMode || this.activeMode || "fast",
          model: this.activeOllamaModel || this.selectedModel || "",
          createdAt: this.historyChatCreatedAt || undefined,
          messages: messages,
        };
        try {
          var response = await fetch("/api/chat-history/" + encodeURIComponent(chatId), {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload),
          });
          var body = await response.json().catch(function () {
            return {};
          });
          if (!response.ok || body.ok === false) {
            return null;
          }
          if (body.chat && body.chat.createdAt) {
            this.historyChatCreatedAt = plainText(body.chat.createdAt);
          }
          await this.refreshChatHistory();
          return body.chat || null;
        } catch (_error) {
          return null;
        }
      },

      archiveCurrentChat: async function () {
        if (this.persistTimer) {
          clearTimeout(this.persistTimer);
          this.persistTimer = null;
        }
        return this.persistCurrentChat(true);
      },

      refreshChatHistory: async function () {
        this.historyLoading = true;
        try {
          var response = await fetch("/api/chat-history", { cache: "no-store" });
          var payload = await response.json().catch(function () {
            return {};
          });
          if (!response.ok || payload.ok === false) {
            this.chatHistory = [];
            return;
          }
          this.chatHistory = Array.isArray(payload.chats) ? payload.chats : [];
        } catch (_error) {
          this.chatHistory = [];
        } finally {
          this.historyLoading = false;
        }
      },

      restoreChatHistoryOnBoot: async function () {
        await this.refreshChatHistory();
        var activeId = null;
        try {
          var response = await fetch("/api/chat-history/active", { cache: "no-store" });
          var payload = await response.json().catch(function () {
            return {};
          });
          if (response.ok && payload && payload.activeId) {
            activeId = plainText(payload.activeId);
          }
        } catch (_error) {
          activeId = null;
        }
        if (!activeId && this.chatHistory.length) {
          activeId = plainText(this.chatHistory[0].id);
        }
        if (activeId) {
          await this.openHistoryChat(activeId, { silent: true });
        }
      },

      openHistoryChat: async function (chatId, options) {
        var id = plainText(chatId);
        if (!id || this.sending) return;
        var silent = options && options.silent;
        if (!silent && this.historyChatId && this.historyChatId !== id) {
          await this.archiveCurrentChat();
        }
        this.historyLoading = true;
        try {
          var response = await fetch("/api/chat-history/" + encodeURIComponent(id), {
            cache: "no-store",
          });
          var payload = await response.json().catch(function () {
            return {};
          });
          if (!response.ok || payload.ok === false || !payload.chat) {
            throw new Error(errorMessage(payload, "Could not open that chat."));
          }
          var chat = payload.chat;
          await this.invalidateChatOperation();
          this.sessionId = null;
          this.continuationToken = null;
          this.streamIndex = 0;
          this.pendingInputs = [];
          this.activities = [];
          this.sending = false;
          this.chatError = "";
          this.currentAssistantId = null;
          this.historyChatId = plainText(chat.id) || id;
          this.historyChatCreatedAt = plainText(chat.createdAt) || null;
          this.messages = (Array.isArray(chat.messages) ? chat.messages : [])
            .filter(function (message) {
              return message && (message.role === "user" || message.role === "assistant");
            })
            .map(function (message) {
              return {
                id: plainText(message.id) || undefined,
                role: message.role,
                text: plainText(message.text),
                createdAt: plainText(message.createdAt) || undefined,
              };
            });
          this.chatStatus = silent
            ? "Ready for a local conversation."
            : "Loaded past chat. Next message starts a fresh Eve session.";
          this.scrollTranscript();
          if (!silent) {
            this.historyOpen = true;
          }
        } catch (error) {
          if (!silent) {
            this.chatError = plainText(error.message) || "Could not open that chat.";
          }
        } finally {
          this.historyLoading = false;
        }
      },

      deleteHistoryChat: async function (chatId) {
        var id = plainText(chatId);
        if (!id || this.sending) return;
        try {
          var response = await fetch("/api/chat-history/" + encodeURIComponent(id), {
            method: "DELETE",
            cache: "no-store",
          });
          var payload = await response.json().catch(function () {
            return {};
          });
          if (!response.ok || payload.ok === false) {
            throw new Error(errorMessage(payload, "Could not delete that chat."));
          }
          if (this.historyChatId === id) {
            this.historyChatId = null;
            this.historyChatCreatedAt = null;
            this.sessionId = null;
            this.continuationToken = null;
            this.messages = [];
            this.activities = [];
            this.pendingInputs = [];
            this.chatStatus = "Ready for a new local conversation.";
          }
          await this.refreshChatHistory();
        } catch (error) {
          this.chatError = plainText(error.message) || "Could not delete that chat.";
        }
      },

      applyOllamaModels: function (payload) {
        var models = Array.isArray(payload && payload.models) ? payload.models : [];
        this.ollamaModels = models.map(function (model) {
          return {
            id: plainText(model && model.id),
            label: plainText(model && model.label) || plainText(model && model.id),
            tools: Boolean(model && model.tools),
          };
        }).filter(function (model) {
          return Boolean(model.id);
        });
        this.chatModes = (Array.isArray(payload && payload.chatModes) ? payload.chatModes : []).map(
          function (mode) {
            return {
              id: plainText(mode && mode.id),
              label: plainText(mode && mode.label) || plainText(mode && mode.id),
              description: plainText(mode && mode.description),
              model: plainText(mode && mode.model),
              numCtx: Number(mode && mode.numCtx) || 8192,
              temperature: Number(mode && mode.temperature) || 0,
            };
          }
        ).filter(function (mode) {
          return Boolean(mode.id);
        });
        if (!this.chatModes.length) {
          this.chatModes = DEFAULT_CHAT_MODES.map(function (mode) {
            return {
              id: mode.id,
              label: mode.label,
              description: mode.description,
              model: mode.model,
              numCtx: mode.numCtx,
              temperature: mode.temperature,
            };
          });
        }
        this.ollamaConnected = Boolean(payload && payload.connected);
        this.activeOllamaModel = plainText(payload && payload.active);
        this.activeMode = plainText(payload && payload.activeMode) || "fast";
        this.activeModeLabel =
          plainText(payload && payload.activeModeLabel) || this.activeMode;
        this.activeModeDescription =
          plainText(payload && payload.activeModeDescription) ||
          (this.chatModes.find(function (mode) {
            return mode.id === this.activeMode;
          }, this) || {}).description ||
          "";
        if (!this.activeModeLabel || this.activeModeLabel === this.activeMode) {
          var activeModeEntry = this.chatModes.find(function (mode) {
            return mode.id === this.activeMode;
          }, this);
          if (activeModeEntry && activeModeEntry.label) {
            this.activeModeLabel = activeModeEntry.label;
          }
        }
        if (this.chatModes.some(function (mode) { return mode.id === this.activeMode; }.bind(this))) {
          this.selectedMode = this.activeMode;
        } else if (this.chatModes.length) {
          this.selectedMode = this.chatModes[0].id;
        }
        if (
          this.activeOllamaModel &&
          this.ollamaModels.some(
            function (model) {
              return model.id === this.activeOllamaModel;
            }.bind(this)
          )
        ) {
          this.selectedModel = this.activeOllamaModel;
        } else if (!this.selectedModel && this.ollamaModels.length) {
          this.selectedModel = this.ollamaModels[0].id;
        }
        this.ollamaStatus = this.ollamaConnected
          ? "Ollama connected · " + (this.activeModeLabel || this.activeOllamaModel || "choose a mode")
          : plainText(payload && payload.error) || "Ollama is unavailable.";
        if (payload && payload.inventory) {
          this.applyModelInventory(payload.inventory);
        }
      },

      applyChatMode: async function () {
        var mode = plainText(this.selectedMode);
        if (!mode || mode === this.activeMode || this.switchingModel) return;
        this.switchingModel = true;
        this.chatError = "";
        this.ollamaStatus = "Loading " + (this.chatModes.find(function (item) {
          return item.id === mode;
        }) || {}).label + "…";
        try {
          var response = await fetch("/api/ollama/model", {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ mode: mode }),
          });
          var payload = await response.json().catch(function () {
            return {};
          });
          if (!response.ok || payload.ok === false) {
            throw new Error(errorMessage(payload, "Ollama could not switch modes."));
          }
          this.applyOllamaModels(payload);
          await this.newChat();
          this.chatStatus = "Ready.";
        } catch (error) {
          this.selectedMode = this.activeMode;
          this.chatError = plainText(error.message) || "Ollama could not switch modes.";
          this.ollamaStatus = this.chatError;
        } finally {
          this.switchingModel = false;
        }
      },

      selectMode: async function (modeId) {
        var mode = plainText(modeId);
        if (!mode || mode === this.selectedMode) return;
        this.selectedMode = mode;
        var details = this.$root.querySelector(".mode-picker");
        if (details) details.open = false;
        await this.applyChatMode();
      },

      askSuggestion: function (text) {
        var cleaned = plainText(text);
        if (!cleaned || this.sending) return;
        this.draft = cleaned;
        this.sendMessage();
      },

      applyOllamaModel: async function () {
        return this.applyChatMode();
      },

      taskUrl: function (id) {
        var path = "/api/collections/tasks/records";
        return POCKETBASE_URL + path + (id ? "/" + encodeURIComponent(id) : "");
      },

      refreshTasks: async function () {
        this.tasksLoading = true;
        this.taskError = "";
        try {
          var response = await fetch(this.taskUrl() + "?sort=-created&perPage=50", {
            cache: "no-store",
          });
          var payload = await response.json().catch(function () {
            return {};
          });
          if (!response.ok) {
            throw new Error(errorMessage(payload, "PocketBase tasks are unavailable."));
          }
          this.tasks = Array.isArray(payload.items) ? payload.items : [];
          if (this.taskSummaryStamp !== this.taskSummaryKey()) {
            this.taskSummary = "";
            this.taskSummaryStamp = "";
            if (this.taskOverviewOpen) this.refreshTaskSummary(true);
          }
        } catch (error) {
          this.taskError =
            plainText(error.message) ||
            "PocketBase is unavailable. Start it, then click Refresh.";
        } finally {
          this.tasksLoading = false;
        }
      },

      createTask: async function () {
        var title = plainText(this.taskDraft.title).trim();
        if (!title || this.tasksLoading) return;
        this.tasksLoading = true;
        this.taskError = "";
        try {
          var response = await fetch(this.taskUrl(), {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              title: title,
              description: plainText(this.taskDraft.description),
              status: TASK_STATUSES.indexOf(this.taskDraft.status) >= 0 ? this.taskDraft.status : "todo",
              priority: Number.isFinite(this.taskDraft.priority) ? this.taskDraft.priority : 1,
            }),
          });
          var payload = await response.json().catch(function () {
            return {};
          });
          if (!response.ok) {
            throw new Error(errorMessage(payload, "The task could not be added."));
          }
          this.taskDraft = emptyTaskDraft();
          await this.refreshTasks();
        } catch (error) {
          this.taskError = plainText(error.message) || "The task could not be added.";
          this.tasksLoading = false;
        }
      },

      startEditTask: function (task) {
        if (!task || !task.id) return;
        this.pendingDeleteId = "";
        this.editingId = task.id;
        this.editDraft = {
          title: plainText(task.title),
          description: plainText(task.description),
          status: TASK_STATUSES.indexOf(task.status) >= 0 ? task.status : "todo",
          priority: Number.isFinite(task.priority) ? task.priority : 1,
        };
      },

      cancelEditTask: function () {
        this.editingId = "";
        this.editDraft = emptyTaskDraft();
      },

      saveTask: async function () {
        var id = plainText(this.editingId);
        var title = plainText(this.editDraft.title).trim();
        if (!id || !title || this.tasksLoading) return;
        this.tasksLoading = true;
        this.taskError = "";
        try {
          var response = await fetch(this.taskUrl(id), {
            method: "PATCH",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              title: title,
              description: plainText(this.editDraft.description),
              status: TASK_STATUSES.indexOf(this.editDraft.status) >= 0 ? this.editDraft.status : "todo",
              priority: Number.isFinite(this.editDraft.priority) ? this.editDraft.priority : 1,
            }),
          });
          var payload = await response.json().catch(function () {
            return {};
          });
          if (!response.ok) {
            throw new Error(errorMessage(payload, "The task could not be saved."));
          }
          this.cancelEditTask();
          await this.refreshTasks();
        } catch (error) {
          this.taskError = plainText(error.message) || "The task could not be saved.";
          this.tasksLoading = false;
        }
      },

      setTaskStatus: async function (task, status) {
        if (!task || !task.id || TASK_STATUSES.indexOf(status) < 0) return;
        if (task.status === status) return;
        this.tasksLoading = true;
        this.taskError = "";
        try {
          var response = await fetch(this.taskUrl(task.id), {
            method: "PATCH",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ status: status }),
          });
          if (!response.ok) {
            var payload = await response.json().catch(function () {
              return {};
            });
            throw new Error(errorMessage(payload, "The task status could not be changed."));
          }
          await this.refreshTasks();
        } catch (error) {
          this.taskError = plainText(error.message) || "The task status could not be changed.";
          this.tasksLoading = false;
        }
      },

      deleteTask: async function (id) {
        var taskId = plainText(id);
        if (!taskId) return;
        if (this.pendingDeleteId !== taskId) {
          this.pendingDeleteId = taskId;
          return;
        }
        this.tasksLoading = true;
        this.taskError = "";
        try {
          var response = await fetch(this.taskUrl(taskId), { method: "DELETE" });
          if (!response.ok && response.status !== 204) {
            var payload = await response.json().catch(function () {
              return {};
            });
            throw new Error(errorMessage(payload, "The task could not be deleted."));
          }
          this.pendingDeleteId = "";
          if (this.editingId === taskId) this.cancelEditTask();
          await this.refreshTasks();
        } catch (error) {
          this.taskError = plainText(error.message) || "The task could not be deleted.";
          this.tasksLoading = false;
        }
      },

      askEveAboutTask: function (task) {
        if (!task) return;
        this.setTab("chat");
        this.draft =
          "Tell me about PocketBase task \"" +
          plainText(task.title) +
          "\" (id " +
          plainText(task.id) +
          ", status " +
          plainText(task.status) +
          "). Use list_tasks or search_tasks, then summarize it and suggest next steps.";
      },

      haveEveDoTask: function (task) {
        if (!task || this.sending) return;
        this.setTab("chat");
        this.draft =
          "Have Eve do this PocketBase task now. Use PocketBase tools. Task id: " +
          plainText(task.id) +
          ". Title: " +
          plainText(task.title) +
          ". Status: " +
          plainText(task.status) +
          ". Directions: " +
          (plainText(task.description) || "No extra directions.") +
          " Execute the directions, update the task status as you go, and summarize what you did.";
        this.sendMessage();
      },

      refreshHealth: async function () {
        var statusServices = [];
        var memoryApiAvailable = false;
        var memoryReady = false;
        var eveReady = false;
        var ollamaPayload = {};
        try {
          var results = await Promise.all([
            fetch("/api/services/status", { cache: "no-store" }),
            fetch("/api/memory/status", { cache: "no-store" }),
            fetch("/api/eve/info", { cache: "no-store" }),
            fetch("/api/ollama/models", { cache: "no-store" }),
          ]);
          if (results[0].ok) {
            var statusPayload = await results[0].json();
            statusServices = Array.isArray(statusPayload.services) ? statusPayload.services : [];
          }
          var memoryPayload = results[1].ok ? await results[1].json() : {};
          memoryApiAvailable = results[1].ok && memoryPayload.ok === true;
          memoryReady =
            memoryApiAvailable &&
            memoryPayload.readiness &&
            memoryPayload.readiness.ready === true;
          eveReady = results[2].ok;
          ollamaPayload = results[3].ok || results[3].status === 503
            ? await results[3].json()
            : {};
          this.applyOllamaModels(ollamaPayload);
        } catch (_error) {
          statusServices = [];
          this.applyOllamaModels({ connected: false, error: "Ollama is unavailable." });
        }
        var states = {
          eve: eveReady,
          memory: memoryReady,
          pocketbase: false,
          ollama: false,
        };
        statusServices.forEach(function (service) {
          if (service.id === "eve") states.eve = Boolean(service.healthy) && eveReady;
          if (service.id === "pocketbase") states.pocketbase = Boolean(service.healthy);
        });
        states.ollama = this.ollamaConnected;
        this.health.services = Object.keys(SERVICE_LABELS).map(function (id) {
          var ready = states[id];
          var status =
            id === "memory" && memoryApiAvailable && !memoryReady
              ? "API available; dependencies unavailable"
              : ready
                ? "Ready"
                : "Unavailable";
          return {
            id: id,
            label: SERVICE_LABELS[id],
            state: ready ? "ready" : "failed",
            status: status,
            symbol: ready ? "✓" : "×",
          };
        });
        var unavailable = this.health.services
          .filter(function (service) {
            return service.state !== "ready";
          })
          .map(function (service) {
            return service.label;
          });
        this.health.summary = unavailable.length
          ? unavailable.join(", ") + (unavailable.length === 1 ? " is unavailable." : " are unavailable.")
          : "Eve and local memory services are ready.";
      },

      repairServices: async function () {
        this.health.repairing = true;
        this.health.summary = "Starting local services…";
        try {
          var response = await fetch("/api/services/start", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ all: true }),
          });
          if (!response.ok) throw new Error("Local services could not be started.");
          await this.refreshHealth();
        } catch (error) {
          this.health.summary =
            plainText(error.message) || "Local services could not be started. Open Dashboard for details.";
        } finally {
          this.health.repairing = false;
        }
      },

      makeId: function (prefix) {
        var id = prefix + "-" + String(this.nextId);
        this.nextId += 1;
        return id;
      },
    };
  };
})();
