import unittest

from app.billing import invoices
from app.db import Store
from app.users.service import UserService


class InvoiceTest(unittest.TestCase):
    def setUp(self):
        self.store = Store()
        self.customer = UserService(self.store).create("Ana", "ana@example.com", plan="team")

    def test_invoice_charges_the_plan_price(self):
        invoice = invoices.issue(self.store, self.customer, "2026-10")
        self.assertEqual(invoice.amount, 49)

    def test_paid_invoices_leave_the_unpaid_list(self):
        first = invoices.issue(self.store, self.customer, "2026-09")
        second = invoices.issue(self.store, self.customer, "2026-10")
        invoices.mark_paid(self.store, first.id)
        self.assertEqual(invoices.unpaid(self.store, self.customer.id), [second])


if __name__ == "__main__":
    unittest.main()
