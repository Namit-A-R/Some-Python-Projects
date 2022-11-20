import tkinter
from tkinter import *

window = tkinter.Tk()
window.minsize(500,300)
window.title("Tkinter")

my_label = Label(text = "I am a label", font = ('Arial', 24,"bold"))
my_label.grid(column = 1, row = 1)



new_button = Button(text = "New Button")
new_button.grid(column= 2, row = 3)

button = Button(text = 'click me')
button.grid(column = 2, row=2)









window.mainloop()