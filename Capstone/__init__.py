from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "sam"

from flask import Flask
from .views import views


def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    with app.app_context():
        from . import views

        app.register_blueprint(views, url_prefix='/')

        return app

