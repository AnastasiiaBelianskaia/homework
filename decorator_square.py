import random


def retry(attempts=5, desired_value=None):
    def wrapper(func):

        def inner(*args, **kwargs):
            count = attempts
            while count != 0:
                value = func(*args, **kwargs)
                if value == desired_value:
                    print("Congrats", value)
                    return desired_value
                count -= 1
            print("Failure massage")

        return inner

    return wrapper


@retry(desired_value=2)
def get_random_value():
    return random.choice((1, 2, 3, 4, 5))


@retry(desired_value=[1, 2])
def get_random_values(choices, size=2):
    return random.choices(choices, k=size)


get_random_value()
get_random_values([1, 2, 3, 4])


def print_square(size):
    print("*" * size)

    def columns(height):
        if height <= 0:
            return "null"
        print("*" + " " * (size - 2) + "*")
        return size * columns(height - 1)

    columns(size - 2)
    if size != 1:
        print("*" * size)


print_square(9)
