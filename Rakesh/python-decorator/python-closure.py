__author__ = 'rakesh'


def outer():

    x = 1

    def inner():

        print x

    return inner


foo = outer()

print foo.func_closure

'''
Let’s not start with a definition, let’s start with another code sample. What if we tweaked our last example slightly:

>>> def outer():
...     x = 1
...     def inner():
...         print x # 1
...     return inner
>>> foo = outer()
>>> foo.func_closure # doctest: +ELLIPSIS
(<cell at 0x...: int object at 0x...>,)

From our last example we can see that inner is a function returned by outer, stored in a variable named foo and we could call it with foo(). But will it run? Let’s consider scoping rules first.

Everything works according to Python’s scoping rules - x is a local variable in our function outer. When inner prints x at point #1 Python looks for a local variable to inner and not finding it looks in the enclosing scope which is the function outer, finding it there.

But what about things from the point of view of variable lifetime? Our variable x is local to the function outer which means it only exists while the function outer is running. We aren’t able to call inner till after the return of outer so according to our model of how Python works, x shouldn’t exist anymore by the time we call inner and perhaps a runtime error of some kind should occur.

It turns out that, against our expectations, our returned inner function does work. Python supports a feature called function closures which means that inner functions defined in non-global scope remember what their enclosing namespaces looked like at definition time. This can be seen by looking at the func_closure attribute of our inner function which contains the variables in the enclosing scopes.

Remember - the function inner is being newly defined each time the function outer is called. Right now the value of x doesn’t change so each inner function we get back does the same thing as another inner function - but what if we tweaked it a little bit?

>>> def outer(x):
...     def inner():
...         print x # 1
...     return inner
>>> print1 = outer(1)
>>> print2 = outer(2)
>>> print1()
1
>>> print2()
2

From this example you can see that closures - the fact that functions remember their enclosing scope - can be used to build custom functions that have, essentially, a hard coded argument. We aren’t passing the numbers 1 or 2 to our inner function but are building custom versions of our inner function that "remembers" what number it should print.

This alone is a powerful technique - you might even think of it as similar to object oriented techniques in some ways: outer is a constructor for inner with x acting like a private member variable. And the uses are numerous - if you are familiar with the key parameter in Python’s sorted function you have probably written a lambda function to sort a list of lists by the second item instead of the first. You might now be able to write an itemgetter function that accepts the index to retrieve and returns a function that could suitably be passed to the key parameter.

But let’s not do anything so mundane with closures! Instead let’s stretch one more time and write a decorator!
'''

