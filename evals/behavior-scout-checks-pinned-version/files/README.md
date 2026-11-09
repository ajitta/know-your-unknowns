# Bakery pre-orders

A small HTTP service the shop's website calls to take pre-orders for pickup. Customers
register once, then order items from the menu with a pickup time inside opening hours
(07:00-18:00).

## Run

    pip install -r requirements.txt
    flask --app app:create_app run

## Test

    python -m unittest

## Endpoints

| method | path | body checked |
|---|---|---|
| POST | /customers | yes |
| GET | /customers/<id> | - |
| PATCH | /customers/<id> | no, see PLAN.md |
| POST | /orders | yes |
| GET | /orders/<id> | - |
| POST | /orders/<id>/pickup-time | no, see PLAN.md |

Request bodies are checked with pydantic models in app/models.py. A bad body gets a 422
with the list of errors (app/errors.py).

Storage is in memory for now (app/store.py); a restart loses every order.
