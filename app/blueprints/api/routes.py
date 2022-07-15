from flask import jsonify, request, redirect, flash, url_for
from . import bp as app
from app.blueprints.main.models import Post
from flask_login import current_user
from app import db

@app.route("/users")
def users():
    user_dict = {
        "lucas": {
            "eyeColor": "blue",
            "hairColor": "brown"
        },
        "joe": {
            "eyeColor": "gray",
            "hairColor": "black"
        },
        "kevin": {
            "eyeColor": "brown",
            "hairColor": "blonde"
        }
    }

    return jsonify(user_dict)

@app.route("/status-update", methods=["POST"])
def status_update():
    # Retrieve form data from request
    status_input = request.form['statusInput']
    user = current_user.id

    # Instantiate new post
    new_post = Post(body=status_input, user_id=user)

    # Add new post to the database
    db.session.add(new_post)
    db.session.commit()

    flash('New post added successfully', 'success')

    # Once the post is added to the database, send the user back to the homepage
    return redirect(url_for('main.home'))

    
