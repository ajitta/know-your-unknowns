import unittest

from app import create_app


class OrderRoutesTest(unittest.TestCase):
    def setUp(self):
        self.client = create_app().test_client()
        customer = self.client.post("/customers", json={"name": "Ana", "email": "ana@example.org"})
        self.customer_id = customer.get_json()["id"]

    def place(self, **changes):
        body = {"customer_id": self.customer_id, "pickup_at": "2026-04-04T09:30:00",
                "lines": [{"item": "rye", "quantity": 1}]}
        body.update(changes)
        return self.client.post("/orders", json=body)

    def test_place_order(self):
        response = self.place()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()["status"], "placed")

    def test_unknown_customer_is_404(self):
        self.assertEqual(self.place(customer_id=999).status_code, 404)

    def test_bad_pickup_time_is_422(self):
        self.assertEqual(self.place(pickup_at="2026-04-04T05:00:00").status_code, 422)

    def test_change_pickup_time(self):
        order = self.place().get_json()
        response = self.client.post("/orders/%d/pickup-time" % order["id"],
                                    json={"pickup_at": "2026-04-04T11:00:00"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["pickup_at"], "2026-04-04T11:00:00")


if __name__ == "__main__":
    unittest.main()
