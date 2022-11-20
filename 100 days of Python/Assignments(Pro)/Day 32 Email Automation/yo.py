import datetime as dt
import pandas as pd
import smtplib
import random

now = dt.datetime.now()
today_day = now.day
today_month = now.month
my_email = "nandunamitfake@gmail.com"
my_password = "mrpoikzvpmxfkehv"


dt = pd.read_csv("birthdays.csv", usecols=["name", "email", "year", "month", "day"])
print(dt)
birthdays_dict = dt.to_dict(orient="records")
print(birthdays_dict)


for n in range(0, len(birthdays_dict)):
    if birthdays_dict[n]["month"] == today_month:
        name_of_friend = birthdays_dict[n]["name"]
        email_of_friend = birthdays_dict[n]["email"]


        with open(f"letter_templates/letter_{random.randint(1,3)}.txt", "r") as l:
            letter = l.read()
            letter = letter.replace("[NAME]", name_of_friend)
            letter = letter.replace("Angela", "Namit") 

        #sending email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=email_of_friend,
                                msg=f"Subject: Happy Birthday!! {name_of_friend}\n\n{letter}")

