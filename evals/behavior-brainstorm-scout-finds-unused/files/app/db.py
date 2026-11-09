"""An in-memory store with the small interface the services use."""
import itertools


class Store:
    def __init__(self):
        self._tables = {}
        self._ids = {}

    def next_id(self, table):
        counter = self._ids.setdefault(table, itertools.count(1))
        return next(counter)

    def put(self, table, row):
        self._tables.setdefault(table, {})[row.id] = row
        return row

    def get(self, table, row_id):
        return self._tables.get(table, {}).get(row_id)

    def all(self, table):
        return list(self._tables.get(table, {}).values())
