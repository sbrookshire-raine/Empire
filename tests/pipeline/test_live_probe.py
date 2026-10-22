"""The live routing battery's reasoning (E-03) — offline, no stack needed.

These tests hold the *contract* the live probe relies on: a turn is judged
by the structured events the framework emitted, and the expectation comes
from the same shared classifier + codex the running system uses.

The wire facts encoded here were measured on the live stack (2026-10-21):
`actions.requested` carries `data.actions[].toolName`, and `action.result`
carries `data.result.toolName` (NOT `data.toolName` — reading it there
found nothing, which is why every live `tool.result` trace line recorded
`"tool": null`).
"""

from __future__ import annotations

import unittest

from pipeline import live_probe, route_classifier


def _requested(tool: str, call_id: str = "call_1", **args: object) -> dict:
    return {
        "type": "actions.requested",
        "data": {
            "actions": [
                {"callId": call_id, "input": dict(args), "kind": "tool-call", "toolName": tool}
            ],
            "sequence": 0,
            "stepIndex": 0,
            "turnId": "turn_0",
        },
    }


def _result(tool: str, status: str = "completed", call_id: str = "call_1") -> dict:
    return {
        "type": "action.result",
        "data": {
            "result": {"callId": call_id, "kind": "tool-result", "output": {}, "toolName": tool},
            "sequence": 0,
            "status": status,
            "stepIndex": 0,
            "turnId": "turn_0",
        },
    }


def _completed(text: str) -> dict:
    return {
        "type": "message.completed",
        "data": {
            "finishReason": "stop",
            "message": text,
            "sequence": 0,
            "stepIndex": 0,
            "turnId": "turn_0",
        },
    }


class ReadTurnTests(unittest.TestCase):
    def test_reads_the_tool_name_from_the_action_envelope(self) -> None:
        evidence = live_probe.read_turn([_requested("wiki_scout_search", query="Kate Bush")])
        self.assertEqual(evidence.tools_called, ["wiki_scout_search"])
        self.assertEqual(evidence.calls[0].arguments, {"query": "Kate Bush"})

    def test_reads_the_tool_name_from_the_result_envelope(self) -> None:
        """The result nests the name under `data.result` - not on `data`."""
        evidence = live_probe.read_turn([_result("wiki_read_section")])
        self.assertEqual(evidence.succeeded_tools, ["wiki_read_section"])
        self.assertTrue(evidence.outcomes[0].ok)

    def test_a_failed_result_is_not_a_success(self) -> None:
        evidence = live_probe.read_turn([_result("wiki_read_section", status="error")])
        self.assertEqual(evidence.succeeded_tools, [])

    def test_non_tool_actions_are_ignored(self) -> None:
        event = {
            "type": "actions.requested",
            "data": {"actions": [{"kind": "load-skill", "toolName": "load_skill"}]},
        }
        self.assertEqual(live_probe.read_turn([event]).tools_called, [])

    def test_malformed_records_do_not_crash_the_reader(self) -> None:
        evidence = live_probe.read_turn(
            [
                "not a dict",
                {"type": "actions.requested", "data": "not a dict"},
                {"type": "actions.requested", "data": {"actions": ["not a dict"]}},
                _requested("list_tasks"),
            ]
        )
        self.assertEqual(evidence.tools_called, ["list_tasks"])

    def test_turn_end_events_mark_the_turn_ended(self) -> None:
        self.assertTrue(live_probe.read_turn([{"type": "session.waiting"}]).ended)
        self.assertTrue(live_probe.read_turn([{"type": "turn.completed"}]).ended)
        self.assertFalse(live_probe.read_turn([_requested("list_tasks")]).ended)

    def test_parse_ndjson_skips_blank_and_broken_lines(self) -> None:
        records = live_probe.parse_ndjson(['{"type": "x"}', "", "   ", "{not json", "null"])
        self.assertEqual(records, [{"type": "x"}])


class CorrectToolTests(unittest.TestCase):
    def test_the_expected_tool_comes_from_the_shared_rules(self) -> None:
        """Not a hard-coded list: the codex the system itself applies."""
        route, tools = live_probe.expected_tools_for("List my open tasks.")
        self.assertEqual(route, route_classifier.TASK)
        self.assertIn("list_tasks", tools)

    def test_a_task_turn_that_reaches_a_task_tool_passes(self) -> None:
        evidence = live_probe.read_turn([_requested("list_tasks"), _result("list_tasks")])
        verdict = live_probe.assert_correct_tool(evidence, "List my open tasks.")
        self.assertTrue(verdict["ok"], verdict["reason"])

    def test_a_wrong_route_tool_fails_even_when_the_turn_answered(self) -> None:
        """The regression this battery exists for: a task ask reaching the wiki."""
        evidence = live_probe.read_turn([_requested("wiki_scout_search"), _result("wiki_scout_search")])
        verdict = live_probe.assert_correct_tool(evidence, "List my open tasks.")
        self.assertFalse(verdict["ok"])
        self.assertIn("wiki_scout_search", verdict["foreign"])

    def test_no_tool_call_fails_when_the_route_requires_one(self) -> None:
        evidence = live_probe.read_turn([_completed("Here are your tasks.")])
        verdict = live_probe.assert_correct_tool(evidence, "List my open tasks.")
        self.assertFalse(verdict["ok"])
        self.assertIn("no tool was called", verdict["reason"])

    def test_no_tool_call_passes_when_the_route_requires_none(self) -> None:
        """The green path serves a wiki ask from prefetched evidence.

        The server tells Eve to skip the tool call, so "no tool called" is
        correct there - only a foreign tool would be a failure.
        """
        evidence = live_probe.read_turn([_completed("The Kick Inside and Lionheart.")])
        verdict = live_probe.assert_correct_tool(
            evidence, "What album did Kate Bush release in 1978?", allowed=[]
        )
        self.assertTrue(verdict["ok"], verdict["reason"])
        self.assertEqual(verdict["foreign"], [])

    def test_a_foreign_tool_still_fails_when_no_tool_is_required(self) -> None:
        evidence = live_probe.read_turn([_requested("cognee_recall")])
        verdict = live_probe.assert_correct_tool(
            evidence, "What album did Kate Bush release in 1978?", allowed=[]
        )
        self.assertFalse(verdict["ok"])
        self.assertIn("cognee_recall", verdict["foreign"])

    def test_the_wiki_tools_are_forbidden_outside_the_wiki_route(self) -> None:
        forbidden = live_probe.forbidden_tools_for(route_classifier.TASK)
        self.assertIn("wiki_scout_search", forbidden)
        self.assertNotIn("list_tasks", forbidden)


class RouteFamilyTests(unittest.TestCase):
    def test_families_are_read_from_the_codex(self) -> None:
        families = live_probe.route_tool_families()
        self.assertIn("wiki_scout_search", families[route_classifier.WIKI])
        self.assertIn("cognee_recall", families[route_classifier.MEMORY])
        self.assertIn("list_tasks", families[route_classifier.TASK])


if __name__ == "__main__":
    unittest.main()
