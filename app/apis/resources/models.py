# Contains db models
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()


class PhModel(db.Model):
    """
    SQLAlchemy DB Class for ph logs
    """

    __tablename__ = "PH_LOG"
    log_id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    ph = db.Column(db.Float)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class EcModel(db.Model):
    """
    SQLAlchemy DB Class for ec logs
    """

    __tablename__ = "EC_LOG"
    log_id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    ec = db.Column(db.Float)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class TempModel(db.Model):
    """
    SQLAlchemy DB Class for temperature logs
    """

    __tablename__ = "TEMP_LOG"
    log_id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    temp = db.Column(db.Float)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class UserModel(db.Model):
    """
    SQLAlchemy DB Class for users
    """

    __tablename__ = "USERS"
    user_id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    email = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(32))
    permission = db.Column(db.String(32))
    password_hash = db.Column(db.String(128))
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class LevelModel(db.Model):
    """
    SQLAlchemy DB Class for water level logs
    """

    __tablename__ = "LEVEL_LOG"
    log_id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    level = db.Column(db.Float)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class SystemModel(db.Model):
    """
    SQLAlchemy DB Class for system parameters
    """

    __tablename__ = "SYSTEM_SETTINGS"
    system_id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    data = db.Column(db.PickleType)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class TaskModel(db.Model):
    """
    SQLAlchemy DB Class for task logs
    """

    __tablename__ = "TASK_LOG"
    log_id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    data = db.Column(db.String)
    task_type = db.Column(db.String, index=True)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
