"""
Database module.
"""

from .extensions import db
from sqlalchemy import Integer

# Aliases
Column = db.Column
Model = db.Model


class IntIdMixin(object):
    id = db.Column(db.Integer, primary_key=True)
