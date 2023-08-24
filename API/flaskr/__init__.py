from flask import flask

def create_app(config_name):
    app = Flask(__name__)
    return app