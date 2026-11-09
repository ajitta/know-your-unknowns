"""Request handlers for tickets; each takes the request data as a dict."""
from app.tickets import metrics


def routes(tickets):
    def create(data):
        ticket = tickets.open_ticket(data["customer_id"], data["subject"], data["body"],
                                     data.get("channel", "web"))
        return {"id": ticket.id, "status": ticket.status}

    def reply(data):
        ticket = tickets.reply(data["ticket_id"], data["author_id"], data["text"])
        return {"id": ticket.id, "status": ticket.status}

    def show(data):
        ticket = tickets.get(data["ticket_id"])
        return {"id": ticket.id, "subject": ticket.subject, "status": ticket.status,
                "priority": ticket.priority, "category": ticket.category,
                "assignee_id": ticket.assignee_id}

    def report(data):
        everything = tickets.all()
        return {"median_first_response_hours": metrics.median_first_response_hours(everything),
                "backlog": len(metrics.backlog(everything))}

    return {
        ("POST", "/tickets"): create,
        ("POST", "/tickets/reply"): reply,
        ("GET", "/tickets/show"): show,
        ("GET", "/tickets/report"): report,
    }
