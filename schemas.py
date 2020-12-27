# Marshmallow Schemas
from flask_marshmallow import Marshmallow
from models import PhModel


# Initialize marshmallow for marshalling
ma = Marshmallow()


class PhSchema(ma.SQLAlchemyAutoSchema):
	'''
	Class that defines how ph logs are marshalled
	Automatically created based on PhModel
	'''
	class Meta:
		model = PhModel





