from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

#Setting up database
db = SQLAlchemy()
DB_NAME = "database.db" #Definition for database name

def create_app():
    app = Flask(__name__)   #Setting the app to an instance class of Flask
    app.config['SECRET_KEY'] = 'helloworld'
    #Configuration of database inside create up function
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    db.init_app(app) #Initializing database with app
    
    from .views import views  #Importing routes relatively from the routes folder
    from .auth import auth 
    
    #Configuring blueprint
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User
    #Call create_database function
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

#Creating database
def create_database(app):
    if not path.exists('web_app/' + DB_NAME):   #Check if database exits, if not create it
        with app.app_context():
            db.create_all()
            print("Created database")