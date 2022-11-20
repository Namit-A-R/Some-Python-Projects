from question_model import Question
from data import question_data
from quiz_brain import Brain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = Brain(question_bank)

while quiz.has_questions():
    quiz.next_question()
