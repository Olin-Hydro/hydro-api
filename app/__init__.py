from flask import Flask
from colorama import init

from .apis.resources.models import db
from .apis.resources.schemas import ma
from .apis import api
from .config import config_by_name


def create_app(env="development"):

    # Initialize colorama
    init()

    # Initialize flask app
    app = Flask(__name__)
    app.config.from_object(config_by_name[env])

    @app.after_request
    def set_headers(response):
        if env == "development":
            response.headers["Access-Control-Allow-Origin"] = "*"
        return response

    # Initialize api
    api.init_app(app)

    # Initialize flask_sqlalchemy
    db.init_app(app)

    # Initialize marshmallow
    ma.init_app(app)

    return app
