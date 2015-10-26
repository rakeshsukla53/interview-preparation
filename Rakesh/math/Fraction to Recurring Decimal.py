__author__ = 'rakesh'

from collections import defaultdict

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        # fraction = str((float(numerator)/denominator))
        # n = abs(len(str(numerator)) - len(str(denominator)))
        # afterDecimal = fraction.split('.')[1]
        # beforeDecimal = fraction.split('.')[0]
        # #print afterDecimal
        # frequency = defaultdict(int)
        # for i in range(len(afterDecimal)):
        #     print afterDecimal[i:i+n+1]
        #     frequency[afterDecimal[i:i + n + 1]] += 1

        #print frequency

        # result = beforeDecimal + "."
        # for i in afterDecimal:
        #     if frequency.has_key(i):
        #         if frequency[i] == 1:
        #             result += i
        #             frequency.pop(i)
        #         else:
        #             result += "(" + i + ")"
        #             frequency.pop(i)
        #
        # return result

print Solution().fractionToDecimal(1, 999)

