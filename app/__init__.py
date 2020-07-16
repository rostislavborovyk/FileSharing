from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import pymysql
from dotenv import load_dotenv

from app.config import BaseConfig

pymysql.install_as_MySQLdb()
load_dotenv()


def register_blueprints(flask_app: Flask) -> None:
    from app.file_handler import bp as file_handler_bp
    flask_app.register_blueprint(file_handler_bp)

    from app.base import bp as base_bp
    flask_app.register_blueprint(base_bp)


app = Flask(__name__)
app.config.from_object(BaseConfig)

db = SQLAlchemy(app)
register_blueprints(app)
migrate = Migrate(app, db)

from app.database import models
