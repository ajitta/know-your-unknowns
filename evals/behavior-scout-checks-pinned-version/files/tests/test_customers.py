import unittest

from app import create_app


class CustomerRoutesTest(unittest.TestCase):
    def setUp(self):
        self.client = create_app().test_client()

    def register(self):
        response = self.client.post("/customers", json={"name": "Ana", "email": "ana@example.org"})
        return response.get_json()

    def test_create_and_fetch(self):
        created = self.register()
        fetched = self.client.get("/customers/%d" % created["id"])
        self.assertEqual(fetched.get_json()["email"], "ana@example.org")

    def test_bad_email_is_422(self):
        response = self.client.post("/customers", json={"name": "Ana", "email": "nope"})
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.get_json()["errors"][0]["loc"], ["email"])

    def test_update_phone(self):
        created = self.register()
        response = self.client.patch("/customers/%d" % created["id"], json={"phone": "5551234567"})
        self.assertEqual(response.get_json()["phone"], "5551234567")

    def test_missing_customer_is_404(self):
        self.assertEqual(self.client.get("/customers/99").status_code, 404)


if __name__ == "__main__":
    unittest.main()
