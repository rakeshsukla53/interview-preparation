
import itertools

A = [
 [1, 2, 3],
 [8, 9, 4],
 [7, 6, 5]
]

print A[::-1]  # reverses the whole matrix

print zip(*A[::-1])  # rotates the whole matrix clockwise 90 degree

print zip(*A[::1])  # if you want to do transpose

print list(itertools.chain(zip(*A[::1])))

print list(itertools.chain((1, 2, 3, 4)))  # it breaks the chain

for i in A:
    print i







#
# class Solution(object):
#     def generateMatrix(self, n):
#         """
#         :type n: int
#         :rtype: List[List[int]]
#         """
#
#
#
#
# Solution().generateMatrix(5)
#
