"""
The extensions module.
Contains Flask extensions, referred to from the app factory module.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
cors = CORS()