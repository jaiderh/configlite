from flask import Blueprint
from flask import request
from flask import jsonify

from flask_jwt_extended import jwt_required

from models.device import Device
from models.socket import Socket
from models.client import Client

socket_routes = Blueprint("socket_routes", __name__)


@socket_routes.route('/', methods=['GET'])
@jwt_required
def get_sockets():
    return jsonify([x.json() for x in Socket.find_all()]), 200


@socket_routes.route('/<int:id>', methods=['GET'])
@jwt_required
def get_socket(id):
    socket = Socket.find_by_id(id)
    if socket:
        return socket.json(), 200

    return {'message': f'No existe socket con el ID [{id}] especificado'}, 404


@socket_routes.route('/', methods=['POST'])
@jwt_required
def create_socket():
    data = request.get_json()
    socketid = data['socketid']
    client_id = None

    if 'client_id' in data:
        client_id = data['client_id']

    if Socket.find_by_socketid(socketid):
        return {'message': f"Existe un socket con el identificador '{socketid}'."}, 500

    socket = Socket(
                    socketid,
                    data['description'],
                    client_id)
    try:
        socket.save_to_db()
    except Exception:
        return {"message": "ocurrio un error en la creacion del socket."}, 500

    return socket.json(), 201


@socket_routes.route('/<int:id>', methods=['PUT'])
@jwt_required
def update_socket(id):
    data = request.get_json()
    socket = Socket.find_by_id(id)

    if not socket:
        return {'message': f'No se encuentra el socket con el ID [{id}] especificado'}, 404

    client_id = None

    if 'client_id' in data:
        client_id = data['client_id']

    socket.description = data['description']
    socket.client_id = client_id

    try:
        socket.save_to_db()
    except Exception:
        return {"message": "ocurrio un error en la actualización del socket."}, 500

    return socket.json(), 201


@socket_routes.route('/<int:id>', methods=['DELETE'])
@jwt_required
def delete_socket(id):

    socket = Socket.find_by_id(id)

    if not socket:
        return {'message': f'No se encuentra el socket con el ID [{id}] especificado'}, 404

    socket.delete_from_db()

    return {'message': 'Socket borrado exitosamente.'}, 200
