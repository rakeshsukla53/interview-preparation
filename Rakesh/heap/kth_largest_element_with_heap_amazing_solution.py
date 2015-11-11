import heapq
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        heap=[]
        for i in nums:
            heapq.heappush(heap,-i)
        for i in range(k):
            res=-heapq.heappop(heap)
        return res

class Solution:
# @param {integer[]} nums
# @param {integer} k
# @return {integer}
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]


