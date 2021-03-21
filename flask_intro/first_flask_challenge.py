import time

current_time = time.time()
print(current_time)

# Use a decorator to find the time it took to run a function and return that
# information
def speed_calc_decorator(function):
    def wrapper_func():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"Time difference was {end_time - start_time}s")

    return wrapper_func


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()