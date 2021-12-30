from flask import Blueprint
from flask import current_app as app
# from flask_sqlalchemy import SQLAlchemy
from cs50 import SQL
# from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
# from application import db

# define user models
users_bp = Blueprint('users_bp', __name__)

# db = SQLAlchemy()
db = SQL("sqlite:///application/user_database.db")


def User(*args, **kwargs):
    """return db.execute(query) from user badatabase, if User(None)'s query is None, return None"""
    if len(args) > 0 and len(kwargs) > 0:
        return db.execute(*args, **kwargs)

    elif len(args) > 0 and len(kwargs) == 0:
        return db.execute(*args)

    else:
        return None
