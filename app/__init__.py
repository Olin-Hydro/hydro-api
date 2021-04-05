from flask import Flask, jsonify
from flask_restx import Api
from colorama import init

from .apis.resources.models import db
from .apis.resources.schemas import ma
from .apis import api
from .config import config_by_name


def create_app(env=None):

    # Initialize colorama
    init()

    # Initialize flask app
    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "dev"])

    # Initialize api
    api.init_app(app)

    # Initialize flask_sqlalchemy
    db.init_app(app)

    # Initialize marshmallow
    ma.init_app(app)

    @app.route("/health")
    def health():
        return jsonify("health")

    return app
