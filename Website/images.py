from datetime import datetime
from flask import Blueprint, render_template, request, flash, current_app, jsonify
import os
import json
from werkzeug.utils import secure_filename, send_file
from . import db
from flask_login import current_user
from .models import Img

images = Blueprint( 'images', __name__)

#PHOTO UPLOADS HERE
UPLOAD_DIRECTORY = 'Website/static/uploadImg/'
current_app.config['UPLOAD_DIRECTORY'] = UPLOAD_DIRECTORY
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
now = datetime.now()

def allowed_file(filename) :
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@images.route('/upload', methods = ['GET', 'POST'])
def upload() :  
    #cur = mycursor
    if request.method == 'POST' :
        files = request.files.getlist('files[]')
        for file in files :
            if file and allowed_file(file.filename) :
                filename = secure_filename(file.filename)
                print(filename)
                mimetype = file.mimetype
                new_image = Img(user_key=current_user.id, image=file.read(), name=filename, metadate=now)
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
    files = request.files.getlist('files[]')
    for file in files :
        if file and allowed_file(file.filename) :
            filename = secure_filename(file.filename)
            new_image = Img(user_key=current_user.id, image=file.read(), name=filename, metadate=now)
    
    List = os.listdir('Website/static/uploadImg/')
    List = ['pics/' + images for images in List]
    return render_template("viewmine.html", user=current_user, List = List, image=files) 

    
@images.route('/delete-img', methods=['POST'])
def deleteimg():
    print("hello world")
    #post = Post.query.get_or_404(item_id)
    images = json.loads(request.data)
    imgId = images['imgId']
    images = Img.query.get(imgId)
    os.unlink(os.path.join(current_app.root_path, 'static/uploadImg/' + images))
    os.remove(os.path.join(current_app.config['UPLOAD_DIRECTORY'], images))
    if images:
        if images.user_id == current_user.id:
            db.session.delete(images)
            #db.session.query(imageId).filter_by(item_id=imageId).delete()
            db.session.commit()
    return jsonify({})
    #END PHOTO VIEW
#===============================================================

#DOWNLOAD HERE
@images.route('/download')
def download_file(dfile) :
    return send_file(dfile, as_attachment="True")
#END PHOTO VIEW
#===============================================================

#PHOTO SHARING HERE
@images.route('/viewshare', methods = ['GET', 'POST'])
def viewshare() :
    return render_template("viewshare.html", user=current_user)
    #END PHOTO VIEWSHARE
#===============================================================