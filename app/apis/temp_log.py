from flask_restx import Namespace, Resource
from flask import jsonify, request, abort

from .resources.models import TempModel, db
from .resources.schemas import TempSchema


api = Namespace("temp", description="Temperature sensor logs")

# Initialize Marshmallow TempSchema
temp_schema = TempSchema()


@api.route("/<log_id>")
@api.param("log_id", "The unique identifier of the temperature sensor log")
class temp_log_by_id(Resource):
    """
    Class for getting an temp log by its id
    """

    def get(self, log_id):
        """
        Find a log by its id and return it
        """
        temp_log = TempModel.query.filter_by(log_id=log_id).first()
        if not temp_log:
            abort(404, "Could not find a temp log with that id")
        return temp_schema.jsonify(temp_log)


@api.route("/")
class temp_log(Resource):
    """
    Class for posting a temp log and getting all temp logs
    """

    def get(self):
        """
        Get all temp logs and return them
        """
        temp_logs = TempModel.query.order_by(TempModel.timestamp).all()
        return jsonify(temp_schema.dump(temp_logs, many=True))

    def post(self):
        """
        Get posted data
        Create a model object
        Add and commit the object to the db
        """
        data = request.get_json()
        new_temp_log = TempModel(temp=data["temp"])
        db.session.add(new_temp_log)
        db.session.commit()
        return temp_schema.jsonify(new_temp_log)
