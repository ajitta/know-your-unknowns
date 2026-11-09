import unittest

from legacy.autotriage.triage import triage


class TriageTest(unittest.TestCase):
    def test_password_ticket_gets_a_canned_reply(self):
        result = triage("Locked out", "I can't log in, the password reset link expired.",
                        name="Ana", ticket_id=7)
        self.assertEqual((result["category"], result["priority"]), ("password_reset", "normal"))
        self.assertIn("Hi Ana", result["reply"])
        self.assertIn("Ticket #7", result["reply"])

    def test_outage_is_urgent_and_goes_to_an_agent(self):
        result = triage("Site is down", "The dashboard is not loading, error 500.")
        self.assertEqual((result["category"], result["priority"]), ("outage", "urgent"))
        self.assertIsNone(result["reply"])

    def test_keywords_match_whole_words(self):
        result = triage("Download", "Where is the markdown download?")
        self.assertNotEqual(result["category"], "outage")

    def test_no_match_is_general(self):
        result = triage("Thanks", "Just wanted to say the new layout looks great.")
        self.assertEqual(result["category"], "general")
        self.assertIsNone(result["reply"])


if __name__ == "__main__":
    unittest.main()
