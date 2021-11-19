#Authorisation, security
from flask import Blueprint, render_template, request, flash, redirect, url_for


auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login() :
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout() :
    return render_template("login.html")

@auth.route('/sign_up', methods = ['GET', 'POST'])
def sign_up() :
    if request.method == 'POST' :
        email = request.form.get('email')
        firstname = request.form.get('firstName')
        password1 = request.form.get('password')
        password2 = request.form.get('cpassword')

        if len(email) < 4:
            flash('Email longer', category='issue')
        elif len(firstname) < 2:
            flash('Email much longer', category='issue')
        else :
            flash('This is okay', category='good')

    return render_template("sign_up.html")