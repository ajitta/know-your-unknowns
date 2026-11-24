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


if __name__ == "__main__":
    unittest.main()
