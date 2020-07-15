from db import db

class Socket(db.Model):
    __tablename__ = 'sockets'
    
    id = db.Column(db.Integer, primary_key=True)
    socketid = db.Column(db.String(50))
    description = db.Column(db.String(100))

    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    client = db.relationship('Client')

    devices = db.relationship('Device', lazy='dynamic')
    

    def __init__(self, socketid, description, client_id):
        self.socketid = socketid
        self.description = description
        self.client_id = client_id
    

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
