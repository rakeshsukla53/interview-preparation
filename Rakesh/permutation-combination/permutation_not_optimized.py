from itertools import permutations
from collections import defaultdict

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        duplicates = defaultdict(int)
        for i in permutations(nums, len(nums)):
            if duplicates.has_key(i):
                pass
            else:
                duplicates[i] += 1
                result.append(list(i))

        return result

Solution().permuteUnique([1, 1, 2])

# next optimization steps

# basically, assume we have "1234", the idea is to increase the number in ascending order, so next is "1243", next is "1324", and so on.
