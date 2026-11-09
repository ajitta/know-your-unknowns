"""Score a ticket against the keyword rules."""
import re

from .rules import DEFAULT, RULES


def _hits(text, keywords):
    return [word for word in keywords if re.search(r"\b%s\b" % re.escape(word), text)]


def classify(subject, body):
    """Return (category, priority, matched keywords) for one ticket."""
    text = ("%s\n%s" % (subject, body)).lower()
    best, best_hits = None, []
    for rule in RULES:
        hits = _hits(text, rule["keywords"])
        if len(hits) > len(best_hits):
            best, best_hits = rule, hits
    rule = best or DEFAULT
    return rule["category"], rule["priority"], best_hits
