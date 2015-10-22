__author__ = 'rakesh'

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        for i in range(1, n + 1):

            number = str(i)
            count = list(number).count('1')
            sum += count

        return sum

print Solution().countDigitOne(3184191)


