from __future__ import annotations

import re
import unittest
from pathlib import Path


class EveWorkbenchStaticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.html = Path("frontend/eve.html").read_text(encoding="utf-8")
        cls.js = Path("frontend/eve-workbench.js").read_text(encoding="utf-8")
        cls.css = Path("frontend/eve-workbench.css").read_text(encoding="utf-8")
        cls.nav = Path("frontend/empire-nav.js").read_text(encoding="utf-8")

    def test_primary_labels_are_clear(self) -> None:
        for text in (
            "Add to memory",
            "Eve",
            "mode-picker",
            "PocketBase tasks",
            "Memory &amp; indexing",
            "Add task",
            "Stop",
            "New chat",
            "Message Eve",
            "AI task summary",
            "workbench-tabs",
        ):
            self.assertIn(text, self.html)
        for token in (
            "chatLineStatus",
            "compactChatStatus",
            "visibleMessages",
            "askSuggestion",
            "selectMode",
            "onComposerKeydown",
            "refreshTaskSummary",
            "setTab",
            "refreshModelInventory",
        ):
            self.assertIn(token, self.js)

    def test_models_tab_has_suite_planner(self) -> None:
        self.assertIn('id="tab-models"', self.html)
        self.assertIn('id="panel-models"', self.html)
        self.assertIn("activeTab === 'models'", self.html)
        self.assertIn("skill-grid", self.html)
        self.assertIn("Model suite", self.html)
        self.assertIn("Pull to fill gaps", self.html)
        self.assertIn("Remove duplicates", self.html)
        self.assertIn("Eve routing briefing", self.html)
        self.assertIn("applyModelInventory", self.js)
        self.assertIn("copyEveBriefing", self.js)
        self.assertIn("suiteStatusLabel", self.js)
        self.assertIn("/api/ollama/inventory", self.js)

    def test_workbench_uses_focused_tabs(self) -> None:
        self.assertIn("activeTab === 'chat'", self.html)
        self.assertIn("activeTab === 'tasks'", self.html)
        self.assertIn("activeTab === 'memory'", self.html)
        self.assertIn("activeTab === 'models'", self.html)
        self.assertIn("activeTab === 'more'", self.html)
        self.assertIn('class="task-overview"', self.html)
        self.assertNotIn("workbench__grid", self.html)

    def test_page_has_one_file_input_and_accessible_regions(self) -> None:
        self.assertEqual(len(re.findall(r'type=["\']file["\']', self.html)), 1)
        self.assertIn('accept=".md,.txt,.pdf"', self.html)
        self.assertIn("multiple", self.html)
        self.assertIn('id="chat-form"', self.html)
        self.assertIn('class="mode-picker"', self.html)
        self.assertIn('class="bubble"', self.html)
        self.assertGreaterEqual(self.html.count("<section"), 2)
        self.assertGreaterEqual(self.html.count("aria-labelledby="), 2)
        self.assertIn('aria-live="polite"', self.html)

    def test_page_uses_existing_zero_build_conventions(self) -> None:
        self.assertIn("@picocss/pico@2", self.html)
        self.assertIn("alpinejs@3.14.8", self.html)
        self.assertIn('href="empire-nav.css"', self.html)
        self.assertIn('src="empire-nav.js"', self.html)
        self.assertIn('data-current="eve"', self.html)
        self.assertNotRegex(self.html.lower(), r"\b(react|vue|svelte)\b")
        self.assertNotIn("fonts.googleapis.com", self.html)
        self.assertNotIn("fonts.gstatic.com", self.html)

    def test_memory_controls_and_job_states_are_present(self) -> None:
        for token in (
            "Advanced options",
            "eve_memory",
            "full_graph",
            "dragenter",
            "drop",
            "selectedFiles",
            "recentJobs",
            "Try again",
            "Eve can now use this file in chat.",
            "Ask Eve about these files",
        ):
            self.assertIn(token, self.html + self.js)
        self.assertIn("setTimeout", self.js)
        self.assertNotIn("setInterval", self.js)
        self.assertIn("1000", self.js)
        for endpoint in (
            "/api/memory/status",
            "/api/memory/upload",
            "/api/memory/jobs/",
            "/retry",
        ):
            self.assertIn(endpoint, self.js)

    def test_client_enforces_local_upload_safety_before_posting(self) -> None:
        for token in (
            "50 * 1024 * 1024",
            "20",
            "SYSTEM.md",
            "LENS_",
            "directives",
            ".md",
            ".txt",
            ".pdf",
        ):
            self.assertIn(token, self.js)
        self.assertRegex(self.js, r"FormData\s*\(")
        self.assertRegex(self.js, r'append\(["\']files["\']')
        self.assertRegex(self.js, r'append\(["\']dataset["\']')
        self.assertRegex(self.js, r'append\(["\']full_graph["\']')

    def test_chat_uses_current_session_contract_and_retained_ndjson_buffer(self) -> None:
        for endpoint in (
            "/api/eve/info",
            "/api/eve/session",
            "/stream?startIndex=",
            "/cancel",
            "/api/ollama/models",
            "/api/ollama/model",
        ):
            self.assertIn(endpoint, self.js)
        for token in (
            "sessionId",
            "continuationToken",
            "streamIndex",
            "response.body.getReader()",
            "TextDecoder",
            "buffer",
            'buffer.indexOf("\\n")',
            "messageDelta",
            "messageSoFar",
            ".cancel()",
            "AbortController",
            "chatGeneration",
            "requestController",
            "upstreamNextIndex",
        ):
            self.assertIn(token, self.js)
        self.assertIn('type === "session.waiting"', self.js)
        self.assertIn('type === "message.received"', self.js)
        self.assertIn("return true", self.js)
        self.assertIn("applyChatMode", self.js)
        self.assertIn("chatModes", self.js)

    def test_projected_event_shapes_have_safe_human_projection(self) -> None:
        for event_type in (
            "message.appended",
            "message.completed",
            "actions.requested",
            "action.result",
            "input.requested",
            "session.waiting",
            "turn.failed",
            "session.failed",
            "proxy.error",
        ):
            self.assertIn(event_type, self.js)
        for tool_name in (
            "cognee_recall",
            "cognee_remember",
            "cognee_improve",
            "cognee_forget",
            "get_model_suite",
            "list_models",
            "switch_chat_model",
            "ollama_health",
            "pb_health",
            "list_tasks",
            "search_tasks",
            "create_task",
            "update_task",
            "delete_task",
            "workbench_list_dir",
            "workbench_read_file",
        ):
            self.assertIn(tool_name, self.js)
        self.assertIn("inputResponses", self.js)
        self.assertIn("requestId", self.js)
        self.assertIn("optionId", self.js)
        self.assertIn("var result = data.result", self.js)
        self.assertIn("data.status", self.js)
        self.assertIn("pendingInputs", self.js)
        self.assertIn("isPrivateEventType", self.js)

    def test_untrusted_content_never_uses_html_sinks_or_raw_event_rendering(self) -> None:
        combined = self.html + self.js + self.nav
        for forbidden in ("x-html", ".innerHTML", "insertAdjacentHTML", "document.write"):
            self.assertNotIn(forbidden, combined)
        self.assertIn("x-text", self.html)
        self.assertIn("textContent", self.js)
        self.assertNotRegex(self.html, r"x-text\s*=\s*[\"'][^\"']*(reasoning|rawEvent)")
        self.assertNotIn("JSON.stringify(event", self.js)
        self.assertNotIn("event.data.details", self.js)

    def test_health_is_plain_language_and_has_single_repair_action(self) -> None:
        for name in ("Eve", "Memory", "PocketBase", "Ollama"):
            self.assertIn(name, self.html + self.js)
        self.assertIn("Start / repair local services", self.html)
        self.assertIn("/api/services/status", self.js)
        self.assertIn("/api/services/start", self.js)
        self.assertIn("memoryApiAvailable", self.js)
        self.assertIn("memoryPayload.readiness", self.js)
        self.assertIn("API available; dependencies unavailable", self.js)
        self.assertIn('JSON.stringify({ all: true })', self.js)

    def test_upload_and_polling_are_race_safe(self) -> None:
        self.assertIn(":disabled=\"memoryLocked\"", self.html)
        self.assertIn("pollInFlight", self.js)
        self.assertIn("pollGeneration", self.js)
        self.assertIn("this.pollTimer !== null || this.pollInFlight", self.js)
        self.assertIn("if (this.memoryLocked)", self.js)
        self.assertIn("schedulePoll", self.js)
        self.assertIn("uploadedContext", self.js)

    def test_file_focus_scroll_and_single_primary_chat_action(self) -> None:
        self.assertIn('x-ref="transcript"', self.html)
        self.assertIn("scrollTranscript", self.js)
        self.assertIn(".drop-zone:focus-within", self.css)
        ask_button = re.search(
            r'<button\s+class="([^"]+)"[^>]*x-show="activeJob && activeJob.status === \'ready\'"'
            r'[^>]*@click="askAboutFilesInChat\(\)"',
            self.html,
            re.DOTALL,
        )
        self.assertIsNotNone(ask_button)
        self.assertNotIn("button--primary", ask_button.group(1))
        self.assertEqual(self.html.count("button button--primary"), 3)
        for token in (
            "refreshTasks",
            "createTask",
            "startEditTask",
            "saveTask",
            "deleteTask",
            "askEveAboutTask",
            "haveEveDoTask",
            "/api/collections/tasks/records",
            "todo",
            "in_progress",
            "done",
        ):
            self.assertIn(token, self.html + self.js)

    def test_css_has_hallmark_stamp_tokens_and_responsive_safety(self) -> None:
        first_line = self.css.splitlines()[0]
        for token in (
            "Hallmark",
            "macrostructure: Workbench",
            "theme: Neon Storm Arcade",
            "audience: local Eve experimenter",
            "pre-emit critique:",
        ):
            self.assertIn(token, first_line)
        self.assertIn(":root", self.css)
        self.assertNotRegex(
            "\n".join(line for line in self.css.splitlines() if not line.lstrip().startswith("--")),
            r"(?:#(?:[0-9a-fA-F]{3,8})\b|rgba?\(|hsla?\(|oklch\()",
        )
        self.assertGreaterEqual(self.css.count("oklch("), 8)
        self.assertIn("overflow-x: clip", self.css)
        self.assertIn("minmax(0, 1fr)", self.css)
        self.assertIn("white-space: nowrap", self.css)
        self.assertIn("overflow-wrap: anywhere", self.css)
        self.assertIn(":focus-visible", self.css)
        self.assertIn("prefers-reduced-motion: reduce", self.css)
        self.assertIn("storm-reply-flash", self.css)
        self.assertIn("triggerReplyFlash", self.js)
        self.assertRegex(self.css, r"@media\s*\(min-width:\s*50rem\)")

    def test_composer_enter_sends_and_shift_enter_stays(self) -> None:
        self.assertIn("onComposerKeydown", self.html + self.js)
        self.assertIn('@keydown="onComposerKeydown($event)"', self.html)
        self.assertIn("event.shiftKey", self.js)
        self.assertIn("event.isComposing", self.js)
        self.assertIn('event.key !== "Enter"', self.js)
        self.assertIn("this.sendMessage()", self.js)

    def test_transcript_is_a_sequential_log(self) -> None:
        self.assertIn('class="bubble"', self.html)
        self.assertIn("bubble--", self.html)
        self.assertIn("visibleMessages", self.js)
        self.assertNotIn('class="message"', self.html)
        self.assertNotIn("activity-list", self.html)

    def test_navigation_adds_eve_immediately_after_dashboard(self) -> None:
        dashboard = self.nav.index('{ id: "dashboard"')
        eve = self.nav.index('{ id: "eve"')
        primitives = self.nav.index('{ id: "primitives"')
        self.assertLess(dashboard, eve)
        self.assertLess(eve, primitives)
        self.assertIn("http://127.0.0.1:8080/eve.html", self.nav)


if __name__ == "__main__":
    unittest.main()
