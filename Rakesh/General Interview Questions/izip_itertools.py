__author__ = 'rakesh'

from itertools import izip_longest, izip, islice


A = [10, 20, 30, 50, 40, 30, 100, 20, 40]

B = ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'G']

print list(islice(A, 3))

for i in izip_longest(A, B):

    print i

for i in izip(A, B):

    print i
