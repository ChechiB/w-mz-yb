import os

from flask import Flask
from mongoengine import connect

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if app.config["ENV"] == "production":
        app.config.from_object("config.DevelopmentConfig")
    else:
        app.config.from_object("config.DevelopmentConfig")

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    with app.app_context():
        #mongo.init_app(app)
        connect(app.config['DB_NAME'],host = app.config['MONGO_URI'])

    print(f'ENV is set to: {app.config["ENV"]}')

    #Register Blueprints
    from .user.routes import user_blueprint 
    app.register_blueprint(user_blueprint)

    #JWT
    from flask_jwt_extended import JWTManager
    JWTManager(app)

    return app