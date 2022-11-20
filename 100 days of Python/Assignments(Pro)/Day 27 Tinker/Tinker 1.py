import tkinter

window = tkinter.Tk()
window.title("This is title")
window.minsize(500, 300)

my_label = tkinter.Label(text = "i am label", font = ("Arial", 24, 'bold'))
my_label.pack()

def button_clicked():
    print("YOU ARE A WEEEEBBBBB!")
    input2 = input1.get()
    my_label.config(text = input2)

button = tkinter.Button(text = 'WEEB CLICK ME', command = button_clicked)
button.pack()


input1 = tkinter.Entry(width = 10)
input1.pack()





window.mainloop()