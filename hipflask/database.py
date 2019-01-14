"""
Database module.
"""

from .extensions import db

# Aliases
Column = db.Column
Model = db.Model
ID = int


class CRUDMixin(object):
    """Mixin that adds convenience methods for CRUD (create, read, update, delete) operations."""

    def update(self, commit=True, **kwargs) -> 'CRUDMixin':
        """
        Update specific fields of a record.
        """
        for attr, value in kwargs.items():
            setattr(self, attr, value)

        return commit and self.save() or self

    def add(self) -> None:
        db.session.add(self)

    def save(self, commit=True) -> 'CRUDMixin':
        """
        Save the record.
        """
        db.session.add(self)

        if commit:
            db.session.commit()

        return self

    def delete(self, commit=True) -> bool:
        """
        Remove the record from the database.
        """
        db.session.delete(self)
        return commit and db.session.commit()


class IntIdMixin(Model):
    id: ID = db.Column(db.Integer, primary_key=True)
