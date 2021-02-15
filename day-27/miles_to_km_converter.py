from tkinter import *

# create a window with appropriate properties
window = Tk()
window.title("Saksham miles to km converter")
window.minsize(width=500, height=500)

entry = Entry(width=10)
entry.grid(row=0, column=1)

label_miles = Label(text="Miles")
label_miles.grid(row=0, column=2)

label_equal = Label(text="is equal to")
label_equal.grid(row=1, column=0)

label_zero = Label()
label_zero.config(text="0")
label_zero.grid(row=1, column=1)

label_km = Label()
label_km.config(text="Km")
label_km.grid(row=1, column=2)

def calculate_km():
    km = round(float(entry.get()) * 1.609, 2)
    label_zero.config(text=f"{km}")

button = Button()
# whenever this button is clicked, call the calculate_km function
button.config(text="Calculate", command=calculate_km)
button.grid(row=2, column=1)

# don't let the window disappear
window.mainloop()