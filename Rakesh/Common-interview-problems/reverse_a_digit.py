__author__ = 'rakesh'

import sys

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            value = str(x)[1:]
            newValue = list(value)[::-1]
            return -1*int("".join(newValue))
        else:
            value = str(x)
            newValue = list(value)[::-1]
            return int("".join(newValue))

rev = Solution()
print rev.reverse(1534236469)
print sys.maxint




