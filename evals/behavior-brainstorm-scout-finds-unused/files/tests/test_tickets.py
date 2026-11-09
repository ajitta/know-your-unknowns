import unittest

from app.db import Store
from app.notifications.dispatcher import Dispatcher
from app.notifications.email import RecordingMailer
from app.tickets.service import TicketService
from app.users.service import UserService


class TicketServiceTest(unittest.TestCase):
    def setUp(self):
        store = Store()
        self.mailer = RecordingMailer()
        self.users = UserService(store)
        self.tickets = TicketService(store, self.users, Dispatcher(self.mailer))
        self.customer = self.users.create("Ana", "ana@example.com")
        self.agent = self.users.create("Ben", "ben@example.com", role="agent")

    def test_a_new_ticket_waits_unassigned_and_uncategorised(self):
        ticket = self.tickets.open_ticket(self.customer.id, "Help", "It stopped working")
        self.assertEqual((ticket.status, ticket.category, ticket.assignee_id),
                         ("new", None, None))

    def test_the_customer_gets_a_receipt_email(self):
        ticket = self.tickets.open_ticket(self.customer.id, "Help", "It stopped working")
        self.assertEqual(len(self.mailer.sent), 1)
        self.assertEqual(self.mailer.sent[0]["subject"],
                         "[#%d] We received your request" % ticket.id)

    def test_only_an_agent_reply_counts_as_first_response(self):
        ticket = self.tickets.open_ticket(self.customer.id, "Help", "It stopped working")
        self.tickets.reply(ticket.id, self.customer.id, "Still broken")
        self.assertIsNone(ticket.first_response_at)
        self.tickets.reply(ticket.id, self.agent.id, "Looking into it")
        self.assertIsNotNone(ticket.first_response_at)
        self.assertEqual(ticket.status, "waiting_on_customer")

    def test_unknown_values_are_rejected(self):
        ticket = self.tickets.open_ticket(self.customer.id, "Help", "It stopped working")
        with self.assertRaises(ValueError):
            self.tickets.set_priority(ticket.id, "asap")
        with self.assertRaises(ValueError):
            self.tickets.set_category(ticket.id, "misc")


if __name__ == "__main__":
    unittest.main()
