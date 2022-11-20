import requests

def question_api(quiz):
    if quiz.type == "Random":
        data = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
        data.raise_for_status()
    elif quiz.type == "Computer Science":
        data = requests.get("https://opentdb.com/api.php?amount=10&category=18&type=boolean")
        data.raise_for_status()
    elif quiz.type == "Animals":
        data = requests.get("https://opentdb.com/api.php?amount=10&category=27&type=boolean")
        data.raise_for_status()
    elif quiz.type == "Anime and Manga":
        data = requests.get("https://opentdb.com/api.php?amount=10&category=31&type=boolean")
        data.raise_for_status()
    elif quiz.type == "Vehicles":
        data = requests.get("https://opentdb.com/api.php?amount=10&category=28&type=boolean")
        data.raise_for_status()
    else:
        data = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
        data.raise_for_status()

    question_data = data.json()['results']
    return question_data
