from flask import render_template, request, redirect, url_for
from . import bp as app
from app.blueprints.main.models import User
from app import db

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Handle login form requests
        user = User.query.filter_by(email=request.form['inputEmail']).first()

        if user is None:
            return f'User with email { request.form["inputEmail"] } does not exist.'
        elif not user.check_my_password(request.form['inputPassword']):
            return 'Password is incorrect'
        else:
            print("User logged in")
            return redirect(url_for('main.home'))
    else:
        return render_template('login.html')

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Query the database for a user with the passed in email
        check_user = User.query.filter_by(email=request.form['inputEmail']).first()

        # If they already exist, show error. Otherwise, create user
        if check_user is not None:
            return 'Error, user already exists'
        else:
            if request.form['inputPassword'] == request.form['inputPasswordConfirm']:
                new_user = User(
                    email=request.form['inputEmail'],
                    password='',
                    username=request.form['inputUsername'],
                    first_name=request.form['inputFirstName'],
                    last_name = request.form['inputLastName']
                )
                new_user.hash_my_password(request.form['inputPassword'])
                db.session.add(new_user)
                db.session.commit()
                return request.form
            else:
                return 'Error, passwords do not match'
    else:
        return render_template('register.html')