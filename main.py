import tkinter
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [random.choice(letters) for _ in range(random.randint(8, 10))]

    symbol_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    number_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = letters_list + symbol_list + number_list
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE AND SEARCH PASSWORD ------------------------------- #
def save():
    website = website_entry.get().lower()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Woops", message="Please don't leave any fields empty!")
    else:

        try:
            with open("data.json", mode="r") as file:
                # Reading old data
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", mode="w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")


def search():
    website = website_entry.get().lower()
    try:
        with open("data.json", "r") as data_file:
            search_data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Woops!", message="No data file found!")
    else:
        if website in data_file:
            email = search_data[website]["email"]
            password = search_data[website]["password"]
            messagebox.showinfo(title=website.title(), message=f"Email/User: {email}\nPassword: {password}\nYour password is "
                                                       f"on your clipboard.")
            pyperclip.copy(password)
        else:
            messagebox.showinfo(title="Woops!", message="There is none website with that name.\nTry to create "
                                                        "a new password.")



# ---------------------------- UI SETUP ------------------------------- #
# ------------WINDOW
window = tkinter.Tk()
window.title("Password manager")
window.minsize()
window.config(padx=50, pady=50)
# -----CANVAS
canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)
# ------Labels
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

# -----Entries
website_entry = tkinter.Entry(width=33)
website_entry.grid(column=1, row=1)

website_entry.focus()
email_entry = tkinter.Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "neroneto97@gmail.com")

password_entry = tkinter.Entry(width=33)
password_entry.grid(column=1, row=3)


# -----Buttons
password_button = tkinter.Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)
add_button = tkinter.Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)
search_button = tkinter.Button(text="Search", width=14, command=search)
search_button.grid(column=2, row=1)

window.mainloop()
