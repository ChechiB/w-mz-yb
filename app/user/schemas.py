from cerberus import Validator

login_schema = {'password': {'type': 'string',"minlength":8,"maxlength": 255,"required":True},
        'email':{
            "type": "string",
            "minlength": 8,
            "maxlength": 255,
            "required": True,
            "regex": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"
        }}

validator = Validator(login_schema)

register_schema = {"name": {'type': 'string',"minlength":1,"maxlength": 100,"required":True},
        "lastname": {'type': 'string',"minlength":1,"maxlength": 100,"required":True},
        "password": {'type': 'string',"minlength":8,"maxlength": 255,"required":True},
        "email": {
            "type": "string",
            "minlength": 8,
            "maxlength": 255,
            "required": True,
            "regex": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"
        }}

validator_reg = Validator(register_schema)


