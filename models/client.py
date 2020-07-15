from db import db

class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100))
    city = db.Column(db.String(30))
    email = db.Column(db.String(254))    

    sockets = db.relationship('Socket', lazy='dynamic')


    def __init__(self, description, city, email):
        self.description = description
        self.city = city
        self.email = email


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        