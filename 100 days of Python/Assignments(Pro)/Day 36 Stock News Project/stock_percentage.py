
def stock_percentage(STOCK):
    import requests
    API_KEY_ALPHA = "3ITRE358XSR075RB"

    alpha_parameters = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK,
        "outputsize": "compact",
        "apikey": API_KEY_ALPHA
    }
    alpha_response = requests.get(url="https://www.alphavantage.co/query", params=alpha_parameters)
    alpha_response.raise_for_status()
    alpha_data = alpha_response.json()["Time Series (Daily)"]

    stock_details_daily = []
    for count in range(0, 2):
        stock_details_daily.append(list(alpha_data.items())[count][1])

    stock_price_yesterday = float(stock_details_daily[0]["4. close"])
    stock_price_daybeforeyesterday = float(stock_details_daily[1]["4. close"])

    percentage_difference = 5
    stock_details = {
        "percentage_difference": percentage_difference,
        "stock_price_yesterday": stock_price_yesterday,
        "stock_price_daybeforeyesterday": stock_price_daybeforeyesterday
    }
    return stock_details
