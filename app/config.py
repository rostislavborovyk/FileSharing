import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FILE_EXPIRATION_CHECK_INTERVAL = 1440  # in minutes, 1440 minutes == 24 hours
