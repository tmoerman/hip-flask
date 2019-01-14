"""
User models.
"""

from hipflask.database import db, Model, IntIdMixin, CRUDMixin
from hipflask.extensions import bcrypt


class User(IntIdMixin, CRUDMixin, Model):
    # main fields
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.Binary(128), nullable=False)

    # orm derived fields

    def __init__(self,
                 username: str,
                 email: str,
                 password: str,
                 **kwargs):
        assert password.strip(), "Password cannot be blank or None."

        db.Model.__init__(self,
                          username=username,
                          email=email,
                          **kwargs)

        self.set_password(password)

    def set_password(self, password: str) -> None:
        self.password_hash = bcrypt.generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self) -> str:
        return f'<User {self.username}>'
