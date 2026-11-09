"""Response-time figures for the weekly support report."""
from statistics import median

CLOSED = ("solved", "closed")


def first_response_hours(tickets):
    return [(t.first_response_at - t.created_at).total_seconds() / 3600
            for t in tickets if t.first_response_at is not None]


def median_first_response_hours(tickets):
    hours = first_response_hours(tickets)
    return median(hours) if hours else None


def backlog(tickets):
    """Tickets still waiting for their first agent reply."""
    return [t for t in tickets if t.first_response_at is None and t.status not in CLOSED]
