import requests
import datetime as dt

APP_ID = "5edcfe52"
APP_KEY = "68bbbb64270cdac41d5854e1cba8bef6"
url = "https://trackapi.nutritionix.com/v2/natural/exercise"

GENDER = "male"
WEIGHT_KG = 53
HEIGHT_CM = 163
AGE = 19

exercise_text = input("Tell me which exercises you did:")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    # "content-type": "application/json"
}

data = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=url, json=data, headers=headers)
response_data = response.json()
print(response_data)

datetime = dt.datetime.now()
datetime = datetime.strftime("%d/%m/%Y %H:%M:%S").split(" ")
date = datetime[0]
time = datetime[1]

for exercise in response_data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheety_url = 'https://api.sheety.co/c6dee4525185d54239747d061af7cad8/myWorkouts/workouts'

try:
    sheet_response = requests.post(sheety_url, json=sheet_inputs)
except NameError:
    pass
