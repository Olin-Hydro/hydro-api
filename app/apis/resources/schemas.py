# Marshmallow Schemas
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields

from .models import (
    PhModel,
    EcModel,
    TempModel,
    UserModel,
    LevelModel,
    SystemModel,
    TaskModel,
)


# Initialize marshmallow for marshalling
ma = Marshmallow()


class PhSchema(ma.SQLAlchemyAutoSchema):
    """
    Class that defines how ph logs are marshalled
    Automatically created based on PhModel
    """

    class Meta:
        model = PhModel


class EcSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = EcModel


class TempSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = TempModel


class UserSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = UserModel


class LevelSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = LevelModel


class SystemSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = SystemModel


class TaskSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = TaskModel


class BlockSchema(Schema):

    data = fields.List(fields.Integer)
