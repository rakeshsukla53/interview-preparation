
# main article http://www.pydanny.com/python-decorator-cheatsheet.html

# Decorators Without Arguments

def arguments_decorator(arg1, arg2):
    def _outer_wrapper(wrapped_function):
        def _wrapper(*args, **kwargs):
            # do something before the function call
            result = wrapped_function(*args, **kwargs)
            # do something after the function call

            # Demonstrating what you can do with decorator arguments
            result = result * arg1 * arg2

            return result
        return _wrapper
    return _outer_wrapper

def arguments_decorator_with_wraps(arg1, arg2):
    def _outer_wrapper(wrapped_function):
        @functools.wraps(wrapped_function)
        def _wrapper(*args, **kwargs):
            # do something before the function call
            result = wrapped_function(*args, **kwargs)
            # do something after the function call

            # Demonstrating what you can do with decorator arguments
            result = result * arg1 * arg2

            return result
        return _wrapper
    return _outer_wrapper

def arguments_decorator_with_wrapt(arg1, arg2):
    @wrapt.decorator
    def _wrapper(wrapped_function, instance, args, kwargs):
        # do something before the function call
        result = wrapped_function(*args, **kwargs)
        # do something after the function call

        # Demonstrating what you can do with decorator arguments
        result = result * arg1 * arg2

        return result
    return _wrapper


def test_arguments_decorators():

    @arguments_decorator(2, 3)
    def func4():
        return 'We'

    @arguments_decorator_with_wraps(2, 2)
    def func5():
        return 'code'

    @arguments_decorator_with_wrapt(3, 2)
    def func6():
        return 'python'

    assert func4() == 'WeWeWeWeWeWe'
    assert func5() == 'codecodecodecode'
    assert func6() == 'pythonpythonpythonpythonpythonpython'


