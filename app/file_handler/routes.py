import os

from flask import request, send_file
from werkzeug.utils import secure_filename

from app.database.queries import add_file, get_file
from app.file_handler import bp
import pickle


@bp.route("/")
def index():
    return "Heloo"


# todo resolve situation when uploading picture with name present in collection
@bp.route("/upload", methods=["POST"])
def upload():
    file = request.files["media"]
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
        add_file(serialized, filename)
        return "File saved"
    return "Ok"


@bp.route("/download/<string:id_>", methods=["GET"])
def download(id_):
    file = get_file(id_)
    serialized = file.file
    data = pickle.loads(serialized)

    file_path = os.getcwd() + "/app/static/file_temp_storage/" + file.filename

    with open(file_path, "wb") as f:
        f.write(data)

    response = send_file(file_path, as_attachment=True)

    # removing file from temp storage
    os.remove(file_path)

    return response
