from flask import Flask


def register_blueprints(app: Flask) -> None:
    from app.file_handler import bp as file_handler_bp
    app.register_blueprint(file_handler_bp)


def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    return app
