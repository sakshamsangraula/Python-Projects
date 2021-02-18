# Imports
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# Constants
FONT_NAME = "Courier"
BLUE = "#add8e6"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    # randomly add letters, symbols, and numbers the number of times the loop runs based on the range
    password_list += [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]
    shuffle(password_list)

    # use the join method to create a string that has all the letters in the password list
    password = "".join(password_list)

    # insert the password in the password entry field
    password_entry.insert(0, password)

    # copy the password to clipboard using the pyperclip module
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# create a save method that gets the website info, email/username info, and password and saves it to a file
# called data.txt
def save():
    # get the info
    website_info = website_entry.get()
    email_username_info = email_username_entry.get()
    password_info = password_entry.get()
    new_data = {
        website_info: {
            "email": email_username_info,
            "password": password_info
        }
    }
    # if any of the fields are empty then tell the user to fill out all the fields
    if len(website_info) <= 0 or len(email_username_info) <= 0 or len(password_info) <= 0:
        messagebox.showinfo(title="Empty fields", message="Please don't leave any fields blank")
    else:
        # # ask the user for validation to save or cancel
        # is_ok = messagebox.askokcancel(title=website_info, message=f"Here are the details you entered:\n\n"
        #                                                            f"Website: {website_info}\nEmail/Username: {email_username_info}\nPassword: {password_info}\n"
        #                                                            f"\nIs it ok to save this information? ")
        # if is_ok:

            # write the information to a file called data.txt if the user says it's ok
            # try to read to a file and if it is not read then catch the exception


# HANDLE EXCEPTIONS
        try:
            # finished adding data to an empty file
            with open("data.json", "r") as data_file:
                    # json.dump(new_data, data_file, indent=4)
                    # read the data (becomes a dictionary after reading)
                    # reading old data
                    data = json.load(data_file)
        except FileNotFoundError:
                    # re-write the new data to the file
            with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
        else:
            # re-write the new data to the file
            with open("data.json", "w") as data_file:
                # updating old data with new data (add new data in json format)
                data.update(new_data)
                json.dump(data, data_file, indent=4)
        finally:

                # clear the existing input from the UI
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def search_password():
        try:
            # read the json data
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Search error", message="No data file found")
        else:
            website_name = website_entry.get()
            # if the website exists in data (dictionary)
            if website_name in data:
                value = data[website_name]
                messagebox.showinfo(title=website_name, message=f"Email:{value['email']}\n"
                                                                f"Password:{value['password']}")
            # Just use Else if you can - you don't have to use an exception unless you can't use
            # if else to catch it and must use an exception to catch it like a file error
            else:
                messagebox.showinfo(title="Search error", message=f"{website_name}'s data does not exist")


# ---------------------------- UI SETUP ------------------------------- #

# set up the window
window = Tk()
window.title('Password Manager')
# specify padding in window by using the config method
window.config(bg="#add8e6", padx=40, pady=40)

# create a canvas
canvas = Canvas(width=200, height=200, bg=BLUE, highlightthickness=0)
# include a image in the canvas
lock_img = PhotoImage(file="logo.png")
# specify the image's x center, and y center - which I made as the half of the width and height
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# setup labels
website_label = Label(text="Website:", bg=BLUE)
website_label.grid(row=1, column=0)
email_username_label = Label(text="Email/Username:", bg=BLUE)
email_username_label.grid(row=2, column=0)
password_label = Label(text="Password:", bg=BLUE)
password_label.grid(row=3, column=0)

# setup entries
website_entry = Entry(width=33)
# focus on the website entry
website_entry.focus()
website_entry.grid(row=1, column=1)
email_username_entry= Entry(width=52)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "saksham@email.com")
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

# setup buttons
# each time generate password button is called, command (call) the random password function
generate_button = Button(text="Generate Password", command=random_password)
generate_button.grid(row=3, column=2)
# each time add button is clicked, command the save function
add_button = Button(text="Add", width=44, command=save)
# make sure the add button spans two rows
add_button.grid(row=4, column=1, columnspan=2)

# each time search button is clicked, call the search function
search_button = Button(text="Search", command=search_password, width=14)
search_button.grid(row=1, column=2)


# don't let the window disappear
window.mainloop()