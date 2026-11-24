"""The scheduler worker process (deploy/processes.yaml). It imports every service's jobs
module, so that the module's nightly jobs and delayed tasks register, then runs what is
due every 30 seconds."""
import importlib
import pkgutil
import time
from datetime import datetime, timezone

import services
from libs.scheduler import run_due


def load_jobs():
    for module in pkgutil.iter_modules(services.__path__):
        try:
            importlib.import_module("services.%s.jobs" % module.name)
        except ModuleNotFoundError:
            continue


def main():
    load_jobs()
    last_run = datetime.now(timezone.utc)
    while True:
        time.sleep(30)
        now = datetime.now(timezone.utc)
        run_due(now, last_run)
        last_run = now


if __name__ == "__main__":
    main()
