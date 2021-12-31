from flask import Blueprint, flash, get_flashed_messages, redirect, render_template, session
from flask_session import Session
from cs50 import *
from tempfile import mkdtemp
from werkzeug.exceptions import HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from ..helpers import apology, login_required, lookup, usd
from ..models.users_db import User
from ..models.criptocoins_db import Coin, coinById, coinBySymbol, coinLogoBySymbol
from ..models.news import newsBySymbol

# index route:
newsView_bp = Blueprint('newsView', __name__, template_folder='../templates', static_folder='../static')


@newsView_bp.route('/news/<symbol>', methods=['GET'])
@login_required
def newsView(symbol):
    """ View for newa """
    # Get message
    message = get_flashed_messages()
    #  Ensure the user is logged in
    if session.get("user_id") is None:
        return render_template("login.html")
    
    else:
        # Get user's name:
        userID = session.get("user_id")
        userName = User("SELECT user_name FROM users WHERE user_id = :userID", userID=userID)[0]['user_name']
        # make an object with coin to view
        coin = coinBySymbol(symbol)
        # make an object with news to view
        news = newsBySymbol(symbol)

        
    return render_template("/news.html", 
        userName=userName, 
        message=message, 
        coin=coin, 
        news=news
    )