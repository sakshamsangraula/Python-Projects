# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repetition = 0
timer = 0

# imports
from tkinter import *
import math


############################## Reset Timer ###############3
def reset_timer():
    # stop the clock
    window.after_cancel(timer)
    # change the clock to 0:00
    canvas.itemconfig(timer_text, text="0:00")
    # reset the checkmarks
    checkmark_label.config(text="")
    # change the title text to Timer
    title_label.config(text="Timer", fg=GREEN)
    # reset repetition to 0
    global repetition
    repetition = 0

##############################  Start Timer ########################
def start_timer():
    global repetition
    repetition += 1

    # call the count down function based on what the state is
    if repetition % 2 == 1:
        count_down(WORK_MIN * 60)
        title_label.config(text="Work", fg=GREEN)
    elif repetition % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Long Break", fg=RED)
    elif repetition % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Short Break", fg=PINK)

############################### Countdown ###################################
def count_down(count):
    # get the number of minutes and seconds from the overall seconds count passed in
    num_mins = math.floor(count / 60)
    num_secs = count % 60

    if num_secs < 10:
        num_secs = f"0{num_secs}"

    canvas.itemconfig(timer_text, text=f"{num_mins}:{num_secs}")
    # create a timer that counts down every 1 second if the count is greater than 0
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    # once a work or long break or short break is complete (meaning count is 0), re-start the timer
    else:
        start_timer()
        # loop through all the work sprints and add checkmarks for each sprint
        # use a loop so that all the checkmarks are counted and shown
        global repetition
        marks = ""
        # floor of the half of the spring is the actual work
        work_sprints = math.floor(repetition / 2)
        for _ in range(work_sprints):
        # if repetition % 2 == 0:
        #     checkmark_label.config(text="✔")
            marks+="✔"
        checkmark_label.config(text=marks)

####################################### UI #####################################

# Create the UI
window = Tk()
window.title("Saksham's Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

# put a canvas in the window
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_pic)
# write on the tomato
timer_text = canvas.create_text(100, 135, text="0:00", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

# create a title on the window
title_label = Label()
title_label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "normal"), bg=YELLOW, highlightthickness=0)
title_label.grid(row=0, column=1)

# create a start button on the window and start the timer every time the start button is clicked
start_button = Button()
start_button.config(text="Start", font=(FONT_NAME, 18, "normal"), highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

# create a checkmark
checkmark_label = Label()
checkmark_label.config(text="", font=(FONT_NAME, 15, "normal"), fg=GREEN, highlightthickness=0, bg=YELLOW)
checkmark_label.grid(row=3, column=1)

# create a reset button on the window and call the reset timer function to reset the timer once clicked
reset_button = Button()
reset_button.config(text="Reset", font=(FONT_NAME, 18, "normal"), highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# make sure the window doesn't disappear
window.mainloop()


