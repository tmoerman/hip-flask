"""
The app factory module. Contains the app factory function.
"""

from flask import Flask

from . import user, analysis
from .config import Config, ProdConfig
from .extensions import db, migrate, bcrypt


def create_app(config: Config = ProdConfig) -> Flask:
    """
    Application factory function.
    :param config: the configuration object to use.
    :return: a configured Flask instance.
    """

    # input validation
    assert config, "config cannot be None"

    # create and configure app
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config)

    # register extensions
    bcrypt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    app.register_blueprint(user.views.blueprint)
    app.register_blueprint(analysis.views.blueprint)

    return app
