
import math


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return n > 0 and pow(3, 19) % n == 0

print Solution().isPowerOfThree(83)


# 3 ^ 19 is the last signed integer number here

# it can be solved in constant time

