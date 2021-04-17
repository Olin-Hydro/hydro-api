# Marshmallow Schemas
from flask_marshmallow import Marshmallow
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
    """
    Class that defines how ec logs are marshalled
    Automatically created based on EcModel
    """

    class Meta:
        model = EcModel


class TempSchema(ma.SQLAlchemyAutoSchema):
    """
    Class that defines how temperature logs are marshalled
    Automatically created based on TempModel
    """

    class Meta:
        model = TempModel


class UserSchema(ma.SQLAlchemyAutoSchema):
    """
    Class that defines how user information is marshalled
    Automatically created based on UserModel
    """

    class Meta:
        model = UserModel


class LevelSchema(ma.SQLAlchemyAutoSchema):
    """
    Class that defines how water level logs are marshalled
    Automatically created based on TempModel
    """

    class Meta:
        model = LevelModel


class SystemSchema(ma.SQLAlchemyAutoSchema):
    """
    Class that defines how system settings are marshalled
    Automatically created based on SystemModel
    """

    class Meta:
        model = SystemModel


class TaskSchema(ma.SQLAlchemyAutoSchema):
    """
    Class that defines how Task logs are marshalled
    Automatically created based on TaskModel
    """

    class Meta:
        model = TaskModel