"""Wires the services together and maps request paths to handlers."""
from app.billing import routes as billing_routes
from app.db import Store
from app.notifications.dispatcher import Dispatcher
from app.notifications.email import Mailer
from app.tickets import routes as ticket_routes
from app.tickets.service import TicketService
from app.users import routes as user_routes
from app.users.service import UserService


def build_app(mailer=None):
    store = Store()
    dispatcher = Dispatcher(mailer or Mailer())
    users = UserService(store)
    tickets = TicketService(store, users, dispatcher)
    handlers = {}
    handlers.update(ticket_routes.routes(tickets))
    handlers.update(user_routes.routes(users))
    handlers.update(billing_routes.routes(store, users))
    return handlers


def handle(handlers, method, path, data):
    handler = handlers.get((method, path))
    if handler is None:
        return 404, {"error": "no route for %s %s" % (method, path)}
    try:
        return 200, handler(data)
    except (KeyError, ValueError) as error:
        return 400, {"error": str(error)}
