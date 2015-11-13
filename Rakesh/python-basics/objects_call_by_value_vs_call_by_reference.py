#
#
# Variables in Python aren't values, they're object references. When you call a Python function the arguments are copies of the references to the original object. I don't know how this relates to the terminology you posed in the question.
#
# For example consider the following Python code:
#
# def foo(bar, baz):
#     bar = 3
#     baz[0] = 4
#
# a = 1
# b = [2]
# foo(a, b)
# print a, b
#
# a is assigned to the object 1, and b is assigned to the list object containing a reference to the object 2. Inside of the function foo, bar is also assigned to the same object 1 and baz is assigned to the same list object. Since 1 is immutable you can't change the object, but you can reassign bar to refer to a different object such as 3. A list is modifiable, so by setting baz[0] to 4 you are also changing the list object that b refers to. The output of the above will be 1 [4].

