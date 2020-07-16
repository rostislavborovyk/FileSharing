from app import db


class File(db.Model):
    __tablename__ = "files"

    id = db.Column(db.String(32), primary_key=True)
    file = db.Column(db.BLOB)
    filename = db.Column(db.String(60))
