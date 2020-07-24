from app.extension import mongo as me
from datetime import datetime

class User(me.Document):
    name = me.StringField(required=True, max_length=100)
    lastname = me.StringField(required=True, max_length=100)
    email = me.EmailField(required=True, unique=True, max_length=100)
    username = me.StringField(required=True, unique=True, max_length=50)
    userpwd = me.StringField(required=True, min_length=8, max_length=16)
    is_admin = me.BooleanField(default=False)
    date_created = me.DateTimeField(default=datetime.utcnow)



