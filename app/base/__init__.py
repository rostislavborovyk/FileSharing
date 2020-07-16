from flask import Blueprint

bp = Blueprint(
    'base',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static'
)

from app.base import routes
