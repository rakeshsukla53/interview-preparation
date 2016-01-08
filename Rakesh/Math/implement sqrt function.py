# you are supposed to implement a sqrt function

import bisect

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        number_range = range(x / 2)
        sqrt_numbers = map(lambda x: x*x, number_range)
        i = bisect.bisect_left(sqrt_numbers, x)
        return i

# this program will result in memory error
