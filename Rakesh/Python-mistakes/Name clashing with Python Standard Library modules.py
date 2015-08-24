__author__ = 'rakesh'

# One of the beauties of Python is the wealth of library modules that it comes with “out of the box”. But as a result, if you’re not consciously avoiding it, it’s not that difficult to run into a name clash between the name of one of your modules and a module with the same name in the standard library that ships with Python (for example, you might have a module named email.py in your code, which would be in conflict with the standard library module of the same name).
#
# This can lead to gnarly problems, such as importing another library which in turns tries to import the Python Standard Library version of a module but, since you have a module with the same name, the other package mistakenly imports your version instead of the one within the Python Standard Library. This is where bad Python errors happen.
#
# Care should therefore be exercised to avoid using the same names as those in the Python Standard Library modules. It’s way easier for you to change the name of a module within your package than it is to file a Python Enhancement Proposal (PEP) to request a name change upstream and to try and get that approved.