"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname('./'))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Base config."""
    # SECRET_KEY = environ.get('SECRET_KEY')
    IEX_API_KEY = environ.get('IEX_API_KEY')
    NEWS_API_KEY = environ.get('NEWS_API_KEY')
    SESSION_TYPE = 'filesystem'
    SESSION_PERMANENT = False
    # SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    DATABASE_URI = environ.get('PROD_DATABASE_URI')


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    # DATABASE_URI = environ.get('DEV_DATABASE_URI')
    # Ensure templates are auto-reloaded
    TEMPLATES_AUTO_RELOAD = True
    # database engine and configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False