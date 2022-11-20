
def messaging(stock_price_yesterday, stock_price_daybeforeyesterday, STOCK, percentage_difference, news_three_articles):
    from twilio.rest import Client
    import smtplib

    VIRTUAL_TWILIO_NUMBER = "+15153033945"
    VERIFIED_NUMBER = "+917306120430"
    TWILIO_SID = "ACf4ba62931331aa329be32e56e2f0b2fa"
    TWILIO_AUTH_TOKEN = "26164419ffda58ae29f44e9fa725fd9b"

    difference = float(stock_price_yesterday) - float(stock_price_daybeforeyesterday)

    if difference > 0:
        up_down = "🔺"
    else:
        up_down = "🔻"

    formatted_articles = [
        f"{STOCK}: {up_down}{percentage_difference}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
        for article in news_three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    my_email = "nandunamitfake@gmail.com"
    my_password = "lelkvrpnctmrksie"

    for article in formatted_articles:
        client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.sendmail(from_addr=my_email, to_addrs="suthishk@yahoo.com",
                                msg=article)
