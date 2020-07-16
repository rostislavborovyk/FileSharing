from flask import Flask


def register_blueprints(flask_app: Flask) -> None:
    from app.file_handler import bp as file_handler_bp
    flask_app.register_blueprint(file_handler_bp)

    from app.base import bp as base_bp
    flask_app.register_blueprint(base_bp)


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app
