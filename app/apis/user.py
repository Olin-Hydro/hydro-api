from flask_restx import Namespace, Resource
from flask import jsonify, request, abort

from .resources.models import UserModel, db
from .resources.schemas import UserSchema


api = Namespace("users", description="user information")

# Initialize Marshmallow PhSchema
user_schema = UserSchema()


@api.route("/")
class user(Resource):
    """
    Class for posting user information, and checking user login
    """

    def get(self):
        """
        Find a user by email
        Check user password against hashed password
        Return user information if password matches
        """
        data = request.get_json()
        user = UserModel.query.filter_by(email=data["email"]).first()
        if not user:
            abort(404, "Could not find a user with that email")
        if not user.check_password(data["password"]):
            abort(400, "Bad password")
        return user_schema.jsonify(user)

    def post(self):
        """
        Get posted data
        Create a model object
        Add and commit the object to the db
        """
        data = request.get_json()
        new_user = UserModel(
            email=data["email"], name=data["name"], permission=data["permission"]
        )
        new_user.set_password(data["password"])
        db.session.add(new_user)
        db.session.commit()
        return user_schema.jsonify(new_user)
