"""The payments service's nightly jobs and delayed tasks."""
from libs.scheduler import nightly, task
from services.payments.card_updater import CardUpdater
from services.payments.config import settings
from services.payments.service import PaymentService


@nightly(at="00:45")
def refresh_cards():
    if not settings.card_updater_enabled:
        return 0
    return CardUpdater().refresh_expiring(within_days=30)


@nightly(at="01:30")
def charge_renewals():
    PaymentService().charge_due_renewals()


@task("payments.retry_due")
def retry_renewal(payload):
    from services.subscriptions.service import SubscriptionService
    subscriptions = SubscriptionService()
    renewal = subscriptions.renewal_for(payload["subscription_id"])
    if renewal is not None:
        PaymentService(subscriptions=subscriptions).charge_renewal(
            renewal, attempt=payload["attempt"])
