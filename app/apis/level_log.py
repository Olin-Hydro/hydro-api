from flask_restx import Namespace, Resource
from flask import jsonify, request, abort

from .resources.models import LevelModel, db
from .resources.schemas import LevelSchema
from .utils import str_to_datetime


api = Namespace("level", description="Water level sensor logs")

# Initialize Marshmallow LevelSchema
level_schema = LevelSchema()


@api.route("/<log_id>")
@api.param("log_id", "The unique identifier of the water level sensor log")
class level_log_by_id(Resource):
    """
    Class for getting a water level log by its id
    """

    def get(self, log_id):
        """
        Find a log by its id and return it
        """
        level_log = LevelModel.query.filter_by(log_id=log_id).first()
        if not level_log:
            abort(404, "Could not find a water level log with that id")
        return level_schema.jsonify(level_log)


@api.param("start_time", "The starting time frame for the desired logs in iso format")
@api.param("end_time", "The ending time frame for the desired logs in iso format")
@api.route("/<start_time>/<end_time>")
class level_log_by_timeframe(Resource):
    """
    Class for getting all level logs in a timeframe
    """

    def get(self, start_time, end_time):
        """
        Get all level logs within start_time and end_time range
        """
        start_time = str_to_datetime(start_time)
        end_time = str_to_datetime(end_time)
        level_logs = LevelModel.query.filter(LevelModel.timestamp >= start_time).\
                                    filter(LevelModel.timestamp <= end_time)
        return jsonify(level_schema.dump(level_logs, many=True))


@api.route("/")
class level_log(Resource):
    """
    Class for posting a water level log and getting all water level logs
    """

    def get(self):
        """
        Get all water level logs and return them
        """
        level_logs = LevelModel.query.order_by(LevelModel.timestamp).all()
        return jsonify(level_schema.dump(level_logs, many=True))

    def post(self):
        """
        Get posted data
        Create a model object
        Add and commit the object to the db
        """
        data = request.get_json()
        new_level_log = LevelModel(level=data["level"])
        db.session.add(new_level_log)
        db.session.commit()
        return level_schema.jsonify(new_level_log)
