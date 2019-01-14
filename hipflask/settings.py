"""
The application configuration module.

See:
* http://flask-sqlalchemy.pocoo.org/2.3/config/
*

"""
import os


class Config(object):
    """
    Base configuration.
    """
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 12


class ProdConfig(Config):
    """
    Production configuration.
    """
    ENV = 'prod'
    DEBUG = False
    DB_NAME = f'{ENV}.db'
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)


class DevConfig(Config):
    """
    Development configuration.
    """
    ENV = 'dev'
    DEBUG = True
    DB_NAME = f'{ENV}.db'
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)


class TestConfig(Config):
    """
    Automated testing configuration.
    """
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    # lower bcrypt log rounds for faster testing
    BCRYPT_LOG_ROUNDS = 4
