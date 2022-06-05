from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()



def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    db.init_app(app)


    with app.app_context():
        from .views import views
        from .auth import auth
        from .models import User

        app.register_blueprint(views, url_prefix='/')
        app.register_blueprint(auth, url_prefix='/')
      

        
        login_manager.login_view = 'auth.login'
        login_manager.init_app(app)
        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))

        from .plotlydash.dashboard import create_dashboard
        app = create_dashboard(app)
        db.create_all()

        if app.config['FLASK_ENV'] == 'development':
            compile_assets(app)

        return app

