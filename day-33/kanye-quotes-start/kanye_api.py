from tkinter import *
import requests

def get_quote():
    # get the quote from kanye api and write it on the screen
    kanye_quote_response = requests.get("https://api.kanye.rest/")
    # raise an exception if there are any errors and we don't get a 200 status code
    kanye_quote_response.raise_for_status()
    kanye_quote_response = kanye_quote_response.json()
    kanye_quote = kanye_quote_response["quote"]
    canvas.itemconfig(kanye_quote_text, text=kanye_quote)

# setup UI
window = Tk()
window.title("Kanye's quotes")
window.config(padx=50, pady=50)

canvas = Canvas(width=500, height=500)
background_image = PhotoImage(file="background.png")
canvas.create_image(250, 250, image=background_image)
# set a width while creating the text so that the text wraps in the width and doesn't go over horizontally
kanye_quote_text = canvas.create_text(250, 250, text="Kanye Says....", font=("Ariel", 15, "bold"), width=250)
canvas.grid(row=0, column=0)

button_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=button_img, highlightthickness=0)
kanye_button.config(command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()