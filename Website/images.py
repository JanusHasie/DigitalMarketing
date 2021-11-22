from datetime import datetime
from flask import Blueprint, render_template, request, flash, current_app, send_file, send_from_directory, safe_join, abort
import os
from flask_mysqldb import MySQL, MySQLdb
from sqlalchemy.sql.functions import now, user
from werkzeug.utils import secure_filename
from . import db
from flask_login import current_user
from .models import Img #mydb, mycursor,

images = Blueprint( 'images', __name__)

#PHOTO UPLOADS HERE
UPLOAD_DIRECTORY = 'Website/static/uploadImg/'
current_app.config['UPLOAD_DIRECTORY'] = UPLOAD_DIRECTORY
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename) :
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@images.route('/upload', methods = ['GET', 'POST'])
def upload() :
    now = datetime.now()
    #cur = mycursor
    if request.method == 'POST' :
        files = request.files.getlist('files[]')
        print(files)
        for file in files :
            if file and allowed_file(file.filename) :
                filename = secure_filename(file.filename)
                new_image = Img(image=file.filename, user_key=current_user.id, metadate=now)
                file.save(os.path.join(current_app.config['UPLOAD_DIRECTORY'], filename))
                db.session.add(new_image)
                db.session.commit()

        flash('Your file(s) have been successfully uploaded!', category='good')
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

# cur.execute("INSERT INTO img (image, alt, metadate) VALUES (%b, %s)", [filename, now])
                # mydb.commit()