from uuid import uuid4

from sqlalchemy import and_
from werkzeug.exceptions import abort

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
    File.query.filter(File.expire_at < time()).delete(synchronize_session=False)
    db.session.commit()


def check_expired_file(id_) -> bool:
    is_deleted = bool(File.query.filter(and_(File.id == id_, File.expire_at < time())).delete(synchronize_session=False))
    db.session.commit()
    return is_deleted
