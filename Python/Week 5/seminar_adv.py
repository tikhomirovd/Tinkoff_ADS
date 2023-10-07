import functools
import random
import time


def make_adder(x):
    def add(y):
        return x + y

    return add


f = make_adder(3)  # f(y) = 3 + y


def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        ret_val = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start_time} seconds")
        return ret_val

    return wrapper


@timeit
def do_sort(a: list):
    a.sort()


@timeit
def do_sorted(a):
    return sorted(a)


a = [random.randint(0, 1_000_000) for _ in range(1_000_000)]
b = a.copy()

# timed_to_sort = timeit(do_sort)
# timed_to_sorted = timeit(do_sorted)
#
# timed_to_sort(a)
# timed_to_sorted(b)

# All upper equal to below

do_sort(a)
do_sorted(b)

print(do_sort.__name__)  # Wrapper
print(do_sorted.__name__)  # Wrapper


# Декоратор, который гарантирует, что функция будет вызвана не более 1 раза

def once(func):
    is_used = False

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal is_used  # Надо использовать nonlocal, потому что переменная из enclose scope, но мы присваиваем значения и по умолчанию интерпертатор думает, что она local
        if not is_used:
            ret_val = func(*args, **kwargs)
            is_used = True
            return ret_val
        print("Already used")

    return wrapper


@once
def foo():
    print("Hello world")


foo()
foo()


def not_more_n_runs(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal n
            if n:
                ret_val = func(*args, **kwargs)
                n -= 1
                return ret_val

        return wrapper

    return decorator


@not_more_n_runs(2)
def foo():
    print("hello world")


foo()
foo()
foo()
foo()