__author__ = 'rakesh'

from itertools import combinations

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        finalResult = []
        nums.sort()

        for i in range(len(nums) + 1):

            for k in combinations(nums, i):
                s = list(k)
                finalResult.append(s)

        return finalResult

print Solution().subsets([1, 2, 3, 4])
