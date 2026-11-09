from flask import jsonify
from pydantic import ValidationError


def register_error_handlers(app):
    @app.errorhandler(ValidationError)
    def invalid_body(error):
        return jsonify({"errors": error.errors()}), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "not found"}), 404
