"""Refresh stored cards before renewals run: a card that has expired or been reissued
by the bank gets its new expiry date or its replacement token from the processor's
account updater, so the renewal charge does not fail on an old card."""
from services.payments.cards import CardStore
from services.payments.processor import ProcessorClient


class CardUpdater:
    def __init__(self, processor=None, cards=None):
        self.processor = processor or ProcessorClient()
        self.cards = cards or CardStore()

    def refresh_expiring(self, within_days=30):
        tokens = self.cards.tokens_expiring_within(within_days)
        updated = 0
        for result in self.processor.account_updater(tokens):
            if result.new_token or result.new_expiry:
                self.cards.replace(result.token, result.new_token or result.token,
                                   result.new_expiry)
                updated += 1
        return updated
