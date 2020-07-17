
from flask import Blueprint, request
from models.user import User
from flask_jwt_extended import create_access_token

user_routes = Blueprint("user_routes", __name__)


@user_routes.route('/', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        data['password'] = User.generate_hash(data['password'])
        user = User(data['username'], data['password'])

        user.save_to_db()

        return {'message': f"Usuario '{user.username}' registrado exitosamente"}, 201
    except Exception as e:
        print(e)
        return {'message': 'Fallo en el registro de usuario'}, 500


@user_routes.route('/login', methods=['POST'])
def authenticate_user():
    try:
        data = request.get_json()
        current_user = User.find_by_username(data['username'])
        if not current_user:
            return {'message': 'Usuario inválido', }, 404

        if User.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity=data['username'])
            return {'message': f'Login como {current_user.username}',
                    'user': {                                
                                'id': current_user.id,
                                'username': current_user.username,
                                'token': access_token}}, 201
        else:
            return {'message': 'Datos de acceso inválidos'}, 401
    except Exception as e:
        print(e)
        return {'message': 'Fallo en el proces de autenticación'}, 500
