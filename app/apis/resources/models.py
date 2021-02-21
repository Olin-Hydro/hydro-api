# Contains db models
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class PhModel(db.Model):
    '''
    SQLAlchemy DB Class for ph logs
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


class EcModel(db.Model):
    '''
    SQLAlchemy DB Class for ec logs
    '''
    __tablename__ = 'EC_LOG'
    log_id = db.Column(db.Integer, 
                            primary_key=True)
    timestamp = db.Column(db.DateTime, 
                            default=datetime.utcnow)               
    ec = db.Column(db.Integer, 
                        index=True)
    ec_raw = db.Column(db.String(32))
    updated_at = db.Column(db.DateTime, 
                        default=datetime.utcnow, 
                        onupdate=datetime.utcnow)


class TempModel(db.Model):
    '''
    SQLAlchemy DB Class for temperature logs
    '''
    __tablename__ = 'TEMP_LOG'
    log_id = db.Column(db.Integer, 
                            primary_key=True)
    timestamp = db.Column(db.DateTime, 
                            default=datetime.utcnow)               
    temp = db.Column(db.Integer, 
                        index=True)
    temp_raw = db.Column(db.String(32))
    updated_at = db.Column(db.DateTime, 
                        default=datetime.utcnow, 
                        onupdate=datetime.utcnow)


class LevelModel(db.Model):
    '''
    SQLAlchemy DB Class for water level logs
    '''
    __tablename__ = 'LEVEL_LOG'
    log_id = db.Column(db.Integer, 
                            primary_key=True)
    timestamp = db.Column(db.DateTime, 
                            default=datetime.utcnow)               
    level = db.Column(db.Integer, 
                        index=True)
    level_raw = db.Column(db.String(32))
    updated_at = db.Column(db.DateTime, 
                        default=datetime.utcnow, 
                        onupdate=datetime.utcnow)