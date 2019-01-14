"""

"""

import pytest

from flask_sqlalchemy import SQLAlchemy
from typing import List

from hipflask.user.models import User
from .conftest import TestConfig
from .factories import UserFactory


@pytest.mark.usefixtures('db')
class TestUsers():
    PWD = 'i_love_mommy'

    def test_get_by_id(self, db: SQLAlchemy):
        user = User(username='tmo', email='tmo@company.com', password=self.PWD)
        user.save()

        fetched = User.query.get(user.id)

        assert fetched == user

    def test_check_password(self, db: SQLAlchemy):
        user = User(username='tmo', email='tmo@company.com', password=self.PWD)

        assert user.check_password(self.PWD)

        # check the bcrypt log rounds
        _, _, log_rounds, _ = str(user.password_hash).split('$')
        assert int(log_rounds) == TestConfig.BCRYPT_LOG_ROUNDS, \
            f'incorrect bcrypt log rounds: {log_rounds}, expected: {TestConfig.BCRYPT_LOG_ROUNDS}'

    def test_user_factory(self, db: SQLAlchemy):
        some_users: List[User] = UserFactory.build_batch(10)

        # add all users to the persistence context
        for user in some_users:
            user.add()

        db.session.commit()

        fetched = User.query.all()

        assert len(fetched) == 10
        for i in range(10):
            assert some_users[i].check_password(f'pwd_{i}')
