from flask import Blueprint

bp = Blueprint(
    'file_handler',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static'
)

from app.file_handler import routes
