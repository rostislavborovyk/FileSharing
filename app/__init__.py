"""
This file inits app instance of Flask
For simplicity and unnecessity to have different instances of app (due to absence of tests)
app instance created directly without create_app() function
"""

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

# importing bg_jobs at this point to avoid circular import error
from app.bg_jobs import init_bg_tasks

init_bg_tasks()

# importing models to allow alembic migrations
from app.database import models

from app.errors import *
