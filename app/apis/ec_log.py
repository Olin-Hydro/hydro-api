from flask_restx import Namespace, Resource
from flask import jsonify, request, abort

from .resources.models import EcModel, db
from .resources.schemas import EcSchema


api = Namespace("ec", description="Electrical conductivity sensor logs")

# Initialize Marshmallow EcSchema
ec_schema = EcSchema()


@api.route("/<log_id>")
@api.param("log_id", "The unique identifier of the ec log")
class ec_log_by_id(Resource):
    """
    Class for getting an ec log by its id
    """

    def get(self, log_id):
        """
        Find a log by its id and return it
        """
        ec_log = EcModel.query.filter_by(log_id=log_id).first()
        if not ec_log:
            abort(404, "Could not find ec log with that id")
        return ec_schema.jsonify(ec_log)


@api.route("/")
class ec_log(Resource):
    """
    Class for posting an ec log and getting all ec logs
    """

    def get(self):
        """
        Get all ec logs and return them
        """
        ec_logs = EcModel.query.order_by(EcModel.timestamp).all()
        return jsonify(ec_schema.dump(ec_logs, many=True))

    def post(self):
        """
        Get posted data
        Create a model object
        Add and commit the object to the db
        """
        data = request.get_json()
        new_ec_log = EcModel(ec=data["ec"])
        db.session.add(new_ec_log)
        db.session.commit()
        return ec_schema.jsonify(new_ec_log)
