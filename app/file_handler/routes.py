import os

from flask import request, send_file, redirect, url_for, jsonify
from werkzeug.utils import secure_filename

from app.database.queries import add_file, get_file
from app.file_handler import bp
import pickle
from time import time


@bp.route("/upload", methods=["POST"])
def upload():
    file = request.files["media"]

    # converting minutes to seconds and adding current timestamp
    expire_at = int(request.form["life_time"]) * 60 + time()

    if file:
        # saving file to temp storage
        filename = secure_filename(file.filename)
        file_path = os.getcwd() + "/app/static/file_temp_storage/" + filename
        file.save(file_path)

        # reading data for serialization
        with open(file_path, "rb") as f:
            data = f.read()

        # removing file from temp storage
        os.remove(file_path)

        # serializing data for db
        serialized = pickle.dumps(data)

        # add file blob to db
        id_ = add_file(serialized, filename, expire_at)
        return jsonify({"id": id_})
    return "Ok"


@bp.route("/download/<string:id_>", methods=["GET"])
def download(id_):
    # getting file from db
    file = get_file(id_)

    # getting deserialized data
    serialized = file.file
    data = pickle.loads(serialized)

    file_path = os.getcwd() + "/app/static/file_temp_storage/" + file.filename

    # saving file from db to temp storage
    with open(file_path, "wb") as f:
        f.write(data)

    # sending file to user
    response = send_file(file_path, as_attachment=True)

    # removing file from temp storage
    os.remove(file_path)
    return response


@bp.route("/download_redirect/<string:id_>", methods=["GET"])
def download_redirect(id_):
    return redirect(url_for("file_handler.download", id_=id_))
