# Given a list in variable `x`, write a Python generator expression that returns only the elements from x that are odd integers or have an even index in `x`. The given list may contain items other than numbers.


def odd_even_generator(x):

    for index, number in enumerate(x):
        if index % 2 == 0 or (type(number) is int and number % 2 != 0):
            yield number
