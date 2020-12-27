from flask import Flask
from flask_restful import Api
from colorama import init

from models import db
from schemas import ma
from ph_log import ph_log_by_id, ph_log
from ec_log import ec_log_by_id, ec_log
from temp_log import temp_log_by_id, temp_log
from create_db import init_db


# Initialize colorama
init()


# Initialize app and db
app = Flask(__name__)
api = Api(app)
app.config.from_object('config.DevelopmentConfig')


# Initialize flask_sqlalchemy
db.init_app(app)


# Initialize marshmallow 
ma.init_app(app)


# Add api resource routing
api.add_resource(ph_log, "/ph")
api.add_resource(ph_log_by_id, "/ph/<log_id>")
api.add_resource(ec_log, "/ec")
api.add_resource(ec_log_by_id, "/ec/<log_id>")
api.add_resource(temp_log, "/temp")
api.add_resource(temp_log_by_id, "/temp/<log_id>")
api.add_resource(init_db, '/create_db')


if __name__ == '__main__':
	app.run()
    #app.run(host = '0.0.0.0', port=8080)
    