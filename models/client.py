from db import db
from datetime import datetime
from sqlalchemy import DateTime


class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    idclient = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100))
    city = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(254), nullable=False)
    created_on = db.Column(DateTime(), default=datetime.now)
    updated_on = db.Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    sockets = db.relationship('Socket', lazy='dynamic')

    def __init__(self, idclient, description, city, email):
        self.idclient = idclient
        self.description = description
        self.city = city
        self.email = email

    def json(self):
        return {
            'id': self.id,
            'idclient': self.idclient,
            'description': self.description,
            'city': self.city,
            'email': self.email
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_idclient(cls, idclient):
        return cls.query.filter_by(idclient=idclient).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
