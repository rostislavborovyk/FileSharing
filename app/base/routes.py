from flask import render_template

from app.base import bp


@bp.route("/")
def index():
    return render_template("main.html")
