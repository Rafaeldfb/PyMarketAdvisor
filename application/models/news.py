import os
from flask import Blueprint
# from flask import current_app as app
from cs50 import SQL
import sqlite3
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
        queryToSearch = 'news for ' + coin['name'] + ' ' + coin['symbol']
        result = newsapi.get_everything(
            q=queryToSearch,
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
    # insertNews()
    update = Coin("SELECT * FROM news WHERE news_symbol = ? ORDER BY news_update DESC LIMIT 1", symbol)
    
    updateDate = date.fromisoformat(update[0]['news_update']) if (len(update) >= 1) else (date.today() - timedelta(days=2))
    timeLapse = date.today() - updateDate
    
    if timeLapse > timedelta(days=1):
        insertNewNews()
        newsBySymbol(symbol)
    else:
        news = Coin("SELECT * FROM news WHERE news_symbol = ? ORDER BY news_update DESC", symbol)
        return news

# send news to database
def insertNewNews():
    rawDict = rawSearch()
    for coin in rawDict:
        results = rawDict[coin]
        # print(results)
        for result in results:
            print(coin)
            articles = result['articles']
            totalResults = result['totalResults']
            status = result['status']
            if status == 'ok' and totalResults > 0:
                for article in articles:
                    title = article['title'] if article['title'] != None else "None"
                    description = article['description'] if article['description'] != None else "None"
                    content = article['content'] if article['content'] != None else "None"
                    url = article['url'] if article['url'] != None else "None"
                    publishedAt = article['publishedAt'] if article['publishedAt'] != None else "None"
                    urlToImage = article['urlToImage'] if article['urlToImage'] != None else "None"
                    author = article['author'] if article['author'] != None else "None"
                    Coin("INSERT INTO news (news_symbol, news_header, news_desc, news_content, news_link, news_date, news_img, news_author, news_update) "
                        + "VALUES (:news_symbol, :news_header, :news_desc, :news_content, :news_link, :news_date, :news_img, :news_author, :news_update)",
                        news_symbol=coin,
                        news_header=title,
                        news_desc=description,
                        news_content=content,
                        news_link=url,
                        news_date=publishedAt,
                        news_img=urlToImage,
                        news_author=author,
                        news_update=date.today())
    return
