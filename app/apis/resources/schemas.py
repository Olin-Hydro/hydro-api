# Marshmallow Schemas
from flask_marshmallow import Marshmallow
from .models import PhModel, EcModel, TempModel, LevelModel


# Initialize marshmallow for marshalling
ma = Marshmallow()


class PhSchema(ma.SQLAlchemyAutoSchema):
	'''
	Class that defines how ph logs are marshalled
	Automatically created based on PhModel
	'''
	class Meta:
		model = PhModel


class EcSchema(ma.SQLAlchemyAutoSchema):
	'''
	Class that defines how ec logs are marshalled
	Automatically created based on EcModel
	'''
	class Meta:
		model = EcModel


class TempSchema(ma.SQLAlchemyAutoSchema):
	'''
	Class that defines how temperature logs are marshalled
	Automatically created based on TempModel
	'''
	class Meta:
		model = TempModel


class LevelSchema(ma.SQLAlchemyAutoSchema):
	'''
	Class that defines how water level logs are marshalled
	Automatically created based on TempModel
	'''
	class Meta:
		model = LevelModel

