__author__ = 'rakesh'

'''
3. variable resolution rules

Of course this doesn’t mean that we can’t access global variables inside our function. Python’s scope rule is that variable creation always creates a new local variable but variable access (including modification) looks in the local scope and then searches all the enclosing scopes to find a match. So if we modify our function foo to print our global variable things work as we would expect:

>>> a_string = "This is a global variable"
>>> def foo():
...     print a_string # 1
>>> foo()
This is a global variable

At point #1 Python looks for a local variable in our function and not finding one, looks for a global variable[2] of the same name.

On the other hand if we try to assign to the global variable inside our function it doesn’t do what we want:

>>> a_string = "This is a global variable"
>>> def foo():
...     a_string = "test" # 1
...     print locals()
>>> foo()
{'a_string': 'test'}
>>> a_string # 2
'This is a global variable'

As we can see, global variables can be accessed (even changed if they are mutable data types) but not (by default) assigned to. At point #1 inside our function we are actually creating a new local variable that "shadows" the global variable with the same name. We can see this be by printing the local namespace inside our function foo and notice it now has an entry. We can also see back out in the global namespace at point #2 that when we check the value of the variable a_string it hasn’t been changed at all.
'''
