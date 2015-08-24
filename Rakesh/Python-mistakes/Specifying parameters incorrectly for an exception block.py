__author__ = 'rakesh'

try:
    l = ['a', 'b']
    int(l[2])

except ValueError, IndexError:
    pass

# he problem here is that the except statement does not take a list of exceptions specified in this manner. Rather, In Python 2.x, the syntax except Exception, e is used to bind the exception to the optional second parameter specified (in this case e), in order to make it available for further inspection. As a result, in the above code, the IndexError exception is not being caught by the except statement; rather, the exception instead ends up being bound to a parameter named IndexError.
#
# The proper way to catch multiple exceptions in an except statement is to specify the first parameter as a tuple containing all exceptions to be caught. Also, for maximum portability, use the as keyword, since that syntax is supported by both Python 2 and Python 3:
#
# >>> try:
# ...     l = ["a", "b"]
# ...     int(l[2])
# ... except (ValueError, IndexError) as e:
# ...     pass
# ...
# >>>
#catching multiple exception is extremely important and by this way you can do this

try:
    l = ['a', 'b']
    int(l[2])

except (ValueError, IndexError) as e:
    print e

