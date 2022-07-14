from flask import render_template, redirect, url_for
from . import bp as app
from app.blueprints.main.models import Post
from flask_login import login_required, current_user

@app.route("/")
# @login_required
def home():
    # If the user is not logged in, redirect to the login page
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))


    posts = Post.query.all()

    # Sort the queried posts by their date created
    # Reverse it to make it go from newest to oldest
    posts.sort(key=lambda post: post.date_created, reverse=True)

    print(posts)

    context = {
        "posts": posts,
        "user": "jen"
    }

    return render_template('index.html', **context)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')