
from collections import defaultdict
from itertools import combinations

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        mapping = defaultdict(dict)

        # amazing way to use default dict of dict
        for index, value in enumerate(nums):
            mapping[value][index] = ''

        # duplicate values
        duplicate_values = filter(lambda x: len(mapping[x].keys()) > 1, mapping)

        for value in duplicate_values:
            for i in combinations(mapping[value].keys(), 2):
                low, high = i
                if abs(low - high) <= k:
                    return True

        return False

print Solution().containsNearbyDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4], 10)

