"""Keyword rules. A ticket whose subject or body contains a rule's keywords gets that
rule's category and priority; the rule with the most matching keywords wins, and on a
tie the earlier rule wins. Keywords match whole words, case-insensitively."""

RULES = [
    {"category": "outage", "priority": "urgent",
     "keywords": ["down", "outage", "not loading", "error 500", "500 error", "site is down",
                  "cannot access", "can't access"]},
    {"category": "password_reset", "priority": "normal",
     "keywords": ["password", "reset link", "locked out", "can't log in", "cannot log in",
                  "login code", "2fa"]},
    {"category": "billing", "priority": "normal",
     "keywords": ["invoice", "refund", "charged", "receipt", "payment", "credit card"]},
    {"category": "account_change", "priority": "low",
     "keywords": ["change my email", "add a user", "remove a user", "delete my account",
                  "rename"]},
    {"category": "how_to", "priority": "low",
     "keywords": ["how do i", "how to", "where do i", "where can i", "is there a way"]},
]

DEFAULT = {"category": "general", "priority": "normal"}
