"""Settings read once at start-up."""
import os

SUPPORT_FROM = os.environ.get("HELPDESK_SUPPORT_FROM", "support@helpdesk.example.com")
SMTP_HOST = os.environ.get("HELPDESK_SMTP_HOST", "localhost")

# The most tickets one agent may hold open at a time.
MAX_OPEN_PER_AGENT = int(os.environ.get("HELPDESK_MAX_OPEN_PER_AGENT", "25"))
