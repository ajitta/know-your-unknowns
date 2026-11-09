import unittest
from datetime import datetime

from pydantic import ValidationError

from app.models import CustomerIn, OrderIn


class CustomerInTest(unittest.TestCase):
    def test_email_is_lowercased(self):
        customer = CustomerIn.parse_obj({"name": "Ana", "email": "Ana@Example.org"})
        self.assertEqual(customer.email, "ana@example.org")

    def test_phone_keeps_digits_only(self):
        customer = CustomerIn(name="Ana", email="ana@example.org", phone="555-123 4567")
        self.assertEqual(customer.phone, "5551234567")

    def test_name_is_stripped(self):
        customer = CustomerIn(name="  Ana  ", email="ana@example.org")
        self.assertEqual(customer.name, "Ana")

    def test_unknown_field_is_rejected(self):
        with self.assertRaises(ValidationError):
            CustomerIn.parse_obj({"name": "Ana", "email": "ana@example.org", "vip": True})


class OrderInTest(unittest.TestCase):
    def payload(self, **changes):
        data = {"customer_id": 1, "pickup_at": "2026-04-04T09:30:00",
                "lines": [{"item": "sourdough", "quantity": 2}]}
        data.update(changes)
        return data

    def test_valid_order(self):
        order = OrderIn.parse_obj(self.payload())
        self.assertEqual(order.pickup_at, datetime(2026, 4, 4, 9, 30))
        self.assertEqual(order.dict()["lines"], [{"item": "sourdough", "quantity": 2}])

    def test_pickup_outside_opening_hours(self):
        with self.assertRaises(ValidationError):
            OrderIn.parse_obj(self.payload(pickup_at="2026-04-04T21:00:00"))

    def test_item_not_on_menu(self):
        with self.assertRaises(ValidationError):
            OrderIn.parse_obj(self.payload(lines=[{"item": "bagel", "quantity": 1}]))

    def test_empty_order(self):
        with self.assertRaises(ValidationError):
            OrderIn.parse_obj(self.payload(lines=[]))


if __name__ == "__main__":
    unittest.main()
