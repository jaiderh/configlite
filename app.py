from flask import Flask

from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required

from db import db

from resources.device import device_routes
from resources.client import client_routes
from resources.socket import socket_routes
from resources.user import user_routes

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Admin_123@localhost:5432/configlite"
app.config['JWT_SECRET_KEY'] = "CONFIG_LITE_SECRET_20200717"

CORS(device_routes)
CORS(client_routes)
CORS(socket_routes)
CORS(user_routes)

app.register_blueprint(device_routes, url_prefix='/api/devices')
app.register_blueprint(client_routes, url_prefix='/api/clients')
app.register_blueprint(socket_routes, url_prefix='/api/sockets')
app.register_blueprint(user_routes, url_prefix='/api/users')

jwt = JWTManager(app)

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()
