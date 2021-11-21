#Database model
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import mysql.connector

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.BLOB)
    data = db.Column(db.CLOB)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin) :
    id = db.Column(db.Integer, primary_key =True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    firstname = db.Column(db.String(100))
    notes = db.relationship('Note')

# mydb = mysql.connector.connect(
#     host="JanusHasie.mysql.pythonanywhere-services.com",
#     user="JanusHasie",
#     password="Janaster0405",
#     database="JanusHasie$Project2DB"
# )

