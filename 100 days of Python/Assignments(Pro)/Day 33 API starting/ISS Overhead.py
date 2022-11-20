import time
import requests
import datetime
import smtplib

my_lat = 8.524139
my_long = 76.936638


def is_night():
    parameters = {
        "lat": my_lat,
        "lng": my_long,
        "formatted": 0
    }

    responses_latlng = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    responses_latlng.raise_for_status()

    latlng_data = responses_latlng.json()

    sunrise_time = latlng_data["results"]["sunrise"].split('T')[1].split(':')[0]
    sunset_time = latlng_data["results"]["sunset"].split('T')[1].split(':')[0]
    time_now = datetime.datetime.now().hour

    if time_now >= sunset_time or time_now <= sunrise_time:
        return True


def is_overhead():
    responses_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    responses_iss.raise_for_status()

    iss_data = responses_iss.json()
    iss_latitude = iss_data["iss_position"]["latitude"]
    iss_longitude = iss_data["iss_position"]["longitude"]

    if my_lat - 5 <= iss_latitude <= my_lat + 5 and my_long - 5 <= iss_longitude <= my_long + 5:
        return True


while True:
    time.sleep(60)
    if is_overhead() and is_night():
        my_email = "nandunamit2332fake@gmail.com"
        my_password = "mrpoikzvpmxfkehv"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="nandunamit2332@gmail.com",
                                msg="Subject: ISS Overhead\n\n Look up BITCH!!")
