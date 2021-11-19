#Initialise
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_OBJ = "database.db"

def create_app() :
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1234'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_OBJ}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    create_database(app)
    
    return app

def create_database(app) :
    if not path.exists('website/' + DB_OBJ) :
        db.create_all(app=app)
        print('Database CREATED!')