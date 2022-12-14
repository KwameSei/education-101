import email
from email.policy import default
from enum import unique
from time import timezone
from web_app import db
from flask_login import UserMixin
from sqlalchemy.sql import func

#Creating user database table
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())