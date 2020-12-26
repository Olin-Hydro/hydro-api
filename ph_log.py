# Ph logs api classes
from flask_restful import Resource, reqparse, abort, marshal_with, fields
from models import PhModel

# Define resource fields to use for marshalling of values returned by class methods
ph_resource_fields = {
    'log_id': fields.Integer,
    'ph': fields.Integer,
    'ph_raw': fields.String,
    'timestamp': fields.String
}

# Define expected inputs for arg parsing
# TODO: Replace with marshmallow
ph_parser = reqparse.RequestParser()
ph_parser.add_argument('ph_raw', type=str)
ph_parser.add_argument('ph', type=int)


class ph_log_by_id(Resource):
	'''
	Class for getting a ph log by its id
	'''
	@marshal_with(ph_resource_fields)
	def get(self, log_id):
	    ph_log = PhModel.query.filter_by(log_id = log_id).first()
	    if not ph_log:
	        abort(404, message="Could not find ph log with that id")
	    return ph_log


class ph_log(Resource):
	'''
	Class for posting a ph log and getting all ph logs
	'''
	@marshal_with(ph_resource_fields)
	def get(self):
	    ph_logs = PhModel.query.order_by(PhModel.timestamp).all()
	    return ph_logs

	@marshal_with(ph_resource_fields)
	def post(self):
	    args = ph_parser.parse_args()
	    ph_log = PhModel(ph = args['ph'], ph_raw = args['ph_raw'])
	    db.session.add(ph_log)
	    db.session.commit()
	    return ph_log, 201
