"""

"""

from flask_sqlalchemy import SQLAlchemy, get_debug_queries
from typing import List

from hipflask.user.models import User
from hipflask.analysis.models import Comment
from .conftest import TestConfig
from .factories import UserFactory

PWD = 'I_love_u_mommy'


class TestUsers():

    def test_get_by_id(self, db: SQLAlchemy):
        user = User(username='tmo', email='tmo@company.com', password=PWD)
        user.save()

        fetched = User.query.get(user.id)
        assert fetched == user

        comments = fetched.comments
        assert len(comments) == 0

    def test_check_password(self, db: SQLAlchemy):
        user = User(username='tmo', email='tmo@company.com', password=PWD)

        assert user.check_password(PWD)

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


class TestComments():

    def test_get_comments_by_user(self, db: SQLAlchemy):
        user = User(username='tmo', email='tmo@company.com', password=PWD)
        user.save()

        Comment("foo", user).add()
        Comment("gee", user).add()
        Comment("bar", user).add()

        db.session.commit()

        user_comments = User.query.get(user.id).comments
        assert {c.text for c in user_comments} == {'foo', 'gee', 'bar'}
