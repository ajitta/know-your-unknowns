"""Nightly jobs and delayed tasks. The scheduler worker (libs/scheduler_worker.py) runs
whatever is due."""
from datetime import datetime

_nightly = []   # ("HH:MM" in UTC, job)
_handlers = {}  # task name -> handler(payload)
_queue = []     # (when, task name, payload)


def nightly(at):
    """Register a function to run every night at the given "HH:MM" (UTC)."""
    def register(job):
        _nightly.append((at, job))
        return job
    return register


def task(name):
    """Register the handler of a named delayed task."""
    def register(handler):
        _handlers[name] = handler
        return handler
    return register


class Scheduler:
    def run_at(self, when: datetime, task_name: str, payload: dict):
        """Queue a named task to run at a given time."""
        _queue.append((when, task_name, payload))


def run_due(now: datetime, last_run: datetime):
    for at, job in _nightly:
        hour, minute = map(int, at.split(":"))
        slot = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
        if last_run < slot <= now:
            job()
    for entry in [entry for entry in _queue if entry[0] <= now]:
        _queue.remove(entry)
        _handlers[entry[1]](entry[2])
