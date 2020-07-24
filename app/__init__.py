import os

from flask import Flask
from .extension import mongo

def create_app(test_config=None):
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

    mongo.init_app(app)

    print(f'ENV is set to: {app.config["ENV"]}')

    #Resgister Blueprints
    from .user.routes import user_blueprint 
    app.register_blueprint(user_blueprint)

    return app