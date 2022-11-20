from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_box = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global check_box
    global timer

    reps = 0
    check_box = ""
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="TIMER")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global check_box
    reps += 1

    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    work_sec = WORK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_secs)
        timer_label.config(text="Ahh Banana Umm")
    elif reps % 2 == 0:
        count_down(short_break_secs)
        timer_label.config(text="Tea Break", fg=GREEN)
    else:
        count_down(work_sec)
        timer_label.config(text="Work Bitch", fg=PINK)
        if reps % 2 == 0:
            check_box += "✔"
            checkbox_label.config(text=check_box)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer

    minutes = str(int(count / 60)).zfill(2)
    seconds = str(count - int(minutes) * 60).zfill(2)
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count >= 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
tomato_img = PhotoImage(file='tomato.png')
window.config(padx=100, pady=50, bg='#f7f5dd')

timer_label = Label(text='TIMER')
timer_label.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, 'bold'))
timer_label.grid(column=2, row=1)

canvas = Canvas(width=202, height=224, bg='#f7f5dd', highlightthickness=0)
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(102, 132, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=2, row=2)

start_button = Button(text='start', highlightthickness=0, bg=YELLOW, command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="reset", highlightthickness=0, bg=YELLOW, command=reset_timer)
reset_button.grid(column=3, row=3)

checkbox_label = Label(text=check_box)
checkbox_label.grid(column=2, row=4)

window.mainloop()
