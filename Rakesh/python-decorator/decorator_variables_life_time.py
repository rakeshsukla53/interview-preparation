__author__ = 'rakesh'

'''
4. Variable lifetime

It’s also important to note that not only do variables live inside a namespace, they also have lifetimes. Consider

>>> def foo():
...     x = 1
>>> foo()
>>> print x # 1
Traceback (most recent call last):
  ...
NameError: name 'x' is not defined

It isn’t just scope rules at point #1 that cause a problem (although that’s why we have a NameError) it also has to do with how function calls are implemented in Python and many other languages. There isn’t any syntax we can use to get the value of the variable x at this point - it literally doesn’t exist! The namespace created for our function foo is created from scratch each time the function is called and it is destroyed when the function ends.
'''

