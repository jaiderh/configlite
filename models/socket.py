from db import db
from datetime import datetime
from sqlalchemy import DateTime


class Socket(db.Model):
    __tablename__ = 'sockets'

    id = db.Column(db.Integer, primary_key=True)
    socketid = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    created_on = db.Column(DateTime(), default=datetime.now)
    updated_on = db.Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    client = db.relationship('Client')

    devices = db.relationship('Device', lazy='dynamic')

    def __init__(self, socketid, description, client_id):
        self.socketid = socketid
        self.description = description
        self.client_id = client_id

    def json(self):
        return {
            'id': self.id,
            'socketid': self.socketid,
            'description': self.description,
            'client_id': self.client_id,
            'devices': [device.json() for device in self.devices.all()],
            'created_on': self.created_on,
            'updated_on': self.updated_on
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_socketid(cls, socketid):
        return cls.query.filter_by(socketid=socketid).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
