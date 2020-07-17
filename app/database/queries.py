from uuid import uuid4
from app import db
from app.database.models import File
from time import time


def add_file(file, filename, expire_at) -> str:
    id_ = uuid4().hex
    file = File(id=id_, file=file, filename=filename, expire_at=expire_at)
    db.session.add(file)
    db.session.commit()
    return id_


def get_file(id_) -> File:
    file = File.query.filter_by(id=id_).first_or_404()
    return file


def delete_expired_files() -> None:
    current_timestamp = time()
    File.query.filter(File.expire_at < current_timestamp).delete(synchronize_session=False)
    db.session.commit()
