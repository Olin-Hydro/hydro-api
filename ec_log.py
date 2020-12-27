# EC log api classes
from flask_restful import abort, Resource
from flask import jsonify, request
from models import EcModel, db
from schemas import EcSchema


# Initialize Marshmallow EcSchema 
ec_schema = EcSchema()


class ec_log_by_id(Resource):
	'''
	Class for getting an ec log by its id
	'''
	def get(self, log_id):
		'''
		Find a log by its id and return it
		'''
		ec_log = EcModel.query.filter_by(log_id = log_id).first()
		if not ec_log:
		    abort(404, message="Could not find ec log with that id")
		return ec_schema.jsonify(ec_log)


class ec_log(Resource):
	'''
	Class for posting a ec log and getting all ec logs
	'''
	def get(self):
		'''
		Get all ec logs and return them
		'''
		ec_logs = EcModel.query.order_by(EcModel.timestamp).all()
		return jsonify(ec_schema.dump(ec_logs, many=True))

	def post(self):
		'''
		Get posted data
		Create a model object
		Add and commit the object to the db
		'''
		data = request.get_json()
		new_ec_log = EcModel(ec = data['ec'], ec_raw = data['ec_raw'])
		db.session.add(new_ec_log)
		db.session.commit()
		return ec_schema.jsonify(new_ec_log)