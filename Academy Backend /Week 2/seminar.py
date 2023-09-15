from datetime import datetime


def my_message(message):
    def my_decorator(my_function):
        def my_wrapper(*args, **kwargs):
            start = datetime.now()
            print(f"Start: {message} {start}")
            print(my_function(*args, **kwargs))
            end = datetime.now()
            print(f"End: {end}")
            print(f"Took: {end - start}")
            return end

        return my_wrapper

    return my_decorator


@my_message("LAUNCH FUNCTION")
def first_function(*args):
    return "abc"


@my_message("Second")
def second_function(a, b):
    return a + b


first_function()
print(second_function(1, 3))