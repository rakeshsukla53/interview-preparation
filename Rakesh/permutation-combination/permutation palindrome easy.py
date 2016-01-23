from collections import Counter
from itertools import permutations, repeat

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1 or len(set(s)) == 1:
            return True

        if len(filter(lambda x: x[1] % 2 == 1, Counter(s).items())) > 1:
            return False

        if len(s) % 2 == 0:
                if len(filter(lambda x: x[1] == 1, Counter(s).items())) == 1:
                    return False

        return True

