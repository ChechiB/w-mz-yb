from flask import Blueprint
from flask_restx import Resource

user_blueprint = Blueprint('user_blueprint',__name__)

@user_blueprint.route('/users', methods = ['GET'])
def get_users():
    return {'msg': 'recibido'}

@user_blueprint.route('/users', methods = ['POST'])
def create_user():

    return 'Ok'

@user_blueprint.route('/users', methods = ['PUT'])
def update_user():
    return 'OK'

@user_blueprint.route('/users', methods = ['DELETE'])
def delete_user():
    return 'OK'


