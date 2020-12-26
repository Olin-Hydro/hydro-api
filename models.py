# Contains db models
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


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