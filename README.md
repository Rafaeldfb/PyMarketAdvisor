# PyMarketAdivisor
A simple market advisor based on sentiment analysis from market news.

Target Functionality:
A web app that shows a card for each stock/cripto with ordinary market data plus indicators built with IA and web Screpped news.

Dependencies:
python 3
request
flask
SQLite 3
beautyfulsoup 4
sklearn


about API for news:
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