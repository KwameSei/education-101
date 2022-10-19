from distutils.log import error
from flask import Blueprint, render_template, redirect, url_for, request, flash
from web_app import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):    #Check if password provided tallies password in the database
                flash("Successfully logged in", category='success')
                login_user(user, remember=True) #Log in the user
                return redirect(url_for('views.home'))
            else:
                flash('Invalid password', category='error')
        else:
            flash('Email does not exist!', category='error')

    return render_template('login.html', user=current_user)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    #Logic for creating a new account
    if request.method == 'POST':
        #Getting the data sent from the form (use request)
        username = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #Checking for the existence with above credentials exists
        email_exists = User.query.filter_by(email=email).first()
    # username_exists = User.query.filter_by(username=username).first()

        if email_exists:
            flash('Email is already exists in our database', category='error')
        #elif username_exists:
            #flash('Username already in use.', category='error')
        elif password1 != password2:
            flash("Passwords don't match", category=error)
        elif len(username) < 2:
            flash('Username is too short', category=error)
        elif len(email) < 5:
            flash('Invalid email', category=error)
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password1, method='sha256'))
            #Adding created user to the database
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)    #Login user after account creation
            flash('User successfully created!', category='success')
            return redirect(url_for('views.home'))
    
    return render_template('register.html', user=current_user)

@auth.route('/logout')
@login_required #Able to access the logout only when user is logged
def logout():
    logout_user()
    return redirect(url_for('views.home'))