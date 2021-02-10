import turtle
from states_functionality import StatesFunctionality


screen = turtle.Screen()
state_functionality = StatesFunctionality()
img = "blank_states_img.gif"
screen.title(" U.S. States Game")
screen.addshape(img)
turtle.shape(img)

# keep going until the user guesses all the 50 states
while state_functionality.get_guessed_num() < 50:
    state_chosen = screen.textinput(title=f"{state_functionality.get_score()}/50 Guess a state: ",
                                    prompt="Choose another state: ").title()

    if state_chosen == "Exit":
        break
    state_functionality.mark_states(state_chosen)


state_functionality.output_remaining_states()
# this is how the x and y coordinates were received

# def mouse_coordinates(x, y):
#     print(x, y)
#
# turtle.onscreenclick(mouse_coordinates)
