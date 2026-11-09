# Helpdesk

Our support helpdesk: customers open tickets from the web form or by email, support
agents pick them up from the queue and reply, and customers get email updates.

    app/tickets/        tickets, the agent queue, response-time figures
    app/users/          customers, agents and admins
    app/notifications/  outgoing email
    app/billing/        plans and invoices
    tests/              unit tests

Standard library only (Python 3.9+). Tests: `python3 -m unittest`
