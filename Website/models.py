#Database model
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import mysql.connector
import MySQLdb
import sshtunnel

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

# sshtunnel.SSH_TIMEOUT = 5.0
# sshtunnel.TUNNEL_TIMEOUT = 5.0

# with sshtunnel.SSHTunnelForwarder(
#     ('JanusHasie.mysql.pythonanywhere-services.com'),
#     ssh_username='JanusHasie', ssh_password='Janaster0405',
#     remote_bind_address=('JanusHasie.mysql.pythonanywhere-services.com', 3306)
# ) as tunnel:
#     connection = MySQLdb.connect(
#         user='JanusHasie',
#         passwd='Janaster0405',
#         host='127.0.0.1', port=tunnel.local_bind_port,
#         db='JanusHasie$Project2DB',
#     )
#     # Do stuff
#     connection.close()

