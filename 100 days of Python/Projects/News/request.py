from models import Articles
from models import Sources
from newsapi import NewsApiClient
from config import Config
import urllib.request,json

all_types_articles = []

def news_sorter(all_articles):

    source = []
    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []
    
    for i in range(len(all_articles)):
        
        article = all_articles[i]
        source.append(article['source'])
        title.append(article['title'])
        desc.append(article['description'])
        author.append(article['author'])
        img.append(article['urlToImage'])
        p_date.append(article['publishedAt'])
        url.append(article['url'])

        article_object = Articles(source, title, desc, author, img, p_date, url)
        all_types_articles.append(article_object)
        contents = zip(source, title, desc, author, img, p_date, url)
    
    return  contents

def publishedArticles():
    newsapi = NewsApiClient(api_key= Config.API_KEY)
    news= []
    
    #todays news

    get_articles = newsapi.get_everything(sources= 'cnn, reuters, cnbc, the-verge, gizmodo, the-next-web, techradar, recode, ars-technica')
    all_articles = get_articles['articles']
    
    output = news_sorter(all_articles)
    news.append(output)
    
    #top headlines
    
    get_articles = newsapi.get_top_headlines(sources= 'cnn, reuters, cnbc, techcrunch, the-verge, gizmodo, the-next-web, techradar, recode, ars-technica')
    all_articles = get_articles['articles']
    
    output = news_sorter(all_articles)
    news.append(output)
    
    #business articles
    
    get_articles = newsapi.get_top_headlines(category='business')
    all_articles = get_articles['articles']
    
    output = news_sorter(all_articles)
    news.append(output)
    
    #tech articles
    
    get_articles = newsapi.get_top_headlines(category='technology')
    all_articles = get_articles['articles']
    
    output = news_sorter(all_articles)
    news.append(output)
    
    #entertainment_articles
    
    get_articles = newsapi.get_top_headlines(category='entertainment')
    all_articles = get_articles['articles']
    
    output = news_sorter(all_articles)
    news.append(output)
    
    #science_articles
    
    science_articles = newsapi.get_top_headlines(category='science')
    all_articles = science_articles['articles']
    
    output = news_sorter(all_articles)
    news.append(output)
    
    #sport articles
    
    sport_articles = newsapi.get_top_headlines(category='sports')
    all_articles = sport_articles['articles']
    
    output = news_sorter(all_articles)
    news.append(output)
    
    #health articles
    
    get_articles = newsapi.get_top_headlines(category='health')
    all_articles = get_articles['articles']
    
    output = news_sorter(all_articles)
    news.append(output)
    
    return news
    

