# A decorator function wraps around a function and gives that function
# more functionality before or after or modifies it like running the function multiple times
#
# import time
#
# def delay_decorator(print_function):
#     def wrapper_function():
#         time.sleep(5)
#         print_function()
#         print_function()
#         print_function()
#
#     return wrapper_function
#
# @delay_decorator
# def say_hi():
#     print("Hi Hi Hi")
#
# @delay_decorator
# def say_bye():
#     print("Bye bye bye")
#
# say_hi()
# say_bye()
#


# Modifying basic flask application

from flask import Flask
app = Flask(__name__)

# Flask decides that if it sees / then it will call the hello world function
# with changes or modifications based on the app.route decorator
@app.route('/')
def hello_world():
    return 'Hello, Saksham!'

@app.route("/saksham")
def introduce_saksham():
    return "My name is Saksham!"


# name refers to the name of the class/function etc
if __name__ == "__main__":
    app.run()
