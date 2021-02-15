from tkinter import *

window = Tk()
window.title('Practice')
window.minsize(width=500, height=400)

# add padding to all 4 edges of the program
window.config(padx= 50, pady = 50)

label = Label(text="This is a label")
label.config(text="This is a new label")
# label.pack()
# label.place(x=200, y=175)
label.grid(row=0, column=0)
# padding around the label
label.config(padx = 50, pady = 50)

def clicked():
    print("Got clicked!")

button = Button(text="Click Me", command=clicked)
button.grid(row=1, column=1)

new_button = Button(text="New", command=clicked)
new_button.grid(row = 0, column= 2)

entry = Entry(width=10)
print(entry.get())
entry.grid(row=2, column=3)




window.mainloop()