# Constants
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

# Imports
from tkinter import *
import pandas
import random

################################ Implementing Functionality ########################

current_cards = {}

# try reading from the updated csv file, if the updated csv file doesn't exist then read from the original file
try:
    df = pandas.read_csv("./data/words_to_learn.csv")
except:
    old_df = pandas.read_csv("./data/french_words.csv")
    df_list = old_df.to_dict(orient="records")
else:
    df_list = df.to_dict(orient="records")


def next_word(*args):
    global flipping_timer
    global current_cards
    # cancel the flipping timer each time we click on the button and only start it after we pick a new word
    window.after_cancel(flipping_timer)
    current_cards = random.choice(df_list)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_cards["French"], fill="black")
    canvas.itemconfig(canvas_image, image=front_img)
    # flip the card after 3 milliseconds by calling the flip card function
    flipping_timer = canvas.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_cards["English"], fill="white")
    # cancel the flipping timer after one flip so that the user can go to the next card

def know_word():
    # remove the card from the list
    df_list.remove(current_cards)
    # create a new data frame and write the unknown words to csv
    df_new = pandas.DataFrame(df_list)
    df_new.to_csv("data/words_to_learn.csv", index=False)

    # call the next word function to move to the next card
    next_word()

################################ Create the UI ######################################

# create the window
window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# put after function after the window creation
flipping_timer = window.after(3000, flip_card)

# create a canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
# write the title on the canvas
title_text = canvas.create_text(400, 150, text="", font=(FONT_NAME, 30, "italic"))
# write the word on the canvas
word_text = canvas.create_text(400, 263, text="", font=(FONT_NAME, 50, "bold"))
# make sure the flashcard image is spanning 2 columns
canvas.grid(row=0, column=0, columnspan=2)

# create the wrong and check buttons
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_word)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=know_word)
right_button.grid(row=1, column=1)

# call the next word function before the screen refreshes with mainloop
next_word()

# make sure the window doesn't disappear
window.mainloop()