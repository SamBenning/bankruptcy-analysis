from os import environ, path

basedir = path.abspath(path.dirname(__file__))
class Config:

    TESTING = True
    DEBUG = True
    FLASK_ENV = 'development'
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    #general config
    SECRET_KEY = 'pollywag'
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')

    #database
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') or \
    'sqlite:///' + path.join(basedir, 'app.db')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False