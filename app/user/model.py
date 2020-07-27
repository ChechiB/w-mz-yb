#from app.extension import mongo as me
import mongoengine as me
from datetime import datetime

#Schema by mongoengine
class User(me.Document):
    name = me.StringField(required=True, max_length=100)
    lastname = me.StringField(required=True, max_length=100)
    password = me.StringField(required=True, min_length=8, max_length=256)
    email = me.EmailField(required=True, unique=True, max_length=256)
    is_admin = me.BooleanField(required=True, default=True)
    date_created = me.DateTimeField(default=datetime.utcnow) 

    #Metadata
    meta = {'collection': 'user'}


