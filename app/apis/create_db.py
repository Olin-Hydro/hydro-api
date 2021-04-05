import os
from flask_restx import Namespace, Resource

from .resources.models import PhModel, EcModel, TempModel, UserModel, LevelModel, db


api = Namespace("init_db", description="Initialize the database with test information")


@api.route("/")
class init_db(Resource):
    """
    Class for initializing the database
    """

    def post(self):
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

        # Delete the database if it exists
        # if os.path.exists('HydroDB.db'):
        #    os.remove('HydroDB.db')

        # Create the database based on models
        db.create_all()

        # Add initial test data
        for log in PH:
            l = PhModel(ph=log["ph"], ph_raw=log["ph_raw"])
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

        # Save changes
        db.session.commit()

        return "Database created successfully"
