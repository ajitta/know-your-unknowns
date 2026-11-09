"""Email bodies, each formatted with the fields named in it."""

TICKET_RECEIVED = """Hi {name},

We have received your request "{subject}" (ticket #{ticket_id}).
An agent will reply as soon as possible.

The Support Team"""

AGENT_REPLIED = """Hi {name},

{text}

Reply to this email to answer. Ticket #{ticket_id}.
The Support Team"""

INVOICE_ISSUED = """Hi {name},

Your invoice for {period} is ready: {amount} USD for the {plan} plan.

The Billing Team"""
