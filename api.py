import logging
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from colorama import init


# Initialize colorama
init()


# Initialize app and db
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///HydroDB.db'
db = SQLAlchemy(app)


ph_resource_fields = {
    'log_id': fields.Integer,
    'ph': fields.Integer,
    'ph_raw': fields.String,
    'timestamp': fields.String
}

ph_parser = reqparse.RequestParser()
ph_parser.add_argument('ph_raw', type=str)
ph_parser.add_argument('ph', type=int)


class PhModel(db.Model):
    '''
    Class for ph logs
    '''
    __tablename__ = 'PH_LOG'
    log_id = db.Column(db.Integer, 
                            primary_key=True)
    timestamp = db.Column(db.DateTime, 
                            default=datetime.utcnow)               
    ph = db.Column(db.Integer, 
                        index=True)
    ph_raw = db.Column(db.String(32))
    updated_at = db.Column(db.DateTime, 
                        default=datetime.utcnow, 
                        onupdate=datetime.utcnow)


class ph_log_by_id(Resource):
    @marshal_with(ph_resource_fields)
    def get(self, log_id):
        ph_log = PhModel.query.filter_by(log_id = log_id).first()
        if not ph_log:
            abort(404, message="Could not find ph log with that id")
        return ph_log


class ph_log(Resource):
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


api.add_resource(ph_log, "/ph")
api.add_resource(ph_log_by_id, "/ph/<log_id>")


if __name__ == '__main__':
    app.run(debug=True)