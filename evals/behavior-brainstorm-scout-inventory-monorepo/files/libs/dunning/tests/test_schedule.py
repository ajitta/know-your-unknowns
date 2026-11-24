from datetime import datetime, timezone

from libs.dunning import DunningSchedule

FRIDAY = datetime(2024, 6, 14, 18, 30, tzinfo=timezone.utc)


def test_first_retry_skips_the_weekend():
    step = DunningSchedule().next_step(FRIDAY, 1, "insufficient_funds")
    assert step.action == "retry"
    assert step.at == datetime(2024, 6, 17, 9, 0, tzinfo=timezone.utc)


def test_last_retry_is_day_eight():
    step = DunningSchedule().next_step(FRIDAY, 4, "insufficient_funds")
    assert step.at.date() == datetime(2024, 6, 24).date()


def test_gives_up_after_the_last_retry():
    assert DunningSchedule().next_step(FRIDAY, 5, "insufficient_funds").action == "cancel"


def test_hard_decline_asks_for_a_new_card():
    assert DunningSchedule().next_step(FRIDAY, 1, "stolen_card").action == "ask_for_new_card"
