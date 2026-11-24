"""Which messages go out for which events. register() runs when the notifications
worker starts and subscribes each handler to its event."""
from pathlib import Path

from libs.events.bus import subscribe
from libs.templating import render
from services.notifications.sender import send_email, send_sms

HERE = Path(__file__).resolve().parent


def order_created(event):
    send_email(event["account_id"], "Your order is confirmed",
               render(HERE, "order_created.html", event))


def payment_failed(event):
    # Ask the subscriber to update their card before the retry runs.
    send_email(event["account_id"], "Your payment didn't go through",
               render(HERE, "payment_failed.html", event))
    send_sms(event["account_id"], render(HERE, "payment_failed.txt", event))


HANDLERS = {
    "order.created": order_created,
    "payment.failed": payment_failed,
}


def register():
    for event_name, handler in HANDLERS.items():
        subscribe(event_name, handler)
