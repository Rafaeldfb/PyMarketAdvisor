from flask import Blueprint, flash, get_flashed_messages, redirect, render_template, session,request
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from ..helpers import apology, login_required, lookup, usd
from ..models.users_db import User

# index route:
register_bp = Blueprint('register', __name__, template_folder='../templates', static_folder='../static')


@register_bp.route('/register', methods=['GET','POST'])
def registerView():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = User("SELECT * FROM users WHERE user_name = ?", request.form.get("username"))

        # Ensure username NOT exists
        if len(rows) != 0:
            return apology("This username is already in use.", 403)

        hashpass = generate_password_hash(request.form.get("password"))
        User("INSERT INTO users (user_name, user_hash) VALUES ( ?, ?);", request.form.get("username"), hashpass)
        flash('You were successfully Regitered! Please log in.')
        return redirect("/login")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")