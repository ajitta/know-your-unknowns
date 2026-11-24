"""When to retry a declined renewal charge.

Retries on days 1, 3, 5 and 8 after the first decline, at 09:00 UTC, moved to the next
weekday when one falls on a weekend: most cards declined for insufficient funds go
through after payday. A hard decline (a lost, stolen or closed card) is never retried;
the subscriber is asked for a new card instead. After the last retry the caller cancels.
"""
from dataclasses import dataclass
from datetime import datetime, time, timedelta

RETRY_DAYS = (1, 3, 5, 8)
RETRY_AT = time(9, 0)
HARD_DECLINES = {"lost_card", "stolen_card", "card_closed", "invalid_account"}


@dataclass
class NextStep:
    action: str  # "retry", "ask_for_new_card" or "cancel"
    at: datetime = None


class DunningSchedule:
    def __init__(self, retry_days=RETRY_DAYS):
        self.retry_days = tuple(retry_days)

    def next_step(self, first_declined_at, attempts_so_far, decline_code):
        """attempts_so_far counts every charge attempt made, the first one included."""
        if decline_code in HARD_DECLINES:
            return NextStep("ask_for_new_card")
        if attempts_so_far > len(self.retry_days):
            return NextStep("cancel")
        day = self.retry_days[attempts_so_far - 1]
        when = datetime.combine((first_declined_at + timedelta(days=day)).date(), RETRY_AT,
                                tzinfo=first_declined_at.tzinfo)
        while when.weekday() >= 5:
            when += timedelta(days=1)
        return NextStep("retry", when)
