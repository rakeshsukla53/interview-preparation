a_string ="this is a global variable"

def foo():

    print locals()

print globals()

foo()

'''
 The builtin globals function returns a dictionary containing all the variable names Python knows about. (For the sake of clarity I’ve omitted in the output a few variables Python automatically creates.) At point #2 I called my function foo which prints the contents of the local namespace inside the function. As we can see the function foo has its own separate namespace which is currently empty.
'''




