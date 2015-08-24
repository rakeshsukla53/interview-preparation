__author__ = 'rakesh'


def foo(bar=[]):        # bar is optional and defaults to [] if not specified
   bar.append("baz")    # but this line could be problematic, as we'll see...
   return bar


print foo()
print foo()
print foo()
print foo()
print foo()
print foo()
print foo()


#why the previous value is there even though we are calling the function.

'''
A common mistake is to think that the optional argument will be set to the specified default expression each time the function is called without supplying a value for the optional argument. In the above code, for example, one might expect that calling foo() repeatedly (i.e., without specifying a bar argument) would always return 'baz', since the assumption would be that each time foo() is called (without a bar argument specified) bar is set to [] (i.e., a new empty list).

But let’s look at what actually happens when you do this:

>>> foo()
["baz"]
>>> foo()
["baz", "baz"]
>>> foo()
["baz", "baz", "baz"]

Huh? Why did it keep appending the default value of "baz" to an existing list each time foo() was called, rather than creating a new list each time?

The more advanced Python programming answer is that the default value for a function argument is only evaluated once, at the time that the function is defined. Thus, the bar argument is initialized to its default (i.e., an empty list) only when foo() is first defined, but then calls to foo() (i.e., without a bar argument specified) will continue to use the same list to which bar was originally initialized.
'''

'''
The command workaround here is important
FYI, a common workaround for this is as follows:

>>> def foo(bar=None):
...    if bar is None:		# or if not bar:
...        bar = []
...    bar.append("baz")
...    return bar
...
>>> foo()
["baz"]
>>> foo()
["baz"]
>>> foo()
["baz"]
'''