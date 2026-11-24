"""A thin key-value layer over Postgres: one JSONB row per record, keyed by id."""
import json
import os

import psycopg

_conn = None


class Connection:
    def __init__(self, dsn):
        self.raw = psycopg.connect(dsn, autocommit=True)

    def upsert(self, table, key, row):
        self.raw.execute(
            "INSERT INTO %s (id, doc) VALUES (%%s, %%s) "
            "ON CONFLICT (id) DO UPDATE SET doc = EXCLUDED.doc" % table,
            (key, json.dumps(row)))

    def fetch(self, table, key):
        found = self.raw.execute("SELECT doc FROM %s WHERE id = %%s" % table, (key,)).fetchone()
        return None if found is None else found[0]

    def scan(self, table, limit=50, offset=0):
        rows = self.raw.execute("SELECT doc FROM %s ORDER BY id LIMIT %%s OFFSET %%s" % table,
                                (limit, offset)).fetchall()
        return [row[0] for row in rows]


def connection():
    global _conn
    if _conn is None:
        _conn = Connection(os.environ["DATABASE_URL"])
    return _conn
