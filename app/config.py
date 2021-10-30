import os

from app import BASE_DIRECTORY

class BaseConfig(object):
    NAME = 'Default'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{BASE_DIRECTORY}/db/app.db'
    SECRET_KEY = 'lajfddlkfjlkj420ijlkdjfal28492040'

class TestConfig(BaseConfig):
    NAME = 'Test'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{BASE_DIRECTORY}/db/app-test.db'

class DevelopmentConfig(BaseConfig):
    NAME = 'Development'
    TESTING = True
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True

EXPORT_CONFIGS = [
    DevelopmentConfig,
    TestConfig
]

config_by_name = {cfg.NAME: cfg for cfg in EXPORT_CONFIGS}