
def foo(x):
    x = 'another value'  # here x is another name bind which points to string variable 'another value'
    print x

bar = 'some value'
foo(bar)

print bar  # bar is named variable and is pointing to a string object

# string objects are immutable, the value cannot be modified

# you can not pass a simple primitive by reference in Python

bar += 'rakesh'  # here you are creating another object of string type

print bar

# you can pass reference only in immutable types in Python like list, dictionary

# call by value and call by reference are definitely a thing but we need to take care of which type of object are we talking about here

# we can pass by reference the following objects

# Mutable: everything else,
#
#     mutable sequences: list, byte array
#     set type: sets
#     mapping type: dict
#     classes, class instances
#     etc.

# we cannot pass by reference the following objects, because here a complete new object will be created

# Immutable:
#
#     numbers: int, float, complex
#     immutable sequences: str, tuples, bytes, frozensets


