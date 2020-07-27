import mongoengine as me

class Token(me.Document):
    valid = me.BooleanField(required=True, default=True)
    user = me.StringField(required=True, max_length=256)

    #Metadata
    meta = {'collection': 'token'}
