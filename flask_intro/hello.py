from flask import Flask
app = Flask(__name__)

# import random
# print(random.__name__)

@app.route('/')
def hello_world():
    return 'Hello, Saksham!'


# name refers to the name of the class/function etc
if __name__ == "__main__":
    app.run()
