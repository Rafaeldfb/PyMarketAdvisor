from flask import Blueprint, flash, get_flashed_messages, redirect, render_template, session
from flask_session import Session
from cs50 import *
from tempfile import mkdtemp
from werkzeug.exceptions import HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from ..helpers import apology, login_required, lookup, usd
from ..models.users_db import User

# index route:
index_bp = Blueprint('index', __name__, template_folder='../templates', static_folder='../static')


@index_bp.route('/', methods=['GET'])
def indexView():
    """ View for index """
    #  Ensure the user is logged in
    if session.get("user_id") is None:
        return render_template("login.html")
    
    else:
        # Get user's name:
        userID = session.get("user_id")
        userName = User.query.filter_by(user_id=userID).first().user_name
        
    return render_template("index.html", userName=userName)