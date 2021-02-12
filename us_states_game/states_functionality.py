from turtle import Turtle
import pandas


class StatesFunctionality(Turtle):

    def __init__(self):
        super().__init__()
        # state functionality has states/works with states
        self.state = Turtle()
        self.state.hideturtle()
        self.state.penup()
        self.states_data = pandas.read_csv("50_states.csv")
        self.x_values_list = self.states_data["x"]
        self.y_values_list = self.states_data["y"]
        self.states = self.states_data["state"]
        self.guessed_states = []
        self.score = 0

    def mark_states(self, chosen_state):
        # if it is then write the text at that location and increase the score using scoreboard class
        # loop through the states
        for index in range(0, len(self.states)):
            state = self.states[index]
            if state == chosen_state.title():
                self.guessed_states.append(state)
                self.score += 1
                x_pos = self.x_values_list[index]
                y_pos = self.y_values_list[index]
                self.state.goto(x_pos, y_pos)
                self.state.write(f"{state}")

    def get_score(self):
        return self.score

    def get_guessed_num(self):
        return len(self.guessed_states)

    def output_remaining_states(self):
        # output a text file that has all the states the user missed
        # loop through all the states and if they are not in the guessed states list then write it to a file
        missing_states = [ state for state in self.states if state not in self.guessed_states]


        # create a new dataframe and output to a file
        df = pandas.DataFrame(missing_states)
        df.to_csv("missing_states_list.csv")
