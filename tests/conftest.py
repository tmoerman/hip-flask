"""
Fixtures for unit tests.
"""

import pytest

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from hipflask.app import create_app
from hipflask.database import db as _db
from hipflask.settings import TestConfig

from typing import Generator


@pytest.fixture(scope='function')
def app():
    """
    :return: a generator function of Flask instances.
    """

    _app = create_app(TestConfig)

    with _app.app_context():
        _db.create_all()

    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope='function')
def db(app: Flask):
    """
    :param app: a Flask application instance.
    :return: a generator function of SQLAlchemy instances.
    """

    _db.app = app

    with app.app_context():
        _db.create_all()

    yield _db

    _db.session.close()
    _db.drop_all()
