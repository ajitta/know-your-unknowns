"""First replies for the routine categories. A category with no reply here (outage,
general) always goes to an agent."""

REPLIES = {
    "password_reset": (
        "Hi {name},\n\n"
        "You can set a new password at https://help.example.com/reset. The link in that\n"
        "email works for 30 minutes. If you use a login code and lost the device, reply\n"
        "to this email and an agent will reset it for you.\n\n"
        "Ticket #{ticket_id}"
    ),
    "billing": (
        "Hi {name},\n\n"
        "Your invoices and receipts are under Settings > Billing. For a refund or a\n"
        "charge you do not recognise, reply with the invoice number and an agent will\n"
        "look into it.\n\n"
        "Ticket #{ticket_id}"
    ),
    "account_change": (
        "Hi {name},\n\n"
        "Account admins can add or remove users and change the account email under\n"
        "Settings > Team. If you are not an admin, ask the person who set up the\n"
        "account, or reply here.\n\n"
        "Ticket #{ticket_id}"
    ),
    "how_to": (
        "Hi {name},\n\n"
        "Our step-by-step guides are at https://help.example.com/guides. If they do not\n"
        "answer your question, reply to this email and an agent will help.\n\n"
        "Ticket #{ticket_id}"
    ),
}


def reply_for(category, name="there", ticket_id="?"):
    template = REPLIES.get(category)
    if template is None:
        return None
    return template.format(name=name, ticket_id=ticket_id)
