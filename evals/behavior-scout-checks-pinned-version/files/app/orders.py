from flask import Blueprint, abort, current_app, request

from .models import Order, OrderIn

bp = Blueprint("orders", __name__, url_prefix="/orders")


def _store():
    return current_app.config["STORE"]


def _respond(model, status=200):
    return current_app.response_class(model.json(), status=status, mimetype="application/json")


@bp.post("")
def create_order():
    data = OrderIn.parse_obj(request.get_json(force=True))
    store = _store()
    if data.customer_id not in store.customers:
        abort(404)
    order = Order(id=store.next_id(), **data.dict())
    store.orders[order.id] = order
    return _respond(order, 201)


@bp.get("/<int:order_id>")
def get_order(order_id):
    order = _store().orders.get(order_id) or abort(404)
    return _respond(order)


@bp.post("/<int:order_id>/pickup-time")
def change_pickup_time(order_id):
    store = _store()
    order = store.orders.get(order_id) or abort(404)
    payload = request.get_json(force=True)
    # Not validated yet: see PLAN.md.
    updated = order.copy(update={"pickup_at": payload["pickup_at"]})
    store.orders[order_id] = updated
    return _respond(updated)
