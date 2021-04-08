import os
import json
from flask_restx import Namespace, Resource

from .resources.models import PhModel, EcModel, TempModel, UserModel, LevelModel, SystemModel, db


api = Namespace("init_db", description="Initialize the database with test information")


@api.route("/")
class init_db(Resource):
    """
    Class for initializing the database
    """

    def get(self):
        """
        Creates new database with initial data
        """
        PH = [{"ph": 6.1}, {"ph": 7}, {"ph": 5.6}]
        EC = [
            {"ec": 998, "ec_raw": "test data"},
            {"ec": 1221, "ec_raw": "test data"},
            {"ec": 1140, "ec_raw": "test data"},
        ]
        TEMP = [
            {"temp": 22.2, "temp_raw": "test data"},
            {"temp": 23.1, "temp_raw": "test data"},
            {"temp": 22.8, "temp_raw": "test data"},
        ]
        USER = [
            {
                "email": "fake_email@mail.net",
                "name": "Jane Doe",
                "password": "password123",
                "permission": "user",
            },
            {
                "email": "email_fake@mail.net",
                "name": "John Doe",
                "password": "password321",
                "permission": "user",
            },
        ]
        LEVEL = [
            {"level": 6.1, "level_raw": "test data"},
            {"level": 7.9, "level_raw": "test data"},
            {"level": 6.6, "level_raw": "test data"},
        ]
        SYSTEM = [
            {
                "data": {
                    "ph_high": 7,
                    "ec_low": 1.4,
                    "sensor_interval": 120,
                    "check_ec_ph_interval": 1200,
                }
            }
        ]

        # Delete the database if it exists
        if os.path.exists('HydroDB.db'):
            os.remove('HydroDB.db')

        # Create the database based on models
        db.create_all()

        # Add initial test data
        for log in PH:
            l = PhModel(ph=log["ph"])
            db.session.add(l)
        for log in EC:
            l = EcModel(ec=log["ec"], ec_raw=log["ec_raw"])
            db.session.add(l)
        for log in TEMP:
            l = TempModel(temp=log["temp"], temp_raw=log["temp_raw"])
            db.session.add(l)
        for user in USER:
            u = UserModel(
                email=user["email"], name=user["name"], permission=user["permission"]
            )
            u.set_password(user["password"])
            db.session.add(u)
        for log in LEVEL:
            l = LevelModel(level=log["level"], level_raw=log["level_raw"])
            db.session.add(l)
        for sys in SYSTEM:
            s = SystemModel(data=sys["data"])
            db.session.add(s)

        # Save changes
        db.session.commit()

        return "Database created successfully"
