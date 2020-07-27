from .model import User
from bson import json_util
from werkzeug.security import generate_password_hash, check_password_hash
import json
from mongoengine import ValidationError, NotUniqueError, DoesNotExist
from ..public.error_handler import new_error

def register(data):
    try:
        hashed_password = generate_password_hash(data['password'], "sha1")
        user = User(name = data['name'], 
                    lastname = data['lastname'],
                    password = hashed_password,
                    email = data['email']).save()
        return str(user._object_key.get('pk'))
    #Email existente excepcion
    except NotUniqueError as er:
        raise new_error(type(er).__name__, str(er), User._fields)

def getAll():
    try:
        user_list = User.objects()
        json_user = user_list.to_json()
        dict_user = json.loads(json_user)
        return dict_user
    except Exception as ex:
        raise ex

def update(id):
    pass

def delete(id):
    pass

def login_user(data):

    user = User.objects(email = data['email']).first() 
    if user == None:
        raise  Exception('{"status": 400, "message": "User not found"}')
    if (check_password_hash(data['password'], user.password)):
        raise Exception('{"status": 400, "message": "Wrong password"}')
    return str(user._object_key.get('pk'))

def hasPermission(user_id):
    user = User.objects(id = user_id).first() 
    if user == None:
        raise Exception('{"status": 400, "message": "User not found"}')
    if user.is_admin == False :
        raise Exception('{"status": 403, "message": "Invalid credentials"}')
    return True