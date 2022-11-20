import requests
import smtplib

api_key = "20b7cf5bbf4817e39ddd777c83d9f548"

parameters = {
    "lat": 8.22,
    "lon": 77.41,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

responses = requests.get(
    "https://api.openweathermap.org/data/2.5/onecall",
    params=parameters)
responses.raise_for_status()
hourly_weather_data = responses.json()["hourly"]

hours = 0
hourly_weather = []
for data in hourly_weather_data:
    if hours <= 11:
        remove_list_data = data["weather"]
        hourly_weather.append(remove_list_data[0])
        hours += 1
    else:
        hours = 0
        break

will_rain = False
for data in hourly_weather:
    if data["id"] < 700:
        will_rain = True
        print("Bring an umbrella")
        break

if will_rain:
    my_email = "nandunamitfake@gmail.com"
    my_password = "lelkvrpnctmrksie"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email, to_addrs="suthishk@yahoo.com",
                            msg=f"Subject: Mazha varunne oodikko!! \n\nkuda kond po, enn mazha peyum. 8===D")
