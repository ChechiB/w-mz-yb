import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    PROJECT_NAME =os.environ.get('PROJECT_NAME')
    CURRENT_DIR =os.path.dirname(os.path.abspath(__file__))
    DB_SERVICE = os.environ.get('DB_SERVICE')

    SESSION_COOKIE_SECURE = True


#Config to running in production
class ProductionConfig(Config):
    pass


#Config use for development
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    DB_NAME = os.environ.get('DB_NAME_DEV')
    DB_HOST = os.environ.get('DB_HOST_DEV')
    DB_PORT = os.environ.get('DB_PORT_DEV')
    #DB_USER = os.environ.get('DB_USER_DEV')
    #DB_PASSWORD = os.environ.get('DB_PASSWORD_DEV')
    DB_SERVICE = os.environ.get('DB_SERVICE_DEV')

    """ DB_URI = '{service}://{user}:{password}@{host}/{db}'.format(
        service = DB_SERVICE,
        user = DB_USER,
        password = DB_PASSWORD,
        host= DB_HOST,
        db= DB_NAME 
    ) """
    DB_URI = '{service}://{host}/{db}'.format(service = DB_SERVICE, host = DB_HOST, db = DB_NAME)

    SESSION_COOKIE_SECURE = False

#Config use for testing
class TestingConfig(Config):
    TESTING = True
    SESSION_COOKIE_SECURE = False