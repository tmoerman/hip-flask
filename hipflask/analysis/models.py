from hipflask.database import db, as_id, ID, relationship, Model, IntIdMixin, CRUDMixin

from typing import Union

class Comment(IntIdMixin, CRUDMixin, Model):
    text = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates='comments')

    def __init__(self, text: str, user: Union[IntIdMixin, ID]):
        assert text.strip(), "Text cannot be blank."
        assert user, "User cannot be None."

        db.Model.__init__(self, text=text, user_id=as_id(user))
