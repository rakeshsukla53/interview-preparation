
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print reduce(lambda x, y: x + y, A)

from itertools import chain

A = [[1, 2, 3], [4, 5, 6]]

print chain(A).next()


