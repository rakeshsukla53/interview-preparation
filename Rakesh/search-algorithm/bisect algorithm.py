__author__ = 'rakesh'

import bisect
#
# def index(a, x):
#     'Locate the leftmost value exactly equal to x'
#     i = bisect.bisect_left(a, x)
#     if i != len(a) and a[i] == x:
#         return i
#     raise ValueError
#
# print index([1, 2, 3, 4, 5], 2)

print bisect.bisect_left([4, 5, 6], 5)

print bisect.bisect([4, 5, 6], 3)

#just go through this documentation and for finding the index it using binary search which is pretty powerful

