"""The agent queue: unassigned tickets, oldest first, picked up by hand."""
from app.config import MAX_OPEN_PER_AGENT

CLOSED = ("solved", "closed")


def unassigned(tickets):
    waiting = [t for t in tickets if t.assignee_id is None and t.status not in CLOSED]
    return sorted(waiting, key=lambda t: t.created_at)


def open_count(tickets, agent_id):
    return sum(1 for t in tickets if t.assignee_id == agent_id and t.status not in CLOSED)


def pick_up(ticket, agent, tickets):
    if agent.role != "agent" or not agent.is_active:
        raise ValueError("user %s cannot take tickets" % agent.id)
    if open_count(tickets, agent.id) >= MAX_OPEN_PER_AGENT:
        raise ValueError("agent %s already holds %d open tickets" % (agent.id, MAX_OPEN_PER_AGENT))
    ticket.assignee_id = agent.id
    if ticket.status == "new":
        ticket.status = "open"
    return ticket
