from flask_restx import Namespace, Resource
from flask import jsonify, request, abort

from .resources.models import EcModel, db
from .resources.schemas import EcSchema
from .utils import str_to_datetime


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


@api.param("start_time", "The starting time frame for the desired logs in iso format")
@api.param("end_time", "The ending time frame for the desired logs in iso format")
@api.route("/<start_time>/<end_time>")
class ec_log_by_timeframe(Resource):
    """
    Class for getting all ec logs in a timeframe
    """

    def get(self, start_time, end_time):
        """
        Get all ec logs within start_time and end_time range
        """
        start_time = str_to_datetime(start_time)
        end_time = str_to_datetime(end_time)
        ec_logs = EcModel.query.filter(EcModel.timestamp >= start_time).\
                                    filter(EcModel.timestamp <= end_time)
        return jsonify(ec_schema.dump(ec_logs, many=True))


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
