from datetime import datetime, time
from typing import List, Optional

from pydantic import BaseModel, Field, validator

OPENING = time(7, 0)
CLOSING = time(18, 0)
MENU = {"sourdough", "rye", "baguette", "croissant", "cinnamon roll"}


class CustomerIn(BaseModel):
    name: str = Field(..., min_length=1, max_length=80)
    email: str
    phone: Optional[str] = None

    class Config:
        anystr_strip_whitespace = True
        extra = "forbid"

    @validator("email")
    def email_has_at(cls, value):
        if "@" not in value or value.startswith("@") or value.endswith("@"):
            raise ValueError("not an email address")
        return value.lower()

    @validator("phone")
    def phone_digits(cls, value):
        if value is None:
            return value
        digits = value.replace(" ", "").replace("-", "")
        if not digits.lstrip("+").isdigit() or len(digits) < 7:
            raise ValueError("phone must be digits, spaces or dashes")
        return digits


class Customer(CustomerIn):
    id: int


class OrderLine(BaseModel):
    item: str
    quantity: int = Field(..., gt=0, le=50)


class OrderIn(BaseModel):
    customer_id: int
    pickup_at: datetime
    lines: List[OrderLine] = Field(..., min_items=1)

    class Config:
        extra = "forbid"

    @validator("pickup_at")
    def within_opening_hours(cls, value):
        if not OPENING <= value.time() <= CLOSING:
            raise ValueError("pickup must be between 07:00 and 18:00")
        return value

    @validator("lines")
    def items_on_menu(cls, lines):
        unknown = [line.item for line in lines if line.item not in MENU]
        if unknown:
            raise ValueError("not on the menu: " + ", ".join(unknown))
        return lines


class Order(OrderIn):
    id: int
    status: str = "placed"
