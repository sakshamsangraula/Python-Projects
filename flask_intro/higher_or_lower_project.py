from flask import Flask
import random

app = Flask(__name__)

# create a decorator that adds h1 tags to the content of a function used with the
# decorator
def add_h1s(func):
    def wrapper():
        content = func()
        content_with_h1 = f'<h1> {content} </h1>'
        return content_with_h1
    return wrapper

random_num = random.randint(0, 9)

# if the user enters the correct answer then congratulate them
@app.route('/<int:user_input>')
def show_results(user_input):
    if user_input == random_num:
        return "<h1 style=color: green> You got it right! </h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'" \
               "alt='correct_guess_gif'>"
    elif user_input < random_num:
        return "<h1 style=color:orange> Too low </h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'" \
               "alt='lower_guess_gif'>"
    else:
        return "<h1 style=color: red> Too high </h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'" \
               " alt='higher_guess_gif'>"


# if the user enters a lower answer then tell them it's too low


# if the user enters a higher answer then tell them it's too high

@app.route('/')
# @add_h1s
def guess_number():
    return "<h1 style=color:blue> Guess a number between 0 and 9<h1>" \
           "<br><br>" \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">' \


if __name__ == "__main__":
    # run the app in debug mode so that the server reloads after update and save
    app.run(debug=True)

