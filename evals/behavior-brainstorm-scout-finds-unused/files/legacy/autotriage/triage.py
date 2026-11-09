"""Triage one ticket: its category, its priority and, when there is one, a canned
first reply."""
from .canned_replies import reply_for
from .classifier import classify


def triage(subject, body, name="there", ticket_id="?"):
    category, priority, matched = classify(subject, body)
    return {
        "category": category,
        "priority": priority,
        "matched": matched,
        "reply": reply_for(category, name, ticket_id),
    }

