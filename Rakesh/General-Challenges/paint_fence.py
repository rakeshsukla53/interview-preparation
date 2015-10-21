__author__ = 'rakesh'

class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        colors = list(range(1, k))

        if n == 1:
            return k

        if n == 2:
            from itertools import product
            count = 0
            for i in product(colors, repeat=2):
                count += 1
            return count

        if n > 2:
            from itertools import combinations



