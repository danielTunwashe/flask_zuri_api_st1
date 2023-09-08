from flask import Flask
from flask_restx import Api
from .tracks.views import track_namespace
from .config.config import config_dict


def create_app(config=config_dict['dev']):
    app = Flask(__name__)

    app.config.from_object(config)

    api=Api(app)


    api.add_namespace(track_namespace)

    return app