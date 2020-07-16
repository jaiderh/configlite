from db import db
from datetime import datetime
from sqlalchemy import DateTime


class Device(db.Model):
    __tablename__ = 'devices'

    id = db.Column(db.Integer, primary_key=True)
    deviceid = db.Column(db.String(50), nullable=False)
    brand = db.Column(db.String(30), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    serial = db.Column(db.String(30), nullable=False)
    socket_id = db.Column(db.Integer, db.ForeignKey('sockets.id'))
    created_on = db.Column(DateTime(), default=datetime.now)
    updated_on = db.Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    socket = db.relationship('Socket')

    def __init__(self, deviceid, brand, model, serial, socket_id):
        self.deviceid = deviceid
        self.brand = brand
        self.model = model
        self.serial = serial
        self.socket_id = socket_id

    def json(self):
        return {
            'id': self.id,
            'deviceid': self.deviceid,
            'brand': self.brand,
            'model': self.model,
            'serial': self.serial,
            'socket_id': self.socket_id
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_deviceid(cls, deviceid):
        return cls.query.filter_by(deviceid=deviceid).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
