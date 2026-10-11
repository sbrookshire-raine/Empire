import unittest

from frontend.speech_aliases import apply_speech_aliases


class SpeechAliasTests(unittest.TestCase):
    def test_get_hub_becomes_github(self) -> None:
        self.assertIn(
            "GitHub",
            apply_speech_aliases("Can you go to get hub and find popular repos?"),
        )
        self.assertIn("GitHub", apply_speech_aliases("go to get-hub for mcp servers"))

    def test_git_hub_becomes_github(self) -> None:
        self.assertEqual(
            apply_speech_aliases("search git hub for duckdb"),
            "search GitHub for duckdb",
        )

    def test_docker_hub_unchanged(self) -> None:
        self.assertIn(
            "docker hub",
            apply_speech_aliases("search docker hub for nginx").casefold(),
        )

    def test_beach_boises_typo(self) -> None:
        self.assertIn(
            "Beach Boys",
            apply_speech_aliases("names of the Beach Boises albums"),
        )


if __name__ == "__main__":
    unittest.main()
