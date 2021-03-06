from flask import render_template, abort

from app.base import bp


@bp.route("/")
def index():
    return render_template("main.html")


@bp.route("/get_file")
def get_file():
    return render_template("get_file.html")


@bp.route("/check_file")
def check_file():
    return render_template("check_file.html")


@bp.route("/error/404")
def error_404():
    """
    This route redirects to 404 error page
    Made for situations when calling abort(404) from route doesnt redirect to 404 error page
    """
    return abort(404)
