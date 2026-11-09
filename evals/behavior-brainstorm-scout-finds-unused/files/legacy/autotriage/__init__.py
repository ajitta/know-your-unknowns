"""Ticket auto-triage from the v1 helpdesk.

Keyword rules put a ticket into a category with a priority and, for the routine
categories, pick a canned first reply.

    python3 -m legacy.autotriage                        # triage the sample tickets
    python3 -m unittest legacy.autotriage.test_triage   # run its tests
"""
from .triage import triage  # noqa: F401
