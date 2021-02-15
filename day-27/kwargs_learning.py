# use kwargs to pass in many optional keyword arguments and use the keyword arguments in the function

def calculate(num, **kwargs):
    sum = num + kwargs["add"]
    diff = num - kwargs["subtract"]
    mult = num * kwargs.get("multiply")
    div = num / kwargs["divide"]

    return (sum, diff, mult, div)

print(calculate(5, add=1, subtract=1, multiply=1, divide=1))

# create a class and use kwargs when initializing the constructor
class Car:

    def __init__(self, **kwargs):
        # better to use get because when we use get it returns "None" and if we don't use get then
        # we get an error if we didn't pass in a value for the attribute we are accessing (or we forgot to
        # pass it before)
        self.mileage = kwargs.get("mileage")
        self.color = kwargs.get("color")
        self.company = kwargs.get("company")

car_object = Car(mileage=180, color="red", company="Toyota")
print(car_object.company)




