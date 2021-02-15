import tkinter

# create a window from tkinter
window = tkinter.Tk()
window.title("Saksham Tkinter Program")
window.minsize(width=500, height=300)

# write to the screen
my_label = tkinter.Label(text="Je suis un label")

# pack the label to the screen
my_label.pack()



# make sure that the window doesn't disappear
window.mainloop()


# create function with default values using the turtle class :)
# Some functions have default arguments so we don't have to pass anything if we just wanna use the default,
# but we will have to pass in new arguments if we want to override the default
# import turtle
# tim = turtle.Turtle()
# tim.write("Hello", font=("Arial", 80, "bold"))
# turtle.mainloop()