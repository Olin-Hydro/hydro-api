import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///HydroDB.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProductionConfig(Config):
    CONFIG_NAME = 'prod'
    DEBUG = False


class StagingConfig(Config):
    CONFIG_NAME = 'stage'
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    CONFIG_NAME = 'dev'
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    CONFIG_NAME = 'test'
    TESTING = True


EXPORT_CONFIGS = [
    ProductionConfig,
    StagingConfig,
    DevelopmentConfig,
    TestingConfig
]
config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}