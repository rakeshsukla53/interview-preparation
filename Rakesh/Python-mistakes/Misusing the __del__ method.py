__author__ = 'rakesh'

# Let’s say you had this in a file called mod.py:
#
# import foo
#
# class Bar(object):
#    	    ...
#     def __del__(self):
#         foo.cleanup(self.myhandle)
#
# And you then tried to do this from another_mod.py:
#
# import mod
# mybar = mod.Bar()
#
# You’d get an ugly AttributeError exception.
#
# Why? Because, as reported here, when the interpreter shuts down, the module’s global variables are all set to None. As a result, in the above example, at the point that __del__ is invoked, the name foo has already been set to None.
#
# A solution to this somewhat more advanced Python programming problem would be to use atexit.register() instead. That way, when your program is finished executing (when exiting normally, that is), your registered handlers are kicked off before the interpreter is shut down.
#
# With that understanding, a fix for the above mod.py code might then look something like this:
#
# import foo
# import atexit
#
# def cleanup(handle):
#     foo.cleanup(handle)
#
#
# class Bar(object):
#     def __init__(self):
#         ...
#         atexit.register(cleanup, self.myhandle)
#
# This implementation provides a clean and reliable way of calling any needed cleanup functionality upon normal program termination. Obviously, it’s up to foo.cleanup to decide what to do with the object bound to the name self.myhandle, but you get the idea.
