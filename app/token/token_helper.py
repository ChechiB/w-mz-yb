from functools import wraps
from flask import request, make_response, jsonify, Request
import jwt
import pprint

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'HTTP_AUTHORIZATION' in request.headers.environ.keys():
            token = get_token(request.headers.environ.get('HTTP_AUTHORIZATION')) 
        if not token:
             return make_response(jsonify({'status':403,'message': 'Missing token'}),403)
        try:
            from run import app
            data = jwt.decode(token, app.config['JWT_SECRET_KEY'])
        #Token exceptions
        except jwt.ExpiredSignatureError:
            return make_response(jsonify({'status':401,'message':'Session expired. Please log in again'}),401)
        except jwt.InvalidTokenError:
            return make_response(jsonify({'status':401,'message': 'Invalid token. Please log in again'}),401)

        return f(data,**kwargs)
    return decorated

PREFIX = 'Bearer'

def get_token(header):
  
    bearer, _, token = header.partition(' ')
    if bearer != PREFIX:
        raise ValueError('Invalid token')
    return token
