"""Client for the card processor's API. Card numbers never reach our servers: the
checkout page sends them to the processor, which returns a token that we store."""
from dataclasses import dataclass

from libs.http import HttpClient
from services.payments.config import settings


class CardDeclined(Exception):
    def __init__(self, code):
        super().__init__(code)
        self.code = code


@dataclass
class UpdatedCard:
    token: str
    new_token: str = ""
    new_expiry: str = ""


class ProcessorClient:
    def __init__(self, http=None):
        self.http = http or HttpClient(settings.processor["base_url"],
                                       api_key=settings.processor["api_key_env"])

    def charge(self, card_token, amount, reference):
        reply = self.http.post("/v2/charges", {"card": card_token, "amount": amount,
                                               "currency": "GBP", "reference": reference})
        if reply["outcome"] != "approved":
            raise CardDeclined(reply.get("decline_code", "unknown"))
        return reply["charge_id"]

    def refund(self, charge_id, amount):
        return self.http.post("/v2/refunds", {"charge": charge_id, "amount": amount})

    def account_updater(self, card_tokens):
        """Ask the card networks, through the processor, which stored cards were renewed
        or reissued. Part of our processing contract; no extra fee per lookup."""
        reply = self.http.post("/v2/account-updater/batches", {"cards": list(card_tokens)})
        return [UpdatedCard(row["card"], row.get("new_card", ""), row.get("new_expiry", ""))
                for row in reply["results"]]
