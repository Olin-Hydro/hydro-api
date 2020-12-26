from flask import Flask
from flask_restful import Api
from colorama import init

from models import PhModel, db
from ph_log import ph_log_by_id, ph_log


# Initialize colorama
init()


# Initialize app and db
app = Flask(__name__)
api = Api(app)
app.config.from_object('config.DevelopmentConfig')


# Initialize flask_sqlalchemy with the app
db.init_app(app)


# Add api resource routing
api.add_resource(ph_log, "/ph")
api.add_resource(ph_log_by_id, "/ph/<log_id>")


if __name__ == '__main__':
    app.run()
    #app.run(host = '0.0.0.0', port=8080)
    