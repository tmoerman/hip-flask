"""
Views for users.
"""

from flask import Blueprint

blueprint = Blueprint('users', __name__)

from hipflask.database import ID
from hipflask.user.models import User
