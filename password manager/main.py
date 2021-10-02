
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password():

    import random
    entry_password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():

    website = entry_website_name.get()
    email = entry_email_username.get()
    password = entry_password.get()

    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showinfo(message="FIELDS CANNOT BE EMPTY")

    else:
        is_ok = messagebox.askokcancel(title="CONFIRMATION", message=f"details entered are: \nEmail: {email}\nPassword: {password}")
        if is_ok:
            with open("passwords.txt", "a") as passwords_file:

                entry_website_name.delete(0, END)
                entry_email_username.delete(0,END)
                entry_password.delete(0,END)
                passwords_file.write(f"{website} | {email} | {password} \n")

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip

window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
img1 = PhotoImage(file="logo.png")
canvas.create_image( 100, 100, image=img1)
canvas.grid(row=0, column=1)

label_website_name = Label(text="WEBSITE")
label_website_name.grid(row=1, column=0)
label_email_username = Label(text="EMAIL/USERNAME")
label_email_username.grid(row=2, column=0)
label_password = Label(text="PASSWORD")
label_password.grid(row=3,column=0)

entry_website_name = Entry(width=56)
entry_website_name.grid(row=1, column=1, columnspan=2)
entry_website_name.focus()
entry_email_username = Entry(width=56)
entry_email_username.grid(row=2, column=1, columnspan=2)
entry_password = Entry(width=33)
entry_password.grid(row=3, column=1) 

button_generate_password = Button(text="GENERATE PASSWORD", width=18, command=password)
button_generate_password.grid(row=3, column=2)
button_add = Button(text="ADD", width=47, command=add)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()