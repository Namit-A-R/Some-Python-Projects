from news import get_news
from stock_percentage import stock_percentage
from messaging import messaging

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_details = stock_percentage(STOCK)
percentage_difference = stock_details["percentage_difference"]
stock_price_yesterday = stock_details["stock_price_yesterday"]
stock_price_daybeforeyesterday = stock_details["stock_price_daybeforeyesterday"]

if percentage_difference >= 5 or percentage_difference <= -5:
    news_three_articles = get_news(STOCK, COMPANY_NAME)
    messaging(stock_price_yesterday, stock_price_daybeforeyesterday, STOCK, percentage_difference, news_three_articles)
