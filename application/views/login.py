from flask import Blueprint, flash, get_flashed_messages, redirect, render_template, session,request
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from ..helpers import apology, login_required, lookup, usd
from ..models.users_db import User

# index route:
login_bp = Blueprint('login', __name__, template_folder='../templates', static_folder='../static')


@login_bp.route('/login', methods=['GET', 'POST'])
def loginView():
    """Log user in"""
    # recover flashed messages before forget session
    message = get_flashed_messages()
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

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["user_hash"], request.form.get("password")):
            return apology("invalid username or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["user_id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html", message=message)