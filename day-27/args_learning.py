
# create an add function that takes in a lot of arguments
def add(*args):
    sum = 0
    for num in args:
        sum+= num
    return f"sum is {sum}"

result = add(1,2,3,4,5,19,57,87,89)
print(result)
