"""
Module containing model factories for testing.
"""

from factory.alchemy import SQLAlchemyModelFactory
from factory import Sequence, PostGenerationMethodCall

from hipflask.database import db, ID
from hipflask.user.models import User


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = db.session


class UserFactory(BaseFactory):
    class Meta:
        model = User

    username = Sequence(lambda id: f'user_{id})')
    email = Sequence(lambda id: f'user_{id}@company.com')
    password = Sequence(lambda id: f'pwd_{id}')

