
from itertools import permutations

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        for value in permutations(nums, len(nums)):
            result.append(list(value))

        return result

"""
def permute(self, nums):
    return map(list, itertools.permutations(nums))
"""




