from flask import Flask

from .customers import bp as customers_bp
from .errors import register_error_handlers
from .orders import bp as orders_bp
from .store import Store


def create_app(store=None):
    app = Flask(__name__)
    app.config["STORE"] = store or Store()
    app.register_blueprint(customers_bp)
    app.register_blueprint(orders_bp)
    register_error_handlers(app)
    return app
