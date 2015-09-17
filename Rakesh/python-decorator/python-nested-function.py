__author__ = 'rakesh'

'''
6. Nested functions

Python allows the creation of nested functions. This means we can declare functions inside of functions and all the scoping and lifetime rules still apply normally.

>>> def outer():
...     x = 1
...     def inner():
...         print x # 1
...     inner() # 2
...
>>> outer()
1

This looks a little more complicated, but it’s still behaving in a pretty sensible manner. Consider what happens at point #1 - Python looks for a local variable named x, failing it then looks in the enclosing scope which is another function! The variable x is a local variable to our function outer but as before our function inner has access to the enclosing scope (read and modify access at least). At point #2 we call our inner function. It’s important to remember that inner is also just a variable name that follows Python’s variable lookup rules - Python looks in the scope of outer first and finds a local variable named inner.
'''

