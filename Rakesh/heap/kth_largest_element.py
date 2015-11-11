import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq._heapify_max(nums)

        for i in range(k):
            if i + 1 == k:
                return heapq.heappop(nums)
            else:
                heapq.heappop(nums)
                heapq._heapify_max(nums)

Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)

