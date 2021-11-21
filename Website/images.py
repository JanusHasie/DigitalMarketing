from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from flask_uploads import UploadSet, configure_uploads, IMAGES
from . import db
from flask_login import login_user, login_required, logout_user, current_user

images = Blueprint('images', __name__)
#mycursor = mydb.cursor()

#PHOTO UPLOADS HERE
photos = UploadSet('photos', IMAGES)
images.config['UPLOADED_PHOTOS_DEST'] = 'static/uploadImg'
configure_uploads(images, photos)
@images.route('/upload', methods = ['GET', 'POST'])
def upload() :
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        return filename
    #     img = "INSERT INTO img (image, alt) VALUES (%b, %s)"
    #     val = ()
    return render_template("upload.html", user=current_user)
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