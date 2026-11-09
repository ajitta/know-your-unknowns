import unittest
from datetime import datetime, timedelta, timezone
from unittest import mock

from app.tickets import metrics, queue
from app.tickets.models import Ticket
from app.users.models import User

START = datetime(2026, 10, 5, 9, 0, tzinfo=timezone.utc)


def ticket(ticket_id, hours_ago=0, **fields):
    return Ticket(id=ticket_id, customer_id=1, subject="s", body="b",
                  created_at=START - timedelta(hours=hours_ago), **fields)


class QueueTest(unittest.TestCase):
    def test_unassigned_is_oldest_first(self):
        tickets = [ticket(1, 2), ticket(2, 30), ticket(3, 5, assignee_id=9)]
        self.assertEqual([t.id for t in queue.unassigned(tickets)], [2, 1])

    def test_pick_up_opens_the_ticket(self):
        agent = User(id=9, name="Ben", email="ben@example.com", role="agent")
        picked = queue.pick_up(ticket(1), agent, [])
        self.assertEqual((picked.assignee_id, picked.status), (9, "open"))

    def test_an_agent_at_the_cap_cannot_take_more(self):
        agent = User(id=9, name="Ben", email="ben@example.com", role="agent")
        held = [ticket(i, assignee_id=9, status="open") for i in range(2, 4)]
        with mock.patch.object(queue, "MAX_OPEN_PER_AGENT", 2):
            with self.assertRaises(ValueError):
                queue.pick_up(ticket(1), agent, held)


class MetricsTest(unittest.TestCase):
    def test_median_first_response(self):
        tickets = [ticket(1, first_response_at=START + timedelta(hours=10)),
                   ticket(2, first_response_at=START + timedelta(hours=72)),
                   ticket(3, first_response_at=START + timedelta(hours=80)),
                   ticket(4)]
        self.assertEqual(metrics.median_first_response_hours(tickets), 72)
        self.assertEqual([t.id for t in metrics.backlog(tickets)], [4])


if __name__ == "__main__":
    unittest.main()
