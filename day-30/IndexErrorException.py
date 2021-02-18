fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    # try the code
    try:
        fruit = fruits[index]
    # catch if exception - if index is more than or equal to len then just print fruit pie
    except IndexError:
        if index >= len(fruits):
            print("fruit pie")
    else:
        # after catching the exception print the index and pie
        print(fruit + " pie.")


make_pie(2)


