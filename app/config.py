import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///HydroDB.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY")


class ProductionConfig(Config):
    CONFIG_NAME = "prod"
    DEBUG = False


class DevelopmentConfig(Config):
    CONFIG_NAME = "development"
    DEVELOPMENT = True
    DEBUG = True


EXPORT_CONFIGS = [ProductionConfig, DevelopmentConfig]
config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}
