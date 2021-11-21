from flask import Blueprint, render_template, request, flash, jsonify, redirect
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
import os

views = Blueprint('views', __name__)

#NOTES
@views.route('/', methods=['GET', 'POST'])
@login_required
def home() :
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

#IMAGES UPLOAD
@views.route("/upload-image", methods=["GET", "POST"])
def upload_image() :
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            image.save(os.path.join())
            return redirect(request.url)
    return render_template("home.html", user=current_user)

#IMAGES VIEW



