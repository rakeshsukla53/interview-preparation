
# Single underscore at the beginning:

Python doesn't have real private methods, so one underscore at the start of a method or attribute name means you shouldn't access this method, because it's not part of the API.

`class BaseForm(StrAndUnicode):`

    def _get_errors(self):
        "Returns an ErrorDict for the data provided for the form"
        if self._errors is None:
            self.full_clean()
        return self._errors

    errors = property(_get_errors)`
 
code snippet taken from django source code (django/forms/forms.py). This means errors is a property, and it's part of the module, but the method this property calls, _get_errors, is "private", so you shouldn't access it.

# double underscore at the beginning 

This causes a lot of confusion. It should not be used to create a private method. It should be used to avoid your method to be overridden by a subclass. Let's see an example:

`class A(object):
    def __test(self):
        print "I'm test method in class A"`

    def test(self):
        self.__test()`
`
a = A()
a.test()`

Output:

`
$ python test.py
I'm test method in class A`

Now create a subclass B and do customization for __test method

class B(A):
    def __test(self):
        print "I'm test method in class B"

b = B()
b.test()

Output will be....

$ python test.py
I'm test method in class A

As we have seen, A.test() didn't call B.__test() methods, as we might expect. But in fact, this is the correct behavior for __. So when you create a method starting with __ it means that you don't want to anyone to be able to override it, it will be accessible only from inside the own class.

# Two underscores at the beginning and at the end:

When we see a method like __this__, don't call it. Because it means it's a method which python calls, not by you. Let's take a look:

`
>>> name = "test string"
>>> name.__len__()
11
>>> len(name)
11
>>> number = 10
>>> number.__add__(40)
50
>>> number + 50
60`

There is always an operator or native function which calls these magic methods. Sometimes it's just a hook python calls in specific situations. For example __init__() is called when the object is created after __new__() is called to build the instance...

    `class FalseCalculator(object):

        def __init__(self, number):
            self.number = number
    
        def __add__(self, number):
            return self.number - number
    
        def __sub__(self, number):
            return self.number + number



        number = FalseCalculator(20)
        print number + 10      # 10
        print number - 20      # 40`
        









