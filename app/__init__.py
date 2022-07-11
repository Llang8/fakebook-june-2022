from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    # WHERE ALL OF OUR APP CONFIGURATION HAPPENS
    @app.route("/")
    def home():
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
                "eyeColor": "green",
                "hairColor": "blonde"
            }
        }

        context = {
            "users": user_dict,
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

    return app