from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# --------------------------- SEARCH PASSWORD ------------------------------ #
def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
        messagebox.showinfo(title=website, message=f"Email: {data[website]["email"]}"
                                                   f"\nPassword: {data[website]["password"]}")
    except FileNotFoundError:
        messagebox.showwarning(title=website, message="No Data File found")
    except KeyError:
        messagebox.showwarning(title=website, message="No details for the website exists")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    warning_message = ""
    if len(website) < 1 or len(password) < 1:
        if len(website) == 0:
            warning_message += "Website not entered"
        if len(password) == 0:
            warning_message += "\nPassword not entered"
        messagebox.showwarning(title="Oops", message=warning_message)
    else:
        try:
            with open("data.json", "r") as data_file:
                # read old data
                data = json.load(data_file)
                # update old data with new data
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # update new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPass")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# labels

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# entries

website_entry = Entry(width=33)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "dhesika@gmail.com(dummy)")
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

# buttons

search_button = Button(text="Search", width=15, command=search)
search_button.grid(row=1, column=2)

generate_password_button = Button(text="Generate Password", width=15, command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
