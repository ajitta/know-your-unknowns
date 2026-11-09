from flask import Blueprint, abort, current_app, jsonify, request

from .models import Customer, CustomerIn

bp = Blueprint("customers", __name__, url_prefix="/customers")


def _store():
    return current_app.config["STORE"]


@bp.post("")
def create_customer():
    data = CustomerIn.parse_obj(request.get_json(force=True))
    store = _store()
    customer = Customer(id=store.next_id(), **data.dict())
    store.customers[customer.id] = customer
    return jsonify(customer.dict()), 201


@bp.get("/<int:customer_id>")
def get_customer(customer_id):
    customer = _store().customers.get(customer_id) or abort(404)
    return jsonify(customer.dict())


@bp.patch("/<int:customer_id>")
def update_customer(customer_id):
    store = _store()
    customer = store.customers.get(customer_id) or abort(404)
    payload = request.get_json(force=True)
    # Not validated yet: see PLAN.md.
    updated = customer.copy(update=payload)
    store.customers[customer_id] = updated
    return jsonify(updated.dict())
