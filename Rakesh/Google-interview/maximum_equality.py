__author__ = 'rakesh'

from itertools import combinations

def answer(x):

    for j in range(len(x), 0, -1):

        for i in combinations(x, j):

            if sum(list(i)) % len(list(i)) == 0:

                return len(list(i))

