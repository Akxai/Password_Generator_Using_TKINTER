import tkinter
from tkinter import END
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

    nr_letters = random.randint(4, 6)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    generated_password = "".join(password_list)

    password_entry.insert(0, generated_password)

    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title="ERROR", message="HEY YOU HAVE LEFT SOME FIELDS EMPTY")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"these are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {password}\nis it ok to save?")
        if is_ok:
            with open("data.txt", "a")as f:
                f.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
# window.minsize(width=500, height=500)
window.config(padx=40, pady=40)

canvas = tkinter.Canvas(width=200, height=200)
lock_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = tkinter.Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = tkinter.Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "akshay@email.com")

password_entry = tkinter.Entry(width=17)
password_entry.grid(column=1, row=3)

generate_password_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=30, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
