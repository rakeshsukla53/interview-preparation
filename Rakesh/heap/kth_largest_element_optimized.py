import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums, reverse=True)

        return nums[k - 1]

Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)

