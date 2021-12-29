from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
# from application import db

# define user models
users_bp = Blueprint('users_bp', __name__)

db = SQLAlchemy()

class User(db.Model):
    """User Model"""
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    user_hash = db.Column(db.String(50), nullable=False)
    user_created = db.Column(db.DateTime, default=datetime.now)
    user_updated = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return '<User %r>' % self.username