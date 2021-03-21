from flask import Flask

app = Flask(__name__)

# decorators to make texts bold, italics, and underlined by adding html tags to content
# in the function

def make_bold(function_name):
    def wrapper_function():
        # get the content of the function by calling the function and modify the content
        content = function_name()
        bolded_content = f'<strong> {content} </strong>'
        return bolded_content
    return wrapper_function

def make_italics(function_name):
    def wrapper_function():
        # get the content of the function by calling the function and modify the content
        content = function_name()
        italics_content = f"<em>{content}</em>"
        return italics_content
    return wrapper_function

def make_underlined(function_name):
    def wrapper_function():
        # get the content of the function by calling the function and modify the content
        content = function_name()
        underlined_content = f'<u> {content} </u>'
        return underlined_content
    return wrapper_function


# return HTML elements using flask
@app.route('/')
def hello_world():
    return '<h1 style="text-align: center"> Hello Saksham!</h1>' \
           '<p> This is a simple website about me.</p>' \
           '<img src="https://legacyneuro.com/wp-content/uploads/2017/10/Teddy.jpg" ' \
           'width=500 alt="TR Pic">' \
           '<img src="https://media.giphy.com/media/3o7TKTxeQEKMD1POUg/giphy.gif" alt="gif">'


@app.route('/bye')
@make_underlined
@make_bold
@make_italics
def bye():
    return 'Bye!'

# get the user entered name, and number, and path from the url
# RETURN FROM THE FUNCTION!! RETURN RETURN RETURN
@app.route('/username/<string:name>/<int:age>/<path:website_name>')
def get_user_info(name, age, website_name):
    return (f"Hello {name}, you are {str(age)} years old!"
          f"And your website, {website_name} is pretty good!")

# name refers to the name of the class/function etc
if __name__ == "__main__":
    # set debug to True so that the server automatically reloads when we update and
    # save our code
    app.run(debug=True)