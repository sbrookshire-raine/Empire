"use strict";

const assert = require("node:assert/strict");
const fs = require("node:fs");
const vm = require("node:vm");

function loadWorkbench(fetchImpl) {
  const context = {
    AbortController,
    FormData,
    JSON,
    TextDecoder,
    Uint8Array,
    clearTimeout,
    console,
    document: {
      createElement() {
        return { textContent: "" };
      },
    },
    fetch: fetchImpl || (async () => {
      throw new Error("Unexpected fetch");
    }),
    setTimeout,
    window: {},
  };
  vm.runInNewContext(
    fs.readFileSync("frontend/eve-workbench.js", "utf8"),
    context,
    { filename: "frontend/eve-workbench.js" },
  );
  const workbench = context.window.eveWorkbench();
  workbench.$nextTick = (callback) => callback();
  workbench.$refs = {
    transcript: {
      scrollHeight: 100,
      scrollTo() {},
    },
  };
  return { context, workbench };
}

async function testWaitingBoundaryUsesProxyIndex() {
  let cancelled = false;
  const { workbench } = loadWorkbench();
  workbench.sending = true;
  workbench.streamReader = {
    cancel() {
      cancelled = true;
      return Promise.resolve();
    },
  };
  const reachedBoundary = workbench.consumeEventLine(JSON.stringify({
    _proxy: { upstreamNextIndex: 12 },
    type: "session.waiting",
    data: { continuationToken: "eve:next" },
  }));

  assert.equal(reachedBoundary, true);
  assert.equal(workbench.streamIndex, 12);
  assert.equal(workbench.continuationToken, "eve:next");
  assert.equal(workbench.sending, false);
  assert.equal(cancelled, true);
}

async function testStreamStopsBeforeTransportEof() {
  let reads = 0;
  let cancelled = false;
  const waiting = new TextEncoder().encode(
    '{"_proxy":{"upstreamNextIndex":4},"type":"session.waiting","data":{"continuationToken":"next"}}\n',
  );
  const reader = {
    read() {
      reads += 1;
      if (reads === 1) return Promise.resolve({ done: false, value: waiting });
      return new Promise(() => {});
    },
    cancel() {
      cancelled = true;
      return Promise.resolve();
    },
  };
  const { workbench } = loadWorkbench(async () => ({
    ok: true,
    body: { getReader: () => reader },
  }));
  workbench.sessionId = "ses_1";
  workbench.sending = true;
  workbench.chatGeneration = 1;
  workbench.requestController = new AbortController();

  await Promise.race([
    workbench.readStream(1),
    new Promise((_, reject) => setTimeout(() => reject(new Error("stream waited for EOF")), 50)),
  ]);
  assert.equal(reads, 1);
  assert.equal(cancelled, true);
}

async function testInputRequestsQueueAndFailedApprovalPersists() {
  const { context, workbench } = loadWorkbench();
  workbench.setPendingInput([
    {
      requestId: "r1",
      prompt: "Delete task?",
      options: [{ id: "approve", label: "Approve" }, { id: "deny", label: "Deny" }],
    },
    {
      requestId: "r2",
      prompt: "Continue?",
      options: [{ id: "yes", label: "Yes" }],
    },
  ]);
  assert.equal(workbench.pendingInputs.length, 2);
  assert.equal(workbench.pendingInput.requestId, "r1");

  workbench.sessionId = "ses_1";
  workbench.continuationToken = "token";
  context.fetch = async () => ({
    ok: false,
    json: async () => ({ error: "Rejected by server." }),
  });
  await workbench.answerInput("r1", "approve", "Approve");

  assert.equal(workbench.pendingInputs.length, 2);
  assert.equal(workbench.pendingInput.requestId, "r1");

  let requestCount = 0;
  context.fetch = async () => {
    requestCount += 1;
    if (requestCount === 1) {
      return {
        ok: true,
        json: async () => ({ continuationToken: "token-2" }),
      };
    }
    return {
      ok: true,
      body: {
        getReader: () => ({
          read: async () => ({
            done: false,
            value: new TextEncoder().encode(
              '{"_proxy":{"upstreamNextIndex":9},"type":"session.waiting","data":{"continuationToken":"token-3"}}\n',
            ),
          }),
          cancel: async () => {},
        }),
      },
    };
  };
  await workbench.answerInput("r1", "approve", "Approve");

  assert.equal(workbench.pendingInputs.length, 1);
  assert.equal(workbench.pendingInput.requestId, "r2");
}

async function testNewChatRejectsStaleSessionResponse() {
  let resolvePost;
  let calls = 0;
  const { context, workbench } = loadWorkbench((_, options) => {
    calls += 1;
    if (calls > 1) throw new Error("stale response opened a stream");
    return new Promise((resolve) => {
      resolvePost = () => resolve({
        headers: { get: () => null },
        json: async () => ({ sessionId: "stale_session", continuationToken: "stale_token" }),
        ok: true,
      });
      if (options.signal) {
        options.signal.addEventListener("abort", () => {});
      }
    });
  });
  workbench.draft = "hello";
  const send = workbench.sendMessage();
  await Promise.resolve();
  await workbench.newChat();
  resolvePost();
  await send;

  assert.equal(workbench.sessionId, null);
  assert.equal(workbench.continuationToken, null);
  assert.equal(workbench.messages.length, 0);
  assert.equal(calls, 1);
}

async function testStopAbortsInitialPost() {
  let capturedSignal;
  let rejectPost;
  const { workbench } = loadWorkbench((_, options) => new Promise((_, reject) => {
    capturedSignal = options.signal;
    rejectPost = reject;
  }));
  workbench.draft = "hello";
  const send = workbench.sendMessage();
  await Promise.resolve();
  await workbench.stopChat();

  assert.ok(capturedSignal);
  assert.equal(capturedSignal.aborted, true);
  const abortError = new Error("aborted");
  abortError.name = "AbortError";
  rejectPost(abortError);
  await send;
}

async function testStopCancelsKnownSession() {
  let cancelRequest = null;
  const { workbench } = loadWorkbench(async (url, options) => {
    cancelRequest = { url, options };
    return { ok: true };
  });
  workbench.sessionId = "ses_known";
  workbench.sending = true;
  workbench.requestController = new AbortController();

  await workbench.stopChat();

  assert.equal(cancelRequest.url, "/api/eve/session/ses_known/cancel");
  assert.equal(cancelRequest.options.method, "POST");
  assert.ok(cancelRequest.options.signal);
  assert.equal(workbench.sending, false);
}

async function testStopPreservesHttpFailure() {
  const { workbench } = loadWorkbench(async () => ({
    ok: false,
    json: async () => ({ error: "Cancellation was rejected." }),
  }));
  workbench.sessionId = "ses_known";
  workbench.sending = true;
  workbench.requestController = new AbortController();

  await workbench.stopChat();

  assert.equal(workbench.chatStatus, "Eve needs attention.");
  assert.match(workbench.chatError, /Cancellation was rejected/);
  assert.notEqual(workbench.chatStatus, "Stopped. You can send another message.");
}

async function testReselectionClearsUploadedAssociation() {
  const { workbench } = loadWorkbench();
  workbench.activeJob = {
    id: "job_old",
    status: "ready",
    dataset: "learned_dataset",
    files: [{ name: "learned.md", bytes: 8 }],
  };
  workbench.uploadedContext = {
    jobId: "job_old",
    dataset: "learned_dataset",
    files: ["learned.md"],
  };

  workbench.selectFiles([{ name: "not_uploaded.md", size: 12 }]);

  assert.equal(workbench.activeJob, null);
  assert.equal(workbench.uploadedContext, null);
  workbench.askAboutFiles();
  assert.equal(workbench.draft, "");
}

async function testInboundUserEventDoesNotBecomeEveReply() {
  const { workbench } = loadWorkbench();
  workbench.messages.push({ id: "message-user", role: "user", text: "hi eve" });
  workbench.consumeEventLine(JSON.stringify({
    type: "message.received",
    data: { message: "hi eve", role: "user" },
  }));
  workbench.consumeEventLine(JSON.stringify({
    type: "message.appended",
    data: { role: "user", message: "hi eve", messageSoFar: "hi eve" },
  }));

  assert.equal(workbench.messages.length, 1);
  assert.equal(workbench.messages[0].role, "user");
  assert.equal(workbench.currentAssistantId, null);
}

async function testApplyOllamaModelSavesSelectionAndStartsNewChat() {
  const calls = [];
  const { workbench } = loadWorkbench(async (url, options) => {
    calls.push({ url, method: options && options.method, body: options && options.body });
    return { ok: true, json: async () => ({ ok: true, active: "qwen3.8:latest" }) };
  });
  workbench.sessionId = "ses_old";
  workbench.messages = [{ id: "message-1", role: "user", text: "hi eve" }];
  workbench.selectedModel = "qwen3.8:latest";
  workbench.activeOllamaModel = "llama3.1:8b";

  await workbench.applyOllamaModel();

  assert.equal(calls[0].url, "/api/ollama/model");
  assert.equal(calls[0].method, "PUT");
  assert.equal(JSON.parse(calls[0].body).model, "qwen3.8:latest");
  assert.equal(workbench.sessionId, null);
  assert.equal(workbench.messages.length, 0);
  assert.equal(workbench.activeOllamaModel, "qwen3.8:latest");
}

async function testTaskCrudAndEveActionsUseButtons() {
  const calls = [];
  const { workbench } = loadWorkbench(async (url, options) => {
    calls.push({
      url: url,
      method: (options && options.method) || "GET",
      body: options && options.body,
    });
    if (String(url).includes("/api/collections/tasks/records") && (!options || !options.method || options.method === "GET")) {
      return {
        ok: true,
        json: async () => ({
          items: [{
            id: "task1",
            title: "Wire Ollama",
            status: "todo",
            priority: 1,
            description: "Use local model",
          }],
        }),
      };
    }
    if (String(url).includes("/api/eve/session")) {
      return {
        ok: true,
        headers: { get: () => null },
        json: async () => ({ sessionId: "ses_task", continuationToken: "tok" }),
        body: {
          getReader: () => ({
            read: async () => ({
              done: false,
              value: new TextEncoder().encode(
                '{"_proxy":{"upstreamNextIndex":1},"type":"session.waiting","data":{"continuationToken":"tok-2"}}\n',
              ),
            }),
            cancel: async () => {},
          }),
        },
      };
    }
    return {
      ok: true,
      json: async () => ({ id: "task1", title: "Wire Ollama", status: "in_progress" }),
    };
  });

  await workbench.refreshTasks();
  assert.equal(workbench.tasks.length, 1);
  assert.equal(workbench.tasks[0].title, "Wire Ollama");

  workbench.taskDraft.title = "New job";
  workbench.taskDraft.status = "todo";
  await workbench.createTask();
  assert.equal(
    calls.some((call) => call.method === "POST" && String(call.url).includes("/api/collections/tasks/records")),
    true,
  );

  workbench.startEditTask(workbench.tasks[0]);
  workbench.editDraft.status = "in_progress";
  await workbench.saveTask();
  assert.equal(calls.some((call) => call.method === "PATCH"), true);

  workbench.pendingDeleteId = "task1";
  await workbench.deleteTask("task1");
  assert.equal(
    calls.some((call) => call.method === "DELETE" && String(call.url).endsWith("/task1")),
    true,
  );

  workbench.draft = "";
  workbench.askEveAboutTask({ id: "task1", title: "Wire Ollama", status: "todo" });
  assert.match(workbench.draft, /Wire Ollama/);

  workbench.haveEveDoTask({
    id: "task1",
    title: "Wire Ollama",
    status: "todo",
    description: "Use local model",
  });
  await Promise.resolve();
  await Promise.resolve();
  assert.equal(workbench.messages[0].role, "user");
  assert.match(workbench.messages[0].text, /execute|work|do this|PocketBase/i);
}

async function testCursorJumpsAcrossDroppedOversizedRecord() {
  const { workbench } = loadWorkbench();
  workbench.streamIndex = 7;
  workbench.consumeEventLine(JSON.stringify({
    _proxy: { upstreamNextIndex: 8 },
    type: "message.appended",
    data: { messageDelta: "visible" },
  }));
  workbench.consumeEventLine(JSON.stringify({
    _proxy: { upstreamNextIndex: 10 },
    type: "session.waiting",
    data: { continuationToken: "next" },
  }));

  assert.equal(workbench.streamIndex, 10);
  assert.equal(workbench.messages[0].text, "visible");
}

async function testComposerEnterSendsAndShiftEnterDoesNot() {
  const { workbench } = loadWorkbench();
  const sent = [];
  workbench.sendMessage = async function () {
    sent.push(this.draft);
  };

  workbench.onComposerKeydown({
    key: "Enter",
    shiftKey: true,
    preventDefault() {
      throw new Error("Shift+Enter should not send");
    },
  });
  assert.equal(sent.length, 0);

  let prevented = false;
  workbench.onComposerKeydown({
    key: "Enter",
    shiftKey: false,
    altKey: false,
    ctrlKey: false,
    metaKey: false,
    isComposing: false,
    preventDefault() {
      prevented = true;
    },
  });
  assert.equal(prevented, true);
  assert.equal(sent.length, 1);
}

async function testToolActivityInterleavesInTranscript() {
  const { workbench } = loadWorkbench();
  workbench.messages.push({ id: "message-user", role: "user", text: "list tasks" });
  workbench.addActions([{ callId: "call-1", name: "list_tasks" }]);
  workbench.consumeEventLine(JSON.stringify({
    type: "message.appended",
    data: { role: "assistant", messageSoFar: "You have 2 tasks." },
  }));

  assert.equal(workbench.messages.length, 3);
  assert.equal(workbench.messages[0].role, "user");
  assert.equal(workbench.messages[1].role, "activity");
  assert.equal(workbench.messages[2].role, "assistant");
  assert.match(workbench.messages[1].label, /task/i);
}

async function testTabsAndModelInventoryApply() {
  const { workbench } = loadWorkbench();
  workbench.setTab("models");
  assert.equal(workbench.activeTab, "models");
  workbench.applyModelInventory({
    ok: true,
    models: [{ id: "llama3.1:8b", role: "chat", fit16gb: "excellent", strengths: ["Fast"], skills: ["dailyChat"] }],
    recommendations: {
      summary: "16 GB VRAM · 64 GB RAM.",
      suite: [
        {
          id: "dailyChat",
          label: "Daily chat",
          status: "covered",
          ideal: { id: "llama3.1:8b", fit16gb: "excellent", sizeGb: 4.7, why: "Fast", whenToUse: "Default chat" },
          installed: { id: "llama3.1:8b", role: "chat", fit16gb: "excellent" },
          installedId: "llama3.1:8b",
          pull: null,
        },
      ],
      pullGaps: [{ id: "deepseek-r1:8b", command: "ollama pull deepseek-r1:8b", label: "Reasoning", why: "Planning" }],
      removeSuggestions: [{ id: "llama3.1:latest", command: "ollama rm llama3.1:latest", reason: "Duplicate" }],
      eveBriefing: "Skill routing:",
      eveGuidance: { dailyChat: "llama3.1:8b" },
    },
  });
  assert.equal(workbench.modelInventory.length, 1);
  assert.equal(workbench.modelRecommendations.suite.length, 1);
  assert.equal(workbench.modelRecommendations.pullGaps.length, 1);
  assert.match(workbench.modelRecommendations.summary, /16 GB VRAM/);
}

async function run() {
  await testWaitingBoundaryUsesProxyIndex();
  await testStreamStopsBeforeTransportEof();
  await testInputRequestsQueueAndFailedApprovalPersists();
  await testNewChatRejectsStaleSessionResponse();
  await testStopAbortsInitialPost();
  await testStopCancelsKnownSession();
  await testStopPreservesHttpFailure();
  await testReselectionClearsUploadedAssociation();
  await testCursorJumpsAcrossDroppedOversizedRecord();
  await testInboundUserEventDoesNotBecomeEveReply();
  await testApplyOllamaModelSavesSelectionAndStartsNewChat();
  await testTaskCrudAndEveActionsUseButtons();
  await testComposerEnterSendsAndShiftEnterDoesNot();
  await testToolActivityInterleavesInTranscript();
  await testTabsAndModelInventoryApply();
  process.stdout.write("Eve Workbench runtime harness: 15 passed\n");
}

run().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
