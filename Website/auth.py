#Authorisation, security
from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from .models import User #, mydb, mycursor
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from flask_mysqldb import MySQL, MySQLdb

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login() :
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in! Welcome!', category= 'good')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password... Please try again', category='issue')
        else:
            flash('Could not find email...', category='issue')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout() :
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign_up', methods = ['GET', 'POST'])
def sign_up() :
    if request.method == "POST" :
        email = request.form.get('email')
        firstname = request.form.get('firstName')
        password1 = request.form.get('password')
        password2 = request.form.get('cpassword')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already signed up', category='issue')
        elif len(email) < 6:
            flash('Email too short. Please try again', category='issue')
        elif len(firstname) < 2:
            flash('First name should be 2 characters or more', category='issue')
        elif password1!=password2 :
            flash('Passwords are not the same, please retry.', category='issue')
        elif len(password1)<6 :
            flash('Your password is less than 6 characters. Might cause weak security.', category='warning')
            # curr.execute("INSERT INTO auth (email, password, firstname) VALUES (%s, %s, %s)", [email, password1, firstname])
            # mydb.commit()
            new_user = User(email=email, firstname=firstname, password=generate_password_hash(password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('views.home'))
        else :
            # curr.execute("INSERT INTO auth (email, password, firstname) VALUES (%s, %s, %s)", [email, password1, firstname])
            # mydb.commit()
            new_user = User(email=email, firstname=firstname, password=generate_password_hash(password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            # curr.close()
            flash('Created Account!', category='good')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)

#"""mysql = MySQL(current_app) curr = mycursor"""