import itertools
#
# a = [[1, 2], [3, 4], [5, 6], [[[[[[100]]]]]]]
# print list(itertools.chain.from_iterable(a))
#
#
# from itertools import chain
#
# B = [[1, 2], [3, 4]]
#
# print sum(B, [])
# print list((chain.from_iterable(B)))

from collections import Iterable

def flatten(l):
    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, basestring):
            for sub in flatten(el):
                yield sub
        else:
            yield el

A = [[[[[[[3]]]]]], 'q', [1], 2.34]

print list(flatten(A))

# if you are wondering why base string is used

'''
>>> import collections
>>> a = 'A
  File "<input>", line 1
    a = 'A
         ^
SyntaxError: EOL while scanning string literal
>>> a = 'A'
>>> isinstance(a, collections.Iterable)
True
>>> a = 1
>>> isinstance(a, collections.Iterable)
False
>>> a = 2
>>> isinstance(a, collections.Iterable)
False
>>> isinstance(a, collections.Iterable)
False
>>> a = 'Rakesh'
>>> isinstance(a, collections.Iterable)
True
>>>
'''












