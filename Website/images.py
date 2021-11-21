from datetime import datetime
from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
import os
from flask_mysqldb import MySQL, MySQLdb
from sqlalchemy.sql.functions import now, user
from werkzeug.utils import secure_filename
from . import db
from flask_login import current_user

images = Blueprint( 'images', __name__)

#DATABASE CONFIGURATIONS
current_app.config['MYSQL_HOST'] = 'JanusHasie.mysql.pythonanywhere-services.com'
current_app.config['MYSQL_USER'] = 'JanusHasie'
current_app.config['MYSQL_PASSWORD'] ='Janaster0405'
current_app.config['MYSQL_DB'] = 'JanusHasie$Project2DB'
current_app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(current_app)

#PHOTO UPLOADS HERE
UPLOAD_DIRECTORY = 'Website/static/uploadImg/'
current_app.config['UPLOAD_DIRECTORY'] = UPLOAD_DIRECTORY
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename) :
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@images.route('/upload', methods = ['GET', 'POST'])
def upload() :
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    now = datetime.now()
    
    if request.method == 'POST' :
        files = request.files.getlist('files[]')
        print(files)
        for file in files :
            if file and allowed_file(file.filename) :
                filename = secure_filename(file.filename)
                file.save(os.path.join(current_app.config['UPLOAD_DIRECTORY'], filename))
                cur.execute("INSERT INTO img (image, alt, metadate) VALUES (%b, 'alternative text here', %s)", [filename, now])

        flash('Your file(s) have been successfully uploaded!')
    return render_template('upload.html', user=current_user)
#END PHOTO UPLOAD
#===============================================================

#PHOTO VIEWING HERE
@images.route('/viewmine', methods = ['GET'])
def viewmine() :
    return render_template('viewmine.html', user=current_user)
    #END PHOTO VIEW
#===============================================================

#PHOTO VIEWING HERE
@images.route('/viewshare', methods = ['GET', 'POST'])
def viewshare() :
    return render_template("viewshare.html", user=current_user)
    #END PHOTO VIEWSHARE
#===============================================================