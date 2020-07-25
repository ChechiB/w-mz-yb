from .model import User
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util
from werkzeug.security import generate_password_hash, check_password_hash
import json

def register(data):
    validate_register()
    hashed_password = generate_password_hash(data['password'], "sha1")
    print(hashed_password)
    user = User(name = data['name'], 
                lastname = data['lastname'],
                password = hashed_password)
    user.save()

def getAll():
    user_list = User.objects()
    json_user = user_list.to_json()
    dict_user = json.loads(json_user)

    return {'users' :dict_user}

def update(id):
    pass

def delete(id):
    pass

def validateLogin():
    pass

def login():
    pass

def validate_register():
    pass