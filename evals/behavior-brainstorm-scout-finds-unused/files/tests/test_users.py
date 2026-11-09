import unittest

from app.db import Store
from app.users.service import UserService


class UserServiceTest(unittest.TestCase):
    def setUp(self):
        self.users = UserService(Store())

    def test_email_is_unique_ignoring_case(self):
        self.users.create("Ana", "ana@example.com")
        with self.assertRaises(ValueError):
            self.users.create("Ana B", "ANA@example.com")

    def test_agents_leaves_out_inactive_ones(self):
        ben = self.users.create("Ben", "ben@example.com", role="agent")
        self.users.create("Cy", "cy@example.com", role="agent")
        self.users.deactivate(ben.id)
        self.assertEqual([u.name for u in self.users.agents()], ["Cy"])


if __name__ == "__main__":
    unittest.main()
