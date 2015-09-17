__author__ = 'rakesh'

#Decorators

def outer(some_func):
    def inner():
        print "before some_func"
        ret = some_func() # 1
        return ret + 1
    return inner

def foo():
    return 1
decorated = outer(foo) # 2
decorated()

# A decorator is just a callable that takes a function as an argument and returns a replacement function. We’ll start simply and work our way up to useful decorators.

'''
>>> def outer(some_func):
...     def inner():
...         print "before some_func"
...         ret = some_func() # 1
...         return ret + 1
...     return inner
>>> def foo():
...     return 1
>>> decorated = outer(foo) # 2
>>> decorated()
before some_func
2

Look carefully through our decorator example. We defined a function named outer that has a single parameter some_func. Inside outer we define an nested function named inner. The inner function will print a string then call some_func, catching its return value at point #1. The value of some_func might be different each time outer is called, but whatever function it is we’ll call it. Finally inner returns the return value of some_func() + 1 - and we can see that when we call our returned function stored in decorated at point #2 we get the results of the print and also a return value of 2 instead of the original return value 1 we would expect to get by calling foo.

We could say that the variable decorated is a decorated version of foo - it’s foo plus something. In fact if we wrote a useful decorator we might want to replace foo with the decorated version altogether so we always got our "plus something" version of foo. We can do that without learning any new syntax simply by re-assigning the variable that contains our function:

>>> foo = outer(foo)
>>> foo # doctest: +ELLIPSIS
<function inner at 0x...>

Now any calls to foo() won’t get the original foo, they’ll get our decorated version! Got the idea? Let’s write a more useful decorator.
'''
