__author__ = 'rakesh'

from itertools import combinations

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        d = dict()
        finalResult = []
        for i in range(len(nums)+1):
            for k in combinations(nums, i):
                value = "".join(map(str, list(k)))
                if d.has_key(value):
                    pass
                else:
                    d[value] = ""
                    finalResult.append(list(k))

        return finalResult

print Solution().subsetsWithDup([1, 2, 2])
