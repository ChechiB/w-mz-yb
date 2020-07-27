
import jwt
import datetime

def create_token(id_user):
    from run import app
    token =jwt.encode({'id': id_user, 
        'exp':datetime.datetime.now().utcnow() + datetime.timedelta(minutes=120),
        },
        app.config['JWT_SECRET_KEY'])
    print('token: {token}'.format(token=token))
    return token

def invalidate_token():
    pass