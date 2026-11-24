# libs/dunning

A retry schedule for declined renewal charges, written in June 2024 for the payments rewrite. The rewrite was paused in August 2024, before the schedule was wired into any service.

    from libs.dunning import DunningSchedule

    step = DunningSchedule().next_step(first_declined_at, attempts_so_far, decline_code)
    # step.action is "retry" (at step.at), "ask_for_new_card" or "cancel"

Tests: `pytest libs/dunning/tests`.
