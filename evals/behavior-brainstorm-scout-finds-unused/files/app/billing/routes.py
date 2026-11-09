"""Request handlers for billing."""
from app.billing import invoices


def routes(store, users):
    def issue(data):
        customer = users.get(data["customer_id"])
        invoice = invoices.issue(store, customer, data["period"])
        return {"id": invoice.id, "amount": invoice.amount}

    def unpaid(data):
        return {"invoices": [i.id for i in invoices.unpaid(store, data["customer_id"])]}

    return {
        ("POST", "/billing/invoices"): issue,
        ("GET", "/billing/unpaid"): unpaid,
    }
