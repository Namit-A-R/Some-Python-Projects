import html
from question_model import Question


class QuizBrain:

    def __init__(self):
        self.question_list = []
        self.question_number = 0
        self.score = 0
        self.wrong = 0
        self.current_question = None
        self.type = ""

    def question_data(self, questions_from_api):
        question_bank = []
        for question in questions_from_api:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            question_bank.append(new_question)
        self.question_list = question_bank

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {html.unescape(self.current_question.text)}"
        # user_answer = input(f"Q.{self.question_number}: {html.unescape(self.current_question.text)} (True/False): ")
        # self.check_answer(user_answer)

    def check_answer(self, user_answer):
        if self.still_has_questions():
            correct_answer = self.current_question.answer
            if user_answer.lower() == correct_answer.lower():
                self.score += 1
                print("You got it right!")
                print(f"Your current score is: {self.score}/{self.question_number}")
                print("\n")
                return True
            else:
                self.wrong += 1
                print("That's wrong.")
                print(f"Your current score is: {self.score}/{self.question_number}")
                print("\n")
                return False

    def quiz_type(self, selection):
        self.type = selection
