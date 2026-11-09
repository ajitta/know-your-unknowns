"""Ticket fields and the values they may take."""
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import List, Optional

STATUSES = ("new", "open", "waiting_on_customer", "solved", "closed")
PRIORITIES = ("low", "normal", "high", "urgent")
CATEGORIES = ("billing", "login", "bug", "how_to", "account", "other")
CHANNELS = ("web", "email")


def _now():
    return datetime.now(timezone.utc)


@dataclass
class Ticket:
    id: int
    customer_id: int
    subject: str
    body: str
    channel: str = "web"
    status: str = "new"
    priority: str = "normal"
    category: Optional[str] = None
    assignee_id: Optional[int] = None
    created_at: datetime = field(default_factory=_now)
    first_response_at: Optional[datetime] = None
    replies: List[dict] = field(default_factory=list)
