from flask_restx import Namespace, Resource
from flask import jsonify, request, abort

from .resources.models import SystemModel, db
from .resources.schemas import SystemSchema


api = Namespace("system", description="System settings")

# Initialize Marshmallow SystemSchema
system_schema = SystemSchema()


@api.route("/<system_id>")
@api.param("system_id", "The unique identifier of the system")
class system_by_id(Resource):
    """
    Class for getting a system settings by id
    """

    def get(self, system_id):
        """
        Find a system by its id and return it
        """
        system = SystemModel.query.filter_by(system_id=system_id).first()
        if not system:
            abort(404, "Could not find a system with that id")
        return system_schema.jsonify(system)

    def put(self, system_id):
        """
        Get data
        Update system data
        Commit object to the db
        """
        data = request.get_json()
        system = SystemModel.query.filter_by(system_id=system_id).first()
        system.data = data
        db.session.commit()
        return system_schema.jsonify(system)


@api.route("/")
class system_settings(Resource):
    """
    Class for creating systems and getting all systems
    """

    def get(self):
        """
        Get all systems and return them
        """
        systems = SystemModel.query.order_by(SystemModel.timestamp).all()
        if not systems:
            abort(404, "Could not find any systems")
        return jsonify(system_schema.dump(systems, many=True))

    def post(self):
        """
        Get posted data
        Create a model object
        Add and commit the object to the db
        """
        data = request.get_json()
        new_system = SystemModel(data=data)
        db.session.add(new_system)
        db.session.commit()
        return system_schema.jsonify(new_system)
