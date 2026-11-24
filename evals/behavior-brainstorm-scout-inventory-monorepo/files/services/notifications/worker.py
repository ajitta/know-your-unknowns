"""The notifications worker process (deploy/processes.yaml): subscribes the handlers in
handlers.py to their events, then delivers events to them."""
from libs.events.bus import listen
from services.notifications import handlers


def main():
    handlers.register()
    listen()


if __name__ == "__main__":
    main()
