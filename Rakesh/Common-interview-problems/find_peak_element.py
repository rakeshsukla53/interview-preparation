__author__ = 'rakesh'

import sys

class Solution(object):
    def findPeakElement(self, nums, i=0, j=0):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = len(nums)
        mid = (j + i) / 2

        if (nums[mid] > nums[mid + 1]) and (nums[mid] > nums[mid - 1]):
            return mid

        if nums[mid + 1] > nums[mid]:
            return self.findPeakElement(nums, mid, j)

        else:
            return self.findPeakElement(nums, i, mid)

print Solution().findPeakElement([1, 2, 3, 1, 2, 3])


