from flask import Flask, request, jsonify

from db import db
from resources.device import device_routes
from resources.client import client_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Admin_123@localhost:5432/configlite"

app.register_blueprint(device_routes, url_prefix='/api/devices')
app.register_blueprint(client_routes, url_prefix='/api/clients')

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()
