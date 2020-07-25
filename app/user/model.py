from app.extension import mongo as me
from datetime import datetime

#Schema by mongoengine
class User(me.Document):
    name = me.StringField(required=True, max_length=100)
    lastname = me.StringField(required=True, max_length=100)
    password = me.StringField(required=True, min_length=8, max_length=54)

    """ email = me.EmailField(required=True, unique=True, max_length=100)
    username = me.StringField(required=True, unique=True, max_length=50)
    password = me.StringField(required=True, min_length=8, max_length=16)
    is_admin = me.BooleanField(default=False)
    date_created = me.DateTimeField(default=datetime.utcnow) """

    #Metadata
    meta = {'collection': 'user'}

    """ def __init__(self,name,lastname,email,username,userpwd,is_admin,date_created):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.username = username
        self.userpwd = userpwd
        self.is_admin = is_admin
        self.date_created = date_created """
