import requests
import datetime

PIXELA_USER_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "nandunamit"
USERNAME = "namit"
PIXELA_USER_PARAMETERS = {
    "token": "nandunamit",
    "username": "namit",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

PIXELA_HEADER = {
    "X-USER-TOKEN": TOKEN
}
PIXELA_GRAPH_CONFIG = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ichou"
}
PIXELA_GRAPH_ENDPOINT = f"https://pixe.la/v1/users/{USERNAME}/graphs"
date = datetime.date.today()
PIXELA_GRAPH_INSERT_ENDPOINT = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1"
PIXELA_GRAPH_INSERT_PARAMETERS = {
    "date": "20211009",
    "quantity": "20.8"
}

response = requests.post(url=PIXELA_GRAPH_INSERT_ENDPOINT, json= PIXELA_GRAPH_INSERT_PARAMETERS, headers=PIXELA_HEADER)
print(response.text)