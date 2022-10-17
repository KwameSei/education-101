from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from os import path
#from flask_login import LoginManager

def create_app():
    app = Flask(__name__)   #Setting the app to an instance class of Flask
    app.config['SECRET_KEY'] = 'helloworld'
    
    from .routes import routes  #Importing routes relatively from the routes folder
    from .auth import auth
    #Configuring blueprint
    app.register_blueprint(routes, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app