from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

db = SQLAlchemy()

def create_app(config_obj=None):

    app = Flask(__name__, instance_relative_config=False)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/mydb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = "12345"
    db.init_app(app)
    
    from core.routes import main
    from core.models import Users
    

    # register the blueprints
    app.register_blueprint(main)

    with app.app_context():
        from . import routes
        db.create_all()

        return app

