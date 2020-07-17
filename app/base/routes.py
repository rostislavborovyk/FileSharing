from flask import render_template

from app.base import bp


@bp.route("/")
def index():
    return render_template("main.html")


@bp.route("/get_file")
def get_file():
    return render_template("get_file.html")


@bp.route("/file_not_found")
def file_not_found():
    return render_template("errors/404.html")
