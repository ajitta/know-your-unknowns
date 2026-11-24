"""Stored card tokens, one default card per account."""
from datetime import date, timedelta

from libs.db import connection


class CardStore:
    table = "cards"

    def __init__(self, conn=None):
        self.conn = conn or connection()

    def token_for(self, account_id):
        row = self.conn.fetch(self.table, account_id)
        return None if row is None else row["token"]

    def tokens_expiring_within(self, days):
        cutoff = (date.today() + timedelta(days=days)).isoformat()
        rows = self.conn.scan(self.table, limit=100000)
        return [row["token"] for row in rows if row["expiry"] <= cutoff]

    def replace(self, old_token, new_token, new_expiry):
        for row in self.conn.scan(self.table, limit=100000):
            if row["token"] == old_token:
                row["token"] = new_token
                if new_expiry:
                    row["expiry"] = new_expiry
                self.conn.upsert(self.table, row["account_id"], row)
