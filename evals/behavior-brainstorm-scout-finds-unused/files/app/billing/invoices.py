"""Monthly invoices."""
from dataclasses import dataclass

from app.billing.plans import plan


@dataclass
class Invoice:
    id: int
    customer_id: int
    plan_code: str
    amount: int
    period: str  # "2026-10"
    paid: bool = False


def issue(store, customer, period):
    details = plan(customer.plan)
    invoice = Invoice(id=store.next_id("invoices"), customer_id=customer.id,
                      plan_code=customer.plan, amount=details["monthly_price"], period=period)
    return store.put("invoices", invoice)


def mark_paid(store, invoice_id):
    invoice = store.get("invoices", invoice_id)
    if invoice is None:
        raise KeyError("no invoice %s" % invoice_id)
    invoice.paid = True
    return invoice


def unpaid(store, customer_id):
    return [i for i in store.all("invoices") if i.customer_id == customer_id and not i.paid]
