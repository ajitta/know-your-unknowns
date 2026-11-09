"""In-memory storage. One counter hands out ids for customers and orders alike."""
import itertools
import threading


class Store:
    def __init__(self):
        self._lock = threading.Lock()
        self._ids = itertools.count(1)
        self.customers = {}
        self.orders = {}

    def next_id(self):
        with self._lock:
            return next(self._ids)
