"""Opening tickets, replying to them and changing their fields."""
from datetime import datetime, timezone

from app.tickets.models import CATEGORIES, CHANNELS, PRIORITIES, STATUSES, Ticket


class TicketService:
    def __init__(self, store, users, dispatcher):
        self.store = store
        self.users = users
        self.dispatcher = dispatcher

    def open_ticket(self, customer_id, subject, body, channel="web"):
        if channel not in CHANNELS:
            raise ValueError("unknown channel %r" % channel)
        customer = self.users.get(customer_id)
        ticket = Ticket(id=self.store.next_id("tickets"), customer_id=customer.id,
                        subject=subject.strip(), body=body, channel=channel)
        self.store.put("tickets", ticket)
        self.dispatcher.ticket_received(customer, ticket)
        return ticket

    def reply(self, ticket_id, author_id, text):
        ticket = self.get(ticket_id)
        author = self.users.get(author_id)
        now = datetime.now(timezone.utc)
        ticket.replies.append({"author_id": author.id, "text": text, "at": now})
        if author.role == "agent":
            if ticket.first_response_at is None:
                ticket.first_response_at = now
            ticket.status = "waiting_on_customer"
            self.dispatcher.agent_replied(self.users.get(ticket.customer_id), ticket, text)
        else:
            ticket.status = "open"
        return ticket

    def set_priority(self, ticket_id, priority):
        if priority not in PRIORITIES:
            raise ValueError("unknown priority %r" % priority)
        ticket = self.get(ticket_id)
        ticket.priority = priority
        return ticket

    def set_category(self, ticket_id, category):
        if category not in CATEGORIES:
            raise ValueError("unknown category %r" % category)
        ticket = self.get(ticket_id)
        ticket.category = category
        return ticket

    def set_status(self, ticket_id, status):
        if status not in STATUSES:
            raise ValueError("unknown status %r" % status)
        ticket = self.get(ticket_id)
        ticket.status = status
        return ticket

    def get(self, ticket_id):
        ticket = self.store.get("tickets", ticket_id)
        if ticket is None:
            raise KeyError("no ticket %s" % ticket_id)
        return ticket

    def all(self):
        return self.store.all("tickets")
