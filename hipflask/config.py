"""
The application configuration module.
"""

class Config(object):
    """
    Base configuration.
    """


class DevConfig(Config):
    """
    Development configuration.
    """


class ProdConfig(Config):
    """
    Production configuration.
    """


class TestConfig(Config):
    """
    Automated testing configuration.
    """
