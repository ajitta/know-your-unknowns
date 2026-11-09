"""Triage the sample tickets: python3 -m legacy.autotriage"""
from .triage import triage

SAMPLES = [
    ("Locked out", "I can't log in, the password reset link expired."),
    ("Charged twice", "My credit card was charged twice for the March invoice."),
    ("Site is down", "The dashboard is not loading, error 500 for everyone here."),
    ("Question", "How do I export my contacts?"),
    ("Thanks", "Just wanted to say the new layout looks great."),
]

for subject, body in SAMPLES:
    result = triage(subject, body)
    print("%-14s -> %-15s %-7s canned reply: %s" % (
        subject, result["category"], result["priority"],
        "yes" if result["reply"] else "no, goes to an agent"))
