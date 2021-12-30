import os
from flask import Flask, Blueprint
# from flask import current_app as app
from flask_session import Session
# from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from tempfile import mkdtemp
from application import config
from .helpers import usd, apology


# Globally accessible libraries
# db = SQLAlchemy()


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config.DevConfig)
    app.config["SESSION_FILE_DIR"] = mkdtemp()


    # Initialize Plugins
    # db.init_app(app)
    Session(app)

    with app.app_context():

        # Make sure API key for Lookup is set
        if not os.environ.get('IEX_API_KEY'):
            raise RuntimeError("IEX_API_KEY not set")

        # Include our Routes
        from .views import index, register, login, logout, settings
        from .models import users_db, criptocoins_db, news

        # Register Blueprints
        app.register_blueprint(index.index_bp)
        app.register_blueprint(register.register_bp)
        app.register_blueprint(login.login_bp)
        app.register_blueprint(logout.logout_bp)
        app.register_blueprint(settings.settings_bp)

        app.register_blueprint(users_db.users_bp)
        app.register_blueprint(criptocoins_db.criptocoins_bp)
        app.register_blueprint(news.news_bp)


        # Ensure responses aren't cached
        @app.after_request
        def after_request(response):
            response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
            response.headers["Expires"] = 0
            response.headers["Pragma"] = "no-cache"
            return response


        # Custom filter
        app.jinja_env.filters["usd"] = usd

        def errorhandler(e):
            """Handle error"""
            if not isinstance(e, HTTPException):
                e = InternalServerError()
            return apology(e.name, e.code)


        # Listen for errors
        for code in default_exceptions:
            app.errorhandler(code)(errorhandler)

    return app
