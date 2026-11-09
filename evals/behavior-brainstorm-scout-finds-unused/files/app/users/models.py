"""User fields."""
from dataclasses import dataclass
from typing import Optional

ROLES = ("customer", "agent", "admin")


@dataclass
class User:
    id: int
    name: str
    email: str
    role: str = "customer"
    is_active: bool = True
    plan: Optional[str] = None  # billing plan code; customers only
