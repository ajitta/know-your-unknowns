"""The plans a customer can be on."""

PLANS = {
    "starter": {"name": "Starter", "monthly_price": 0, "seats": 1, "priority_support": False},
    "team": {"name": "Team", "monthly_price": 49, "seats": 10, "priority_support": False},
    "business": {"name": "Business", "monthly_price": 199, "seats": 50, "priority_support": True},
}


def plan(code):
    if code not in PLANS:
        raise KeyError("no plan %r" % code)
    return PLANS[code]
