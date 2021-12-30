from flask import Blueprint, flash, get_flashed_messages, redirect, render_template, session,request
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from ..helpers import apology, login_required, lookup, usd
from ..models.users_db import User

# index route:
settings_bp = Blueprint('settings', __name__, template_folder='../templates', static_folder='../static')


@settings_bp.route('/settings', methods=['GET', 'POST'])
@login_required
def settingsView():
    """Show settings"""
    # User settings - change user name and password
    userName = User("SELECT user_name FROM users WHERE user_id = :userID", userID=session["user_id"])[0]['user_name']
    userHash = User("SELECT user_hash FROM users WHERE user_id = :userId", userId=session["user_id"])[0]['user_hash']
    
    if request.method == "GET":
        return render_template("settings.html", userName=userName)
    else:
        # Ensure user has selected a new username as option
        if request.form.get("selectUpdate") == "changeName":
            if not request.form.get("username"):
                return apology("must provide username")
            # Ensure username NOT exists
            rows = User("SELECT * FROM users WHERE user_name = ?", request.form.get("username"))
            if len(rows) != 0:
                return apology("This username is already in use.", 403)
            userName = request.form.get("username")
            User("UPDATE users SET user_name == ? WHERE user_id == ?", userName, session["user_id"])
        
        # Ensure user has selected a new password as option
        if request.form.get("selectUpdate") == "changePwd":
            # Ensure password was submitted
            if not request.form.get("password"):
                return apology("must provide password")
            else:
                # Ensure password was confirmed
                if not request.form.get("confirmation"):
                    return apology("must confirm password")
                else:
                    # Ensure password and confirmation match
                    if request.form.get("password") != request.form.get("confirmation"):
                        return apology("passwords do not match")
                    else:
                        hashpass = generate_password_hash(request.form.get("password"))
                        User("UPDATE users SET user_hash == ? WHERE user_id == ?;", hashpass, session["user_id"])

        # No option selected - return to settings
        if request.form.get("selectUpdate") is None:
            return redirect("/settings", userName=userName)

        # All done - return to index
        flash("Your login data are successfully Updated! Please log in.")
        return redirect("/login")