from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class User_Interface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.wrong_label = Label(text="Wrong Answers: 0", fg="white", bg=THEME_COLOR)
        self.wrong_label.grid(row=0, column=0)

        self.score_label = Label(text="Score: ", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="some random text", width=290, fill=THEME_COLOR,
                                                     font=("MV Boli", 20, "italic"))

        self.get_next_question()

        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.wrong_label.config(text=f"Wrong Answers: {self.quiz.wrong}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz. "
                                                            f"your final score is: {self.quiz.score}")

    def true_pressed(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if self.quiz.still_has_questions():
            if is_right:
                self.canvas.config(bg="green")
            if not is_right:
                self.canvas.config(bg="red")

        self.window.after(500, self.get_next_question)