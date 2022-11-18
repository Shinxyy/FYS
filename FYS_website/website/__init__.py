from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(23)

    from .page import page

    app.register_blueprint(page, url_prefix='/')

    return app
