# Ph log api classes
from flask_restful import abort, Resource
from flask import jsonify, request
from models import PhModel, db
from schemas import PhSchema


# Initialize Marshmallow PhSchema 
ph_schema = PhSchema()


class ph_log_by_id(Resource):
	'''
	Class for getting a ph log by its id
	'''
	def get(self, log_id):
		'''
		Find a log by its id and return it
		'''
		ph_log = PhModel.query.filter_by(log_id = log_id).first()
		if not ph_log:
		    abort(404, message="Could not find ph log with that id")
		return ph_schema.jsonify(ph_log)


class ph_log(Resource):
	'''
	Class for posting a ph log and getting all ph logs
	'''
	def get(self):
		'''
		Get all ph logs and return them
		'''
		ph_logs = PhModel.query.order_by(PhModel.timestamp).all()
		return jsonify(ph_schema.dump(ph_logs, many=True))

	def post(self):
		'''
		Get posted data
		Create a model object
		Add and commit the object to the db
		'''
		data = request.get_json()
		new_ph_log = PhModel(ph = data['ph'], ph_raw = data['ph_raw'])
		db.session.add(new_ph_log)
		db.session.commit()
		return ph_schema.jsonify(new_ph_log)
