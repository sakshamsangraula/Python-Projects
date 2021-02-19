# Imports
from tkinter import *
import pandas
import random
# constants and global variables
BACKGROUND_COLOR = "#B1DDC6"

current_words = {}
data_dict = {}
# try to open the new updated file with remaining words and if there is an error, then catch the exception
# and open the french_words.csv original file , if the trying part works then create a list of dictionaries
# with orient="records" parameter
try:
    # get the data from the original french words file
    updated_data_frame = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data_frame = pandas.read_csv("data/french_words.csv")
    data_dict = original_data_frame.to_dict(orient="records")
else:
    data_dict = updated_data_frame.to_dict(orient="records")


# next card configurations
def next_card():
    global current_words, flip_timer
    # get a random current dictionary
    current_words = random.choice(data_dict)
    # stop the window after function each time a next card is asked so that
    # the previous 3 seconds that may not have ran because of user's excessive clicking
    # doesn't keep running and accidentally flip a card
    window.after_cancel(flip_timer)
    # change the title and text
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_words["French"], fill="black")
    # change to the front background because flipping the card turns it to a back background
    canvas.itemconfig(card_image, image=front_image)
    # set flip_timer variable to the window.after function that calls the flip_card function in 3 seconds
    flip_timer = window.after(3000, flip_card)

# if the user knows the word then call this funciton
def user_known():
    # remove the word from the list
    data_dict.remove(current_words)
    # create a new data frame from the list of dictionaries(data_dict) and convert the data frame to csv
    new_data_frame = pandas.DataFrame(data_dict)
    new_data_frame.to_csv("data/words_to_learn.csv", index=False)
    # call the next card function
    next_card()

# flip the cards automatically after some time
def flip_card():
    # change the background, title, and text
    canvas.itemconfig(card_image, image=back_image)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_words["English"], fill="white")

# Create a window
window = Tk()
window.title("Saksham Flashcard App- Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
# call the after function so that the flip card function is called after 3 seconds
flip_timer = window.after(3000, flip_card)

# Create a canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 263, image=front_image)
title_text= canvas.create_text(400, 150, text="Title", font=("Ariel", 30, "italic"))
word_text = canvas.create_text(400, 275, text="Word", font=("Ariel", 50, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Create buttons
wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_image, command=next_card)
unknown_button.grid(row=1, column=0)
right_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_image, command=user_known)
known_button.grid(row=1, column=1)

# call the next card function so that we immediately start out with the french title and word
# and not start with the default "title" text and "word" text
next_card()
window.mainloop()