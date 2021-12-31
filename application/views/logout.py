from flask import Blueprint, flash, get_flashed_messages, redirect, render_template, session,request
from flask_session import Session

from ..helpers import apology, login_required, lookup, usd
from ..models.users_db import User

# index route:
logout_bp = Blueprint('logout', __name__, template_folder='../templates', static_folder='../static')


@logout_bp.route('/logout', methods=['GET', 'POST'])
def logoutView():
    """Log user out"""

    # recover flashed messages before forget session
    message = get_flashed_messages()
    # Forget any user_id
    session.clear()
    # Redirect user to login form
    return render_template("login.html", message=message)