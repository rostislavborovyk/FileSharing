import os

from flask import request
from werkzeug.utils import secure_filename

from app.file_handler import bp


@bp.route("/")
def index():
    return "Heloo"


@bp.route("/upload", methods=["POST"])
def upload():
    if request.method == "POST":
        file = request.files["media"]
        if file:
            filename = secure_filename(file.filename)
            file_path = os.getcwd() + "/app/static/files/" + filename
            file.save(file_path)
            return "File saved"
    return "Ok"


@bp.route("/test", methods=["GET"])
def test():
    return "Ok"
