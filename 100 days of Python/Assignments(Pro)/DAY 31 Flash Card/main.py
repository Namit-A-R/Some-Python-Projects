from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("data/french_words.csv")
words = data.to_dict(orient="records")
current_card = {}


def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English")

def next_card():
    import random
    global current_card
    current_card = random.choice(words)
    current_word = current_card["French"]
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_word)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 48, "italic"))
card_word = canvas.create_text(400, 300, text="word", font=("Ariel", 60, "italic"))
canvas.grid(row=0, column=0, columnspan=3)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, command=next_card)
known_button.grid(row=1, column=2)

next_card()

window.mainloop()

