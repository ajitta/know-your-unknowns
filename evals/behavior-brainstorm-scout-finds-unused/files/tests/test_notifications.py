import unittest

from app.main import build_app, handle
from app.notifications.email import RecordingMailer


class NotificationTest(unittest.TestCase):
    def test_agent_reply_is_emailed_to_the_customer(self):
        mailer = RecordingMailer()
        app = build_app(mailer)
        _, ana = handle(app, "POST", "/users", {"name": "Ana", "email": "ana@example.com"})
        _, ben = handle(app, "POST", "/users",
                        {"name": "Ben", "email": "ben@example.com", "role": "agent"})
        _, ticket = handle(app, "POST", "/tickets",
                           {"customer_id": ana["id"], "subject": "Export", "body": "How?"})
        handle(app, "POST", "/tickets/reply",
               {"ticket_id": ticket["id"], "author_id": ben["id"],
                "text": "Use Settings > Export."})
        self.assertEqual([m["to"] for m in mailer.sent], ["ana@example.com"] * 2)
        self.assertIn("Use Settings > Export.", mailer.sent[1]["body"])

    def test_unknown_route_is_404(self):
        status, _ = handle(build_app(RecordingMailer()), "GET", "/nowhere", {})
        self.assertEqual(status, 404)


if __name__ == "__main__":
    unittest.main()
