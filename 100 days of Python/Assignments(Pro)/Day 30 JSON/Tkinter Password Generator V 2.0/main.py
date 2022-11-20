from tkinter import *
from tkinter import messagebox
import json
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    import random
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    number_of_letters = random.randint(8, 10)
    number_of_numbers = random.randint(2, 4)
    number_of_symbols = random.randint(2, 4)
    password = ""

    for letter in range(0, number_of_letters):
        password += random.choice(letters)

    for number in range(0, number_of_numbers):
        password += random.choice(numbers)

    for symbol in range(0, number_of_symbols):
        password += random.choice(symbols)

    password = "".join(random.sample(password, number_of_symbols + number_of_numbers + number_of_letters))
    password_entry.insert(string=password, index=0)
    pyperclip.copy(password)


# ------------------------------- SEARCH METHOD --------------------------------- #
def button_search():
    website = website_entry.get()
    data = open("data.json", "r")
    data = json.load(data)
    try:
        searched_data = data[website]
    except KeyError:
        messagebox.showinfo(title="ERROR", message=f"Website '{website}' does not exist in the database")
    else:
        username = searched_data["username"]
        password = searched_data["password"]
        messagebox.showinfo(title=website, message=f"your {website} website has the following details:\n\n"
                                                   f"Username: {username}\nPassword: {password}\n\n"
                                                   f"Your password has been copied to the clipboard")
        pyperclip.copy(password)
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def button_add():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    data_dictionary = {
        website: {
            "username": username,
            "password": password
        }
    }

    if website == "" or password == "" or username == "":
        messagebox.showinfo(title="No input", message="Some fields are empty")

    else:
        confirmation = messagebox.askokcancel(title=website,
                                              message=f"These are the details entered: \nEmail: {username}"
                                                      f"\nPassword: {password} \n Is this ok to save?")
        if confirmation:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(data_dictionary)

            except FileNotFoundError:
                data = data_dictionary

            finally:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_image)
canvas.grid(column=2, row=1)

website_label = Label(text='Website: ')
website_label.grid(column=1, row=2)
website_entry = Entry()
website_entry.grid(column=2, row=2, sticky="EW")

username_label = Label(text="Username/Email: ")
username_label.grid(column=1, row=3)
username_entry = Entry()
username_entry.grid(column=2, row=3, columnspan=2, sticky="EW")
username_entry.insert(0, "nandunamit2332@gmail.com")

password_label = Label(text="Password: ")
password_label.grid(column=1, row=4)
password_entry = Entry()
password_entry.grid(column=2, row=4, sticky="EW")

generate_button = Button(text='Generate Password', command=password_generator)
generate_button.grid(column=3, row=4)
add_button = Button(text='Add', command=button_add)
add_button.grid(column=1, row=5, columnspan=3, sticky="EW")
search_button = Button(text='Search', command=button_search)
search_button.grid(column=3, row=2, sticky="EW")

window.mainloop()
