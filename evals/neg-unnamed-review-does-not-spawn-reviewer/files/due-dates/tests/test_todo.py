import unittest

import todo


class TodoTest(unittest.TestCase):
    def test_add_numbers_tasks(self):
        tasks = []
        todo.add(tasks, "buy milk")
        todo.add(tasks, "call Sam")
        self.assertEqual([task["id"] for task in tasks], [1, 2])

    def test_pending_skips_done_tasks(self):
        tasks = []
        todo.add(tasks, "buy milk")
        todo.add(tasks, "call Sam")
        todo.complete(tasks, 1)
        self.assertEqual([task["title"] for task in todo.pending(tasks)], ["call Sam"])

    def test_add_keeps_the_due_date(self):
        tasks = []
        todo.add(tasks, "file taxes", due="2026-04-30")
        self.assertEqual(tasks[0]["due"], "2026-04-30")

    def test_line_shows_the_due_date(self):
        tasks = []
        todo.add(tasks, "file taxes", due="2026-04-30")
        self.assertEqual(todo.line(tasks[0]), "- 1 file taxes (due 2026-04-30)")


if __name__ == "__main__":
    unittest.main()
