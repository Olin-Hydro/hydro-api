from flask_restx import Namespace, Resource
from flask import jsonify, request, abort

from .resources.models import LevelModel, db
from .resources.schemas import LevelSchema


api = Namespace('level', description='Water level sensor logs')

# Initialize Marshmallow LevelSchema 
level_schema = LevelSchema()


@api.route('/<log_id>')
@api.param('log_id', 'The unique identifier of the water level sensor log')
class level_log_by_id(Resource):
	'''
	Class for getting a water level log by its id
	'''
	def get(self, log_id):
		'''
		Find a log by its id and return it
		'''
		level_log = LevelModel.query.filter_by(log_id = log_id).first()
		if not level_log:
		    abort(404, 'Could not find a water level log with that id')
		return level_schema.jsonify(level_log)


@api.route('/')
class level_log(Resource):
	'''
	Class for posting a water level log and getting all water level logs
	'''
	def get(self):
		'''
		Get all water level logs and return them
		'''
		level_logs = LevelModel.query.order_by(LevelModel.timestamp).all()
		return jsonify(level_schema.dump(level_logs, many=True))

	def post(self):
		'''
		Get posted data
		Create a model object
		Add and commit the object to the db
		'''
		data = request.get_json()
		new_level_log = LevelModel(level = data['level'], level_raw = data['level_raw'])
		db.session.add(new_level_log)
		db.session.commit()
		return level_schema.jsonify(new_level_log)