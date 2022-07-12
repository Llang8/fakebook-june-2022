from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    # WHERE ALL OF OUR APP CONFIGURATION HAPPENS
    from app.blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.blueprints.api import bp as api_bp
    app.register_blueprint(api_bp)

    return app