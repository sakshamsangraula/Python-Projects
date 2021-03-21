def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

def calculate(func_name, n1, n2):
    return func_name(n1, n2)

result = calculate(add, 5, 10)
print(result)

# Function inside a Function
def outer():
    print("outer function")

    def inner():
        print("inner function")

    return inner

inner_func = outer()
inner_func()

# A FUNCTION CAN BE PASSED AS A PARAMETER TO ANOTHER FUNCTION
# A FUNCTION CAN HAVE ANOTHER FUNCTION INSIDE
# A FUNCTION CAN RETURN ANOTHER FUNCTION