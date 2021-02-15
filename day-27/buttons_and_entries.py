# create a text and a button

from tkinter import *

window = Tk()
window.title('Testing')
window.minsize(width=500, height=500)

# write a text in the window

text_label = Label(text="This is a label")
# pack up the label into the window
text_label.pack()
text_label.config(text="New text")


def got_clicked():
    # update the "text" attribute in text_label
    new_text = user_input.get()
    text_label.config(text=new_text)

# create a button and call the got_clicked function every time it gets clicked
button = Button(text="Click Me", command=got_clicked)
# pack the button into the screen
button.pack()


# Entry
user_input = Entry(window, width=20)
user_input.pack()
# answer = user_input.get()
# print(answer)



window.mainloop()