
import bisect

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        return bisect.bisect_left(nums, target)



print Solution().searchInsert([1, 3, 5, 6], 0)
