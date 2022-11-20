

def get_news(STOCK, COMPANY_NAME):
    import requests
    import datetime
    TODAY = datetime.date.today()
    YESTERDAY = TODAY - datetime.timedelta(days=1)
    API_KEY_NEWS = "eb262594d5df4b6baf88d4494a069252"

    news_parameters = {
        "apiKey": API_KEY_NEWS,
        "q": STOCK,
        "qlnTitle": COMPANY_NAME,
        "from": YESTERDAY,
        "to": TODAY,
    }
    news_responses = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_responses.raise_for_status()

    news_articles = news_responses.json()["articles"]
    news_three_articles = news_articles[:3]

    return news_three_articles
    # count = 0
    # news_three_titles = []
    # news_three_url = []
    # for data in news_three_articles:
    #     news_three_url.append(news_three_articles[count]["url"])
    #     news_three_titles.append(news_three_articles[count]["title"])
    # news_three_titles_and_urls = {
    #     "url": news_three_url,
    #     "title": news_three_titles
    # }
    # return news_three_titles_and_urls
