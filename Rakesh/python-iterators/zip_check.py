__author__ = 'rakesh'

from itertools import izip_longest

v1 = [1, 3]
v2 = [2, 4, 5]

finalresult = []

[finalresult.append(filter(None, list(i))) for i in izip_longest(v1, v2)]

print sum(finalresult, [])







