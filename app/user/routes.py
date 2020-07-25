from flask import Blueprint, request, Response, jsonify
import json
from .service import validateLogin,register, getAll

user_blueprint = Blueprint('user_blueprint',__name__)

@user_blueprint.route('/users', methods = ['GET'])
def get_users():
    return getAll()

@user_blueprint.route('/users', methods = ['POST'])
def create_user():
    #Receiving data
    user_dict = request.get_json()
    #print(data)
    #Validate Json
    register(user_dict)
    return 'ok'

@user_blueprint.route('/users', methods = ['PUT'])
def update_user():
    return 'OK'

@user_blueprint.route('/users', methods = ['DELETE'])
def delete_user():
    return 'OK'


