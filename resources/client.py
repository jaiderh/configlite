from flask import Blueprint
from flask import request

from models.device import Device
from models.socket import Socket
from models.client import Client


client_routes = Blueprint("client_routes", __name__)


@client_routes.route('/', methods=['GET'])
def get_clients():
    return {'clients': [x.json() for x in Client.find_all()]}, 200


@client_routes.route('/<int:id>', methods=['GET'])
def get_client(id):
    client = Client.find_by_id(id)
    if client:
        return client.json(), 200

    return {'message': f'No existe cliente con el ID [{id}] especificado'}, 404


@client_routes.route('/', methods=['POST'])
def create_client():
    data = request.get_json()
    idclient = data['idclient']

    if Client.find_by_idclient(idclient):
        return {'message': f"Existe un cliente con el identificador '{idclient}'."}, 500

    client = Client(
                    idclient,
                    data['description'],
                    data['city'],
                    data['email'])
    try:
        client.save_to_db()
    except Exception:
        return {"message": "ocurrio un error en la creacion del cliente."}, 500

    return client.json(), 201


@client_routes.route('/<int:id>', methods=['PUT'])
def update_client(id):
    data = request.get_json()
    client = Client.find_by_id(id)

    if not client:
        return {'message': f'No se encuentra el client con el ID [{id}] especificado'}, 404

    client.description = data['description']
    client.city = data['city']
    client.email = data['email']

    try:
        client.save_to_db()
    except Exception:
        return {"message": "ocurrio un error en la actualización del medidor."}, 500

    return client.json(), 201


@client_routes.route('/<int:id>', methods=['DELETE'])
def delete_client(id):

    client = Client.find_by_id(id)

    if not client:
        return {'message': f'No se encuentra el client con el ID [{id}] especificado'}, 404

    client.delete_from_db()

    return {'message': 'Cliente borrado.'}, 200
