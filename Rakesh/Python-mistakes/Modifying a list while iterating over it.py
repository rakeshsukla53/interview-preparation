__author__ = 'rakesh'


odd = lambda x: bool(x % 2)  #this is really cool way to define whether this odd is boolean or not

numbers = [n for n in range(10)]
for i in range(len(numbers)):
    if odd(numbers[i]):
        del numbers[i]  # BAD: Deleting item from a list while iterating over it
#
# The problem with the following code should be fairly obvious:
#
# >>> odd = lambda x : bool(x % 2)
# >>> numbers = [n for n in range(10)]
# >>> for i in range(len(numbers)):
# ...     if odd(numbers[i]):
# ...         del numbers[i]  # BAD: Deleting item from a list while iterating over it
# ...
# Traceback (most recent call last):
#   	  File "<stdin>", line 2, in <module>
# IndexError: list index out of range
#
# Deleting an item from a list or array while iterating over it is a Python problem that is well known to any experienced software developer. But while the example above may be fairly obvious, even advanced developers can be unintentionally bitten by this in code that is much more complex.
#
# Fortunately, Python incorporates a number of elegant programming paradigms which, when used properly, can result in significantly simplified and streamlined code. A side benefit of this is that simpler code is less likely to be bitten by the accidental-deletion-of-a-list-item-while-iterating-over-it bug. One such paradigm is that of list comprehensions. Moreover, list comprehensions are particularly useful for avoiding this specific problem, as shown by this alternate implementation of the above code which works perfectly:
#
# >>> odd = lambda x : bool(x % 2)
# >>> numbers = [n for n in range(10)]
# >>> numbers[:] = [n for n in numbers if not odd(n)]  # ahh, the beauty of it all
# >>> numbers
# [0, 2, 4, 6, 8]
