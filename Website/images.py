from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

images = Blueprint('images', __name__)

@images.route('/upload', methods = ['GET'])
def upload() :
    return render_template("upload.html", user=current_user)

@images.route('/viewmine', methods = ['GET'])
def viewmine() :
    return render_template('viewmine.html', user=current_user)

@images.route('/viewshare', methods = ['GET', 'POST'])
def viewshare() :
    return render_template("viewshare.html", user=current_user)