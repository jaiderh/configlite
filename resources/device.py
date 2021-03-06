from flask import Blueprint
from flask import request
from flask import jsonify

from flask_jwt_extended import jwt_required

from models.device import Device
from models.socket import Socket
from models.client import Client

device_routes = Blueprint("device_routes", __name__)


@device_routes.route('/', methods=['GET'])
@jwt_required
def get_devices():
    return jsonify([x.json() for x in Device.find_all()]), 200


@device_routes.route('/<int:id>', methods=['GET'])
@jwt_required
def get_device(id):
    device = Device.find_by_id(id)
    if device:
        return device.json(), 200

    return {'message': f'No existe medidor con el ID [{id}] especificado'}, 404


@device_routes.route('/', methods=['POST'])
@jwt_required
def create_device():
    data = request.get_json()
    deviceid = data['deviceid']
    socketid = None

    if 'socketid' in data:
        socketid = data['socketid']

    if Device.find_by_deviceid(deviceid):
        return {'message': f"Existe un medidor con el identificador '{deviceid}'."}, 500

    device = Device(
                    deviceid,
                    data['brand'],
                    data['model'],
                    data['serial'],
                    socketid)
    try:
        device.save_to_db()
    except Exception:
        return {"message": "ocurrio un error en la creacion del medidor."}, 500

    return device.json(), 201


@device_routes.route('/<int:id>', methods=['PUT'])
@jwt_required
def update_device(id):
    data = request.get_json()
    device = Device.find_by_id(id)

    if not device:
        return {'message': f'No se encuentra el medidor con el ID [{id}] especificado'}, 404

    socketid = None

    if 'socketid' in data:
        socketid = data['socketid']

    device.brand = data['brand']
    device.model = data['model']
    device.serial = data['serial']
    device.socketid = socketid

    try:
        device.save_to_db()
    except Exception:
        return {"message": "ocurrio un error en la actualización del medidor."}, 500

    return device.json(), 201


@device_routes.route('/<int:id>', methods=['DELETE'])
@jwt_required
def delete_device(id):

    device = Device.find_by_id(id)

    if not device:
        return {'message': f'No se encuentra el medidor con el ID [{id}] especificado'}, 404

    device.delete_from_db()

    return {'message': 'Medidor borrado exitosamente.'}, 200
