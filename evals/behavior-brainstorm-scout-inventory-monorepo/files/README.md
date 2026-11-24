# Platform monorepo

The services behind the meal-kit subscription: sign-up and checkout, the weekly box, the packing site, delivery, payments and customer care.

    services/<name>/   one service each: api.py (routes), service.py, models.py,
                       repository.py, schemas.py, client.py, config.yaml,
                       migrations/, tests/, RUNBOOK.md
    libs/              shared code: database, HTTP, events, scheduler, config, templating
    deploy/            the worker processes each deploy starts

Every service publishes `<record>.created` and `<record>.updated` on the event bus (`libs/events`); a service that reacts to another's events subscribes to them in its own handlers. Nightly jobs and delayed tasks live in a service's `jobs.py` and register with `libs/scheduler`. Each service's settings are in its `config.yaml`.

Python 3.11. `pip install -e .`, then `pytest`.
