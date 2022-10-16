from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    char_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    symbol_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    number_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = char_list + symbol_list + number_list
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ----------------------------search---------------------------------------#
def search():
    website = website_entry.get()
    try:
        with open("manage password.json") as password_file:
            data = json.load(password_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Opps", message=f"you dont have any saved websites yet")
    else:
        if website in data:
            searched_side = data[website]
            messagebox.showinfo(title=website,
                                message=f" Email: {searched_side['email']}\n password: {searched_side['password']}")
        else:
            messagebox.showinfo(title="Opps", message=f"no data for the site {website} exists")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password_final = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password_final,
        }
    }
    if len(website) == 0 or len(password_final) == 0:
        messagebox.showinfo(title="Oops", message="please dont leave any field empty")
    else:
        try:
            with open("manage password.json", mode="r") as password_file:
                # json.dump(new_data, password_file,indent=4)
                data = json.load(password_file)

        except FileNotFoundError:
            with open("manage password.json", "w") as password_file:
                json.dump(new_data, password_file, indent=4)
        else:
            data.update(new_data)
            with open("manage password.json", "w") as password_file:
                json.dump(data, password_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("my_password manager")
window.config(padx=50, pady=50)
image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=image, )
canvas.grid(column=1, row=0)
# ----------------------------labels ---------------------------- #
website_label = Label(text="website:")
website_label.grid(row=1, column=0, sticky="e")
email_label = Label(text="email/username:")
email_label.grid(row=2, column=0, sticky="e")
password_label = Label(text="password:")
password_label.grid(row=3, column=0, sticky="e")

# ----------------------------text inputs------------------------------------ #
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
email_entry = Entry(width=52)
email_entry.insert(0, string="nkemdiran88@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3, columnspan=2, sticky="w")
# ----------------------------buttons--------------------------------#
generate_password_button = Button(text="Generate password", width=14, command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="e", columnspan=2)
ok_button = Button(text="add", width=29, command=save)
ok_button.grid(column=1, row=4, columnspan=2, sticky="w")
search_button = Button(text="Search", width=14, command=search)
search_button.grid(column=2, row=1, sticky="e", columnspan=2)

window.mainloop()
