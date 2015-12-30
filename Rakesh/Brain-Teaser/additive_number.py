
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        if len(num) < 3:
            return 0

        for i in range(2, len(num)):
            digits = num[:i]
            for j in range(1, len(digits)):
                b, a = int(digits[j:]), int(digits[:j])
                c = b + a
                if str(c) == num[i: i + len(str(c))]:
                    return 1

        return 0

Solution().isAdditiveNumber("199100199299")

