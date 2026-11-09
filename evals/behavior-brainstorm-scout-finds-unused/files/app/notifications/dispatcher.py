"""Which email goes out on which event."""
from app.notifications import templates


class Dispatcher:
    def __init__(self, mailer):
        self.mailer = mailer

    def ticket_received(self, customer, ticket):
        body = templates.TICKET_RECEIVED.format(name=customer.name, subject=ticket.subject,
                                                ticket_id=ticket.id)
        self.mailer.send(customer.email, "[#%d] We received your request" % ticket.id, body)

    def agent_replied(self, customer, ticket, text):
        body = templates.AGENT_REPLIED.format(name=customer.name, text=text, ticket_id=ticket.id)
        self.mailer.send(customer.email, "[#%d] %s" % (ticket.id, ticket.subject), body)

    def invoice_issued(self, customer, invoice, plan_name):
        body = templates.INVOICE_ISSUED.format(name=customer.name, period=invoice.period,
                                               amount=invoice.amount, plan=plan_name)
        self.mailer.send(customer.email, "Your invoice for %s" % invoice.period, body)
