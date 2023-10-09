from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # password_list = []
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# password = ""
# for char in password_list:
#   password += char


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {website: {"email": email, "password": password}}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            website = entry_website.get().title()
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"Email: {email}\nPassword: {password}"
            )
    except KeyError:
        messagebox.showinfo(title="Error", message="No details for the website exists.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(width=220, height=220)
window.config(padx=50, pady=50)

logo_png = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_png)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

entry_website = Entry(width=21)
entry_website.grid(row=1, column=1, sticky="EW")
entry_website.focus()

entry_email = Entry(width=35)
entry_email.grid(row=2, column=1, columnspan=2, sticky="EW")
entry_email.insert(0, "jasonqxkao@gmail.com")

entry_password = Entry(width=21)
entry_password.grid(row=3, column=1, sticky="EW")

button_generate = Button(text="Generate Password", width=14, command=generate_password)
button_generate.grid(row=3, column=2, sticky="EW")

button_add = Button(text="Add", width=36, command=save)
button_add.grid(row=4, column=1, columnspan=2, sticky="EW")

button_search = Button(text="Search", width=14, command=search_password)
button_search.grid(row=1, column=2)


window.mainloop()
