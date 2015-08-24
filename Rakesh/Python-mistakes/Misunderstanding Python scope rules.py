__author__ = 'rakesh'

x = 10

def foo():
    x += 1
    print x


foo()
#
# Python scope resolution is based on what is known as the LEGB rule, which is shorthand for Local, Enclosing, Global, Built-in. Seems straightforward enough, right? Well, actually, there are some subtleties to the way this works in Python, which brings us to the common more advanced Python programming problem below.
#
# What’s the problem?
#
# The above error occurs because, when you make an assignment to a variable in a scope, that variable is automatically considered by Python to be local to that scope and shadows any similarly named variable in any outer scope.
#
# Many are thereby surprised to get an UnboundLocalError in previously working code when it is modified by adding an assignment statement somewhere in the body of a function. (You can read more about this here.)
#
# It is particularly common for this to trip up developers when using lists. Consider the following example:
#
# >>> lst = [1, 2, 3]
# >>> def foo1():
# ...     lst.append(5)   # This works ok...
# ...
# >>> foo1()
# >>> lst
# [1, 2, 3, 5]
#
# >>> lst = [1, 2, 3]
# >>> def foo2():
# ...     lst += [5]      # ... but this bombs!
# ...
# >>> foo2()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 2, in foo
# UnboundLocalError: local variable 'lst' referenced before assignment
#
# Huh? Why did foo2 bomb while foo1 ran fine?
#
# The answer is the same as in the prior example problem, but is admittedly more subtle. foo1 is not making an assignment to lst, whereas foo2 is. Remembering that lst += [5] is really just shorthand for lst = lst + [5], we see that we are attempting to assign a value to lst (therefore presumed by Python to be in the local scope). However, the value we are looking to assign to lst is based on lst itself (again, now presumed to be in the local scope), which has not yet been defined. Boom.
