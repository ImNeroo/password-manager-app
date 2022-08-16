import tkinter
from tkinter import messagebox
import random
import pyperclip


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


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Woops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\n"
                                                              f"Password: {password}\n Is it ok to save?")
        if is_ok:
            with open("saved_passwords.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")


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
website_entry = tkinter.Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2)

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

window.mainloop()
