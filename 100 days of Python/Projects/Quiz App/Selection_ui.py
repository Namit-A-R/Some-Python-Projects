from tkinter import *
from QA_ui import QAUser_Interface
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Selection_User_Interface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.root = Tk()
        self.root.title("Quizzler")
        self.root.config(padx=20, pady=20, bg=THEME_COLOR)

        self.clicked = StringVar()
        self.clicked.set("Random")
        self.root_label = Label(text="Select the type of quiz", fg="white", bg=THEME_COLOR, )
        self.root_label.grid(row=0, column=0)

        self.quiz_type_selection_list = OptionMenu(self.root, self.clicked, "Random", "Computer Science", "Animals",
                                                   "Anime and Manga", "Vehicles")
        self.quiz_type_selection_list.grid(row=2, column=0)

        self.submit_button = Button(text="Submit", fg="white", bg=THEME_COLOR, command=self.final_submission)
        self.submit_button.grid(row=3, column=0)
        self.root.mainloop()

    def final_submission(self):
        selection = self.clicked.get()
        self.quiz.quiz_type(selection)
        self.root.quit()
        self.root.destroy()
