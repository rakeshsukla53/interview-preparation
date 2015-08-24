__author__ = 'rakesh'

class A(object):
    x = 1

class B(A):  #B is inherting from A class
    pass

class C(A): #C is inherting from B class
   pass

print A.x, B.x, C.x


# Makes sense.
#
# >>> B.x = 2
# >>> print A.x, B.x, C.x
# 1 2 1
#
# Yup, again as expected.
#
# >>> A.x = 3
# >>> print A.x, B.x, C.x
# 3 2 3
#
# What the $%#!&?? We only changed A.x. Why did C.x change too?
#
# In Python, class variables are internally handled as dictionaries and follow what is often referred to as Method Resolution Order (MRO). So in the above code, since the attribute x is not found in class C, it will be looked up in its base classes (only A in the above example, although Python supports multiple inheritance). In other words, C doesn’t have its own x property, independent of A. Thus, references to C.x are in fact references to A.x. This causes a Python problem unless it’s handled properly. Learn more aout class attributes in Python.
#

#ctrl + \ will block comment in my code