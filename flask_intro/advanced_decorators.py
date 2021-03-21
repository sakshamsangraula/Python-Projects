#
#
# class User:
#
#     def __init__(self, user_name):
#         self.name = user_name
#         self.logged_in = False
#
# # DON'T USE SELF WHEN CREATING A DECORATOR FUNCTION
#     def authentication_check(function_name):
#         # get the function parameters using args and kwargs
#         def wrapper(*args, **kwargs):
#             user = args[0]
#             if user.logged_in == True:
#                 function_name(user)
#             else:
#                 print("Not authenticated")
#         return wrapper
#
#     # onlu create the blog post if the user is authenticated by calling a
#     # decorator that handles this
#     @authentication_check
#     def create_blog_post(self, user):
#         print(f"Created the blog post for {user.name}")
#
#
# user1 = User("Saksham")
# user1.create_blog_post(user1)


# log the name, inputs, and outputs of the function used with the decorator
def logging_decorator(function):
    def wrapper(*args, **kwargs):
        name = function.__name__
        input_name = args[0]
        output = function(input_name)
        print(f"Function name is {name}, input is {input_name} and output is {output}")

    return wrapper


# Use the decorator 👇
@logging_decorator
def hello(name):
    return (f"Hello, {name}")

hello("Saksham")