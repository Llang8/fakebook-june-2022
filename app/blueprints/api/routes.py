from flask import jsonify
from . import bp as app

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
