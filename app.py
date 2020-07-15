from flask import Flask, request, jsonify

from db import db
from models.device import Device
from models.client import Client
from models.socket import Socket

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Admin_123@localhost:5432/configlite"

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/devices', methods=['GET'])
def get_devices():
    return {'devices': [x.json() for x in Device.find_all()]}, 200


@app.route('/devices/<int:id>', methods=['GET'])
def get_device(id):
    device = Device.find_by_id(id)
    if device:
        return device.json()
    return {'message': 'No existe medidor con el ID [{}] especificado'.format(id)}, 404


@app.route('/devices', methods=['POST'])
def create_device():
    data = request.get_json()
    deviceid = data['deviceid']
    socketid = None

    if 'socketid' in data:
        socketid = data['socketid']

    if Device.find_by_deviceid (deviceid):
        return {'message': "Existe un medidor '{}' con el mismo identificador.".format(deviceid)}, 400

    device = Device(
                    deviceid, 
                    data['brand'], 
                    data['model'], 
                    data['serial'], 
                    socketid
                    )
    try:
        device.save_to_db()
    except:
        return {"message": "ocurrio un error en la creacion del medidor."}, 500

    return device.json(), 201


@app.route('/devices/<int:id>', methods=['PUT'])
def update_device(id):    
    data = request.get_json()
    device = Device.find_by_id(id)

    if not device:
        return {'message': 'No se encuentra el medidor con el ID [{}] especificado'.format(id)}, 404
    
    socketid = None

    if 'socketid' in data:
        socketid = data['socketid']
        
    device.brand = data['brand']
    device.model = data['model']
    device.serial = data['serial']
    device.socketid = data['socketid']

    try:
        device.save_to_db()
    except:
        return {"message": "ocurrio un error en la actualización del medidor."}, 500

    return device.json(), 201
    

@app.route('/devices/<int:id>', methods=['DELETE'])
def delete_device(id):

    device = Device.find_by_id(id)
    
    if not device:
        return {'message': 'No se encuentra el medidor con el ID [{}] especificado'.format(id)}, 404
    
    device.delete_from_db()

    return {'message': 'Medidor borrado.'}, 200


if __name__ == '__main__':
    app.run()

