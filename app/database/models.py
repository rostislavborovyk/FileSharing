from app import db


class File(db.Model):
    __tablename__ = "files"

    id = db.Column(db.String(32), primary_key=True)
    file = db.Column(db.LargeBinary(2**24 - 1))
    filename = db.Column(db.String(60))
    expire_at = db.Column(db.Integer)
