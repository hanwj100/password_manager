from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from pyperclip import copy

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    """generates a random password including letters, symbols, and numbers, then copies the new password to clipboard"""
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbol + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    copy(password)
    # ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """[Checks for whether the website exists within .txt file, asks the user to confirm the information, then
    stores the values inside each entry box in .txt file"""
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if 0 in {len(website), len(email), len(password)}:
        messagebox.showinfo(title="Error Message", message=f"All fields are required to be completed")
    else:
        # TODO 1 Check for whether the website already exists within the stored passwords
        # Message box to confirm whether the information is correct
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n\n"
                                                      f"Email/Username: {email}\n"
                                                      f"Password: {password}\n\n"
                                                      f"Is it ok to save?")
        if is_ok:
            # Save data to txt file
            with open("saved_passwords.txt", 'a') as f:
                f.write(f"{website.ljust(30)} | {email.ljust(30)} | {password.ljust(30)}\n")

            # Clear entry boxes
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky=EW)
website_entry.focus()
email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky=EW)
password_entry = Entry()
password_entry.grid(row=3, column=1, sticky=EW)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW)

window.mainloop()