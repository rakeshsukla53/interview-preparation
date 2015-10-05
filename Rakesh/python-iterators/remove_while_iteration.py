__author__ = 'rakesh'

somelist = range(10)
for x in somelist:
    somelist.remove(x)  #so here you are modifying the main list which you should not be doing
print somelist

somelist = range(10)
for x in somelist[:]:  #Because the second one iterates over a copy of the list. So when you modify the original list, you do not modify the copy that you iterate over
    somelist.remove(x)
print somelist

#list(somelist) will convert an iterable into a list. somelist[:] makes a copy of an object that supports slicing. So they don't necessarily do the same thing. In this case I want to make a copy of the somelistobject, so I use [:]



