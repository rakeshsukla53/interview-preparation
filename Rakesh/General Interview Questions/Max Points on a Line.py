
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        for i in points:
            print i.x, i.y

        return 0

# How to solve this problem

'''
Suppose you have a = [[1, 2], [3, 4], [6, 7], [2, 3]]
it will take you n*n to find the all the slopes. If slope is same with same coordinate, it will lie on the same line equation. You can use a hash table to store the frequency, and then find the max.
'''


