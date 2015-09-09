__author__ = 'rakesh'

import re

value = '0987654321'

pattern = re.compile(r'(?=(87654))')

occurence = [m.start() for m in re.finditer('87654', value)]

print occurence

print pattern.findall(value)
#https://www.hackerrank.com/challenges/the-grid-search

#solve it using pattern matching

'''
m.start() for m in re.finditer('test', 'test test test test')]
[0, 5, 10, 15]

If you want to find overlapping matches, lookahead will do that:

>>> [m.start() for m in re.finditer('(?=tt)', 'ttt')]
[0, 1]

If you want a reverse find-all without overlaps, you can combine positive and negative lookahead into an expression like this:

>>> search = 'tt'
>>> [m.start() for m in re.finditer('(?=%s)(?!.{1,%d}%s)' % (search, len(search)-
'''

