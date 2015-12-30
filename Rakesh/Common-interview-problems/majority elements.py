from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        element_frequency = Counter(nums)  # this is a wrong approach since if it will expand with input
        result = dict(element_frequency)
        for i in element_frequency:
            if element_frequency[i] < len(nums) / 3:
                del result[i]

        return result.keys()

print Solution().majorityElement([1, 1, 1, 1, 2, 2, 2, 3])

