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

@app.route('/posts')
def posts():
    result_posts = Post.query.all()    
    
    # Sort the queried posts by their date created
    # Reverse it to make it go from newest to oldest
    result_posts.sort(key=lambda post: post.date_created, reverse=True)

    result_posts = list(map(lambda post: {
        "id": post.id,
        "body": post.body,
        "date_created": post.date_created,
        "user_id": post.user_id
    }, result_posts))

    print(result_posts)

    return jsonify(result_posts)

@app.route('/post/<id>')
def post(id):
    result_post = Post.query.get(id)

    result_post = {
        "id": result_post.id,
        "body": result_post.body,
        "date_created": result_post.date_created,
        "user_id": result_post.user_id
    }

    return jsonify(result_post)

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




