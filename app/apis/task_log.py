from flask_restx import Namespace, Resource
from flask import jsonify, request, abort

from .resources.models import TaskModel, db
from .resources.schemas import TaskSchema
from .utils import str_to_datetime


api = Namespace("task", description="task logs")

# Initialize Marshmallow TaskSchema
task_schema = TaskSchema()


@api.route("/<log_id>")
@api.param("log_id", "The unique identifier of the task log")
class task_log_by_id(Resource):
    """
    Class for getting a task log by its id
    """

    def get(self, log_id):
        """
        Find a log by its id and return it
        """
        task_log = TaskModel.query.filter_by(log_id=log_id).first()
        if not task_log:
            abort(404, "Could not find a task log with that id")
        return task_schema.jsonify(task_log)


@api.param("start_time", "The starting time frame for the desired logs in iso format")
@api.param("end_time", "The ending time frame for the desired logs in iso format")
@api.route("/<start_time>/<end_time>")
class task_log_by_timeframe(Resource):
    """
    Class for getting all task logs in a timeframe
    """

    def get(self, start_time, end_time):
        """
        Get all task logs within start_time and end_time range
        """
        start_time = str_to_datetime(start_time)
        end_time = str_to_datetime(end_time)
        task_logs = TaskModel.query.filter(TaskModel.timestamp >= start_time).\
                                    filter(TaskModel.timestamp <= end_time)
        return jsonify(task_schema.dump(task_logs, many=True))


@api.route("/")
class task_log(Resource):
    """
    Class for posting a task log and getting all task logs
    """

    def get(self):
        """
        Get all task logs and return them
        """
        task_logs = TaskModel.query.order_by(TaskModel.timestamp).all()
        return jsonify(task_schema.dump(task_logs, many=True))

    def post(self):
        """
        Get posted data
        Create a model object
        Add and commit the object to the db
        """
        data = request.get_json()["task"]
        new_task_log = TaskModel(data=data["data"], task_type=data["task_type"])
        db.session.add(new_task_log)
        db.session.commit()
        return task_schema.jsonify(new_task_log)
