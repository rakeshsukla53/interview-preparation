__author__ = 'rakesh'

'''
5. Function arguments and parameters

Python does allow us to pass arguments to functions. The parameter names become local variables in our function.

>>> def foo(x):
...     print locals()
>>> foo(1)
{'x': 1}

Python has a variety of ways to define function parameters and pass arguments to them. For the full skinny you’ll want to see the Python documentation on defining functions. I’ll give you the short version here: function parameters can be either positional parameters that are mandatory or named, default value parameters that are optional.

>>> def foo(x, y=0): # 1
...     return x - y
>>> foo(3, 1) # 2
2
>>> foo(3) # 3
3
>>> foo() # 4
Traceback (most recent call last):
  ...
TypeError: foo() takes at least 1 argument (0 given)
>>> foo(y=1, x=3) # 5
2

At point #1 we are defining a function that has a single positional parameter x and a single named parameter y. As we see at point #2 we can call this function passing arguments normally - the values are passed to the parameters of foo by position even though one is defined in the function definition as a named parameter. We can also call the function without passing any arguments at all for the named parameter as you can see at point #3 - Python uses the default value of 0 we declared if it doesn’t receive a value for the named parameter y. Of course we can’t leave out values for the first (mandatory, positional) parameter - point #4 demonstrates that this results in an exception.

All clear and straightforward? Now it gets slightly confusing - Python supports named arguments at function call time. Look at point #5 - here we are calling a function with two named arguments even though it was defined with one named and one positional parameter. Since we have names for our parameters the order we pass them in doesn’t matter.

The opposite case is true of course. One of the parameters for our function is defined as a named parameter but we passed an argument to it by position - the call foo(3,1) at point #2 passes a 3 as the argument to our ordered parameter x and passes the second (an integer 1) to the second parameter even though it was defined as a named parameter.

Whoo! That feels like a lot of words to describe a pretty simple concept: function parameters can have names or positions. This means slightly different things depending on whether we’re at function definition or function call time and we can use named arguments to functions defined only with positional parameters and vice-versa! Again - if that was all too rushed be sure to check out the the docs.
'''

