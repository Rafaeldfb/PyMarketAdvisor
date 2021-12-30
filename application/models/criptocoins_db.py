from flask import Blueprint
from flask import current_app as app
from cs50 import SQL
# from datetime import datetime


# define user models
criptocoins_bp = Blueprint('criptocoins_bp', __name__)

# db = SQLAlchemy()
db = SQL("sqlite:///application/market_database.db")

'''
MARKET
    coins (coin_id, symbol, name, logo_url),
    news (news_id, symbol, title, url, date, source),
    symbol#1 (symbol (id), value... date&time), symbol#2, symbol#3, symbol#4, symbol#5....
'''
def coinById(coin_id):
    """return coin by id"""
    return Coin("SELECT * FROM coins WHERE coin_id = ?", coin_id)

def coinBySymbol(symbol):
    """return coin by symbol"""
    return Coin("SELECT * FROM coins WHERE symbol = ?", symbol.upper())

def coinLogoBySymbol(symbol):
    """return coin logo by symbol"""
    return Coin("SELECT logo FROM coins WHERE symbol = ?", symbol.upper())

def Coin(*args, **kwargs):
    """return db.execute(query) from criptos database, if Coin(None)'s query is None, return None"""
    if len(args) > 0 and len(kwargs) > 0:
        return db.execute(*args, **kwargs)

    elif len(args) > 0 and len(kwargs) == 0:
        return db.execute(*args)

    else:
        return None