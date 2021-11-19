#Database model
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.BLOB)
    data = db.Column(db.CLOB)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin) :
    id = db.Column(db.Integer, primary_key =True)
    email = db.Column(db.String(100), unique=True)
    password = db.Columnn(db.String(100))
    firstName = db.Column(db.String(100))
    notes = db.relationship('Note')