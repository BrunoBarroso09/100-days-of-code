from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

def generate_password():
    input_password.delete(0, "end")
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password = [choice(alphabet) for _ in range(randint(8,10))]
    password += [choice(numbers) for _ in range(randint(2,4))]
    password += [choice(symbols) for _ in range(randint(2,4))]

    shuffle(password)
    password = "".join(password)

    #Copy to Clipboard
    pyperclip.copy(password)

    input_password.insert(0, password)

def save_information():
    website = input_website.get()
    email = input_email_user.get()
    password = input_password.get()
    if website == "" or email == "" or password == "":
        messagebox.showwarning(title="Empty fields", message="Please don't leave any empty fields")

    messagebox.showwarning(title="Password Manager",
    message=f"Email: {email}, Password: {password} \n Is this ok?")

    with open("password.txt", mode="a") as file:
        file.write(f"{website} | {email} | {password} \n")

window = Tk()
window.title("Password Manager")
window.config(padx=25, pady=25, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_png)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:", font=("Courier", 18, "bold"), fg="black", bg="white")
label_website.grid(column=0, row=1)

input_website = Entry(width=35)
input_website.config(fg="black", bg="white", highlightthickness=0)
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()

label_email_user = Label(text="Email/Username:", font=("Courier", 18, "bold"), fg="black", bg="white")
label_email_user.grid(column=0, row=2)

input_email_user = Entry(width=35)
input_email_user.config(fg="black", bg="white", highlightthickness=0)
input_email_user.grid(column=1, row=2, columnspan=2)
input_email_user.insert(0, "peter@email.com")

label_password = Label(text="Password:", width=21, font=("Courier", 18, "bold"), fg="black", bg="white")
label_password.grid(column=0, row=3)

input_password = Entry(width=22)
input_password.config(fg="black", bg="white", highlightthickness=0)
input_password.grid(column=1, row=3)

gen_password = Button(text="Generate Password", width=21, command=generate_password)
gen_password.config(fg="black", bg="white", highlightthickness=0)
gen_password.grid(column=2, row=3, columnspan=2)

add_button = Button(text="Add", width=36, fg="black", bg="white", command=save_information)
add_button.config(fg="black", bg="white", highlightthickness=0)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()