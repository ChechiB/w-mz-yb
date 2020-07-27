from flask import Blueprint, request, Response, jsonify, sessions, make_response
import json
from .service import login_user,register, getAll, hasPermission
from ..token.token_helper import token_required
from ..token.service import create_token
from .schemas import validator, validator_reg

user_blueprint = Blueprint('user_blueprint',__name__)


@user_blueprint.route('/user', methods = ['GET'])
@token_required
def get_users(data):
    #hasPermission() Search by email
    try:
        print(data)
        hasPermission(data['id'])
        result = getAll()
        return make_response({'status': 200, 'message': result}), 200
    except Exception as ex:
        json_msg = json.loads(ex.args[0])
        return make_response(json_msg), json_msg['status']

@user_blueprint.route('/user', methods = ['POST'])
#@token_required
def create_user():
    try:
        #Receiving data
        user_dict = request.get_json()
        #Validate Json
        if validator_reg.validate(user_dict):
            id_user = register(user_dict)
            token = create_token(id_user)
            return make_response({'status':200,'token':token.decode('UTF-8')}),200
        else:
            schema_errors = validator_reg.errors
            return make_response({'status':400,'message':"Invalid JSON:{e}".format(e = schema_errors)}),400
    except Exception as ex:
        json_msg = json.loads(ex.args[0])
        return make_response(json_msg), json_msg['status']

@user_blueprint.route('/user', methods = ['PUT'])
def update_user():
    return 'OK'

@user_blueprint.route('/user', methods = ['DELETE'])
def delete_user():
    return 'OK'

@user_blueprint.route('/auth/login', methods = ['POST'])
def login():
    try:
        user_dict = request.get_json()
        v = validator.validate(user_dict)
        if v:
            id_user = login_user(user_dict)
            token = create_token(id_user)
            return make_response({'status':200, 'token':token.decode('UTF-8')}),200
        else:
            schema_errors = validator.errors
            return make_response({'status':400,'message':"Invalid JSON:{e}".format(e = schema_errors)}),400
    except Exception as ex:
        json_msg = json.loads(ex.args[0])
        return make_response(json_msg), json_msg['status']

@user_blueprint.route('/auth/logout', methods = ['POST'])
def logout():
    #invalidate token
    pass

@user_blueprint.errorhandler(500)
def server_error():
    return make_response(jsonify({'error': 'Internal Server Error'}), 500)

@user_blueprint.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 400)
