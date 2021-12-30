from flask import Blueprint
# from flask import current_app as app
from cs50 import SQL
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
from datetime import datetime


news_bp = Blueprint('news_bp', __name__)

db = SQL("sqlite:///application/market_database.db")

'''
MARKET
    coins (coin_id, symbol, name, logo_url),
    news (news_id, symbol, title, url, date, source),
    symbol#1 (symbol (id), value... date&time), symbol#2, symbol#3, symbol#4, symbol#5....
'''

#some logic to scrap google news for each coin and symbol and save at news DB.