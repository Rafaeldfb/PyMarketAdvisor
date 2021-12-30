import os
from flask import Blueprint
# from flask import current_app as app
from cs50 import SQL
from .criptocoins_db import Coin
from urllib.request import Request, urlopen
# from bs4 import BeautifulSoup
from newsapi import NewsApiClient
import requests
from datetime import datetime, date, timedelta


news_bp = Blueprint('news_bp', __name__)

db = SQL("sqlite:///application/market_database.db")

'''
MARKET
    coins (coin_id, symbol, name, logo_url),
    news (news_id, symbol, title, url, date, source),
    symbol#1 (symbol (id), value... date&time), symbol#2, symbol#3, symbol#4, symbol#5....
'''

# Init
newsapi = NewsApiClient(api_key=os.environ.get('NEWS_API_KEY'))


#      Setting up search parameters and variables
def rawSearch():
    coins = Coin("SELECT name, symbol FROM coins;")

    today = date.today()
    yesterday = today - timedelta(days=1)
    results = []
    raw_results = {}
    for coin in coins:
        result = newsapi.get_everything(
            q=coin['symbol']+coin['name'],
            from_param=yesterday,
            to=today,
            language='en',
            sort_by='relevancy',
            page=1
        )
        results.append(result)
        raw_results[coin['symbol']] = results
    return raw_results


def newsBySymbol(symbol):
    news = []
    for i in rawSearch()[symbol]:
        for j in i['articles']:
            news.append(j)
    return news





# # /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(
#     q='bitcoin',
#     sources='bbc-news,the-verge',
#     category='business',
#     language='en',
#     country='us'
# )

# # /v2/everything
# all_articles = newsapi.get_everything(
#     q='bitcoin',
#     sources='bbc-news,the-verge',
#     domains='bbc.co.uk,techcrunch.com',
#     from_param='2017-12-01',
#     to='2017-12-12',
#     language='en',
#     sort_by='relevancy',
#     page=2
# )

# # /v2/top-headlines/sources
# sources = newsapi.get_sources()