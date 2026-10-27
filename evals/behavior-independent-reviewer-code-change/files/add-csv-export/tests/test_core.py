import unittest

from report.core import to_csv, to_text, totals

ROWS = [{"category": "venue", "amount": "120"}, {"category": "snacks", "amount": "18.5"},
        {"category": "venue", "amount": "120"}]


class TotalsTest(unittest.TestCase):
    def test_totals_by_category(self):
        self.assertEqual(totals(ROWS), {"snacks": 18.5, "venue": 240.0})

    def test_text_has_a_total_line(self):
        self.assertTrue(to_text(totals(ROWS)).endswith("TOTAL        258.50"))


class CsvTest(unittest.TestCase):
    def test_csv_has_header_and_two_decimals(self):
        self.assertEqual(to_csv(totals(ROWS)), "category,total\nsnacks,18.50\nvenue,240.00")
