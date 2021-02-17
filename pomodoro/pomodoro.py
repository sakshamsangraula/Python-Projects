
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

from tkinter import *
import math
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    # stop the timer
    window.after_cancel(timer)
    # make the text 0:0 and change the title to Timer
    canvas.itemconfig(timer_text, text="0:00")
    title_label.config(text="Timer")

    # reset the checkmarks
    checkmark_label.config(text="")
    # set reps to 0 again
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
# create a start_timer function to start the countdown
def start_timer():
    global reps
    reps += 1
    # increment reps each time we increase timer

    working_session_sec = WORK_MIN * 60
    short_session_sec = SHORT_BREAK_MIN * 60
    long_session_sec = LONG_BREAK_MIN * 60

    # if reps is odd call with the working session sec
    if reps % 2 == 1:
        count_down(working_session_sec)
        title_label.config(text="Work", fg=GREEN)
    # if reps is divisible by 8 then call the count down function with long session break
    elif reps % 8 == 0:
        count_down(long_session_sec)
        title_label.config(text="Long Break", fg=RED)
    # if reps is even then call the count down function with short session secs
    elif reps % 2 == 0:
        count_down(short_session_sec)
        title_label.config(text="Short Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# create a countdown that changes every 1 second
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60

    # if count is less than 10 then put a value inside that single digit number
    if seconds < 10:
        seconds = f"{0}{seconds}"

    # Note: This functionality is achieved through dynamic typing in python:
    # seconds is int first then it is set to a string so it becomes a string
    # DYNAMIC TYPING IS WHEN A DATA TYPE OF THE VARIABLE CHANGES BASED ON THE CONTENT OF THE VARIABLE
    # Ex- x="hello" x is a str now and x = 10, now x is 10

    # change the text each time count down function is called
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    # call the start timer function again once count is 0
    else:
        start_timer()
        marks  = ""
        # add a checkmark for each work session
        for _ in range(math.floor(reps/2)):
            marks += "✅"
        checkmark_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

# setup the window and canvas
window = Tk()
window.title("Pomodoro")
# add padding to the window so that the tomato doesn't cover all the screen
window.config(padx=100, pady=50, bg=YELLOW)

# create the title
title_label = Label()
title_label.config(text="Timer", bg=YELLOW, font=(FONT_NAME, 50, "normal"), fg=GREEN)
title_label.grid(row=0, column=1)


# setup canvas by setting color to yellow and set highlightthickness to 0 so that the outline is not seen
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_pic)
timer_text = canvas.create_text(100, 130, text="0:00", font=(FONT_NAME, 35, "bold"))

# pack the canvas on the screen
canvas.grid(row=1, column=1)

# create the start button
start_button = Button(highlightthickness=0)
# whenever there is a command to start the button, call the start_timer function
start_button.config(text="Start", font=(FONT_NAME, 14, "normal"), command=start_timer)
start_button.grid(row=2, column=0)

# make a checkmark label

checkmark_label = Label()
checkmark_label.config(font=(FONT_NAME, 14, "normal"), bg=YELLOW, fg=GREEN)
checkmark_label.grid(row=3, column=1)



# create the Reset button
reset_button = Button()
reset_button.config(text="Reset", highlightthickness=0, font=(FONT_NAME, 14, "normal"), command=reset_timer)
reset_button.grid(row=2, column=2)

# don't let the window disappear
window.mainloop()