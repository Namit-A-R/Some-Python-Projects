from quiz_brain import QuizBrain
from data import question_api
from QA_ui import QAUser_Interface
from Selection_ui import Selection_User_Interface


quiz = QuizBrain()
selection_quiz_ui = Selection_User_Interface(quiz)
questions_from_api = question_api(quiz)
quiz.question_data(questions_from_api)
QA_quiz_ui = QAUser_Interface(quiz)


# while quiz.still_has_questions():
#     quiz.next_question()
#
# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
